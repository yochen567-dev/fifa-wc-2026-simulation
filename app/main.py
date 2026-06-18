import os
import subprocess

# 1. 强行把当前运行环境的目录，切换到项目的绝对根目录下
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
os.chdir(base_dir)

# 2. 检查如果数据库文件不存在，则强制触发数据初始化
db_path = os.path.join(base_dir, "app", "data", "predictions.db") # 或者项目的db名
if not os.path.exists(db_path):
    # 使用绝对路径强制执行初始化脚本
    script_path = os.path.join(base_dir, "duckdb_run.py")
    subprocess.run(["python", script_path], check=True)

# Add app directory to path for local imports
sys.path.insert(0, os.path.dirname(__file__))

st.set_page_config(
    page_title="FIFA World Cup 2026 Simulation Explorer",
    page_icon="\U0001f3c6",
    layout="wide",
    initial_sidebar_state="collapsed",
)

from ui.theme import inject_css

inject_css()

# Define pages
pages = [
    st.Page("pages/landing.py", title="Home", icon="\U0001f3c6", default=True),
    st.Page("pages/competition.py", title="Competition Explorer", icon="\U0001f4ca"),
    st.Page("pages/team.py", title="Team Explorer", icon="\u26bd"),
    st.Page("pages/city.py", title="City Explorer", icon="\U0001f3d9\ufe0f"),
    st.Page("pages/simulator.py", title="Simulator", icon="\U0001f3ae"),
    st.Page("pages/about.py", title="About Project", icon="\u2139\ufe0f"),
]

pg = st.navigation(pages, position="hidden")

# ── Navigation ───────────────────────────────────────────────────────────────

# Desktop Navigation — native Streamlit page links styled horizontally via CSS
# Hidden on mobile via CSS (.st-key-desktop_nav).
with st.container(key="desktop_nav"):
    st.markdown("<div class='wc-nav-brand'>🏆 FIFA WC 2026</div>", unsafe_allow_html=True)
    st.page_link("pages/landing.py", label="🏆 Home")
    st.page_link("pages/competition.py", label="📊 Competition")
    st.page_link("pages/team.py", label="⚽ Teams")
    st.page_link("pages/city.py", label="🏙️ City")
    st.page_link("pages/simulator.py", label="🎮 Simulator")

# Mobile Navigation (Hamburger / Expander) — hidden on desktop via CSS (.st-key-mobile_nav)
with st.container(key="mobile_nav"):
    with st.expander("🏆 FIFA WC 2026  ·  Menu", expanded=False):
        st.page_link(
            "pages/landing.py", label="\U0001f3c6 Home", width="stretch"
        )
        st.page_link(
            "pages/competition.py",
            label="\U0001f4ca Competition",
            width="stretch",
        )
        st.page_link("pages/team.py", label="\u26bd Teams", width="stretch")
        st.page_link(
            "pages/city.py", label="\U0001f3d9\ufe0f City", width="stretch"
        )
        st.page_link(
            "pages/simulator.py", label="\U0001f3ae Simulator", width="stretch"
        )

st.divider()

pg.run()
