# MODULE 4 — Introduction to Project Management

**Subject:** BCS501 — Software Engineering and Project Management  
**Course module:** Module 4 (10 teaching hours)  
**Topic covered in this document:** Introduction to Project Management; Project; Importance of Project Management  
**Institution:** AMC Engineering College, Department of CSE (AI & ML)  
**Section:** B | **Team:** 5  
**Case-study project:** **Sentinel — Intelligent Machine Learning-Based Cybersecurity System Using Synthetic Data for Real-Time Anomaly Detection**  
**Documentation date:** 20 November 2026

| Student | USN |
|---|---|
| R Rahul Nayaka | 1AM24CI116 |
| Mohammed Zaid Faizan | 1AM24CI092 |
| P Vishal Ravi | 1AM24CI101 |
| Ujwal sy | 1AM25CI412 |

> **Evidence convention:** "Implemented / verified" refers to the current repository's code, README, and test scripts. "Proposed" or "illustrative" indicates a project-management plan or goal, **not** a claim that the activity has already happened. The module's **10 hours** is a teaching allocation; it is **not** the project's actual development duration.

---

## 1. Introduction to Project Management

**Project management** is the application of knowledge, skills, tools, and techniques to plan, organize, execute, monitor, and control activities so that a defined project objective is achieved within agreed scope, time, cost, and quality constraints.

Software projects need management because changing requirements, technical uncertainty, integration problems, limited resources, and delivery deadlines can affect results even when the programming is correct.

In **Sentinel**, project management links the academic assignment's cybersecurity problem to a demonstrable, testable software deliverable. It coordinates synthetic-data generation, ML model training, model export, website construction, browser inference, quality checks, documentation, and presentation.

### Why technical work alone is not enough

A model with strong classification metrics is not a complete project unless it also has a usable interface, validated inputs, reproducible experiments, honest performance reporting, documentation, and a submission-ready demonstration.

The team therefore manages **both** the technical output and the process used to produce it.

## 2. What Is a Project?

A **project** is a temporary endeavor undertaken to create a unique product, service, or result. It has a defined objective, a beginning and an end, identifiable stakeholders, limited resources, and measurable acceptance criteria.

### Characteristics of Sentinel as a project

| Project characteristic | Application to Sentinel |
|---|---|
| Temporary | Built as a defined BCS501 academic submission with a deliverable and review. |
| Unique output | A cybersecurity anomaly-detection learning and demonstration website combining generated traffic, trained inference, and evaluation. |
| Clear goal | Demonstrate how an ML model can score synthetic network flows as normal or anomalous. |
| Scope boundaries | Browser-local synthetic-data inference and analysis, not production intrusion prevention. |
| Stakeholders | Four-member student team, course faculty/reviewer, and demonstration users. |
| Constraints | Academic submission requirements, validation, available computing resources, and team coordination. |
| Risk/uncertainty | Model generalization, data leakage, unsuitable test claims, inconsistent web inference, and UI defects. |
| Deliverables | Website, source code, training script, model artifacts, test code, README, and project documentation. |

**Project versus operations:** Building and submitting Sentinel is a **project**; continuously running, monitoring, patching, and supporting a production security service would be **operations**. Sentinel does not currently represent that operational service.

## 3. Project Overview and Problem Statement

### 3.1 Problem statement

Students and early-stage security teams need a safe way to understand anomaly detection on network-flow features. Using real attack traffic raises collection, privacy, permission, and operational challenges. A simulation-based educational system can demonstrate the development and evaluation workflow without monitoring real user traffic.

### 3.2 Existing limitations addressed

- Raw model results are difficult to explain without interactive visual inspection.
- Demonstrations may show predetermined labels rather than running a trained model.
- ML metrics can be misleading when the source data is synthetic or when validation is weak.
- A college project also needs traceable code, reproducible testing, and a presentation-ready interface.

### 3.3 Proposed solution and verified current implementation

Sentinel is a **browser-based anomaly-detection laboratory**, not an operational network intrusion detection system.

**Implemented / verified in the repository:**

1. A reproducible synthetic-data generator and model-training pipeline in [submission/ml/train.py](../submission/ml/train.py).
2. **6,000 synthetic observations** with eight numeric flow features, divided using an **80:20 stratified train/test split** (random seed 42).
3. A trained **40-tree Random Forest** anomaly classifier, compared with a Decision Tree and Logistic Regression.
4. Exported model and evaluation artifacts consumed by the browser application in [submission/dist/](../submission/dist/).
5. Interactive synthetic flow replay, manual feature entry, CSV scoring, session inspection, model evaluation, and export features, described in the [main README](../README.md).
6. Numerical parity and input-validation checks in [submission/ml/test_inference.mjs](../submission/ml/test_inference.mjs).

**Not claimed:** live packet capture, device isolation/blocking, attack-family prediction from the binary model, real-world operational detection accuracy, or permanent server-side monitoring.

