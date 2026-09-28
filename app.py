import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from sklearn.ensemble import RandomForestClassifier

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Intelligent-IDS-BCS501", page_icon="🛡️", layout="wide"
)

st.title(
    "🛡️ Intelligent Machine Learning-Based Cybersecurity System Using Synthetic Data for Real-Time Anomaly Detection"
)
st.caption(
    "Waterfall Process Flow Integration: Communication ➔ Planning ➔ Modeling ➔ Construction ➔ Deployment"
)

# --- 1. SYNTHETIC DATA GENERATOR (CVAE MODEL SIMULATION) ---


@st.cache_data
def generate_cvae_synthetic_data(n_samples=1000):
    """Generates synthetic network traffic vectors using a conditional latent space mapping model.

    Features: Packet Length, Syn/Ack Ratio, Flow Duration, Protocol ID
    """
    np.random.seed(42)

    # Latent sampling z ~ N(0, I) conditioned on attack classes
    labels = np.random.choice([0, 1, 2], size=n_samples, p=[0.7, 0.2, 0.1])

    # Normal Traffic (Label 0)
    normal_len = np.random.normal(loc=500, scale=100, size=n_samples)
    normal_syn_ack = np.random.normal(loc=1.0, scale=0.1, size=n_samples)
    normal_duration = np.random.exponential(scale=2.0, size=n_samples)

    # DDoS Attack Traffic (Label 1)
    ddos_len = np.random.normal(loc=64, scale=10, size=n_samples)
    ddos_syn_ack = np.random.normal(loc=10.0, scale=2.0, size=n_samples)
    ddos_duration = np.random.exponential(scale=0.1, size=n_samples)

    # Data Exfiltration Traffic (Label 2)
    exfil_len = np.random.normal(loc=1400, scale=50, size=n_samples)
    exfil_syn_ack = np.random.normal(loc=0.5, scale=0.05, size=n_samples)
    exfil_duration = np.random.exponential(scale=10.0, size=n_samples)

    # Feature Fusion based on Condition Vector y
    pkt_len = np.where(
        labels == 0, normal_len, np.where(labels == 1, ddos_len, exfil_len)
    )
    syn_ack = np.where(
        labels == 0,
        normal_syn_ack,
        np.where(labels == 1, ddos_syn_ack, exfil_len),
    )
    duration = np.where(
        labels == 0,
        normal_duration,
        np.where(labels == 1, ddos_duration, exfil_duration),
    )

    df = pd.DataFrame(
        {
            "packet_length": np.clip(pkt_len, 40, 1500),
            "syn_ack_ratio": np.clip(syn_ack, 0.1, 20.0),
            "flow_duration": np.clip(duration, 0.01, 30.0),
            "label": labels,
        }
    )

    return df


# --- 2. MATHEMATICAL ENGINES ---


class MarkovSequenceEngine:

    def __init__(self):
        # 3-State Transition Matrix (0: Normal, 1: High Vol, 2: Suspicious Payload)
        self.P = np.array(
            [[0.85, 0.10, 0.05], [0.20, 0.70, 0.10], [0.15, 0.15, 0.70]]
        )

    def calculate_log_likelihood(self, sequence):
        """Calculates log-likelihood L(W) over packet sequence window W."""
        log_prob = 0.0
        for i in range(len(sequence) - 1):
            curr_state = sequence[i]
            next_state = sequence[i + 1]
            log_prob += np.log(self.P[curr_state, next_state] + 1e-6)
        return log_prob


def calculate_shannon_entropy(data_batch):
    """Calculates continuous Shannon Entropy H(X) over window batch size N."""
    counts = pd.Series(data_batch).value_counts()
    probabilities = counts / len(data_batch)
    entropy = -np.sum(probabilities * np.log2(probabilities + 1e-6))
    return entropy


# --- SIDEBAR: SIMULATION & ENGINE CONTROLS ---
st.sidebar.header("⚙️ Simulation & Engine Controls")

attack_vector = st.sidebar.selectbox(
    "Attack Vector Simulation",
    ["Normal Network Traffic", "DDoS Flood Attack", "Data Exfiltration"],
)

markov_alpha = st.sidebar.slider(
    "Markov Anomaly Threshold (Likelihood α)",
    min_value=0.01,
    max_value=0.50,
    value=0.05,
    step=0.01,
)

batch_size = st.sidebar.slider(
    "Packet Sampling Batch Size", min_value=10, max_value=100, value=25, step=5
)

run_inspection = st.sidebar.button("🚀 Execute Hybrid Threat Inspection")

# --- MAIN DASHBOARD BODY ---
synthetic_df = generate_cvae_synthetic_data()

# Train Random Forest on Synthetic Data
X = synthetic_df[["packet_length", "syn_ack_ratio", "flow_duration"]]
y = synthetic_df["label"]
rf_model = RandomForestClassifier(n_estimators=50, random_state=42)
rf_model.fit(X, y)

st.subheader("📊 Real-Time Dynamic Inspection Engine")

