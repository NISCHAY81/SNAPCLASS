import streamlit as st


# ===========================================================================
#  SNAPCLASS design system  -  modern CSS edition
#  Uses: oklch() colours, CSS nesting, @property, :has()/:is(), color-mix(),
#        clamp(), text-wrap, variable fonts, `translate` property,
#        animated conic-gradient borders, prefers-reduced-motion.
# ===========================================================================

# One <link>-free font import. @import must be the FIRST thing in a <style>.
FONTS = """
@import url('https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,200..800&family=Plus+Jakarta+Sans:wght@200..800&family=JetBrains+Mono:wght@400..700&display=swap');
"""

# ---------------------------------------------------------------------------
# Design tokens. Change a value here and every screen updates.
# ---------------------------------------------------------------------------
TOKENS = """
@property --angle {
    syntax: "<angle>";
    initial-value: 0deg;
    inherits: false;
}

:root {
    color-scheme: light;

    /* colour (oklch = perceptually even, easy to tweak: L C H) */
    --indigo-300: oklch(0.76 0.12 272);
    --indigo-400: oklch(0.68 0.17 272);
    --indigo-500: oklch(0.58 0.20 272);
    --indigo-700: oklch(0.42 0.18 275);
    --indigo-900: oklch(0.27 0.10 275);
    --pink-400:   oklch(0.76 0.17 352);
    --pink-500:   oklch(0.67 0.23 352);
    --lilac-50:   oklch(0.985 0.012 280);
    --lilac-100:  oklch(0.955 0.030 280);
    --lilac-200:  oklch(0.910 0.050 280);
    --ink:        oklch(0.25 0.025 270);
    --ink-soft:   oklch(0.25 0.025 270 / .55);
    --white:      oklch(1 0 0);

    /* shape */
    --radius-sm:   .75rem;
    --radius-md:   1rem;
    --radius-lg:   1.75rem;
    --radius-card: clamp(2rem, 4vw, 3.5rem);
    --radius-pill: 999px;

    /* motion */
    --ease-out:    cubic-bezier(.22, 1, .36, 1);
    --ease-spring: cubic-bezier(.34, 1.56, .64, 1);

    /* elevation */
    --shadow-sm: 0 1px 2px oklch(0.25 0.05 270 / .08),
                 0 6px 14px -6px oklch(0.25 0.05 270 / .14);
    --shadow-lg: 0 1px 0 oklch(1 0 0 / .75) inset,
                 0 24px 48px -24px oklch(0.20 0.12 275 / .50),
                 0 8px 16px -8px  oklch(0.20 0.12 275 / .30);
    --shadow-xl: 0 1px 0 oklch(1 0 0 / .85) inset,
                 0 40px 70px -28px oklch(0.20 0.12 275 / .60),
                 0 14px 26px -12px oklch(0.20 0.12 275 / .35);

    /* type */
    --font-display: 'Bricolage Grotesque', 'Plus Jakarta Sans', system-ui, sans-serif;
    --font-body:    'Plus Jakarta Sans', system-ui, -apple-system, 'Segoe UI', sans-serif;
    --font-mono:    'JetBrains Mono', ui-monospace, 'Cascadia Code', Consolas, monospace;
}
"""


def _inject(css: str, fonts: bool = False):
    head = FONTS if fonts else ""
    st.markdown(f"<style>{head}{TOKENS}{css}</style>", unsafe_allow_html=True)


