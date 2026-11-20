"""Generates the 1024x1024 world news front-page graphic for 19 November 2026."""

from pathlib import Path
import shutil
import subprocess
import tempfile


OUT_PATH = Path(__file__).resolve().parent / "entry.png"

CHROME_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    "/usr/bin/google-chrome",
    "/usr/bin/chromium",
    "/usr/bin/chromium-browser",
]


def locate_chrome() -> str:
    """Return the first available Chromium/Chrome executable path."""
    for candidate in CHROME_CANDIDATES:
        if Path(candidate).exists():
            return candidate
    for cmd in ("google-chrome", "chromium", "chrome"):
        found = shutil.which(cmd)
        if found:
            return found
    raise FileNotFoundError("Chrome binary not found on host.")


def render_shenzhen_svg() -> str:
    """Vector illustration for the US-China-Russia trilateral summit in Shenzhen."""
    return """
    <svg viewBox="0 0 490 184" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="szSky" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stop-color="#0B1325"/>
          <stop offset="72%" stop-color="#1D3557"/>
          <stop offset="100%" stop-color="#7C2D12"/>
        </linearGradient>
      </defs>
      <rect width="490" height="184" fill="url(#szSky)"/>
      <path d="M0,152 L24,152 L24,116 L46,116 L46,152 L60,152 L60,96 L88,96 L88,152
               L116,152 L116,108 L140,108 L140,152 L222,152 L222,88 L245,44 L268,88 L268,152
               L290,152 L290,102 L322,102 L322,152 L348,152 L348,92 L378,92 L378,152
               L406,152 L406,114 L436,114 L436,152 L456,152 L456,124 L490,124 L490,184 L0,184 Z"
            fill="#070D19" opacity="0.88"/>
      <rect x="0" y="152" width="490" height="32" fill="#0F172A"/>
      <line x1="126" y1="84" x2="245" y2="62" stroke="#FBBF24" stroke-width="2.4"/>
      <line x1="364" y1="84" x2="245" y2="62" stroke="#FBBF24" stroke-width="2.4"/>
      <line x1="126" y1="84" x2="364" y2="84" stroke="#93C5FD" stroke-width="1.8" stroke-dasharray="5,4"/>
      <g transform="translate(126,84)">
        <circle r="31" fill="#1E3A8A" stroke="#FFFFFF" stroke-width="2.4"/>
        <text y="-4" text-anchor="middle" fill="#FFFFFF" font-family="Arial, sans-serif" font-size="14" font-weight="800">USA</text>
        <text y="13" text-anchor="middle" fill="#BFDBFE" font-family="Arial, sans-serif" font-size="11" font-weight="700">TRUMP</text>
      </g>
      <g transform="translate(245,62)">
        <circle r="34" fill="#B91C1C" stroke="#FDE047" stroke-width="2.6"/>
        <text y="-4" text-anchor="middle" fill="#FEF08A" font-family="Arial, sans-serif" font-size="14" font-weight="800">CHINA</text>
        <text y="14" text-anchor="middle" fill="#FFFFFF" font-family="Arial, sans-serif" font-size="11" font-weight="700">XI · HOST</text>
      </g>
      <g transform="translate(364,84)">
        <circle r="31" fill="#1E293B" stroke="#93C5FD" stroke-width="2.4"/>
        <text y="-4" text-anchor="middle" fill="#FFFFFF" font-family="Arial, sans-serif" font-size="13.5" font-weight="800">RUSSIA</text>
        <text y="13" text-anchor="middle" fill="#CBD5E1" font-family="Arial, sans-serif" font-size="11" font-weight="700">PUTIN</text>
      </g>
      <rect x="316" y="10" width="164" height="24" rx="4" fill="rgba(15,23,42,0.9)" stroke="#F87171"/>
      <text x="398" y="26" text-anchor="middle" fill="#FECACA" font-family="Arial, sans-serif" font-size="10.5" font-weight="800">UKRAINE &amp; IRAN OMITTED</text>
      <rect x="64" y="146" width="362" height="28" rx="4" fill="#111827" stroke="#FBBF24" stroke-width="1.4"/>
      <text x="245" y="164" text-anchor="middle" fill="#FDE68A" font-family="Arial, sans-serif" font-size="11.5" font-weight="800">APEC SHENZHEN · NUCLEAR RISK &amp; UN REFORM</text>
    </svg>
    """