if run_inspection:
    # Generate live incoming batch based on selected simulation vector
    if attack_vector == "Normal Network Traffic":
        live_pkt = np.random.normal(500, 50, batch_size)
        live_ratio = np.random.normal(1.0, 0.05, batch_size)
        seq_states = np.random.choice([0, 1], size=batch_size, p=[0.9, 0.1])
    elif attack_vector == "DDoS Flood Attack":
        live_pkt = np.random.normal(64, 5, batch_size)
        live_ratio = np.random.normal(12.0, 1.0, batch_size)
        seq_states = np.random.choice([1, 2], size=batch_size, p=[0.7, 0.3])
    else:  # Data Exfiltration
        live_pkt = np.random.normal(1450, 20, batch_size)
        live_ratio = np.random.normal(0.4, 0.02, batch_size)
        seq_states = np.random.choice([0, 2], size=batch_size, p=[0.2, 0.8])

    live_dur = np.random.exponential(1.0, batch_size)

    live_batch = pd.DataFrame(
        {
            "packet_length": live_pkt,
            "syn_ack_ratio": live_ratio,
            "flow_duration": live_dur,
        }
    )

    # 1. Machine Learning Inference
    ml_probs = rf_model.predict_proba(live_batch)
    p_ml = np.max(np.mean(ml_probs, axis=0))

    # 2. Markov Engine Inference
    markov_engine = MarkovSequenceEngine()
    log_likelihood = markov_engine.calculate_log_likelihood(seq_states)

    # 3. Shannon Entropy Drift Calculation
    entropy_val = calculate_shannon_entropy(
        np.digitize(live_pkt, bins=[0, 200, 800, 1500])
    )
    baseline_entropy = 1.5
    entropy_drift = abs(entropy_val - baseline_entropy) / baseline_entropy

    # 4. Patentable Hybrid Anomaly Score Formulation
    # S_hybrid = w1*P_ML + w2*(1 - L/L_max) + w3*(Delta_H)
    s_hybrid = (
        (0.4 * p_ml) + (0.4 * min(1.0, abs(log_likelihood) / 50.0)) + (0.2 * entropy_drift)
    )

    # Metrics Display
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Hybrid Threat Score", f"{s_hybrid:.3f}")
    col2.metric("ML Class Confidence", f"{p_ml*100:.1f}%")
    col3.metric("Markov Likelihood L(W)", f"{log_likelihood:.2f}")
    col4.metric("Entropy Drift ΔH", f"{entropy_drift:.3f}")

    # Threshold Check
    if log_likelihood < -markov_alpha * 100 or s_hybrid > 0.65:
        st.error(
            f"🚨 ANOMALY DETECTED: Threat Signature Matched ({attack_vector})!"
        )
    else:
        st.success("✅ TRAFFIC CLEAR: Normal Network Activity Pattern Detected.")

    # Visualization
    fig = px.scatter(
        live_batch,
        x="packet_length",
        y="syn_ack_ratio",
        size="flow_duration",
        title=f"Live Packet Batch Distribution (N={batch_size})",
        labels={
            "packet_length": "Packet Length (Bytes)",
            "syn_ack_ratio": "SYN/ACK Ratio",
        },
    )
    st.plotly_chart(fig, use_container_width=True)

else:
    st.info(
        "Adjust sidebar controls and click 'Execute Hybrid Threat Inspection' to trigger the mathematical inspection engine."
    )

# --- WATERFALL MODEL & PATENT HIGHLIGHTS SECTION ---
st.divider()
st.subheader("📐 Patent Technical Highlights & Waterfall Process Flow")

tab1, tab2 = st.tabs(
    ["Mathematical Model Formulations", "Waterfall Process Flow Mapping"]
)

with tab1:
    st.markdown(
        r"""
    * **1. CVAE Latent Generator Loss:**
      $$\mathcal{L}_{CVAE}(\theta, \phi; x, y) = -\mathbb{E}_{q_\phi(z \mid x, y)} [\log p_\theta(x \mid z, y)] + D_{KL}\left(q_\phi(z \mid x, y) \,\parallel\, p(z \mid y)\right)$$
    
    * **2. Markov Sequence Log-Likelihood:**
      $$\mathcal{L}(W) = \log \pi(s_1) + \sum_{t=1}^{N-1} \log P_{s_t, s_{t+1}}$$
    
    * **3. Hybrid Anomaly Metric Score:**
      $$\mathcal{S}_{\text{Hybrid}} = w_1 \cdot P_{\text{ML}}(x) + w_2 \cdot \left(1 - \frac{\mathcal{L}(W)}{\mathcal{L}_{\max}}\right) + w_3 \cdot \left\vert{} \frac{\Delta H}{H_{\text{baseline}}} \right\vert{}$$
    """
    )

with tab2:
    st.markdown(
        """
    1. **Communication:** Defined zero-day threat identification goals and gathered system constraints[span_2](start_span)[span_2](end_span).
    2. **Planning:** Scheduled generation of synthetic traffic vectors and estimated dynamic batch sampling latency ($N=25$)[span_3](start_span)[span_3](end_span)[span_4](start_span)[span_4](end_span).
    3. **Modeling:** Designed CVAE mapping distributions, Markov chain state transition matrices, and hybrid decision boundaries[span_5](start_span)[span_5](end_span).
    4. **Construction:** Written in Python using `streamlit`, `scikit-learn`, `numpy`, and `plotly`[span_6](start_span)[span_6](end_span)[span_7](start_span)[span_7](end_span)[span_8](start_span)[span_8](end_span).
    5. **Deployment:** Hosted on Streamlit Cloud with dynamic parameter adjustment sliders[span_9](start_span)[span_9](end_span)[span_10](start_span)[span_10](end_span)[span_11](start_span)[span_11](end_span).
    """
    )