# ---------------------------------------------------------------------------
# HOME  -  deep aurora background + frosted cards with an animated border
# ---------------------------------------------------------------------------
def style_background_home():
    _inject("""
        .stApp {
            background:
                radial-gradient(60rem 40rem at   5% -10%, oklch(0.67 0.23 352 / .55), transparent 60%),
                radial-gradient(50rem 40rem at 105%  10%, oklch(0.68 0.17 272 / .60), transparent 55%),
                radial-gradient(45rem 30rem at  50% 120%, oklch(0.76 0.12 200 / .35), transparent 60%),
                linear-gradient(165deg in oklch, var(--indigo-700), var(--indigo-900))
                !important;
            background-attachment: fixed !important;
        }

        .stApp div[data-testid="stColumn"] {
            position: relative;
            background: oklch(1 0 0 / .80) !important;
            -webkit-backdrop-filter: blur(20px) saturate(150%);
            backdrop-filter: blur(20px) saturate(150%);
            border-radius: var(--radius-card) !important;
            padding: clamp(1.5rem, 3.5vw, 2.5rem) !important;
            box-shadow: var(--shadow-lg);
            transition: translate .5s var(--ease-out), box-shadow .5s var(--ease-out);
            animation: card-rise .9s var(--ease-out) both;

            &:nth-child(2) { animation-delay: .12s; }

            /* animated conic-gradient border, only visible on hover */
            &::before {
                content: "";
                position: absolute;
                inset: 0;
                border-radius: inherit;
                padding: 2px;
                background: conic-gradient(from var(--angle),
                    transparent 0 55%,
                    var(--pink-500),
                    var(--indigo-400),
                    transparent 95%);
                -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
                -webkit-mask-composite: xor;
                mask: linear-gradient(#000 0 0) content-box exclude, linear-gradient(#000 0 0);
                opacity: 0;
                transition: opacity .4s var(--ease-out);
                animation: spin 5s linear infinite;
                pointer-events: none;
            }

            &:hover {
                translate: 0 -8px;
                box-shadow: var(--shadow-xl);
                &::before { opacity: 1; }
            }

            /* headings inside the cards are always dark */
            & [data-testid="stHeading"] :is(h1, h2, h3) { color: var(--ink) !important; }

            /* mascots float */
            & img {
                filter: drop-shadow(0 14px 16px oklch(0.2 0.1 275 / .28));
                animation: float 5s ease-in-out infinite;
            }
            &:nth-child(2) img { animation-delay: -2.5s; }

            @media (max-width: 640px) { border-radius: 2rem !important; }
        }

        @keyframes card-rise {
            from { opacity: 0; translate: 0 32px; scale: .97; }
            to   { opacity: 1; translate: 0 0;    scale: 1; }
        }
        @keyframes float {
            0%, 100% { translate: 0 0; }
            50%      { translate: 0 -8px; }
        }
        @keyframes spin { to { --angle: 360deg; } }
    """)


# ---------------------------------------------------------------------------
# DASHBOARD / LOGIN  -  light canvas with a subtle dot grid and colour glow
# ---------------------------------------------------------------------------
def style_background_dashboard():
    _inject("""
        .stApp {
            background:
                radial-gradient(oklch(0.58 0.20 272 / .13) 1px, transparent 1.2px) 0 0 / 22px 22px,
                radial-gradient(42rem 28rem at   0%   0%, oklch(0.68 0.17 272 / .20), transparent 60%),
                radial-gradient(38rem 26rem at 100% 100%, oklch(0.67 0.23 352 / .16), transparent 60%),
                var(--lilac-100) !important;
            background-attachment: fixed !important;
        }
    """)