def render_anthropic_svg() -> str:
    """Vector illustration for Anthropic's Nasdaq ANT IPO debut."""
    return """
    <svg viewBox="0 0 470 184" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="antBg" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0%" stop-color="#052E24"/>
          <stop offset="100%" stop-color="#0F172A"/>
        </linearGradient>
      </defs>
      <rect width="470" height="184" fill="url(#antBg)"/>
      <g stroke="#134E4A" stroke-width="1">
        <line x1="0" y1="42" x2="470" y2="42"/>
        <line x1="0" y1="84" x2="470" y2="84"/>
        <line x1="0" y1="126" x2="470" y2="126"/>
        <line x1="115" y1="0" x2="115" y2="184"/>
        <line x1="235" y1="0" x2="235" y2="184"/>
        <line x1="355" y1="0" x2="355" y2="184"/>
      </g>
      <path d="M32,140 L152,130 L272,56 L422,86 L422,148 L32,148 Z" fill="#10B981" opacity="0.22"/>
      <polyline points="32,140 152,130 272,56 422,86" fill="none" stroke="#34D399" stroke-width="4.5" stroke-linejoin="round"/>
      <circle cx="32" cy="140" r="6" fill="#A7F3D0" stroke="#065F46" stroke-width="2"/>
      <circle cx="152" cy="130" r="7" fill="#FFFFFF" stroke="#059669" stroke-width="2.5"/>
      <circle cx="272" cy="56" r="7.5" fill="#FDE047" stroke="#B45309" stroke-width="2.5"/>
      <circle cx="422" cy="86" r="7" fill="#34D399" stroke="#FFFFFF" stroke-width="2.5"/>
      <text x="20" y="68" fill="#34D399" font-family="Georgia, serif" font-size="36" font-weight="700">$81B+</text>
      <text x="22" y="87" fill="#D1FAE5" font-family="Arial, sans-serif" font-size="11.5" font-weight="800">RAISED ON NASDAQ: ANT</text>
      <rect x="272" y="10" width="184" height="24" rx="4" fill="rgba(6,78,59,0.92)" stroke="#34D399"/>
      <text x="364" y="26" text-anchor="middle" fill="#A7F3D0" font-family="Arial, sans-serif" font-size="11" font-weight="800">RECORD TECH DEBUT</text>
      <rect x="20" y="146" width="430" height="28" rx="4" fill="#0B1320" stroke="#10B981" stroke-width="1.3"/>
      <text x="235" y="164" text-anchor="middle" fill="#ECFDF5" font-family="Arial, sans-serif" font-size="12" font-weight="800">IPO $83.00  |  OPEN $111.50  |  CLOSE $97.17</text>
    </svg>
    """


def render_icj_svg() -> str:
    """Vector illustration for the ICJ Rohingya genocide ruling against Myanmar."""
    return """
    <svg viewBox="0 0 320 136" xmlns="http://www.w3.org/2000/svg">
      <rect width="320" height="136" fill="#1E1B3A"/>
      <rect x="12" y="12" width="136" height="112" rx="6" fill="#2A2454" stroke="#A78BFA" stroke-width="1.2"/>
      <g transform="translate(80,58)">
        <line x1="0" y1="-28" x2="0" y2="28" stroke="#FDE68A" stroke-width="3"/>
        <line x1="-26" y1="28" x2="26" y2="28" stroke="#FDE68A" stroke-width="3"/>
        <line x1="-38" y1="-18" x2="38" y2="-18" stroke="#FDE68A" stroke-width="2.5"/>
        <path d="M-38,-18 L-48,8 L-28,8 Z" fill="none" stroke="#FBBF24" stroke-width="1.8"/>
        <path d="M38,-18 L28,8 L48,8 Z" fill="none" stroke="#FBBF24" stroke-width="1.8"/>
        <path d="M-50,8 Q-38,17 -26,8 Z" fill="#FBBF24"/>
        <path d="M26,8 Q38,17 50,8 Z" fill="#FBBF24"/>
      </g>
      <text x="80" y="109" text-anchor="middle" fill="#DDD6FE" font-family="Arial, sans-serif" font-size="10.5" font-weight="800">THE HAGUE · ICJ</text>
      <text x="234" y="44" text-anchor="middle" fill="#FFFFFF" font-family="Arial, sans-serif" font-size="13" font-weight="800">GAMBIA v. MYANMAR</text>
      <rect x="164" y="54" width="140" height="28" rx="4" fill="#991B1B" stroke="#FCA5A5" stroke-width="1.5"/>
      <text x="234" y="73" text-anchor="middle" fill="#FFFFFF" font-family="Arial, sans-serif" font-size="13" font-weight="800">GENOCIDE RULING</text>
      <rect x="164" y="92" width="140" height="24" rx="4" fill="#0F172A" stroke="#C4B5FD"/>
      <text x="234" y="108" text-anchor="middle" fill="#EDE9FE" font-family="Arial, sans-serif" font-size="10.5" font-weight="700">REPARATIONS ORDERED</text>
    </svg>
    """


