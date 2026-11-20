# Sentinel — Intelligent Cybersecurity

**Intelligent Machine Learning-Based Cybersecurity System Using Synthetic Data for Real-Time Anomaly Detection**

AMC Engineering College · CSE (AI & ML) · BCS501 · 20 November 2026

| Team member | USN |
|---|---|
| R Rahul Nayaka | 1AM24CI116 |
| Mohammed Zaid Faizan | 1AM24CI092 |
| P Vishal Ravi | 1AM24CI101 |
| Ujwal sy | 1AM25CI412 |

## Working website

https://sentinel-synth-cybersecurity.vishalravi20k.chatgpt.site

The Sites deployment starts owner-private. The repository and local demo can be used independently; sharing the hosted site requires changing its access setting.


## BCS501 Module 4 — Project Management Documentation

- [Introduction to Project Management: Project and Importance of Project Management](docs/MODULE_4_PROJECT_MANAGEMENT.md) — Team 5, Section B; applies project-management concepts to the verified Sentinel implementation.

## Final implementation

The `submission/` folder is the current, self-contained submission version. Earlier root notebooks, `app.py`, and Markov-model code are retained as historical experiments, not the deployed implementation. This README supersedes earlier unverified performance claims.

- Interactive traffic replay with five synthetic generator profiles, pause/resume, rate selection, anomaly filtering, feature inspection and review acknowledgement.
- Real inference using an exported, trained 40-tree Random Forest; no label-based decisions.
- Manual input and browser-local CSV scoring with strict schema/range validation (5 MB / 5,000 rows).
- Session JSON and prediction CSV exports.
- Threshold exploration, confusion matrix, global feature importance and two measured baseline comparisons.
- Responsive interface, team dossier and completed assignment PDFs in the hosted site's Project dossier.

The website demonstrates real-time **inference on synthetic replay**, not live network capture. It does not block devices or predict attack families. Scenario names are generator ground truth. Refresh clears session state; at most 2,000 session flows are retained.

## Run the final website locally

Python 3.11+ and Node 20+ are sufficient for serving and validation; no npm install is needed.

```bash
cd submission
python -m http.server 8000 --directory dist
```

Open http://localhost:8000. Use an HTTP server; opening index.html directly as a file will prevent fetching JSON artifacts in many browsers.

## Reproduce training and tests

```bash
cd submission
python -m pip install -r requirements.txt
python ml/train.py
node ml/test_inference.mjs
```

`ml/train.py` regenerates 6,000 samples and the exact 80:20 stratified split (seed 42), trains the forest and two baselines, and exports all artifacts into `dist/`. Tree inputs are converted to float32 in JavaScript to match scikit-learn semantics. Every one of the 1,200 held-out predictions is checked for numerical parity.

## Measured results

At threshold 0.50, on 1,200 held-out synthetic samples:

| Model | Accuracy | Precision | Recall | F1 | ROC AUC |
|---|---:|---:|---:|---:|---:|
| Random Forest | 96.83% | 94.79% | 93.64% | 94.21% | 99.00% |
| Decision Tree | 95.67% | 94.55% | 89.39% | 91.90% | 94.30% |
| Logistic Regression | 88.83% | 83.33% | 74.24% | 78.53% | 94.22% |

Forest confusion matrix: TN 853, FP 17, FN 21, TP 309. Synthetic-data results do not establish real-world security effectiveness. Threshold tuning on the test view is exploratory; an operationally selected cutoff requires an independent validation split and untouched final evaluation.

## Data contract

`packet_bytes,duration_ms,packets_per_second,failed_logins,unique_ports,outbound_kb,syn_ratio,error_rate`

All values must be finite and non-negative. Upper bounds, in column order: 65535, 86400000, 10000000, 100000, 65535, 1000000000, 1, 1. Column order may vary. Optional label/scenario fields are ignored by inference. Data is scored locally and is not uploaded to a server. Downloads contain numeric features and system-generated decisions only.

## Three-minute presentation

1. Explain synthetic data and the train/test separation.
2. Start mixed replay; pause and inspect a high-score flow.
3. Show false-positive/false-negative counts and adjust threshold.
4. Run a manual example; upload `sample_traffic.csv`; export predictions.
5. Explain limitations, proposed incremental process and team roles.

## Validation

Automated tests: prediction parity for all 1,200 rows; confusion counts; malformed/missing/range-invalid CSVs; reordered columns; threshold behavior. Browser checks: replay/pause, flow details, review, normal/anomaly manual inference, 150-row CSV import/export, threshold metrics, responsive 390px view. Native iOS Safari was not available; mobile layout was tested in a 390px browser frame.

## References

- [scikit-learn RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)
- [scikit-learn model evaluation](https://scikit-learn.org/stable/modules/model_evaluation.html)
- Assignment templates supplied by the user; completed PDFs delivered separately and available inside the hosted project dossier.
