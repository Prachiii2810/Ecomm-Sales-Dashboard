# 📊 E-commerce Sales & Customer Segmentation Dashboard

An interactive end-to-end data analytics application that transforms raw retail sales data into actionable business strategy. This project features a real-time dashboard and a machine-learning-powered customer segmentation model.

## 🚀 [Live Demo Link](PASTE_YOUR_STREAMLIT

---

## 🌟 Project Highlights
- **Business Problem:** Identifying underperforming regions and high-value customer segments to optimize marketing spend.
- **Solution:** Built a dynamic dashboard with **KPI tracking** and **RFM (Recency, Frequency, Monetary) Analysis**.
- **Impact:** Enabled "at-risk" customer identification and identified that **discounts >20%** significantly impact profit margins in the Furniture category.

## 🛠️ Tech Stack
- **Python:** Data processing and modeling.
- **Pandas:** Cleaning and Feature Engineering (RFM).
- **Scikit-Learn:** K-Means Clustering for behavioral segmentation.
- **Plotly:** Interactive time-series and scatter visualizations.
- **Streamlit:** Web-based interface and deployment.

## 📈 Dashboard Features
### 1. Executive Summary (KPIs)
- **Total Revenue & Profit:** High-level metrics with margin percentage indicators.
- **Average Order Value (AOV):** Tracking customer spending behavior per transaction.

### 2. Sales Trend Analysis
- **Monthly Revenue:** Interactive line charts to identify seasonality (specifically the Q4 holiday spike).
- **Sub-Category Breakdown:** Identifying "Cash Cows" vs. "Underperformers."

### 3. RFM Customer Segmentation (Machine Learning)
Using **K-Means Clustering**, customers are grouped into:
- **Champions:** High spenders, bought recently.
- **At-Risk:** Haven't purchased in months; need re-engagement.
- **Loyal:** Consistent shoppers with steady frequency.
- **New/Potential:** Recent first-time buyers.



## 📂 Repository Structure
| File | Description |
| :--- | :--- |
| `app.py` | The main Streamlit application script. |
| `Sample - Superstore.csv` | Raw transaction dataset (9,000+ rows). |
| `requirements.txt` | Configuration file for Streamlit Cloud deployment. |

## ⚙️ How to Run Locally
1. Clone the repo: `git clone [YOUR_REPO_URL]`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `streamlit run app.py`

---
**Developed as part of my Final Year Data Science Portfolio.**