def render_greenland_svg() -> str:
    """Vector illustration for Denmark's 109-0 Greenland Arctic Defense Pact vote."""
    return """
    <svg viewBox="0 0 320 136" xmlns="http://www.w3.org/2000/svg">
      <rect width="320" height="136" fill="#0B3B5C"/>
      <circle cx="115" cy="70" r="44" fill="none" stroke="#38BDF8" stroke-width="1.2" opacity="0.45"/>
      <circle cx="115" cy="70" r="68" fill="none" stroke="#38BDF8" stroke-width="1" stroke-dasharray="4,3" opacity="0.35"/>
      <path d="M90,22 L126,18 L152,32 L144,64 L132,96 L108,118 L86,104 L76,72 L72,44 Z"
            fill="#E0F2FE" stroke="#7DD3FC" stroke-width="2"/>
      <circle cx="88" cy="48" r="5.5" fill="#DC2626" stroke="#FDE047" stroke-width="2"/>
      <text x="16" y="52" fill="#BAE6FD" font-family="Arial, sans-serif" font-size="10" font-weight="800">PITUFFIK</text>
      <rect x="172" y="24" width="134" height="54" rx="6" fill="#0F172A" stroke="#60A5FA" stroke-width="1.8"/>
      <text x="239" y="54" text-anchor="middle" fill="#FFFFFF" font-family="Georgia, serif" font-size="24" font-weight="700">109 - 0</text>
      <text x="239" y="70" text-anchor="middle" fill="#93C5FD" font-family="Arial, sans-serif" font-size="10" font-weight="800">FOLKETING VOTE</text>
      <rect x="172" y="88" width="134" height="30" rx="4" fill="#1E3A8A" stroke="#93C5FD"/>
      <text x="239" y="107" text-anchor="middle" fill="#FFFFFF" font-family="Arial, sans-serif" font-size="10.5" font-weight="800">US-DK-GL ACCORD</text>
    </svg>
    """


def render_cop31_svg() -> str:
    """Vector illustration for the COP31 Antalya final-stretch climate text clash."""
    return """
    <svg viewBox="0 0 320 136" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="heatBg" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0%" stop-color="#451A03"/>
          <stop offset="100%" stop-color="#1E293B"/>
        </linearGradient>
      </defs>
      <rect width="320" height="136" fill="url(#heatBg)"/>
      <circle cx="84" cy="74" r="42" fill="#EA580C" opacity="0.28"/>
      <path d="M36,104 C36,64 132,64 132,104 Z" fill="#0F172A" stroke="#FDBA74" stroke-width="2"/>
      <path d="M86,32 L76,64 L92,79 L80,111" fill="none" stroke="#FDE047" stroke-width="3.2"/>
      <text x="84" y="124" text-anchor="middle" fill="#FED7AA" font-family="Arial, sans-serif" font-size="10" font-weight="800">ANTALYA DRAFT CLASH</text>
      <rect x="150" y="16" width="158" height="50" rx="6" fill="#7C2D12" stroke="#F97316" stroke-width="1.6"/>
      <text x="229" y="42" text-anchor="middle" fill="#FDE047" font-family="Georgia, serif" font-size="20" font-weight="700">2.8°C PATH</text>
      <text x="229" y="58" text-anchor="middle" fill="#FFEDD5" font-family="Arial, sans-serif" font-size="9.5" font-weight="800">WMO WARNING (vs 1.5°C)</text>
      <rect x="150" y="76" width="158" height="44" rx="4" fill="#0F172A" stroke="#FBBF24"/>
      <text x="229" y="95" text-anchor="middle" fill="#FEF08A" font-family="Arial, sans-serif" font-size="10" font-weight="800">35-BY-35 POWER GOAL</text>
      <text x="229" y="111" text-anchor="middle" fill="#FCA5A5" font-family="Arial, sans-serif" font-size="9.5" font-weight="700">US ABSENT · NGO PROTEST</text>
    </svg>
    """


