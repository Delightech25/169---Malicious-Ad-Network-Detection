# Malicious Ad Network Detection

An advanced security analytics and machine learning framework designed to detect, analyze, and mitigate malicious advertising (malvertising) networks, fraudulent tracking domains, and unauthorized payload injections across web platforms.

---

## 📖 Overview
Modern digital advertising ecosystems are frequently exploited by malicious actors to distribute malware, phishing links, and drive-by downloads through compromised ad networks (malvertising). Traditional signature-based blockers often struggle against obfuscated JavaScript and dynamic redirect chains.

The **Malicious Ad Network Detection** project provides a robust framework to monitor advertising traffic, analyze network request behaviors, inspect iframe hierarchies, and classify malicious ad domains. By leveraging machine learning classification and heuristic rule sets, this tool empowers security analysts and web administrators to protect users from deceptive ad campaigns and supply-chain compromises.

---

## 🔑 Key Features & Objectives
* **Ad Traffic Behavioral Analysis:** Ingests and parses web traffic telemetry, ad-server callbacks, and redirection chains to identify anomalies.
* **Heuristic & Signature Screening:** Detects obfuscated scripts, malicious landing page redirects, and known threat indicators associated with fraudulent ad networks.
* **Risk Scoring & Classification:** Evaluates ad domains and banner payloads using machine learning models to categorize threats (Safe, Suspicious, Malicious).
* **Actionable Reporting:** Generates comprehensive audit logs and threat summaries to streamline ad-fraud prevention and endpoint security.

---

## 🛠️ Core Architecture & Pipeline

1. **Data Collection & Ingestion:** 
   * Captures network logs, HTTP/HTTPS request headers, script execution payloads, and redirection URLs.
2. **Feature Extraction & Processing:** 
   * Extracts behavioral features, domain entropy, iframe mutation frequencies, and third-party script call patterns.
3. **Machine Learning Classification Engine:** 
   * Trains robust classification models (such as Random Forest and Gradient Boosting) to differentiate between legitimate ad networks and malicious actors.
4. **Reporting & Dashboarding:** 
   * Outputs structured incident logs and visualization metrics tracking blocked malvertising attempts.

---

## 🛠️ Tech Stack
* **Language:** Python
* **Data Processing & Analysis:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn
* **Visualization:** Matplotlib, Seaborn

---

## ⚙️ Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Delightech25/169---Malicious-Ad-Network-Detection.git](https://github.com/Delightech25/169---Malicious-Ad-Network-Detection.git)
   cd 169---Malicious-Ad-Network-Detection