## 4. Project Objectives

| ID | Objective | How success can be checked |
|---|---|---|
| O1 | Produce synthetic normal/anomalous flow data with defined feature meanings. | Generator runs reproducibly; dataset schema is consistent. |
| O2 | Train and compare anomaly-detection models. | Reproducible training and published held-out synthetic metrics. |
| O3 | Use a real exported model for browser-side predictions. | JavaScript results match Python outputs on held-out examples. |
| O4 | Provide a comprehensible demonstration website. | Replay, details, manual entry, CSV analysis, and export can be exercised. |
| O5 | Prevent misleading or invalid data input. | Invalid/missing/out-of-range inputs are rejected by tests. |
| O6 | Produce maintainable submission evidence. | Repository code, instructions, report, and demonstrated limitations are accessible. |

## 5. Project Scope

### In scope — current demonstrator

- Synthetic traffic scenario generation and replay.
- Binary anomaly scoring using a trained Random Forest.
- Eight numeric features: `packet_bytes`, `duration_ms`, `packets_per_second`, `failed_logins`, `unique_ports`, `outbound_kb`, `syn_ratio`, and `error_rate`.
- Manual and CSV input, with in-browser validation.
- Synthetic holdout evaluation, visualizations, and data exports.
- Basic responsiveness and user-facing documentation.

### Out of scope — not implemented

- Real-time capture from campus or external networks.
- Enforcement actions such as blocking IP addresses or devices.
- A verified production deployment or SOC integration.
- Detection claims validated against independent real-world traffic.
- Persistent multi-user authentication, case management, or storage.

**Scope-control rule:** a requested new feature should be assessed for educational value, feasibility, evidence requirements, and effect on testing before it is accepted into the baseline.

## 6. Importance of Project Management — Applied to Sentinel

| Why project management matters | How it applies to this project |
|---|---|
| **Clear objectives** | Keeps the deliverable focused on demonstrating synthetic-data anomaly detection rather than promising a complete cybersecurity defense product. |
| **Scope management** | Prevents last-minute additions such as live packet sniffing that would require permissions, new architecture, and separate validation. |
| **Time management** | Orders data generation, training, inference integration, front-end work, testing, and submission so that dependencies are respected. |
| **Resource management** | Coordinates four students, their code contributions, review time, and available computers/tools. |
| **Cost management** | Favors open-source libraries and a static website for the demonstrator; any monetary budget must be separately approved and recorded. |
| **Quality assurance** | Requires model-comparison results, input-validation tests, and Python/JavaScript prediction parity, not just an attractive UI. |
| **Risk management** | Identifies synthetic-to-real-world generalization limitations, false alarms, broken exports, and deployment-access problems early. |
| **Communication** | Provides a README, evidence links, deliverable checklist, and a consistent explanation for the faculty reviewer. |
| **Accountability** | Makes tasks, acceptance checks, and contributions visible without inventing who completed unspecified work. |
| **Stakeholder satisfaction** | Ensures that a faculty member can understand the problem, demonstrate the system, and inspect supporting evidence. |

### An example of an unmanaged change

If the team added "capture and block live campus network attacks" just before review, the requirement would change data permissions, architecture, threat model, safety review, testing, and deployment needs. A managed response is to record it as a **future enhancement** and preserve the validated demonstration scope for the present submission.

## 7. Stakeholders and Team Management

| Stakeholder | Interest or expectation | Suggested engagement |
|---|---|---|
| Faculty / course reviewer | Correct software-engineering concepts and defensible project evidence | Review requirements, progress, demo, and documentation. |
| Four team members | Clear tasks, integration, achievable deadlines | Maintain a shared task board, review changes, and check deliverables. |
| Demonstration users | Intuitive navigation and understandable anomaly scores | Conduct short usability trials and collect observations. |
| Future security researchers (possible) | Reproducibility and clear limitations | Publish generator, scripts, test cases, and assumptions. |

**Suggested task ownership (not a historical record):** one owner for ML/data, one for web interface, one for integration/testing, and one for documentation/presentation; all four should cross-review the final system. Confirm individual assignments with the team rather than treating these roles as established fact.

## 8. Project Life Cycle — Illustrative Management Plan

| Stage | Activities applied to Sentinel | Milestone / evidence |
|---|---|---|
| **Initiation** | Identify the cybersecurity education problem, users, project title, and scope boundaries. | Approved problem statement and project concept. |
| **Planning** | Specify eight features, data pipeline, training plan, UI components, tests, responsibilities, and risks. | Requirements, work breakdown, acceptance criteria. |
| **Execution** | Implement data generator, train/evaluate models, export trees, build the browser lab, add CSV/replay workflows. | Working source files and application. |
| **Monitoring and control** | Compare model predictions, run tests, review issues, verify UI behavior, manage changes. | Test outputs, review notes, tracked defects. |
| **Closing** | Demonstrate features, finalize README and assignments, record limitations and future work. | Repository and faculty presentation package. |