def render_tatarstan_svg() -> str:
    """Vector illustration for Ukraine's Kaleykino oil hub strike in Tatarstan."""
    return """
    <svg viewBox="0 0 320 120" xmlns="http://www.w3.org/2000/svg">
      <rect width="320" height="120" fill="#18181B"/>
      <path d="M22,98 Q106,38 198,62" fill="none" stroke="#F87171" stroke-width="2.5" stroke-dasharray="5,3"/>
      <circle cx="22" cy="98" r="5" fill="#60A5FA"/>
      <text x="24" y="112" fill="#93C5FD" font-family="Arial, sans-serif" font-size="9.5" font-weight="800">UKRAINE UAV</text>
      <rect x="190" y="58" width="38" height="42" rx="3" fill="#3F3F46" stroke="#A1A1AA"/>
      <rect x="234" y="66" width="34" height="34" rx="3" fill="#3F3F46" stroke="#A1A1AA"/>
      <line x1="168" y1="96" x2="296" y2="96" stroke="#71717A" stroke-width="4"/>
      <circle cx="209" cy="54" r="16" fill="#EF4444" opacity="0.75"/>
      <circle cx="209" cy="52" r="8" fill="#FDE047"/>
      <rect x="164" y="8" width="146" height="23" rx="4" fill="#7F1D1D" stroke="#FCA5A5"/>
      <text x="237" y="23" text-anchor="middle" fill="#FFFFFF" font-family="Arial, sans-serif" font-size="10" font-weight="800">&gt;1,000 KM DEEP STRIKE</text>
      <text x="98" y="49" text-anchor="middle" fill="#FCA5A5" font-family="Arial, sans-serif" font-size="10.5" font-weight="800">DRUZHBA HUB</text>
    </svg>
    """


def render_crisis_svg() -> str:
    """Vector illustration for Gaza winter crisis and Sudan drone warfare."""
    return """
    <svg viewBox="0 0 320 120" xmlns="http://www.w3.org/2000/svg">
      <rect width="320" height="120" fill="#1F1711"/>
      <line x1="160" y1="8" x2="160" y2="112" stroke="#78350F" stroke-width="1.5"/>
      <polygon points="36,88 74,46 112,88" fill="#334155" stroke="#93C5FD" stroke-width="1.6"/>
      <rect x="14" y="88" width="132" height="12" fill="#0369A1" opacity="0.75"/>
      <line x1="34" y1="24" x2="28" y2="38" stroke="#7DD3FC" stroke-width="2"/>
      <line x1="58" y1="20" x2="52" y2="34" stroke="#7DD3FC" stroke-width="2"/>
      <line x1="84" y1="24" x2="78" y2="38" stroke="#7DD3FC" stroke-width="2"/>
      <text x="80" y="113" text-anchor="middle" fill="#BAE6FD" font-family="Arial, sans-serif" font-size="10.5" font-weight="800">GAZA WINTER FLOODS</text>
      <circle cx="240" cy="58" r="26" fill="none" stroke="#EF4444" stroke-width="1.5" stroke-dasharray="3,3"/>
      <line x1="222" y1="46" x2="258" y2="70" stroke="#F8FAFC" stroke-width="3"/>
      <line x1="222" y1="70" x2="258" y2="46" stroke="#F8FAFC" stroke-width="3"/>
      <circle cx="240" cy="58" r="6" fill="#EF4444"/>
      <text x="240" y="113" text-anchor="middle" fill="#FDE68A" font-family="Arial, sans-serif" font-size="10.5" font-weight="800">SUDAN DRONE TOLL</text>
    </svg>
    """


