# Australian Electricity Price Analysis: The Duck Curve in Queensland (QLD)

A data analytics project that explores real-time electricity market data from the **Australian Energy Market Operator (AEMO)** to investigate the occurrence of negative wholesale electricity prices and the famous "Duck Curve" phenomenon in Queensland.

---

## 📌 Project Overview
With the rapid adoption of rooftop solar in Queensland, the National Electricity Market (NEM) frequently experiences **negative electricity prices** during midday. This project uses Python (`pandas` & `matplotlib`) to analyze historical data from June 2026 to identify:
* The specific hours when electricity prices drop below \$0/MWh.
* The financial and operational impacts of solar peak generation on the grid.

---

## 📊 Key Findings from Data
* **Data Source:** AEMO Monthly Price and Demand (June 2026 - QLD1).
* **The "Clean Energy Peak" Trap:** Wholesale prices regularly crash below zero between **9 AM and 3 PM** due to massive solar injection.
* **The Evening Peak:** As the sun sets and household demand spikes, prices sharp spike back to positive territory, forming the classic **Duck Curve**.

---

## 💻 Tech Stack & Features
* **Language:** Python
* **Libraries:** `pandas` (Data processing & Aggregation), `matplotlib` (Data Visualization).
* **Core Logic:** 
  * Parses datetime intervals from AEMO settlement data.
  * Filters and groups negative price intervals to find the lowest-priced hours.
  * Generates bar charts analyzing average hourly price fluctuations.

---

## 🚀 How to Run the Code
1. Clone this repository to your local machine.
2. Download NEM Price and Demand data file from AEMO and upload into your local machine.
3. Run the interactive script (`main.py` or `.ipynb` notebook) and follow the instruction
4. You expect to see some major information of the data and 2 illustration windows pop up
