# Echoes of History: An Interactive Exploration of Human Development (1960-2020)

## DSC 209R Final Project - Team Data Echoes

### Team Members
- Camila Paik - capaik@ucsd.edu - A13500891
- Gabrielle Despaigne - gdespaigne@ucsd.edu - A69036674
- Harsh Arya - harya@ucsd.edu - A14644435
- Raghav Vasappanavara - rvasappanavara@ucsd.edu - A69037944

---

## Project Overview

An interactive web-based explorable explanation visualizing 60 years of global development using World Bank data across 20 key indicators and 250+ countries.

## Dataset

**World Bank Data by Indicators (1960-2020)**
- Source: https://github.com/light-and-salt/World-Bank-Data-by-Indicators
- 20 indicator categories (climate, economy, education, health, infrastructure, poverty, etc.)
- 250+ countries, 60 years (1960-2020)

## Project Structure

```
Final_Proj/
├── FINAL_PROPOSAL.md          # Main proposal document for submission
├── visualizations/             # 6 static visualizations (PNG)
├── data/                       # Downloaded World Bank datasets
├── src/                        # Python scripts for data processing
└── requirements.txt            # Python dependencies
```

## Visualizations

1. **Economic Growth Trends** - Major economies comparison (1960-2020)
2. **Health Indicator Evolution** - Regional demographic changes
3. **Education & Demographics** - Working-age population trends
4. **Economic Inequality** - Development and inequality metrics
5. **Climate & CO₂ Emissions** - Environmental indicators
6. **Digital Infrastructure** - Broadband/internet growth

## Setup (Optional)

To regenerate visualizations:

```bash
pip install -r requirements.txt
cd src
python download_data.py
python create_visualizations_v2.py
```

## Submission

- **Team Registration:** Wed 11/12, 11:59pm
- **Proposal:** Fri 11/14, 11:59pm
- **Main Document:** `FINAL_PROPOSAL.md`

---

**Course:** DSC 209R - Data Visualization | Fall 2025
