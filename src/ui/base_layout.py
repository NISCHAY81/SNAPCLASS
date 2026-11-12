import streamlit as st


# ---------------------------------------------------------------------------
# Design tokens (CSS custom properties). Change a colour/radius here once and
# every screen updates.
# ---------------------------------------------------------------------------
TOKENS = """
:root {
    /* brand */
    --c-blurple:      #5865F2;
    --c-blurple-600:  #4752C4;
    --c-blurple-300:  #7983F5;
    --c-pink:         #EB459E;
    --c-pink-600:     #C73383;
    --c-lilac:        #E0E3FF;
    --c-ink:          #23272A;
    --c-white:        #FFFFFF;

    /* shape */
    --radius-pill: 999px;
    --radius-md:   1rem;
    --radius-card: clamp(2rem, 4vw, 4rem);

    /* motion */
    --ease-out:    cubic-bezier(.22, 1, .36, 1);
    --ease-spring: cubic-bezier(.34, 1.56, .64, 1);

    /* elevation */
    --shadow-sm:   0 2px 6px rgba(35, 39, 42, .08);
    --shadow-card: 0 1px 0 rgba(255,255,255,.7) inset,
                   0 20px 40px -20px rgba(20, 24, 80, .45),
                   0 8px 16px -8px rgba(20, 24, 80, .25);
    --shadow-card-hover: 0 1px 0 rgba(255,255,255,.8) inset,
                         0 32px 60px -24px rgba(20, 24, 80, .55),
                         0 12px 24px -10px rgba(20, 24, 80, .3);

    /* type */
    --font-display: 'Climate Crisis', 'Outfit', sans-serif;
    --font-body:    'Outfit', system-ui, -apple-system, 'Segoe UI', sans-serif;
}
"""

FONTS = """
@import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');
"""


def _inject(css: str, fonts: bool = False):
    # NOTE: @import rules must come before every other rule in a <style> tag.
    head = FONTS if fonts else ""
    st.markdown(f"<style>{head}{TOKENS}{css}</style>", unsafe_allow_html=True)


# ---------------------------------------------------------------------------
# HOME: bold gradient mesh background + frosted-glass cards
# ---------------------------------------------------------------------------
def style_background_home():
    _inject("""
        .stApp {
            background:
                radial-gradient(55rem 38rem at 8% -8%,  rgba(235, 69, 158, .55), transparent 60%),
                radial-gradient(48rem 36rem at 105% 12%, rgba(255, 255, 255, .22), transparent 55%),
                radial-gradient(40rem 30rem at 50% 115%, rgba(20, 24, 80, .55),  transparent 60%),
                linear-gradient(160deg, var(--c-blurple-300) 0%, var(--c-blurple) 45%, #3C45C9 100%)
                !important;
            background-attachment: fixed !important;
        }

        /* Cards */
        .stApp div[data-testid="stColumn"] {
            background: rgba(255, 255, 255, .72) !important;
            -webkit-backdrop-filter: blur(18px) saturate(140%);
            backdrop-filter: blur(18px) saturate(140%);
            border: 1px solid rgba(255, 255, 255, .65);
            border-radius: var(--radius-card) !important;
            padding: clamp(1.5rem, 3.5vw, 2.5rem) !important;
            box-shadow: var(--shadow-card);
            transition: transform .5s var(--ease-out), box-shadow .5s var(--ease-out);
            animation: card-rise .8s var(--ease-out) both;
        }
        .stApp div[data-testid="stColumn"]:nth-child(2) { animation-delay: .12s; }

        .stApp div[data-testid="stColumn"]:hover {
            transform: translateY(-8px);
            box-shadow: var(--shadow-card-hover);
        }

        /* Headings inside the cards */
        .stApp div[data-testid="stColumn"] [data-testid="stHeading"] h1,
        .stApp div[data-testid="stColumn"] [data-testid="stHeading"] h2,
        .stApp div[data-testid="stColumn"] [data-testid="stHeading"] h3 {
            color: var(--c-ink) !important;
        }

        /* Mascot images get a gentle float */
        .stApp div[data-testid="stColumn"] img {
            filter: drop-shadow(0 12px 14px rgba(20, 24, 80, .25));
            animation: float 5s ease-in-out infinite;
        }
        .stApp div[data-testid="stColumn"]:nth-child(2) img { animation-delay: -2.5s; }

        @keyframes card-rise {
            from { opacity: 0; transform: translateY(32px) scale(.97); }
            to   { opacity: 1; transform: translateY(0)    scale(1);   }
        }
        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50%      { transform: translateY(-8px); }
        }

        @media (max-width: 640px) {
            .stApp div[data-testid="stColumn"] { border-radius: 2rem !important; }
        }
    """)


