import streamlit as st
from searcher import search_videos
from youtube_fetcher import get_video_description
from extractor import extract_and_classify
from extractor import get_stopwords
get_stopwords()
st.set_page_config(
    page_title="PromoTube️",
    page_icon="assets/discount.png",  # Or use a file: "assets/favicon.ico"
    layout="centered",
    initial_sidebar_state="auto",
)
st.markdown("<h1 style='text-align: center;'>PromoTube</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Find hidden promo codes from YouTube videos 🔎💸</p>", unsafe_allow_html=True)
st.divider()

query = st.text_input("Enter app or product name (e.g., 'NordVPN')")
num = st.number_input("Max videos to check", min_value=1, max_value=10, value=5)
col1, col2 = st.columns([1, 1])

with col1:
    search_clicked = st.button("🔎 Search & Scan", use_container_width=True)

with col2:
    refresh_clicked = st.button("🔄 Refresh", use_container_width=True)

if refresh_clicked:
    st.rerun()

# 🚀 Run search if clicked
if search_clicked and query:
    full_query = f"{query.strip()} Promo Codes"
    st.markdown(f"🔎 Searching for: **{full_query}**")
    videos = search_videos(full_query, max_results=num)

    results = []
    total = len(videos)
    progress = st.progress(0)

    for i, (url, title) in enumerate(videos):

        desc = get_video_description(url)
        if not desc:
            st.warning(f"⚠️ Could not fetch description for: {title}")
            progress.progress((i + 1) / total)
            continue

        info = extract_and_classify(desc)
        if info["links"] or info["promo_codes"]:
            results.append({"title": title, "url": url, **info})

        progress.progress((i + 1) / total)

    st.markdown("---")

    if results:
        st.subheader("📦 Found Promo Links & Codes:")

        for r in results:
            st.markdown(f"""
                <div class='promo-box'>
                    <h4>📺 <a href="{r['url']}" target="_blank">{r['title']}</a></h4>
                """, unsafe_allow_html=True)

            if r["links"]:
                st.markdown("#### 🔗 Promo Links")
                categorized = {}
                for item in r["links"]:
                    link_type = item["type"]
                    categorized.setdefault(link_type, []).append(item["link"])

                for cat, links in categorized.items():
                    with st.expander(f"🔖 {cat.title()}"):
                        for l in links:
                            st.markdown(f"- [{l}]({l})")

            if r["promo_codes"]:
                st.markdown("#### 🔐 Promo Codes")
                for code in r["promo_codes"]:
                    st.code(code)
            st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.info("No promo codes or links found in the top videos.")
