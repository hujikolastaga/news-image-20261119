"""Deterministic pure-Python editorial news infographic renderer for 19 November 2026."""

import math
import struct
import zlib

WIDTH = 1024
HEIGHT = 1024

# 5x7 crisp pixel font covering uppercase, lowercase, digits, and punctuation.
FONT_5X7 = {
    " ": [".....", ".....", ".....", ".....", ".....", ".....", "....."],
    "A": [".###.", "#...#", "#...#", "#####", "#...#", "#...#", "#...#"],
    "B": ["####.", "#...#", "#...#", "####.", "#...#", "#...#", "####."],
    "C": [".####", "#....", "#....", "#....", "#....", "#....", ".####"],
    "D": ["####.", "#...#", "#...#", "#...#", "#...#", "#...#", "####."],
    "E": ["#####", "#....", "#....", "####.", "#....", "#....", "#####"],
    "F": ["#####", "#....", "#....", "####.", "#....", "#....", "#...."],
    "G": [".####", "#....", "#....", "#..##", "#...#", "#...#", ".####"],
    "H": ["#...#", "#...#", "#...#", "#####", "#...#", "#...#", "#...#"],
    "I": ["#####", "..#..", "..#..", "..#..", "..#..", "..#..", "#####"],
    "J": ["..###", "...#.", "...#.", "...#.", "#..#.", "#..#.", ".##.."],
    "K": ["#...#", "#..#.", "#.#..", "##...", "#.#..", "#..#.", "#...#"],
    "L": ["#....", "#....", "#....", "#....", "#....", "#....", "#####"],
    "M": ["#...#", "##.##", "#.#.#", "#.#.#", "#...#", "#...#", "#...#"],
    "N": ["#...#", "##..#", "#.#.#", "#..##", "#...#", "#...#", "#...#"],
    "O": [".###.", "#...#", "#...#", "#...#", "#...#", "#...#", ".###."],
    "P": ["####.", "#...#", "#...#", "####.", "#....", "#....", "#...."],
    "Q": [".###.", "#...#", "#...#", "#...#", "#.#.#", "#..#.", ".##.#"],
    "R": ["####.", "#...#", "#...#", "####.", "#.#..", "#..#.", "#...#"],
    "S": [".####", "#....", "#....", ".###.", "....#", "....#", "####."],
    "T": ["#####", "..#..", "..#..", "..#..", "..#..", "..#..", "..#.."],
    "U": ["#...#", "#...#", "#...#", "#...#", "#...#", "#...#", ".###."],
    "V": ["#...#", "#...#", "#...#", "#...#", "#...#", ".#.#.", "..#.."],
    "W": ["#...#", "#...#", "#...#", "#.#.#", "#.#.#", "##.##", "#...#"],
    "X": ["#...#", "#...#", ".#.#.", "..#..", ".#.#.", "#...#", "#...#"],
    "Y": ["#...#", "#...#", ".#.#.", "..#..", "..#..", "..#..", "..#.."],
    "Z": ["#####", "....#", "...#.", "..#..", ".#...", "#....", "#####"],
    "a": [".....", ".....", ".###.", "....#", ".####", "#...#", ".####"],
    "b": ["#....", "#....", "####.", "#...#", "#...#", "#...#", "####."],
    "c": [".....", ".....", ".####", "#....", "#....", "#....", ".####"],
    "d": ["....#", "....#", ".####", "#...#", "#...#", "#...#", ".####"],
    "e": [".....", ".....", ".###.", "#...#", "#####", "#....", ".####"],
    "f": ["..##.", ".#...", "####.", ".#...", ".#...", ".#...", ".#..."],
    "g": [".....", ".....", ".###.", "#...#", ".####", "....#", "####."],
    "h": ["#....", "#....", "####.", "#...#", "#...#", "#...#", "#...#"],
    "i": ["..#..", ".....", ".##..", "..#..", "..#..", "..#..", ".###."],
    "j": ["...#.", ".....", "..##.", "...#.", "...#.", "#..#.", ".##.."],
    "k": ["#....", "#....", "#..#.", "#.#..", "##...", "#.#..", "#..#."],
    "l": [".##..", "..#..", "..#..", "..#..", "..#..", "..#..", ".###."],
    "m": [".....", ".....", "##.#.", "#.#.#", "#.#.#", "#...#", "#...#"],
    "n": [".....", ".....", "####.", "#...#", "#...#", "#...#", "#...#"],
    "o": [".....", ".....", ".###.", "#...#", "#...#", "#...#", ".###."],
    "p": [".....", ".....", "####.", "#...#", "####.", "#....", "#...."],
    "q": [".....", ".....", ".####", "#...#", ".####", "....#", "....#"],
    "r": [".....", ".....", "#.##.", "##...", "#....", "#....", "#...."],
    "s": [".....", ".....", ".####", "#....", ".###.", "....#", "####."],
    "t": [".#...", ".#...", "####.", ".#...", ".#...", ".#..#", "..##."],
    "u": [".....", ".....", "#...#", "#...#", "#...#", "#..##", ".##.#"],
    "v": [".....", ".....", "#...#", "#...#", "#...#", ".#.#.", "..#.."],
    "w": [".....", ".....", "#...#", "#...#", "#.#.#", "#.#.#", ".#.#."],
    "x": [".....", ".....", "#...#", ".#.#.", "..#..", ".#.#.", "#...#"],
    "y": [".....", ".....", "#...#", "#...#", ".####", "....#", ".###."],
    "z": [".....", ".....", "#####", "...#.", "..#..", ".#...", "#####"],
    "0": [".###.", "#..##", "#.#.#", "#.#.#", "##..#", "#...#", ".###."],
    "1": ["..#..", ".##..", "..#..", "..#..", "..#..", "..#..", "#####"],
    "2": [".###.", "#...#", "....#", "..##.", ".#...", "#....", "#####"],
    "3": ["####.", "....#", "....#", ".###.", "....#", "....#", "####."],
    "4": ["#...#", "#...#", "#...#", "#####", "....#", "....#", "....#"],
    "5": ["#####", "#....", "####.", "....#", "....#", "#...#", ".###."],
    "6": [".###.", "#....", "#....", "####.", "#...#", "#...#", ".###."],
    "7": ["#####", "....#", "...#.", "..#..", ".#...", ".#...", ".#..."],
    "8": [".###.", "#...#", "#...#", ".###.", "#...#", "#...#", ".###."],
    "9": [".###.", "#...#", "#...#", ".####", "....#", "....#", ".###."],
    ".": [".....", ".....", ".....", ".....", ".....", ".##..", ".##.."],
    ",": [".....", ".....", ".....", ".....", ".....", "..#..", ".#..."],
    ":": [".....", ".##..", ".##..", ".....", ".##..", ".##..", "....."],
    ";": [".....", "..#..", ".....", ".....", "..#..", "..#..", ".#..."],
    "-": [".....", ".....", ".....", "#####", ".....", ".....", "....."],
    "+": [".....", "..#..", "..#..", "#####", "..#..", "..#..", "....."],
    "/": ["....#", "...#.", "...#.", "..#..", ".#...", ".#...", "#...."],
    "&": [".##..", "#..#.", "#.#..", ".##..", "#.#.#", "#..#.", ".##.#"],
    "$": ["..#..", ".####", "#.#..", ".###.", "..#.#", "####.", "..#.."],
    "%": ["##..#", "##.#.", "..#..", "..#..", ".#...", "#..##", "#..##"],
    "(": ["..#..", ".#...", "#....", "#....", "#....", ".#...", "..#.."],
    ")": ["..#..", "...#.", "....#", "....#", "....#", "...#.", "..#.."],
    "!": ["..#..", "..#..", "..#..", "..#..", "..#..", ".....", "..#.."],
    "'": ["..#..", "..#..", ".#...", ".....", ".....", ".....", "....."],
    "|": ["..#..", "..#..", "..#..", "..#..", "..#..", "..#..", "..#.."],
    "·": [".....", ".....", ".....", "..##.", "..##.", ".....", "....."],
    ">": [".#...", "..#..", "...#.", "....#", "...#.", "..#..", ".#..."],
    "<": ["...#.", "..#..", ".#...", "#....", ".#...", "..#..", "...#."],
    "=": [".....", ".....", "#####", ".....", "#####", ".....", "....."],
    "?": [".###.", "#...#", "....#", "..##.", "..#..", ".....", "..#.."],
    "~": [".....", ".....", ".#.#.", "..#.#", ".....", ".....", "....."],
}