# ---------------------------------------------------------------------------
# DASHBOARD / LOGIN screens: soft lilac background with subtle colour glow
# ---------------------------------------------------------------------------
def style_background_dashboard():
    _inject("""
        .stApp {
            background:
                radial-gradient(40rem 28rem at 0% 0%,   rgba(88, 101, 242, .18), transparent 60%),
                radial-gradient(36rem 26rem at 100% 100%, rgba(235, 69, 158, .14), transparent 60%),
                var(--c-lilac) !important;
            background-attachment: fixed !important;
        }
    """)


# ---------------------------------------------------------------------------
# SHARED: typography, buttons, inputs, alerts, dividers, small details
# ---------------------------------------------------------------------------
def style_base_layout():
    _inject("""
        /* ---------- base ---------- */
        html { scroll-behavior: smooth; }

        .stApp {
            font-family: var(--font-body);
            -webkit-font-smoothing: antialiased;
        }

        ::selection { background: var(--c-pink); color: var(--c-white); }

        /* Hide Streamlit chrome */
        #MainMenu, footer, header,
        [data-testid="stHeader"],
        [data-testid="stToolbar"],
        [data-testid="stDecoration"] {
            visibility: hidden;
            height: 0;
        }

        .block-container { padding-top: 1.5rem !important; }

        /* Slim, branded scrollbar */
        * { scrollbar-width: thin; scrollbar-color: var(--c-blurple) transparent; }
        *::-webkit-scrollbar { width: 8px; height: 8px; }
        *::-webkit-scrollbar-thumb { background: var(--c-blurple); border-radius: var(--radius-pill); }

        /* ---------- typography ---------- */
        [data-testid="stHeading"] h1 {
            font-family: var(--font-display) !important;
            font-size: clamp(2.25rem, 5vw, 3.5rem) !important;
            line-height: 1.05 !important;
            letter-spacing: -.01em;
            margin-bottom: 0 !important;
            color: var(--c-blurple) !important;
        }

        [data-testid="stHeading"] h2 {
            font-family: var(--font-display) !important;
            font-size: clamp(1.5rem, 3vw, 2rem) !important;
            line-height: 1.1 !important;
            margin-bottom: 0 !important;
            color: var(--c-pink) !important;
        }

        h3, h4 { font-family: var(--font-body); }

        /* Body text. Scoped so it does NOT recolour button labels. */
        .stApp [data-testid="stMarkdownContainer"] p,
        .stApp [data-testid="stWidgetLabel"] p {
            font-family: var(--font-body);
            color: var(--c-ink) !important;
        }
        .stApp [data-testid="stWidgetLabel"] p { font-weight: 600; }

        /* ---------- buttons ---------- */
        .stApp .stButton > button,
        .stApp .stFormSubmitButton > button,
        .stApp [data-testid="stCameraInputButton"] {
            position: relative;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: .5rem;
            padding: .7rem 1.5rem !important;
            border: 1px solid rgba(255, 255, 255, .25) !important;
            border-radius: var(--radius-pill) !important;
            font-family: var(--font-body);
            font-weight: 600;
            letter-spacing: .01em;
            color: var(--c-white) !important;
            background: linear-gradient(135deg, var(--c-blurple-300), var(--c-blurple)) !important;
            box-shadow:
                0 10px 22px -10px rgba(88, 101, 242, .85),
                0 1px 0 rgba(255, 255, 255, .35) inset;
            transition:
                transform .3s var(--ease-spring),
                box-shadow .3s var(--ease-out),
                filter .3s var(--ease-out);
        }

        /* label text inherits the button colour (fixes black labels) */
        .stApp .stButton > button p,
        .stApp .stFormSubmitButton > button p {
            color: inherit !important;
            font-family: inherit;
            font-weight: inherit;
            margin: 0;
        }

        /* variants */
        .stApp .stButton > button[kind="secondary"],
        .stApp .stButton > button[data-testid="stBaseButton-secondary"] {
            background: linear-gradient(135deg, #F46BB5, var(--c-pink)) !important;
            box-shadow:
                0 10px 22px -10px rgba(235, 69, 158, .85),
                0 1px 0 rgba(255, 255, 255, .35) inset;
        }
        .stApp .stButton > button[kind="tertiary"],
        .stApp .stButton > button[data-testid="stBaseButton-tertiary"] {
            background: linear-gradient(135deg, #3a3f44, #000) !important;
            box-shadow:
                0 10px 22px -10px rgba(0, 0, 0, .7),
                0 1px 0 rgba(255, 255, 255, .15) inset;
        }

        .stApp .stButton > button:hover,
        .stApp .stFormSubmitButton > button:hover,
        .stApp [data-testid="stCameraInputButton"]:hover {
            transform: translateY(-2px) scale(1.04);
            filter: brightness(1.06) saturate(1.1);
        }
        .stApp .stButton > button:active,
        .stApp .stFormSubmitButton > button:active {
            transform: translateY(0) scale(.97);
            filter: brightness(.96);
        }
        .stApp .stButton > button:focus-visible,
        .stApp .stFormSubmitButton > button:focus-visible {
            outline: 3px solid rgba(88, 101, 242, .35);   /* fallback */
            outline: 3px solid color-mix(in srgb, var(--c-blurple) 40%, transparent);
            outline-offset: 3px;
        }

        /* ---------- inputs ---------- */
        .stApp [data-baseweb="input"] {
            background: rgba(255, 255, 255, .85) !important;
            border: 1.5px solid rgba(88, 101, 242, .25) !important;
            border-radius: var(--radius-md) !important;
            box-shadow: var(--shadow-sm);
            transition: border-color .25s var(--ease-out), box-shadow .25s var(--ease-out);
        }
        .stApp [data-baseweb="input"]:hover { border-color: rgba(88, 101, 242, .5) !important; }
        .stApp [data-baseweb="input"]:focus-within {
            border-color: var(--c-blurple) !important;
            box-shadow: 0 0 0 4px rgba(88, 101, 242, .22);   /* fallback */
            box-shadow: 0 0 0 4px color-mix(in srgb, var(--c-blurple) 25%, transparent);
        }
        .stApp [data-baseweb="base-input"] { background: transparent !important; }
        .stApp [data-baseweb="input"] input {
            font-family: var(--font-body);
            color: var(--c-ink) !important;
            -webkit-text-fill-color: var(--c-ink);
        }
        .stApp [data-baseweb="input"] input::placeholder {
            color: rgba(35, 39, 42, .45) !important;
            -webkit-text-fill-color: rgba(35, 39, 42, .45);
        }

        /* camera / audio widgets */
        .stApp [data-testid="stCameraInput"],
        .stApp [data-testid="stAudioInput"] {
            border-radius: 1.5rem;
            overflow: hidden;
        }
        .stApp [data-testid="stCameraInput"] > div {
            border-radius: 1.5rem;
            border: 1.5px solid rgba(88, 101, 242, .25);
            background: rgba(255, 255, 255, .6);
        }

        /* ---------- alerts / toasts ---------- */
        /* 1. clear every inner layer, because Streamlit paints the
              (dark) tint on an inner element, not on stAlert itself */
        .stApp [data-testid="stAlert"],
        .stApp [data-testid="stAlert"] * {
            background: transparent !important;
        }

        /* 2. one light card with an accent stripe */
        .stApp [data-testid="stAlert"] {
            border: 0 !important;
            animation: alert-in .4s var(--ease-out) both;
        }
        .stApp [data-testid="stAlertContainer"],
        .stApp [data-testid="stAlert"] > div,
        .stApp [data-testid="stAlert"] [data-baseweb="notification"] {
            background: #FFFFFF !important;
            border: 1px solid rgba(35, 39, 42, .08) !important;
            border-left: 6px solid var(--c-blurple) !important;
            border-radius: var(--radius-md) !important;
            box-shadow: var(--shadow-sm);
        }

        /* 3. readable dark text and icons on the light card */
        .stApp [data-testid="stAlert"] p,
        .stApp [data-testid="stAlert"] span,
        .stApp [data-testid="stAlert"] svg {
            color: var(--c-ink) !important;
            fill: currentColor;
        }

        /* 4. colour by type (info keeps the blue default above) */
        .stApp [data-testid="stAlert"]:has([data-testid="stAlertContentWarning"]) > div,
        .stApp [data-testid="stAlertContainer"]:has([data-testid="stAlertContentWarning"]) {
            background: #FFF4D6 !important;
            border-left-color: #F5A623 !important;
        }
        .stApp [data-testid="stAlert"]:has([data-testid="stAlertContentError"]) > div,
        .stApp [data-testid="stAlertContainer"]:has([data-testid="stAlertContentError"]) {
            background: #FFE3E3 !important;
            border-left-color: #ED4245 !important;
        }
        .stApp [data-testid="stAlert"]:has([data-testid="stAlertContentSuccess"]) > div,
        .stApp [data-testid="stAlertContainer"]:has([data-testid="stAlertContentSuccess"]) {
            background: #DDF6E6 !important;
            border-left-color: #3BA55D !important;
        }
        .stApp [data-testid="stAlert"]:has([data-testid="stAlertContentInfo"]) > div,
        .stApp [data-testid="stAlertContainer"]:has([data-testid="stAlertContentInfo"]) {
            background: #E3E6FF !important;
            border-left-color: var(--c-blurple) !important;
        }

        @keyframes alert-in {
            from { opacity: 0; transform: translateY(-6px); }
            to   { opacity: 1; transform: translateY(0); }
        }

        /* ---------- divider ---------- */
        .stApp hr {
            border: 0 !important;
            height: 2px !important;
            opacity: 1 !important;
            background: linear-gradient(90deg,
                transparent,
                rgba(88, 101, 242, .55),
                rgba(235, 69, 158, .55),
                transparent) !important;
        }

        /* ---------- respect reduced-motion preferences ---------- */
        @media (prefers-reduced-motion: reduce) {
            *, *::before, *::after {
                animation: none !important;
                transition: none !important;
                scroll-behavior: auto !important;
            }
        }
    """, fonts=True)