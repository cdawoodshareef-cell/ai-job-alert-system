import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="AI Job Alert", layout="wide")

st.title("🚀 AI Job Alert Dashboard")

st.write("Click the button below to fetch AI jobs")

# ✅ SEARCH BAR (ALWAYS VISIBLE)
search = st.text_input("🔎 Search Jobs")

# Button
if st.button("🔍 Fetch AI Jobs"):

    url = "https://remoteok.com/api"
    response = requests.get(url)
    jobs = response.json()

    keywords = ["python", "ai", "machine learning", "data", "automation"]

    data = []

    for job in jobs[1:]:
        title = str(job.get("position")).lower()
        company = job.get("company")

        if any(word in title for word in keywords):
            data.append({
                "Position": job.get("position"),
                "Company": company
            })

    df = pd.DataFrame(data)

    # ✅ APPLY SEARCH FILTER
    if search:
        df = df[
            df["Position"].str.contains(search, case=False) |
            df["Company"].str.contains(search, case=False)
        ]

    st.success(f"✅ Found {len(df)} AI Jobs")

    st.dataframe(df, use_container_width=True)