This table describes an appropriate **management interpretation**, not a reconstructed log of dated historical events.

### Suggested work breakdown structure (WBS)

1. **Requirements & planning:** scope, stakeholders, success criteria, risks.
2. **Data & ML:** synthetic generator, split, models, metrics, exported artifacts.
3. **Application:** website interface, browser inference, CSV parser, replay, charts.
4. **Verification:** inference parity, negative tests, responsive checks, documentation review.
5. **Submission:** README, assignment PDFs, project demo, limitations, presentation.

### Dependency sequence

`Requirements → Data schema → Training/evaluation → Model export → Browser integration → Tests → Demo/submission`

The UI and documentation can be worked on concurrently after the interfaces and scope are agreed upon.

## 9. Balancing the Project Constraints

The classic project constraints are **scope, schedule, cost/resources, and quality**. Changing one affects the others.

- **Scope:** Retain a verifiable educational system; treat production security features as future work.
- **Time:** Use milestones and prioritize the working minimum demonstrator before polish.
- **Cost/resources:** Use existing student machines, Python, scikit-learn, JavaScript, and suitable static hosting; no actual spend or labor-hour total is asserted here.
- **Quality:** Require valid input handling, reproducibility, numerical parity, clear interface behavior, and limitations disclosure.

**Example trade-off:** A new flow visualization may be valuable, but if it puts regression testing at risk, the team should defer it until the validated baseline is secure.

## 10. Risks and Mitigation Plans

| Risk | Impact | Proposed response |
|---|---|---|
| Synthetic performance mistaken for field performance | Misleading academic claim | Label metrics as synthetic-only; explicitly discuss external-validity limitations. |
| Train/test leakage or unrepeatable results | Inflated or irreproducible scores | Fix random seed, document split, preserve holdout metrics and test artifacts. |
| Browser model differs from Python model | Incorrect predictions | Run numerical parity tests for every exported held-out prediction. |
| Invalid or oversized CSV input | Application errors or slow response | Validate schema, ranges, row count, and file size before scoring. |
| Late feature expansion | Missed review or incomplete validation | Use a change log, priority ranking, and explicit scope acceptance. |
| Unavailable or private hosted site | Demo inaccessible to reviewer | Keep the GitHub repository and local HTTP-server demonstration path available; verify website access before submission. |
| Lack of team coordination | Duplicate effort and unresolved defects | Assign owners and reviewers and use brief milestone check-ins. |

These are **recommended controls**, not evidence that every formal management process was already completed.

## 11. Verification and Project Success Criteria

### Repository-based evidence

According to the [README](../README.md), the Random Forest measured on **1,200 held-out synthetic flows** (threshold 0.50):

| Measure | Reported synthetic holdout result |
|---|---:|
| Accuracy | 96.83% |
| Precision | 94.79% |
| Recall | 93.64% |
| F1 score | 94.21% |
| ROC AUC | 99.00% |
| Confusion matrix | TN 853, FP 17, FN 21, TP 309 |

These results support an **educational synthetic-data demonstration**; they do **not** prove performance on live or independently sourced network traffic. Threshold choices explored on the held-out view would require separate validation before any operational decision.

### Recommended final acceptance checklist

- [ ] Problem statement and scope match the application.
- [ ] All four student names/USNs and team details are accurate.
- [ ] Training can be reproduced from the documented instructions.
- [ ] Prediction-parity and input-validation tests pass.
- [ ] Replay, manual prediction, CSV analysis, and export can be demonstrated.
- [ ] README explains synthetic-only operation and limitations.
- [ ] Faculty can open the required repository and demonstration.
- [ ] Final assignment documentation is reviewed and approved.

Items in this checklist require final submission review; their presence is **not** an assertion that all checks are complete.

## 12. Conclusion

Sentinel shows why project management is necessary even for a student software project. A successful outcome needs more than an ML algorithm: it requires a well-defined temporary endeavor, realistic scope, stakeholder coordination, sequencing, quality evidence, controlled change, and an honest explanation of limitations.

**Module 4 takeaway:** Project management transforms an idea into a planned, testable, reviewable software deliverable while balancing **scope, time, cost/resources, and quality**.

---

## Repository References and Reproduction

- [Main README: final implementation and limitations](../README.md)
- [ML training and synthetic-data generation](../submission/ml/train.py)
- [Browser-inference validation tests](../submission/ml/test_inference.mjs)
- [Python dependency versions](../submission/requirements.txt)
- [Static website entry point](../submission/dist/index.html)

Reproduce the training and automated checks using the commands documented in [README.md](../README.md):

```bash
cd submission
python -m pip install -r requirements.txt
python ml/train.py
node ml/test_inference.mjs
```

**Faculty note:** This document addresses the *specified introductory part of Module 4*. The term **10 hours** labels the full module's teaching allocation, not an estimate of time spent developing Sentinel.