def render_gtavi_svg() -> str:
    """Vector illustration for GTA VI's worldwide 19 Nov launch."""
    return """
    <svg viewBox="0 0 320 120" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="viceSky" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stop-color="#3B0764"/>
          <stop offset="55%" stop-color="#DB2777"/>
          <stop offset="100%" stop-color="#F97316"/>
        </linearGradient>
      </defs>
      <rect width="320" height="120" fill="url(#viceSky)"/>
      <circle cx="160" cy="68" r="34" fill="#FDE047"/>
      <rect x="0" y="72" width="320" height="4" fill="#DB2777"/>
      <rect x="0" y="82" width="320" height="4" fill="#BE185D"/>
      <path d="M0,120 L0,82 L18,82 L18,62 L38,62 L38,94 L56,94 L56,74 L74,74 L74,120
               M244,120 L244,68 L266,68 L266,92 L286,92 L286,56 L306,56 L306,84 L320,84 L320,120 Z"
            fill="#1E1030"/>
      <line x1="28" y1="120" x2="40" y2="54" stroke="#1E1030" stroke-width="3.5"/>
      <path d="M40,54 Q20,44 10,56 M40,54 Q58,44 68,54 M40,54 Q26,38 22,42 M40,54 Q54,38 58,44"
            fill="none" stroke="#1E1030" stroke-width="2.4" stroke-linecap="round"/>
      <text x="163" y="78" text-anchor="middle" fill="#1E1030" font-family="Georgia, serif" font-size="52" font-weight="700">VI</text>
      <text x="160" y="75" text-anchor="middle" fill="#22D3EE" font-family="Georgia, serif" font-size="52" font-weight="700">VI</text>
      <rect x="190" y="8" width="122" height="22" rx="4" fill="rgba(24,16,44,0.9)" stroke="#FDE047"/>
      <text x="251" y="23" text-anchor="middle" fill="#FEF08A" font-family="Arial, sans-serif" font-size="10.5" font-weight="800">99 METACRITIC</text>
    </svg>
    """


