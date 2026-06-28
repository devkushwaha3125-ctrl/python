import random
import streamlit as st

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Number Hunt",
    page_icon="🎯",
    layout="centered",
)

# ── Global CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Space+Mono:wght@400;700&display=swap');

/* Reset & base */
html, body, [data-testid="stAppViewContainer"] {
    background: #0d0d12 !important;
    font-family: 'Space Grotesk', sans-serif;
    color: #e8e8f0;
}
[data-testid="stHeader"] { background: transparent !important; }
[data-testid="stToolbar"] { display: none; }
.block-container { padding: 2.5rem 1.5rem 4rem; max-width: 520px; margin: auto; }

/* Typography */
h1 { font-family: 'Space Mono', monospace; letter-spacing: -1px; }

/* Card shell */
.card {
    background: #16161f;
    border: 1px solid #2a2a3a;
    border-radius: 16px;
    padding: 2rem;
    margin-bottom: 1.25rem;
}

/* Attempt pip row */
.pips { display: flex; gap: 8px; margin-top: .5rem; }
.pip {
    width: 32px; height: 32px; border-radius: 50%;
    background: #2a2a3a; border: 2px solid #3a3a4e;
    display: flex; align-items: center; justify-content: center;
    font-size: 13px; font-family: 'Space Mono', monospace;
    font-weight: 700; transition: all .3s;
}
.pip.used   { background: #7c3aed; border-color: #a78bfa; color: #fff; }
.pip.active { background: #0d0d12; border-color: #7c3aed;
              box-shadow: 0 0 0 3px #7c3aed44; }
.pip.win    { background: #059669; border-color: #34d399; color: #fff; }
.pip.loss   { background: #dc2626; border-color: #f87171; color: #fff; }

/* Range bar */
.range-bar-outer {
    height: 6px; background: #2a2a3a; border-radius: 99px;
    position: relative; overflow: visible; margin: .75rem 0 .5rem;
}
.range-bar-inner {
    position: absolute; top: 0; height: 100%;
    background: linear-gradient(90deg, #7c3aed, #a78bfa);
    border-radius: 99px; transition: all .4s;
}
.range-labels {
    display: flex; justify-content: space-between;
    font-family: 'Space Mono', monospace; font-size: 12px; color: #6b6b85;
}

/* Feedback banner */
.feedback {
    border-radius: 10px; padding: .75rem 1rem;
    font-size: 14px; font-weight: 500; margin-top: .75rem;
    display: flex; align-items: center; gap: .5rem;
}
.feedback.low    { background: #1e1040; border: 1px solid #7c3aed; color: #c4b5fd; }
.feedback.high   { background: #2a1010; border: 1px solid #dc2626; color: #fca5a5; }
.feedback.win    { background: #052e16; border: 1px solid #059669; color: #6ee7b7; }
.feedback.loss   { background: #1c0d0d; border: 1px solid #dc2626; color: #fca5a5; }
.feedback.start  { background: #111120; border: 1px solid #3a3a4e; color: #8b8ba7; }

/* Number input override */
[data-testid="stNumberInput"] > div > div {
    background: #0d0d12 !important;
    border: 1.5px solid #3a3a4e !important;
    border-radius: 10px !important;
    color: #e8e8f0 !important;
    font-family: 'Space Mono', monospace !important;
}
[data-testid="stNumberInput"] > div > div:focus-within {
    border-color: #7c3aed !important;
    box-shadow: 0 0 0 3px #7c3aed33 !important;
}

/* Primary button */
[data-testid="stButton"] > button {
    background: #7c3aed !important;
    color: #fff !important;
    border: none !important;
    border-radius: 10px !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 600 !important;
    font-size: 15px !important;
    padding: .6rem 1.4rem !important;
    width: 100% !important;
    transition: background .2s, transform .1s !important;
}
[data-testid="stButton"] > button:hover {
    background: #6d28d9 !important;
    transform: translateY(-1px) !important;
}
[data-testid="stButton"] > button:active { transform: translateY(0) !important; }

/* History list */
.hist-row {
    display: flex; justify-content: space-between; align-items: center;
    padding: .45rem 0; border-bottom: 1px solid #1e1e2e;
    font-size: 14px;
}
.hist-row:last-child { border-bottom: none; }
.hist-num { font-family: 'Space Mono', monospace; font-weight: 700; }
.hist-badge {
    font-size: 12px; padding: 2px 8px; border-radius: 99px;
}
.badge-low  { background: #1e1040; color: #a78bfa; }
.badge-high { background: #2a1010; color: #fca5a5; }

/* Divider */
.divider { border: none; border-top: 1px solid #2a2a3a; margin: 1rem 0; }
</style>
""", unsafe_allow_html=True)


# ── Session state init ────────────────────────────────────────────────────────
def new_game():
    st.session_state.number   = random.randint(1, 100)
    st.session_state.count    = 0
    st.session_state.guesses  = []          # list of (guess, "low"|"high"|"win")
    st.session_state.status   = "playing"   # playing | win | loss
    st.session_state.lo       = 1
    st.session_state.hi       = 100

if "number" not in st.session_state:
    new_game()

MAX = 5
s   = st.session_state


# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("""
<div style='text-align:center; padding: 1.5rem 0 .5rem'>
  <div style='font-size:40px; margin-bottom:.25rem'>🎯</div>
  <h1 style='font-size:2rem; margin:0; color:#e8e8f0'>Number Hunt</h1>
  <p style='color:#6b6b85; font-size:14px; margin:.4rem 0 0'>
    Crack the code in 5 guesses · Range 1 – 100
  </p>
</div>
""", unsafe_allow_html=True)

# ── Attempts pips ─────────────────────────────────────────────────────────────
def pips_html():
    html = "<div class='pips'>"
    for i in range(1, MAX + 1):
        if i < s.count + 1:
            cls = "win" if (s.status == "win" and i == s.count) else \
                  "loss" if (s.status == "loss" and i == s.count) else "used"
            html += f"<div class='pip {cls}'>{i}</div>"
        elif i == s.count + 1 and s.status == "playing":
            html += f"<div class='pip active'>{i}</div>"
        else:
            html += f"<div class='pip'>{i}</div>"
    html += "</div>"
    return html

st.markdown(f"""
<div class='card'>
  <div style='display:flex;justify-content:space-between;align-items:center'>
    <span style='font-size:13px;color:#6b6b85;letter-spacing:.05em;text-transform:uppercase'>Attempts</span>
    <span style='font-family:"Space Mono",monospace;font-size:13px;color:#a78bfa'>{s.count}/{MAX}</span>
  </div>
  {pips_html()}
</div>
""", unsafe_allow_html=True)


# ── Narrowing range bar ───────────────────────────────────────────────────────
lo, hi = s.lo, s.hi
bar_left  = (lo - 1) / 99 * 100
bar_width = (hi - lo) / 99 * 100

st.markdown(f"""
<div class='card' style='padding:1.25rem 2rem'>
  <div style='font-size:13px;color:#6b6b85;text-transform:uppercase;letter-spacing:.05em;margin-bottom:.25rem'>
    Narrowed range
  </div>
  <div class='range-bar-outer'>
    <div class='range-bar-inner'
         style='left:{bar_left:.1f}%; width:{bar_width:.1f}%'></div>
  </div>
  <div class='range-labels'><span>{lo}</span><span>{hi}</span></div>
</div>
""", unsafe_allow_html=True)


# ── Feedback banner ───────────────────────────────────────────────────────────
def feedback_html():
    if not s.guesses:
        return "<div class='feedback start'>💡 Pick a number and fire your first guess.</div>"
    last_g, last_r = s.guesses[-1]
    if last_r == "win":
        return f"<div class='feedback win'>🎉 <strong>{last_g}</strong> is correct — you nailed it!</div>"
    if last_r == "loss":
        return f"<div class='feedback loss'>💀 Out of chances. The number was <strong>{s.number}</strong>.</div>"
    if last_r == "low":
        return f"<div class='feedback low'>⬆️ <strong>{last_g}</strong> is too low — go higher.</div>"
    return f"<div class='feedback high'>⬇️ <strong>{last_g}</strong> is too high — go lower.</div>"

st.markdown(feedback_html(), unsafe_allow_html=True)


# ── Win / loss balloons ───────────────────────────────────────────────────────
if s.status == "win":
    st.balloons()
elif s.status == "loss":
    st.snow()          # snow feels like "game over" confetti; or swap to st.balloons()


# ── Input + submit ────────────────────────────────────────────────────────────
if s.status == "playing":
    st.markdown("<div style='height:.5rem'></div>", unsafe_allow_html=True)
    guess = st.number_input(
        "Your guess",
        min_value=1, max_value=100,
        step=1, value=50,
        key="guess_input",
        label_visibility="collapsed",
        placeholder="Enter a number 1 – 100",
    )

    if st.button("Guess →", key="submit"):
        s.count += 1

        if guess == s.number:
            s.guesses.append((guess, "win"))
            s.status = "win"
        elif guess < s.number:
            s.guesses.append((guess, "low"))
            s.lo = max(s.lo, guess + 1)
        else:
            s.guesses.append((guess, "high"))
            s.hi = min(s.hi, guess - 1)

        if s.status == "playing" and s.count == MAX:
            s.guesses[-1] = (s.guesses[-1][0], "loss")
            s.status = "loss"

        st.rerun()
else:
    # Play again
    st.markdown("<div style='height:.75rem'></div>", unsafe_allow_html=True)
    if st.button("Play again →", key="replay"):
        new_game()
        st.rerun()


# ── Guess history ─────────────────────────────────────────────────────────────
if s.guesses:
    rows = ""
    for i, (g, r) in enumerate(s.guesses, 1):
        if r == "low":
            badge = "<span class='hist-badge badge-low'>Too low ↑</span>"
        elif r == "high":
            badge = "<span class='hist-badge badge-high'>Too high ↓</span>"
        elif r == "win":
            badge = "<span class='hist-badge' style='background:#052e16;color:#6ee7b7'>Correct ✓</span>"
        else:
            badge = "<span class='hist-badge' style='background:#1c0d0d;color:#fca5a5'>✗ Last guess</span>"

        rows += f"""
        <div class='hist-row'>
          <span style='color:#6b6b85;font-size:13px'>#{i}</span>
          <span class='hist-num'>{g}</span>
          {badge}
        </div>"""

    st.markdown(f"""
    <div class='card' style='margin-top:1.5rem'>
      <div style='font-size:13px;color:#6b6b85;text-transform:uppercase;
                  letter-spacing:.05em;margin-bottom:.75rem'>Guess history</div>
      {rows}
    </div>
    """, unsafe_allow_html=True)

