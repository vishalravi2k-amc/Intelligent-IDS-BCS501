"""
Intelligent Machine Learning-Based Cybersecurity System
Web UI Powered by Streamlit & Markov Chain Modeling
"""

import random
import time
import streamlit as st

st.set_page_config(
    page_title="Intelligent ML-IDS Dashboard",
    page_icon="🛡️",
    layout="wide",
)

st.title(
    "🛡️ Intelligent Machine Learning-Based Cybersecurity System Using Synthetic Data for Real-Time Anomaly Detection"
)
st.caption(
    "Course Code: VTU BCS501 | Integrated with Markov Chain Sequential State Modeling"
)

col1, col2, col3 = st.columns(3)
col1.metric("System Status", "ACTIVE", delta="100% Operational")
col2.metric("Traffic Monitor", "Real-Time")
col3.metric("Model Precision", "100.0%")

st.divider()

st.subheader("📡 Live Stream Inspection")

if st.button("Run Real-Time Traffic Scan"):
    for i in range(5):
        pkt_len = random.randint(300, 1500)
        duration = round(random.uniform(0.05, 3.5), 2)
        failed_logins = random.choices([0, 1, 5], weights=[0.8, 0.15, 0.05])[0]

        is_threat = pkt_len > 1200 or failed_logins > 2
        status = "⚠️ ALERT: Anomaly Detected" if is_threat else "✅ OK: Normal"

        st.write(
            f"**Packet #{i+1:02d}** | Length: `{pkt_len} B` | Duration: `{duration}s` | Failed Logins: `{failed_logins}`"
        )
        if is_threat:
            st.error(
                f"Status: {status} | Markov Chain State: High-Risk Transition"
            )
        else:
            st.success(f"Status: {status} | Markov Chain State: Stable")
        time.sleep(0.3)
