
# 🚗 EV Adoption & Market Dynamics – Washington State

_An data analysis project examining electric vehicle adoption trends, technology evolution, and geographic concentration to support policy, infrastructure, and business decisions._


---

## 📌 Table of Contents
- <a href="#overview">Overview</a>
- <a href="#business-problem">Business Problem</a>
- <a href="#Analytical-Scope">Analytical Scope</a>
- <a href="#dataset">Dataset</a>
- <a href="#tools--technologies">Tools & Technologies</a>
- <a href="#project-structure">Project Structure</a>
- <a href="#data-cleaning--preparation">Data Cleaning & Preparation</a>
- <a href="#exploratory-data-analysis-eda">Exploratory Data Analysis (EDA)</a>
- <a href="#research-questions--key-findings">Research Questions & Key Findings</a>
- <a href="#Key KPIs">Key KPIs</a>
- <a href="#how-to-run-this-project">How to Run This Project</a>
- <a href="#final-recommendations">Final Recommendations</a>
- <a href="#author--contact">Author & Contact</a>

---
<h2><a class="anchor" id="overview"></a>Overview</h2>

- This project analyzes Electric Vehicle (EV) adoption trends in Washington State from 2000 to 2026.

- The analysis focuses on:
  - EV adoption growth over time
  - Technology comparison (BEVs vs PHEVs)
  - Electric range evolution
  - Manufacturer and model dominance
  - Geographic concentration at county and city levels

- The goal is to convert public EV registration data into actionable insights for:
  - Policymakers
  - Infrastructure planners
  - Automotive businesses
  - Market strategists

---
<h2><a class="anchor" id="business-problem"></a>Business Problem</h2>

- Washington State has been a leader in EV adoption, but recent data shows:
  - Rapid adoption growth peaking in 2023
  - A noticeable decline post-2023
  - Heavy geographic concentration in a few counties and cities
  - Clear technological divergence between BEVs and PHEVs

- This raises key questions:
  - Is EV adoption sustainable without continued policy support?
  - Which regions should be prioritized for charging infrastructure?
  - Which EV technologies and manufacturers are shaping the future?

---
<h2><a class="anchor" id="Analytical-Scope"></a>Analytical Scope</h2>

- Adoption trends and year-over-year growth (2000–2026)
- Market share comparison: BEVs vs PHEVs
- Manufacturer dominance and model-level concentration
- Electric range distribution and median benchmarking
- Range improvement trends across model years
- County-wise and city-wise EV adoption concentration
- Identification of core EV hubs vs emerging regions

---
<h2><a class="anchor" id="dataset"></a>Dataset</h2>

- Public Electric Vehicle registration data for Washington State
- Includes:
  - Model year
  - Vehicle make & model
  - EV type (BEV / PHEV)
  - Electric range
  - County and city-level registration counts

- The dataset supports both trend analysis and geographic segmentation.

---
<h2><a class="anchor" id="tools--technologies"></a>Tools & Technologies</h2>

- Python
  - Pandas
  - Matplotlib
  - Seaborn
- Jupyter Notebook
- Git & GitHub
- PDF Reporting

---
<h2><a class="anchor" id="project-structure"></a>Project Structure</h2>

``` 
EV-Adoption-Market-Dynamics-WA/
│
├── README.md
├── EV_Adoption&Market_Dynamics.pdf
│
├── Notebooks/
│   └── EV Adoption & Market Dynamics – Washington State.ipynb
│
├── Images/
│   └── (Exported charts & visuals)
``` 

---
<h2><a class="anchor" id="data-cleaning--preparation"></a>Data Cleaning & Preparation</h2>

- Key preparation steps performed in Python:
  - Removed missing and invalid electric range values
  - Standardized EV type labels (BEV / PHEV)
  - Converted model year to numeric format
  - Filtered incomplete records for recent years

- Created derived metrics:
  - Year-over-Year (YoY) growth
  - Median and average electric range
  - Percentage contribution by geography

---
<h2><a class="anchor" id="exploratory-data-analysis-eda"></a>Exploratory Data Analysis (EDA)</h2>

#### EV Adoption Over Time
- Minimal adoption before 2010 (experimental phase)
- Strong growth post-2017
- Peak adoption in 2023 (~60,000 registrations)
- Decline observed in 2024–2025 (policy, supply, or saturation effects)

#### Technology Comparison
- BEVs dominate the market (~80%)
- PHEVs remain a secondary, transitional technology

#### Electric Range Analysis
- BEVs: Wide range distribution (100–350+ miles)
- PHEVs: Tightly clustered around 20–50 miles
- Clear technology gap favoring BEVs

#### Geographic Concentration
- King County alone accounts for ~50% of all EVs
- Seattle contributes ~16% of statewide adoption
- Top 5 cities account for ~31% of total EVs

---
<h2><a class="anchor" id="research-questions--key-findings"></a>Research Questions & Key Findings</h2>

Research Questions & Key Findings

**Which EV type dominates adoption?** 
- BEVs lead with ~79.6% market share.

**Which manufacturers dominate?**
- Tesla leads with ~41.5% of total EVs.

**Which models are most popular?**
- Tesla Model Y and Model 3 together exceed one-third of all EVs.

**How has electric range evolved?**
- BEV range improved by ~136% since early 2000s; PHEVs remain flat.

**Where is adoption concentrated?**
- King County and Seattle act as the core EV hubs.

---
<h2><a class="anchor" id="Key KPIs"></a>Dashboard</h2>

- Peak Adoption Year: 2023 (+103% YoY growth)
- Median Electric Range
  - BEV: ~215 miles
  - PHEV: ~25 miles
- King County Share: ~50% of all EVs
- Seattle Share: ~41,000 EVs (~15.8%)
- BEV Range Growth: +136% since early 2000s

---

<h2><a class="anchor" id="how-to-run-this-project"></a>How to Run This Project</h2>

1. Clone the repository:
```bash
git clone https://github.com/yourusername/EV-Adoption-Market-Dynamics-WA.git
```
2. Open the Jupyter Notebook:
   - 'Notebooks/EV Adoption & Market Dynamics – Washington State.ipynb'

3. Run all cells to reproduce the analysis, visualizations and insights

4. Review the detailed report:
   - 'EV_Adoption&Market_Dynamics.pdf'


---
<h2><a class="anchor" id="final-recommendations"></a>Final Recommendations</h2>

- Prioritize BEV-focused infrastructure (fast chargers, grid upgrades)
- Expand charging networks beyond King County to reduce adoption imbalance
- Support affordability and incentives post-2023 to stabilize adoption
- Target secondary cities (Bellevue, Redmond, Vancouver) for growth
- De-emphasize PHEVs as long-term investments favor BEVs
- These actions support sustainable EV growth and smarter infrastructure planning.


---
<h2><a class="anchor" id="author--contact"></a>Author & Contact</h2>

**Kishan Patil**  
Data Analyst  

📧 **Email:** kishanpatil.da@gmail.com  
🔗 **LinkedIn:** https://www.linkedin.com/in/kishanspatil

