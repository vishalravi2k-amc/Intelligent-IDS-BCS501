Here is the updated, patent-grade README.md text formatted so that it pastes cleanly on touchscreens without markdown code block rendering issues:
# ML-Based Cybersecurity System Using Synthetic Data for Real-Time Anomaly Detection
**Course Code:** VTU BCS501
**Author:** Vishal Ravi
## 📌 Executive Summary
This project presents an Intrusion Detection System (IDS) designed to identify malicious network activities in real time using Machine Learning. Using synthetic traffic profiles generated via standard statistical distributions, the system trains a **Random Forest Classifier** to evaluate incoming network packets.
## 🏗 System Architecture
 * **Phase 1:** Synthetic Network Data Generation
 * **Phase 2:** Feature Preprocessing & Stratified Train/Test Split
 * **Phase 3:** Random Forest Anomaly Classifier Training
 * **Phase 4:** Real-Time Stream Simulation & Alerting
## 📊 Dataset Specifications
Synthetic network records consist of 5,000 samples categorized into two profiles:
 * **Normal Traffic (85%)**: Gaussian packet length (~500 bytes), exponential flow duration (~2s), low failed login attempts.
 * **Anomalous Traffic (15%)**: High packet length (~1400 bytes), rapid bursts (~0.1s duration), elevated failed login frequency.
## 🚀 Performance Metrics
The model achieves **99.8% classification accuracy** on test sets:
| Metric | Normal (0.0) | Anomaly (1.0) | Macro Avg |
|---|---|---|---|
| **Precision** | 1.00 | 1.00 | 1.00 |
| **Recall** | 1.00 | 0.99 | 0.99 |
| **F1-Score** | 1.00 | 0.99 | 1.00 |
## 💻 How to Run
 1. Open 01_Data_Generation.ipynb in **Google Colab**.
 2. Run all cells sequentially to generate synthetic_ids_data.csv, train the classifier, and trigger live network stream detection.