def build_html_page() -> str:
    """Assemble the complete 1024x1024 front-page HTML markup."""
    hero_cards = [
        {
            "accent": "#B91C1C",
            "tag": "ASIA-PACIFIC · SHENZHEN",
            "title": "Trump, Xi &amp; Putin Hold Tri-Summit",
            "body": "First-ever 3-way talks on APEC sidelines yield joint pledge on <strong>nuclear risk reduction &amp; UN reform</strong>; Ukraine &amp; Iran left out.",
            "svg": render_shenzhen_svg(),
        },
        {
            "accent": "#047857",
            "tag": "MARKETS &amp; AI · NASDAQ: ANT",
            "title": "Anthropic Raises $81B+ in Nasdaq IPO",
            "body": "Priced at <strong>$83</strong> above range, shares open at <strong>$111.50</strong> and close at <strong>$97.17</strong> in one of history's largest market debuts.",
            "svg": render_anthropic_svg(),
        },
    ]

    mid_cards = [
        {
            "accent": "#6D28D9",
            "tag": "INTL LAW · THE HAGUE",
            "title": "ICJ Finds Myanmar Guilty of Genocide",
            "body": "UN top court backs <strong>The Gambia</strong> over 2017 Rohingya atrocities, ordering reparations in landmark state ruling.",
            "svg": render_icj_svg(),
        },
        {
            "accent": "#1D4ED8",
            "tag": "EUROPE &amp; ARCTIC",
            "title": "Denmark Passes Greenland Pact 109-0",
            "body": "Unanimous parliament vote expands <strong>Pituffik</strong> defense access while affirming Danish sovereignty &amp; self-rule.",
            "svg": render_greenland_svg(),
        },
        {
            "accent": "#C2410C",
            "tag": "CLIMATE · COP31 ANTALYA",
            "title": "COP31 Draft Draws Walkout Threats",
            "body": "With <strong>US absent</strong>, nations &amp; NGOs slam weak fossil-fuel text as WMO warns of <strong>2.8°C</strong> warming trajectory.",
            "svg": render_cop31_svg(),
        },
    ]

    bot_cards = [
        {
            "accent": "#DC2626",
            "tag": "EAST EUROPE · ENERGY",
            "title": "Drones Strike Tatarstan Oil Hub",
            "body": "Ukrainian UAVs hit <strong>Kaleykino</strong> pumping station (&gt;1,000 km inside Russia), igniting Druzhba pipeline tanks.",
            "svg": render_tatarstan_svg(),
        },
        {
            "accent": "#B45309",
            "tag": "MIDEAST &amp; AFRICA",
            "title": "Gaza Cold Toll &amp; Sudan Drone War",
            "body": "First infant hypothermia death hits flooded Gaza camps; UN warns drones now lead <strong>Sudan</strong> civilian casualties.",
            "svg": render_crisis_svg(),
        },
        {
            "accent": "#9333EA",
            "tag": "CULTURE &amp; TECH",
            "title": "GTA VI Debuts Worldwide Nov 19",
            "body": "PS5 &amp; Xbox launch earns <strong>99/100</strong>, smashes pre-orders &amp; drives record global internet traffic surge.",
            "svg": render_gtavi_svg(),
        },
    ]

    def card_markup(item: dict) -> str:
        return (
            f'<article class="card" style="--accent:{item["accent"]}">'
            f'<div class="art"><span class="pill">{item["tag"]}</span>{item["svg"]}</div>'
            f'<div class="copy"><h2>{item["title"]}</h2><p>{item["body"]}</p></div>'
            f"</article>"
        )

    hero_html = "".join(card_markup(c) for c in hero_cards)
    mid_html = "".join(card_markup(c) for c in mid_cards)
    bot_html = "".join(card_markup(c) for c in bot_cards)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  html, body {{
    width: 1024px;
    height: 1024px;
    overflow: hidden;
    background: #EFE9DC;
    color: #0F172A;
    font-family: 'Segoe UI', Arial, sans-serif;
  }}
  .page {{
    width: 1024px;
    height: 1024px;
    padding: 10px 12px;
    display: flex;
    flex-direction: column;
    gap: 8px;
    background: #EFE9DC;
  }}
  .masthead {{
    height: 108px;
    background: linear-gradient(125deg, #0A1220 0%, #16243D 100%);
    color: #F8FAFC;
    border-radius: 6px;
    border-bottom: 4px solid #DC2626;
    padding: 9px 16px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}
  .kicker {{
    display: flex;
    justify-content: space-between;
    font-size: 11.5px;
    font-weight: 800;
    letter-spacing: 1.4px;
    color: #FBBF24;
    text-transform: uppercase;
  }}
  .banner {{
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}
  .banner h1 {{
    font-family: Georgia, 'Times New Roman', serif;
    font-size: 38px;
    line-height: 1;
    color: #FFFFFF;
    letter-spacing: -0.3px;
  }}
  .edition-badge {{
    font-size: 14px;
    font-weight: 800;
    letter-spacing: 0.9px;
    color: #FEF3C7;
    background: #B91C1C;
    border: 1px solid #FBBF24;
    padding: 5px 12px;
    border-radius: 4px;
  }}
  .deck {{
    font-size: 10.8px;
    font-weight: 700;
    letter-spacing: 0.45px;
    color: #CBD5E1;
    border-top: 1px solid rgba(255,255,255,0.16);
    padding-top: 4px;
    white-space: nowrap;
  }}
  .row-hero {{
    height: 316px;
    display: grid;
    grid-template-columns: 1.04fr 1fr;
    gap: 8px;
  }}
  .row-mid {{
    height: 272px;
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 8px;
  }}
  .row-bot {{
    height: 250px;
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 8px;
  }}
  .card {{
    background: #FFFDF9;
    border: 1.5px solid #CBD5E1;
    border-top: 4px solid var(--accent);
    border-radius: 6px;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    box-shadow: 0 2px 5px rgba(15,23,42,0.08);
  }}
  .art {{
    position: relative;
    width: 100%;
    flex-shrink: 0;
    border-bottom: 1px solid #E2E8F0;
  }}
  .row-hero .art {{ height: 184px; }}
  .row-mid .art {{ height: 136px; }}
  .row-bot .art {{ height: 120px; }}
  svg {{ display: block; width: 100%; height: 100%; }}
  .pill {{
    position: absolute;
    top: 7px;
    left: 7px;
    background: var(--accent);
    color: #FFFFFF;
    font-size: 10.5px;
    font-weight: 800;
    letter-spacing: 0.7px;
    padding: 2.5px 7px;
    border-radius: 3px;
    box-shadow: 0 1px 4px rgba(0,0,0,0.45);
  }}
  .copy {{
    padding: 8px 11px;
    display: flex;
    flex-direction: column;
    gap: 4px;
    flex: 1;
  }}
  .row-hero .copy {{ padding: 9px 13px; gap: 5px; }}
  .copy h2 {{
    font-family: Georgia, serif;
    font-weight: 700;
    color: #0F172A;
    line-height: 1.15;
  }}
  .row-hero .copy h2 {{ font-size: 22px; }}
  .row-mid .copy h2 {{ font-size: 18px; }}
  .row-bot .copy h2 {{ font-size: 17.5px; }}
  .copy p {{
    color: #334155;
    line-height: 1.32;
    font-weight: 500;
  }}
  .row-hero .copy p {{ font-size: 14px; }}
  .row-mid .copy p {{ font-size: 12.6px; }}
  .row-bot .copy p {{ font-size: 12.2px; }}
  .copy strong {{ color: #0F172A; font-weight: 700; }}
  .footer {{
    height: 26px;
    background: #0F172A;
    color: #E2E8F0;
    border-radius: 4px;
    padding: 0 12px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.65px;
  }}
  .footer span:last-child {{ color: #FBBF24; }}
</style>
</head>
<body>
<div class="page">
  <header class="masthead">
    <div class="kicker">
      <span>THE GLOBAL DISPATCH · WORLD NEWS SUMMARY</span>
      <span>AMERICAS · EUROPE · ASIA · MIDEAST · AFRICA · OCEANIA</span>
    </div>
    <div class="banner">
      <h1>THURSDAY, 19 NOVEMBER 2026</h1>
      <div class="edition-badge">WORLD FRONT PAGE</div>
    </div>
    <div class="deck">
      SHENZHEN SUMMIT · ANTHROPIC $81B+ IPO · ICJ ROHINGYA GENOCIDE · GREENLAND 109-0 · COP31 · TATARSTAN STRIKE · GAZA &amp; SUDAN · GTA VI
    </div>
  </header>
  <section class="row-hero">{hero_html}</section>
  <section class="row-mid">{mid_html}</section>
  <section class="row-bot">{bot_html}</section>
  <footer class="footer">
    <span>GULF BLOCKADE ESCALATES · TÜRKİYE-AUSTRALIA COP31 PRESIDENCY · GLOBAL ISP RECORD</span>
    <span>ONE-DAY EDITION: 19 NOVEMBER 2026</span>
  </footer>
</div>
</body>
</html>"""


def render_png(out_file: Path) -> tuple[int, int, int]:
    """Render the HTML poster to a 1024x1024 PNG via headless Chrome."""
    chrome_exe = locate_chrome()
    html_body = build_html_page()
    with tempfile.TemporaryDirectory(prefix="nov19_news_") as tmp_dir:
        tmp_path = Path(tmp_dir)
        html_file = tmp_path / "frontpage.html"
        profile_dir = tmp_path / "chrome_profile"
        html_file.write_text(html_body, encoding="utf-8")
        subprocess.run(
            [
                chrome_exe,
                "--headless=new",
                "--disable-gpu",
                "--no-sandbox",
                "--hide-scrollbars",
                f"--user-data-dir={profile_dir}",
                "--window-size=1024,1024",
                "--force-device-scale-factor=1",
                f"--screenshot={out_file}",
                html_file.as_uri(),
            ],
            check=True,
            capture_output=True,
            timeout=30,
        )
    raw = out_file.read_bytes()
    w = int.from_bytes(raw[16:20], "big")
    h = int.from_bytes(raw[20:24], "big")
    return w, h, len(raw)


if __name__ == "__main__":
    width, height, size_bytes = render_png(OUT_PATH)
    print(f"Rendered {OUT_PATH}: {width}x{height}, {size_bytes} bytes")