# ---------------------------------------------------------------------------
# SHARED  -  type, buttons, inputs, code, alerts, dialog, toast, details
# ---------------------------------------------------------------------------
def style_base_layout():
    _inject("""
        /* ============================ base ============================ */
        html { scroll-behavior: smooth; }

        .stApp {
            font-family: var(--font-body);
            font-optical-sizing: auto;
            -webkit-font-smoothing: antialiased;
            text-rendering: optimizeLegibility;
        }

        ::selection { background: var(--pink-500); color: var(--white); }

        /* ===== force the light look, whatever Streamlit's theme is =====
           (replaces .streamlit/config.toml: no extra file needed) */
        .stApp {
            color-scheme: light;
            color: var(--ink);
        }
        :is([data-testid="stAppViewContainer"],
            [data-testid="stMain"],
            [data-testid="stMainBlockContainer"],
            [data-testid="stBottom"]) {
            background: transparent !important;
        }
        .stApp :is([data-testid="stCaptionContainer"],
                   [data-testid="stCaptionContainer"] *,
                   [data-testid="stSpinner"],
                   [data-testid="stSpinner"] *,
                   [data-testid="stText"],
                   label, label *) {
            color: var(--ink) !important;
        }

        /* hide Streamlit chrome */
        :is(#MainMenu, footer, header,
            [data-testid="stHeader"],
            [data-testid="stToolbar"],
            [data-testid="stDecoration"]) {
            visibility: hidden;
            height: 0;
        }

        .block-container { padding-top: 1.5rem !important; }

        * {
            scrollbar-width: thin;
            scrollbar-color: var(--indigo-500) transparent;
        }

        /* =========================== typography ======================= */
        [data-testid="stHeading"] {
            & h1 {
                font-family: var(--font-display) !important;
                font-size: clamp(2.5rem, 6vw, 4rem) !important;
                font-weight: 800 !important;
                line-height: 1 !important;
                letter-spacing: -.035em;
                text-wrap: balance;
                margin-bottom: 0 !important;
                color: var(--indigo-700) !important;
            }
            & h2 {
                font-family: var(--font-display) !important;
                font-size: clamp(1.6rem, 3.2vw, 2.25rem) !important;
                font-weight: 700 !important;
                line-height: 1.08 !important;
                letter-spacing: -.025em;
                text-wrap: balance;
                margin-bottom: 0 !important;
                color: var(--ink) !important;
            }
            & h3 {
                font-family: var(--font-display) !important;
                font-weight: 650 !important;
                letter-spacing: -.015em;
                color: var(--ink) !important;
            }
        }

        h3, h4 { font-family: var(--font-display); }

        /* body text - scoped so it never recolours button labels */
        .stApp :is([data-testid="stMarkdownContainer"] :is(p, li),
                   [data-testid="stWidgetLabel"] p) {
            font-family: var(--font-body);
            color: var(--ink) !important;
            text-wrap: pretty;
        }
        .stApp [data-testid="stWidgetLabel"] p {
            font-weight: 600;
            font-size: .9rem;
            letter-spacing: .01em;
        }

        /* ============================ buttons ========================= */
        .stApp :is(.stButton, .stFormSubmitButton) > button,
        .stApp [data-testid="stCameraInputButton"] {
            position: relative;
            overflow: hidden;
            isolation: isolate;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: .55rem;
            padding: .75rem 1.6rem !important;
            border: 1px solid oklch(1 0 0 / .28) !important;
            border-radius: var(--radius-pill) !important;
            font-family: var(--font-body);
            font-weight: 650;
            letter-spacing: .005em;
            color: var(--white) !important;
            background: linear-gradient(135deg in oklch, var(--indigo-400), var(--indigo-500)) !important;
            box-shadow:
                0 12px 24px -12px oklch(0.58 0.20 272 / .90),
                0 1px 0 oklch(1 0 0 / .35) inset;
            transition:
                translate .3s var(--ease-spring),
                scale .3s var(--ease-spring),
                box-shadow .3s var(--ease-out),
                filter .3s var(--ease-out);

            /* shine sweep */
            &::before {
                content: "";
                position: absolute;
                inset: 0;
                z-index: -1;
                background: linear-gradient(110deg, transparent 35%, oklch(1 0 0 / .38) 50%, transparent 65%);
                translate: -130% 0;
                transition: translate .7s var(--ease-out);
            }

            &:hover {
                translate: 0 -2px;
                scale: 1.04;
                filter: saturate(1.15) brightness(1.04);
                &::before { translate: 130% 0; }
            }
            &:active { translate: 0 0; scale: .97; filter: brightness(.96); }

            &:focus-visible {
                outline: 3px solid color-mix(in oklch, var(--indigo-500) 45%, transparent);
                outline-offset: 3px;
            }

            /* label inherits the button colour */
            & p {
                color: inherit !important;
                font-family: inherit;
                font-weight: inherit;
                margin: 0;
            }
        }

        /* secondary = pink, tertiary = ink */
        .stApp .stButton > button:is([kind="secondary"], [data-testid="stBaseButton-secondary"]) {
            background: linear-gradient(135deg in oklch, var(--pink-400), var(--pink-500)) !important;
            box-shadow:
                0 12px 24px -12px oklch(0.67 0.23 352 / .90),
                0 1px 0 oklch(1 0 0 / .35) inset;
        }
        .stApp .stButton > button:is([kind="tertiary"], [data-testid="stBaseButton-tertiary"]) {
            background: linear-gradient(135deg in oklch, oklch(0.38 0.02 270), oklch(0.18 0.02 270)) !important;
            box-shadow:
                0 12px 24px -12px oklch(0.2 0.02 270 / .85),
                0 1px 0 oklch(1 0 0 / .15) inset;
        }

        /* ============================= inputs ========================= */
        .stApp :is([data-baseweb="input"], [data-baseweb="textarea"]) {
            background: oklch(1 0 0 / .88) !important;
            border: 1.5px solid oklch(0.58 0.20 272 / .22) !important;
            border-radius: var(--radius-md) !important;
            box-shadow: var(--shadow-sm);
            transition: border-color .25s var(--ease-out), box-shadow .25s var(--ease-out);

            &:hover { border-color: oklch(0.58 0.20 272 / .5) !important; }
            &:focus-within {
                border-color: var(--indigo-500) !important;
                box-shadow: 0 0 0 4px color-mix(in oklch, var(--indigo-500) 24%, transparent);
            }

            & :is(input, textarea) {
                font-family: var(--font-body);
                color: var(--ink) !important;
                -webkit-text-fill-color: var(--ink);

                &::placeholder {
                    color: var(--ink-soft) !important;
                    -webkit-text-fill-color: var(--ink-soft);
                }
            }
        }
        .stApp [data-baseweb="base-input"] { background: transparent !important; }

        /* camera + audio widgets */
        .stApp :is([data-testid="stCameraInput"], [data-testid="stAudioInput"]) {
            border-radius: var(--radius-lg);
            overflow: hidden;
        }
        .stApp :is([data-testid="stCameraInput"], [data-testid="stAudioInput"]) > div {
            border-radius: var(--radius-lg);
            border: 1.5px solid oklch(0.58 0.20 272 / .22);
            background: oklch(1 0 0 / .75) !important;
        }
        .stApp [data-testid="stAudioInput"] :is(p, span, svg) {
            color: var(--ink) !important;
        }

        /* ========================= code blocks ======================== */
        [data-testid="stCode"] {
            background: var(--lilac-50) !important;
            border: 1px solid oklch(0.58 0.20 272 / .18);
            border-radius: var(--radius-md);

            & :is(pre, code) {
                background: transparent !important;
                font-family: var(--font-mono) !important;
                font-size: .88rem;
            }
            & :is(code, code span) { color: var(--ink) !important; }
        }

        /* ===================== alerts (st.warning etc.) =============== */
        /* 1. clear every inner layer: Streamlit paints its tint on an inner node */
        .stApp [data-testid="stAlert"],
        .stApp [data-testid="stAlert"] * { background: transparent !important; }

        .stApp [data-testid="stAlert"] {
            border: 0 !important;
            animation: alert-in .45s var(--ease-out) both;
        }

        /* 2. one light card with an accent stripe */
        .stApp :is([data-testid="stAlertContainer"],
                   [data-testid="stAlert"] > div,
                   [data-testid="stAlert"] [data-baseweb="notification"]) {
            background: var(--white) !important;
            border: 1px solid oklch(0.25 0.03 270 / .08) !important;
            border-left: 6px solid var(--indigo-500) !important;
            border-radius: var(--radius-md) !important;
            box-shadow: var(--shadow-sm);
        }

        /* 3. dark text and icons */
        .stApp [data-testid="stAlert"] :is(p, span, svg) {
            color: var(--ink) !important;
            fill: currentColor;
        }

        /* 4. tint by type */
        .stApp :is([data-testid="stAlert"] > div, [data-testid="stAlertContainer"]) {
            &:has([data-testid="stAlertContentWarning"]) {
                background: oklch(0.965 0.06 90) !important;
                border-left-color: oklch(0.78 0.16 75) !important;
            }
            &:has([data-testid="stAlertContentError"]) {
                background: oklch(0.95 0.04 20) !important;
                border-left-color: oklch(0.63 0.22 25) !important;
            }
            &:has([data-testid="stAlertContentSuccess"]) {
                background: oklch(0.95 0.06 155) !important;
                border-left-color: oklch(0.68 0.17 150) !important;
            }
            &:has([data-testid="stAlertContentInfo"]) {
                background: var(--lilac-100) !important;
                border-left-color: var(--indigo-500) !important;
            }
        }

        @keyframes alert-in {
            from { opacity: 0; translate: 0 -6px; }
            to   { opacity: 1; translate: 0 0; }
        }

        /* ========================= dialog (modal) ===================== */
        [data-testid="stDialog"] {
            -webkit-backdrop-filter: blur(6px);
            backdrop-filter: blur(6px);

            & div[role="dialog"] {
                background: var(--lilac-50) !important;
                border: 1px solid oklch(1 0 0 / .8);
                border-radius: var(--radius-lg) !important;
                box-shadow: var(--shadow-xl);
            }
            & :is(h1, h2, h3, h4) {
                font-family: var(--font-display) !important;
                color: var(--ink) !important;
            }
            & [data-testid="stMarkdownContainer"] :is(p, li) { color: var(--ink) !important; }
        }

        /* ============================= toast ========================== */
        [data-testid="stToast"] {
            background: var(--white) !important;
            border-radius: var(--radius-md) !important;
            box-shadow: var(--shadow-lg);

            & * { background: transparent !important; color: var(--ink) !important; }
        }

        /* ============================ divider ========================= */
        .stApp hr {
            border: 0 !important;
            height: 2px !important;
            opacity: 1 !important;
            background: linear-gradient(90deg in oklch,
                transparent,
                oklch(0.58 0.20 272 / .55),
                oklch(0.67 0.23 352 / .55),
                transparent) !important;
        }

        /* ===================== accessibility: reduced motion ========== */
        @media (prefers-reduced-motion: reduce) {
            *, *::before, *::after {
                animation: none !important;
                transition: none !important;
                scroll-behavior: auto !important;
            }
        }
    """, fonts=True)