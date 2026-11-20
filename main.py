"""Entrypoint for make.fun news-image-20261119 submission."""

from pathlib import Path
import os
import struct
import zlib


PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_IMAGE_BYTES = 1048576
MAX_EDGE_PX = 1024


def verify_png_payload(payload: bytes) -> tuple[int, int]:
    """Validate PNG signature, chunk CRCs, dimensions, size cap, and IEND."""
    if not (1 <= len(payload) <= MAX_IMAGE_BYTES):
        raise ValueError(f"Invalid PNG byte count: {len(payload)}")
    if len(payload) < 33 or not payload.startswith(PNG_MAGIC):
        raise ValueError("Missing PNG signature")
    pos = 8
    saw_iend = False
    width = height = 0
    while pos + 12 <= len(payload):
        chunk_len = struct.unpack(">I", payload[pos:pos + 4])[0]
        chunk_tag = payload[pos + 4:pos + 8]
        data_start = pos + 8
        data_end = data_start + chunk_len
        if data_end + 4 > len(payload):
            raise ValueError("Truncated PNG chunk")
        chunk_body = payload[data_start:data_end]
        expected_crc = struct.unpack(">I", payload[data_end:data_end + 4])[0]
        if (zlib.crc32(chunk_tag + chunk_body) & 0xFFFFFFFF) != expected_crc:
            raise ValueError(f"CRC mismatch in {chunk_tag!r}")
        if pos == 8:
            if chunk_tag != b"IHDR" or chunk_len != 13:
                raise ValueError("First PNG chunk must be 13-byte IHDR")
            width, height = struct.unpack(">II", chunk_body[:8])
        if chunk_tag == b"IEND":
            saw_iend = True
            pos = data_end + 4
            break
        pos = data_end + 4
    if not saw_iend or pos != len(payload):
        raise ValueError("Missing or trailing data after IEND")
    if not (1 <= width <= MAX_EDGE_PX and 1 <= height <= MAX_EDGE_PX):
        raise ValueError(f"Dimensions out of range: {width}x{height}")
    return width, height


def emit_entry() -> None:
    """Copy verified entry.png to MAKEFUN_OUTPUT_DIR or /output."""
    bot_root = Path(os.environ.get("MAKEFUN_BOT_DIR") or Path(__file__).resolve().parent)
    out_root = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    src_file = bot_root / "entry.png"
    dst_file = out_root / "entry.png"

    raw = src_file.read_bytes()
    verify_png_payload(raw)
    out_root.mkdir(parents=True, exist_ok=True)
    dst_file.write_bytes(raw)


if __name__ == "__main__":
    emit_entry()