def clamp_byte(v):
    return 0 if v < 0 else (255 if v > 255 else int(v + 0.5))


def lerp_color(c1, c2, t):
    if t <= 0.0:
        return c1
    if t >= 1.0:
        return c2
    return (
        c1[0] + (c2[0] - c1[0]) * t,
        c1[1] + (c2[1] - c1[1]) * t,
        c1[2] + (c2[2] - c1[2]) * t,
    )


class Canvas:
    """Anti-aliased RGB raster canvas using pure Python standard library."""

    def __init__(self, width=WIDTH, height=HEIGHT, bg=(244, 239, 230)):
        self.w = width
        self.h = height
        r, g, b = bg
        row = bytes([r, g, b]) * width
        self.buf = bytearray(row * height)

    def blend_px(self, x, y, color, alpha):
        if alpha <= 0.0 or x < 0 or y < 0 or x >= self.w or y >= self.h:
            return
        idx = (y * self.w + x) * 3
        if alpha >= 0.999:
            self.buf[idx] = clamp_byte(color[0])
            self.buf[idx + 1] = clamp_byte(color[1])
            self.buf[idx + 2] = clamp_byte(color[2])
            return
        inv = 1.0 - alpha
        self.buf[idx] = clamp_byte(self.buf[idx] * inv + color[0] * alpha)
        self.buf[idx + 1] = clamp_byte(self.buf[idx + 1] * inv + color[1] * alpha)
        self.buf[idx + 2] = clamp_byte(self.buf[idx + 2] * inv + color[2] * alpha)

    def fill_rect(self, x0, y0, x1, y1, color, alpha=1.0):
        ix0 = max(0, int(math.floor(x0)))
        iy0 = max(0, int(math.floor(y0)))
        ix1 = min(self.w, int(math.ceil(x1)))
        iy1 = min(self.h, int(math.ceil(y1)))
        if alpha >= 0.999 and ix0 >= 0 and iy0 >= 0:
            r, g, b = clamp_byte(color[0]), clamp_byte(color[1]), clamp_byte(color[2])
            span = ix1 - ix0
            if span <= 0:
                return
            row_bytes = bytes([r, g, b]) * span
            for y in range(iy0, iy1):
                start = (y * self.w + ix0) * 3
                self.buf[start:start + span * 3] = row_bytes
            return
        for y in range(iy0, iy1):
            for x in range(ix0, ix1):
                self.blend_px(x, y, color, alpha)

    def fill_vgradient(self, x0, y0, x1, y1, c_top, c_bot):
        ix0 = max(0, int(x0))
        iy0 = max(0, int(y0))
        ix1 = min(self.w, int(x1))
        iy1 = min(self.h, int(y1))
        span = ix1 - ix0
        h = max(1, iy1 - iy0 - 1)
        if span <= 0:
            return
        for y in range(iy0, iy1):
            t = (y - iy0) / h
            c = lerp_color(c_top, c_bot, t)
            row_bytes = bytes([clamp_byte(c[0]), clamp_byte(c[1]), clamp_byte(c[2])]) * span
            start = (y * self.w + ix0) * 3
            self.buf[start:start + span * 3] = row_bytes

    def fill_rounded_rect(self, x0, y0, x1, y1, radius, color, alpha=1.0):
        cx = (x0 + x1) * 0.5
        cy = (y0 + y1) * 0.5
        hw = (x1 - x0) * 0.5 - radius
        hh = (y1 - y0) * 0.5 - radius
        ix0 = max(0, int(math.floor(x0 - 1)))
        iy0 = max(0, int(math.floor(y0 - 1)))
        ix1 = min(self.w, int(math.ceil(x1 + 1)))
        iy1 = min(self.h, int(math.ceil(y1 + 1)))
        for y in range(iy0, iy1):
            dy = abs(y + 0.5 - cy) - hh
            ady = max(0.0, dy)
            for x in range(ix0, ix1):
                dx = abs(x + 0.5 - cx) - hw
                adx = max(0.0, dx)
                dist = math.hypot(adx, ady) + min(max(dx, dy), 0.0) - radius
                cov = max(0.0, min(1.0, 0.5 - dist))
                if cov > 0.0:
                    self.blend_px(x, y, color, cov * alpha)

    def stroke_rounded_rect(self, x0, y0, x1, y1, radius, thickness, color, alpha=1.0):
        cx = (x0 + x1) * 0.5
        cy = (y0 + y1) * 0.5
        hw = (x1 - x0) * 0.5 - radius
        hh = (y1 - y0) * 0.5 - radius
        half_t = thickness * 0.5
        ix0 = max(0, int(math.floor(x0 - half_t - 1)))
        iy0 = max(0, int(math.floor(y0 - half_t - 1)))
        ix1 = min(self.w, int(math.ceil(x1 + half_t + 1)))
        iy1 = min(self.h, int(math.ceil(y1 + half_t + 1)))
        for y in range(iy0, iy1):
            dy = abs(y + 0.5 - cy) - hh
            ady = max(0.0, dy)
            for x in range(ix0, ix1):
                dx = abs(x + 0.5 - cx) - hw
                adx = max(0.0, dx)
                sdf = math.hypot(adx, ady) + min(max(dx, dy), 0.0) - radius
                dist = abs(sdf) - half_t
                cov = max(0.0, min(1.0, 0.5 - dist))
                if cov > 0.0:
                    self.blend_px(x, y, color, cov * alpha)

    def fill_circle(self, cx, cy, r, color, alpha=1.0):
        ix0 = max(0, int(math.floor(cx - r - 1)))
        iy0 = max(0, int(math.floor(cy - r - 1)))
        ix1 = min(self.w, int(math.ceil(cx + r + 1)))
        iy1 = min(self.h, int(math.ceil(cy + r + 1)))
        for y in range(iy0, iy1):
            dy = y + 0.5 - cy
            for x in range(ix0, ix1):
                dx = x + 0.5 - cx
                dist = math.hypot(dx, dy) - r
                cov = max(0.0, min(1.0, 0.5 - dist))
                if cov > 0.0:
                    self.blend_px(x, y, color, cov * alpha)

    def stroke_circle(self, cx, cy, r, thickness, color, alpha=1.0):
        half_t = thickness * 0.5
        ix0 = max(0, int(math.floor(cx - r - half_t - 1)))
        iy0 = max(0, int(math.floor(cy - r - half_t - 1)))
        ix1 = min(self.w, int(math.ceil(cx + r + half_t + 1)))
        iy1 = min(self.h, int(math.ceil(cy + r + half_t + 1)))
        for y in range(iy0, iy1):
            dy = y + 0.5 - cy
            for x in range(ix0, ix1):
                dx = x + 0.5 - cx
                dist = abs(math.hypot(dx, dy) - r) - half_t
                cov = max(0.0, min(1.0, 0.5 - dist))
                if cov > 0.0:
                    self.blend_px(x, y, color, cov * alpha)

    def draw_line(self, x0, y0, x1, y1, thickness, color, alpha=1.0):
        vx = x1 - x0
        vy = y1 - y0
        len_sq = vx * vx + vy * vy
        half_t = thickness * 0.5
        pad = half_t + 1.5
        ix0 = max(0, int(math.floor(min(x0, x1) - pad)))
        iy0 = max(0, int(math.floor(min(y0, y1) - pad)))
        ix1 = min(self.w, int(math.ceil(max(x0, x1) + pad)))
        iy1 = min(self.h, int(math.ceil(max(y0, y1) + pad)))
        for y in range(iy0, iy1):
            py = y + 0.5
            for x in range(ix0, ix1):
                px = x + 0.5
                if len_sq == 0.0:
                    d = math.hypot(px - x0, py - y0)
                else:
                    t = max(0.0, min(1.0, ((px - x0) * vx + (py - y0) * vy) / len_sq))
                    d = math.hypot(px - (x0 + t * vx), py - (y0 + t * vy))
                cov = max(0.0, min(1.0, 0.5 - (d - half_t)))
                if cov > 0.0:
                    self.blend_px(x, y, color, cov * alpha)

    def fill_polygon(self, pts, color, alpha=1.0):
        if len(pts) < 3:
            return
        xs = [p[0] for p in pts]
        ys = [p[1] for p in pts]
        ix0 = max(0, int(math.floor(min(xs) - 1)))
        iy0 = max(0, int(math.floor(min(ys) - 1)))
        ix1 = min(self.w, int(math.ceil(max(xs) + 1)))
        iy1 = min(self.h, int(math.ceil(max(ys) + 1)))
        n = len(pts)
        edges = [(pts[i], pts[(i + 1) % n]) for i in range(n)]
        sub_offsets = (0.25, 0.75)
        for y in range(iy0, iy1):
            for x in range(ix0, ix1):
                hits = 0
                for oy in sub_offsets:
                    sy = y + oy
                    for ox in sub_offsets:
                        sx = x + ox
                        inside = False
                        for (ax, ay), (bx, by) in edges:
                            if (ay > sy) != (by > sy):
                                x_int = ax + (sy - ay) * (bx - ax) / (by - ay)
                                if sx < x_int:
                                    inside = not inside
                        if inside:
                            hits += 1
                if hits:
                    self.blend_px(x, y, color, (hits * 0.25) * alpha)

    def measure_text(self, text, scale=2, tracking=1):
        if not text:
            return 0
        step = (5 + tracking) * scale
        return len(text) * step - tracking * scale

    def draw_text(self, x, y, text, color, scale=2, tracking=1, bold=False, alpha=1.0):
        cur_x = int(x)
        base_y = int(y)
        step = (5 + tracking) * scale
        for ch in text:
            glyph = FONT_5X7.get(ch)
            if glyph is None:
                glyph = FONT_5X7.get(ch.upper(), FONT_5X7[" "])
            for row_i, row_str in enumerate(glyph):
                for col_i, bit in enumerate(row_str):
                    if bit == "#":
                        px0 = cur_x + col_i * scale
                        py0 = base_y + row_i * scale
                        w_extra = max(1, scale // 2) if bold else 0
                        self.fill_rect(px0, py0, px0 + scale + w_extra, py0 + scale, color, alpha=alpha)
            cur_x += step

    def draw_text_centered(self, cx, y, text, color, scale=2, tracking=1, bold=False, alpha=1.0):
        w = self.measure_text(text, scale=scale, tracking=tracking)
        if bold:
            w += max(1, scale // 2)
        self.draw_text(cx - w // 2, y, text, color, scale=scale, tracking=tracking, bold=bold, alpha=alpha)

    def to_png_bytes(self):
        """Encode RGB buffer as a valid filtered PNG byte stream."""
        stride = self.w * 3
        raw = bytearray((stride + 1) * self.h)
        for y in range(self.h):
            row_start = y * stride
            out_start = y * (stride + 1)
            raw[out_start] = 1  # Sub filter for tight lossless compression
            row_slice = self.buf[row_start:row_start + stride]
            raw[out_start + 1] = row_slice[0]
            raw[out_start + 2] = row_slice[1]
            raw[out_start + 3] = row_slice[2]
            for i in range(3, stride):
                raw[out_start + 1 + i] = (row_slice[i] - row_slice[i - 3]) & 0xFF

        compressed = zlib.compress(bytes(raw), level=9)

        def chunk(tag, payload):
            crc = zlib.crc32(tag + payload) & 0xFFFFFFFF
            return struct.pack(">I", len(payload)) + tag + payload + struct.pack(">I", crc)

        ihdr = struct.pack(">IIBBBBB", self.w, self.h, 8, 2, 0, 0, 0)
        return b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", ihdr) + chunk(b"IDAT", compressed) + chunk(b"IEND", b"")


def draw_badge(c, x, y, text, bg_color, fg_color=(255, 255, 255), scale=2):
    pad_x = 10
    pad_y = 5
    tw = c.measure_text(text, scale=scale)
    th = 7 * scale
    c.fill_rounded_rect(x, y, x + tw + pad_x * 2, y + th + pad_y * 2, 6, bg_color)
    c.draw_text(x + pad_x, y + pad_y, text, fg_color, scale=scale, bold=True)
    return tw + pad_x * 2


def draw_masthead(c):
    c.fill_vgradient(0, 0, 1024, 134, (15, 23, 42), (24, 36, 62))
    c.fill_rect(0, 0, 1024, 7, (220, 38, 38))
    c.fill_rect(0, 131, 1024, 135, (217, 119, 6))

    # Top kicker line
    c.draw_text(28, 19, "THURSDAY · 19 NOVEMBER 2026", (251, 191, 36), scale=2, bold=True)
    draw_badge(c, 816, 15, "GLOBAL EDITION", (185, 28, 28), (255, 255, 255), scale=2)

    # Hero Masthead
    c.draw_text_centered(512, 47, "WORLD NEWS · 19 NOV 2026", (255, 255, 255), scale=5, tracking=1, bold=True)

    # Summary strip inside masthead
    c.draw_text_centered(
        512,
        101,
        "SHENZHEN SUMMIT · $81.3B AI IPO · GREENLAND 109-0 · GTA VI · FRONTLINES",
        (203, 213, 225),
        scale=2,
    )


def draw_apec_panel(c):
    x0, y0, x1, y1 = 24, 152, 548, 548
    c.fill_rounded_rect(x0 + 3, y0 + 4, x1 + 3, y1 + 4, 14, (206, 198, 184))
    c.fill_rounded_rect(x0, y0, x1, y1, 14, (255, 252, 246))
    c.stroke_rounded_rect(x0, y0, x1, y1, 14, 2, (30, 41, 59))

    # Header
    draw_badge(c, x0 + 16, y0 + 14, "ASIA-PACIFIC · DIPLOMACY", (185, 28, 28), scale=2)
    c.draw_text(x0 + 16, y0 + 48, "APEC: TRUMP, XI, PUTIN", (15, 23, 42), scale=3, bold=True)

    # Illustration Canvas
    ix0, iy0, ix1, iy1 = x0 + 16, y0 + 82, x1 - 16, y0 + 286
    c.fill_vgradient(ix0, iy0, ix1, iy1 - 44, (24, 42, 74), (190, 92, 66))
    c.fill_vgradient(ix0, iy1 - 44, ix1, iy1, (18, 30, 52), (12, 20, 36))

    # Shenzhen skyline silhouettes
    skyline = [
        (0, 48, 28), (30, 74, 34), (66, 56, 26), (100, 92, 32), (138, 64, 30),
        (220, 128, 22), (246, 86, 28), (280, 66, 30), (350, 78, 32), (388, 102, 28),
        (422, 68, 30), (456, 54, 36),
    ]
    base_sky_y = iy1 - 44
    for sx, sh, sw in skyline:
        bx = ix0 + sx
        c.fill_rect(bx, base_sky_y - sh, bx + sw, base_sky_y, (17, 24, 39))
    # Ping An Tower spire (bounded strictly inside [iy0, iy1])
    c.fill_polygon([(ix0 + 231, base_sky_y - 146), (ix0 + 223, base_sky_y - 122), (ix0 + 239, base_sky_y - 122)], (17, 24, 39))
    c.draw_line(ix0 + 231, base_sky_y - 154, ix0 + 231, base_sky_y - 142, 2, (251, 191, 36))

    # Harbor reflections
    for rx in range(ix0 + 12, ix1 - 20, 36):
        c.fill_rect(rx, iy1 - 32, rx + 22, iy1 - 29, (245, 158, 11), alpha=0.45)
        c.fill_rect(rx + 8, iy1 - 18, rx + 26, iy1 - 16, (251, 191, 36), alpha=0.3)

    # Summit conference table strictly inside illustration frame
    tbl_cx = (ix0 + ix1) // 2
    c.fill_rounded_rect(tbl_cx - 104, iy1 - 36, tbl_cx + 104, iy1 - 10, 10, (120, 53, 15))
    c.stroke_rounded_rect(tbl_cx - 104, iy1 - 36, tbl_cx + 104, iy1 - 10, 10, 2, (251, 191, 36))
    c.fill_rect(ix0, iy1 - 8, ix1, iy1, (15, 23, 42))

    # Left podium: USA
    ux, uy = tbl_cx - 135, iy0 + 114
    c.fill_rounded_rect(ux - 44, uy - 34, ux + 44, uy + 24, 8, (30, 58, 138))
    c.fill_rect(ux - 40, uy - 28, ux + 40, uy - 18, (220, 38, 38))
    c.fill_rect(ux - 40, uy - 14, ux + 40, uy - 6, (255, 255, 255))
    c.fill_rect(ux - 40, uy - 2, ux + 40, uy + 6, (220, 38, 38))
    c.fill_rect(ux - 40, uy - 28, ux - 6, uy - 4, (29, 78, 216))
    c.draw_text_centered(ux, uy + 8, "TRUMP", (255, 255, 255), scale=2, bold=True)

    # Center podium: CHINA (APEC Host)
    cx_p, cy_p = tbl_cx, iy0 + 78
    c.fill_rounded_rect(cx_p - 48, cy_p - 34, cx_p + 48, cy_p + 24, 8, (185, 28, 28))
    c.fill_circle(cx_p - 22, cy_p - 16, 8, (251, 191, 36))
    c.fill_circle(cx_p - 6, cy_p - 22, 3, (251, 191, 36))
    c.fill_circle(cx_p - 2, cy_p - 13, 3, (251, 191, 36))
    c.draw_text_centered(cx_p, cy_p + 7, "XI · HOST", (255, 255, 255), scale=2, bold=True)

    # Right podium: RUSSIA
    rx_p, ry_p = tbl_cx + 135, iy0 + 114
    c.fill_rounded_rect(rx_p - 44, ry_p - 34, rx_p + 44, ry_p + 24, 8, (30, 41, 59))
    c.fill_rect(rx_p - 40, ry_p - 28, rx_p + 40, ry_p - 17, (255, 255, 255))
    c.fill_rect(rx_p - 40, ry_p - 17, rx_p + 40, ry_p - 6, (37, 99, 235))
    c.fill_rect(rx_p - 40, ry_p - 6, rx_p + 40, ry_p + 5, (220, 38, 38))
    c.draw_text_centered(rx_p, ry_p + 8, "PUTIN", (255, 255, 255), scale=2, bold=True)

    # Diplomatic risk-reduction / status badges inside upper corners
    draw_badge(c, ix0 + 10, iy0 + 10, "SHENZHEN", (15, 23, 42), (251, 191, 36), scale=2)
    no_deal_w = c.measure_text("TALKS: NO DEAL", scale=2) + 20
    draw_badge(c, ix1 - no_deal_w - 8, iy0 + 10, "TALKS: NO DEAL", (127, 29, 29), (254, 226, 226), scale=2)

    # Caption takeaways
    c.draw_text(x0 + 18, y0 + 298, "3-WAY TALKS ON APEC SIDELINES", (185, 28, 28), scale=2, bold=True)
    c.draw_text(x0 + 18, y0 + 324, "- Joint pledge on nuclear risk dialogue", (30, 41, 59), scale=2)
    c.draw_text(x0 + 18, y0 + 348, "- No deal on Ukraine, Iran or trade", (30, 41, 59), scale=2)
    c.draw_text(x0 + 18, y0 + 372, "- EU allies meet in Berlin in alarm", (30, 41, 59), scale=2)


def draw_anthropic_panel(c):
    x0, y0, x1, y1 = 568, 152, 1000, 548
    c.fill_rounded_rect(x0 + 3, y0 + 4, x1 + 3, y1 + 4, 14, (206, 198, 184))
    c.fill_rounded_rect(x0, y0, x1, y1, 14, (255, 252, 246))
    c.stroke_rounded_rect(x0, y0, x1, y1, 14, 2, (30, 41, 59))

    draw_badge(c, x0 + 16, y0 + 14, "MARKETS & AI · NASDAQ: ANT", (4, 120, 87), scale=2)
    c.draw_text(x0 + 16, y0 + 48, "ANTHROPIC $81.3B IPO", (15, 23, 42), scale=3, bold=True)

    # Chart illustration
    ix0, iy0, ix1, iy1 = x0 + 16, y0 + 82, x1 - 16, y0 + 286
    c.fill_vgradient(ix0, iy0, ix1, iy1, (6, 44, 34), (11, 24, 38))

    # Subtle grid
    for gy in range(iy0 + 32, iy1, 36):
        c.draw_line(ix0 + 12, gy, ix1 - 12, gy, 1, (30, 75, 62))
    for gx in range(ix0 + 48, ix1, 64):
        c.draw_line(gx, iy0 + 12, gx, iy1 - 12, 1, (30, 75, 62))

    # Area polygon + glowing chart line ($74 target -> $83 IPO -> $111.50 open -> $97.17 close)
    pts = [
        (ix0 + 24, iy1 - 36),
        (ix0 + 112, iy1 - 64),
        (ix0 + 206, iy0 + 42),
        (ix0 + 298, iy0 + 88),
        (ix1 - 24, iy0 + 78),
    ]
    poly = [(pts[0][0], iy1 - 14)] + pts + [(pts[-1][0], iy1 - 14)]
    c.fill_polygon(poly, (16, 185, 129), alpha=0.28)
    for i in range(len(pts) - 1):
        c.draw_line(pts[i][0], pts[i][1], pts[i + 1][0], pts[i + 1][1], 5, (52, 211, 153))
    for px, py in pts:
        c.fill_circle(px, py, 6, (255, 255, 255))
        c.stroke_circle(px, py, 6, 2, (5, 150, 105))

    # Key figure overlays
    c.draw_text(ix0 + 14, iy0 + 12, "$81.3B", (52, 211, 153), scale=3, bold=True)
    c.draw_text(ix0 + 14, iy0 + 40, "LARGEST IPO EVER", (209, 250, 229), scale=2)
    c.draw_text(ix0 + 16, iy1 - 32, "IPO $83", (167, 243, 208), scale=2, bold=True)
    c.draw_text(ix1 - 154, iy0 + 14, "OPEN $111.50", (251, 191, 36), scale=2, bold=True)
    c.draw_text(ix1 - 154, iy1 - 32, "CLOSE $97.17", (255, 255, 255), scale=2, bold=True)

    # Caption
    c.draw_text(x0 + 18, y0 + 298, "$1.5T VALUATION · 980M SHARES", (4, 120, 87), scale=2, bold=True)
    c.draw_text(x0 + 18, y0 + 324, "- Record $81.3B Nasdaq debut", (30, 41, 59), scale=2)
    c.draw_text(x0 + 18, y0 + 348, "- Hit >$2T intraday; $1.3T cap", (30, 41, 59), scale=2)
    c.draw_text(x0 + 18, y0 + 372, "- AZ AG probes AI bank agents", (180, 83, 9), scale=2)


def draw_greenland_panel(c):
    x0, y0, x1, y1 = 24, 568, 336, 922
    c.fill_rounded_rect(x0 + 3, y0 + 4, x1 + 3, y1 + 4, 14, (206, 198, 184))
    c.fill_rounded_rect(x0, y0, x1, y1, 14, (255, 252, 246))
    c.stroke_rounded_rect(x0, y0, x1, y1, 14, 2, (30, 41, 59))

    draw_badge(c, x0 + 14, y0 + 14, "EUROPE · ARCTIC", (29, 78, 216), scale=2)
    c.draw_text(x0 + 14, y0 + 46, "GREENLAND PACT", (15, 23, 42), scale=3, bold=True)

    ix0, iy0, ix1, iy1 = x0 + 14, y0 + 76, x1 - 14, y0 + 242
    c.fill_vgradient(ix0, iy0, ix1, iy1, (12, 74, 110), (7, 45, 76))

    # Polar latitude rings
    cx, cy = (ix0 + ix1) // 2 + 24, (iy0 + iy1) // 2
    c.stroke_circle(cx, cy, 42, 1, (56, 189, 248), alpha=0.45)
    c.stroke_circle(cx, cy, 68, 1, (56, 189, 248), alpha=0.35)

    # Stylized Greenland landmass silhouette
    gl_pts = [
        (cx - 22, iy0 + 24), (cx + 16, iy0 + 18), (cx + 42, iy0 + 34),
        (cx + 32, iy0 + 66), (cx + 20, iy0 + 98), (cx - 4, iy1 - 22),
        (cx - 20, iy1 - 36), (cx - 28, iy0 + 82), (cx - 34, iy0 + 50),
    ]
    c.fill_polygon(gl_pts, (224, 242, 254))
    # Ice cap contour
    gl_inner = [(p[0] * 0.7 + cx * 0.3, p[1] * 0.7 + cy * 0.3) for p in gl_pts]
    c.fill_polygon(gl_inner, (255, 255, 255))

    # Defense base markers (Pituffik, Mestersvig, Narsarsuaq)
    for bx, by in [(cx - 24, iy0 + 48), (cx + 24, iy0 + 66), (cx - 8, iy1 - 30)]:
        c.stroke_circle(bx, by, 10, 2, (251, 191, 36))
        c.fill_circle(bx, by, 4, (239, 68, 68))

    draw_badge(c, ix0 + 8, iy0 + 8, "109-0 VOTE", (29, 78, 216), (255, 255, 255), scale=2)

    c.draw_text(x0 + 14, y0 + 252, "DENMARK VOTES 109-0", (29, 78, 216), scale=2, bold=True)
    c.draw_text(x0 + 14, y0 + 276, "- US Arctic defense", (30, 41, 59), scale=2)
    c.draw_text(x0 + 14, y0 + 298, "- Base access + Dome", (30, 41, 59), scale=2)
    c.draw_text(x0 + 14, y0 + 320, "- Self-rule & NATO", (30, 41, 59), scale=2)


def draw_gtavi_panel(c):
    x0, y0, x1, y1 = 356, 568, 668, 922
    c.fill_rounded_rect(x0 + 3, y0 + 4, x1 + 3, y1 + 4, 14, (206, 198, 184))
    c.fill_rounded_rect(x0, y0, x1, y1, 14, (255, 252, 246))
    c.stroke_rounded_rect(x0, y0, x1, y1, 14, 2, (30, 41, 59))

    draw_badge(c, x0 + 14, y0 + 14, "CULTURE · GAMING", (124, 58, 237), scale=2)
    c.draw_text(x0 + 14, y0 + 46, "GTA VI LAUNCHES", (15, 23, 42), scale=3, bold=True)

    ix0, iy0, ix1, iy1 = x0 + 14, y0 + 76, x1 - 14, y0 + 242
    c.fill_vgradient(ix0, iy0, ix1, iy0 + 96, (91, 33, 182), (236, 72, 153))
    c.fill_vgradient(ix0, iy0 + 96, ix1, iy1, (249, 115, 22), (49, 16, 66))

    # Retro sun & ocean horizon
    c.fill_circle((ix0 + ix1) // 2, iy0 + 96, 42, (253, 224, 71))
    c.fill_rect(ix0, iy0 + 96, ix1, iy0 + 100, (236, 72, 153))
    c.fill_rect(ix0, iy0 + 106, ix1, iy0 + 109, (236, 72, 153))

    # Vice skyline silhouettes
    for sx, sh, sw in [(14, 48, 20), (38, 62, 18), (62, 42, 22), (204, 56, 20), (228, 68, 22), (254, 44, 18)]:
        c.fill_rect(ix0 + sx, iy1 - sh, ix0 + sx + sw, iy1, (24, 16, 44))
    # Palm fronds left & right
    c.draw_line(ix0 + 12, iy1, ix0 + 36, iy0 + 58, 4, (24, 16, 44))
    c.draw_line(ix0 + 36, iy0 + 58, ix0 + 16, iy0 + 50, 3, (24, 16, 44))
    c.draw_line(ix0 + 36, iy0 + 58, ix0 + 58, iy0 + 52, 3, (24, 16, 44))
    c.draw_line(ix0 + 36, iy0 + 58, ix0 + 48, iy0 + 72, 3, (24, 16, 44))
    c.draw_line(ix1 - 14, iy1, ix1 - 34, iy0 + 62, 4, (24, 16, 44))
    c.draw_line(ix1 - 34, iy0 + 62, ix1 - 54, iy0 + 54, 3, (24, 16, 44))
    c.draw_line(ix1 - 34, iy0 + 62, ix1 - 14, iy0 + 54, 3, (24, 16, 44))
    c.draw_line(ix1 - 34, iy0 + 62, ix1 - 46, iy0 + 76, 3, (24, 16, 44))

    # Bold "VI" emblem
    c.draw_text_centered((ix0 + ix1) // 2 + 2, iy0 + 58, "VI", (24, 16, 44), scale=6, bold=True)
    c.draw_text_centered((ix0 + ix1) // 2, iy0 + 56, "VI", (34, 211, 238), scale=6, bold=True)
    draw_badge(c, ix0 + 10, iy0 + 10, "AFTER 13 YRS", (24, 16, 44), (253, 224, 71), scale=2)

    c.draw_text(x0 + 14, y0 + 252, "NOV 19 GLOBAL DEBUT", (124, 58, 237), scale=2, bold=True)
    c.draw_text(x0 + 14, y0 + 276, "- PS5 & Xbox X|S out", (30, 41, 59), scale=2)
    c.draw_text(x0 + 14, y0 + 298, "- Record stream peak", (30, 41, 59), scale=2)
    c.draw_text(x0 + 14, y0 + 320, "- Global web surge", (30, 41, 59), scale=2)


def draw_frontlines_panel(c):
    x0, y0, x1, y1 = 688, 568, 1000, 922
    c.fill_rounded_rect(x0 + 3, y0 + 4, x1 + 3, y1 + 4, 14, (206, 198, 184))
    c.fill_rounded_rect(x0, y0, x1, y1, 14, (255, 252, 246))
    c.stroke_rounded_rect(x0, y0, x1, y1, 14, 2, (30, 41, 59))

    draw_badge(c, x0 + 14, y0 + 14, "CONFLICTS · CRISES", (185, 28, 28), scale=2)
    c.draw_text(x0 + 14, y0 + 46, "GLOBAL FRONTS", (15, 23, 42), scale=3, bold=True)

    # Three distinct visual crisis bands inside panel
    bx0, bx1 = x0 + 14, x1 - 14
    # Band 1: Ukraine & Russian Refineries
    c.fill_rounded_rect(bx0, y0 + 78, bx1, y0 + 152, 8, (254, 242, 242))
    c.stroke_rounded_rect(bx0, y0 + 78, bx1, y0 + 152, 8, 1.5, (220, 38, 38))
    c.fill_rect(bx0 + 6, y0 + 98, bx0 + 17, y0 + 138, (71, 85, 105))
    c.fill_rect(bx0 + 21, y0 + 110, bx0 + 32, y0 + 138, (71, 85, 105))
    c.fill_circle(bx0 + 19, y0 + 94, 8, (239, 68, 68))
    c.draw_text(bx0 + 40, y0 + 86, "UKRAINE: -45% OIL", (185, 28, 28), scale=2, bold=True)
    c.draw_text(bx0 + 40, y0 + 109, "15/35 RU plants", (30, 41, 59), scale=2)
    c.draw_text(bx0 + 40, y0 + 129, "hit by strikes", (30, 41, 59), scale=2)

    # Band 2: Gaza & Iran Middle East Tensions
    c.fill_rounded_rect(bx0, y0 + 162, bx1, y0 + 236, 8, (255, 247, 237))
    c.stroke_rounded_rect(bx0, y0 + 162, bx1, y0 + 236, 8, 1.5, (217, 119, 6))
    c.fill_circle(bx0 + 20, y0 + 199, 12, (217, 119, 6))
    c.fill_rect(bx0 + 18, y0 + 191, bx0 + 22, y0 + 201, (255, 255, 255))
    c.fill_rect(bx0 + 18, y0 + 204, bx0 + 22, y0 + 208, (255, 255, 255))
    c.draw_text(bx0 + 40, y0 + 170, "GAZA & IRAN ALERT", (180, 83, 9), scale=2, bold=True)
    c.draw_text(bx0 + 40, y0 + 194, "UN winter aid warn", (30, 41, 59), scale=2)
    c.draw_text(bx0 + 40, y0 + 214, "Riyadh air alert", (30, 41, 59), scale=2)

    # Band 3: Sudan Drone Warfare
    c.fill_rounded_rect(bx0, y0 + 246, bx1, y0 + 324, 8, (241, 245, 249))
    c.stroke_rounded_rect(bx0, y0 + 246, bx1, y0 + 324, 8, 1.5, (51, 65, 85))
    c.draw_line(bx0 + 8, y0 + 278, bx0 + 32, y0 + 292, 3, (30, 41, 59))
    c.draw_line(bx0 + 8, y0 + 292, bx0 + 32, y0 + 278, 3, (30, 41, 59))
    c.fill_circle(bx0 + 20, y0 + 285, 5, (185, 28, 28))
    c.draw_text(bx0 + 40, y0 + 256, "SUDAN DRONE WAR", (30, 41, 59), scale=2, bold=True)
    c.draw_text(bx0 + 40, y0 + 280, "Drones top deaths", (30, 41, 59), scale=2)
    c.draw_text(bx0 + 40, y0 + 300, "Darfur airstrikes", (30, 41, 59), scale=2)


def draw_footer(c):
    c.fill_rounded_rect(24, 940, 1000, 1000, 10, (15, 23, 42))
    c.draw_text_centered(
        512,
        963,
        "19 NOV 2026 · AMERICAS · EUROPE · ASIA · MIDEAST · AFRICA",
        (251, 191, 36),
        scale=2,
        bold=True,
    )


def render_news_image(output_path):
    """Render the complete 1024x1024 editorial infographic and write it to output_path."""
    canvas = Canvas(WIDTH, HEIGHT, bg=(244, 239, 230))
    draw_masthead(canvas)
    draw_apec_panel(canvas)
    draw_anthropic_panel(canvas)
    draw_greenland_panel(canvas)
    draw_gtavi_panel(canvas)
    draw_frontlines_panel(canvas)
    draw_footer(canvas)
    png_bytes = canvas.to_png_bytes()
    with open(output_path, "wb") as f:
        f.write(png_bytes)
    return len(png_bytes)
