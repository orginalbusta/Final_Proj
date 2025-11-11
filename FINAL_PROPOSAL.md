# DSC 209R Final Project Proposal

## Team Information
**Team Name:** Data Echoes

**Team Members:**
- Camila Paik - capaik@ucsd.edu - A13500891
- Gabrielle Despaigne - gdespaigne@ucsd.edu - A69036674
- Harsh Arya - harya@ucsd.edu - A14644435
- Raghav Vasappanavara - rvasappanavara@ucsd.edu - A69037944

---

## Project Title
**Echoes of History: An Interactive Exploration of Human Development (1960-2020)**

---

## Dataset

**World Bank Data by Indicators (1960-2020)**
- **Source:** https://github.com/light-and-salt/World-Bank-Data-by-Indicators
- **Description:** Pre-cleaned World Bank data tracking 250+ countries across 20 development indicators (climate change, economy, education, health, infrastructure, poverty, etc.) from 1960-2020
- **Size:** Each indicator file contains 10,000+ rows and 50+ columns
- **Type:** Real-world data (not synthetic)

**Why This Dataset:** This dataset is uniquely positioned for an explorable explanation because it spans 60 years of global development during pivotal historical moments—the Cold War, China's economic reforms, the digital revolution, and the 2008 financial crisis. With 20 interconnected indicators across 250+ countries, we can create interactive narratives showing how major events rippled through nations, affecting everything from life expectancy to carbon emissions. The comprehensive coverage allows us to contrast different developmental trajectories and reveal patterns invisible when examining single indicators or countries in isolation.

---

## Project Description

We will create an interactive web-based explorable explanation that transforms 60 years of global development data into an engaging narrative experience. Users will explore through three main modes: (1) a Timeline Navigator for scrubbing through decades while watching animated global changes with historical event annotations; (2) Country Deep Dives where users select any nation to see its development story across all 20 indicators with contextual explanations; and (3) Cross-National Pattern Analysis enabling comparisons of how different regions responded to shared challenges. The experience will emphasize visual storytelling through smooth transitions, linked views, and responsive animations, revealing human stories like how the Green Revolution transformed poverty in Asia, how digital infrastructure created new divides, and how environmental policies shaped our climate crisis. We'll build the visualization using D3.js for custom interactivity, Scrollama.js for scroll-driven storytelling, and deploy as a responsive, publicly accessible webpage.

---

## Static Visualizations

### Visualization 1: Economic Growth Trends (1960-2020)
![GDP Trends](visualizations/01_gdp_trends.png)

Multi-line time series comparing economic indicators for major economies (United States, China, Germany, Japan, India, Brazil). Shows dramatic shifts in global economic power over six decades.

### Visualization 2: Health Indicator Evolution by Region
![Health Indicators](visualizations/02_life_expectancy.png)

Regional comparison of demographic and health metrics across North America, Europe, East Asia, South Asia, Africa, and Latin America, illustrating global health convergence and persistent disparities.

### Visualization 3: Education & Demographics Trends
![Education Progress](visualizations/03_education_progress.png)

Working-age population trends showing demographic transitions in major economies, reflecting education and development patterns.

### Visualization 4: Economic Inequality Indicators
![Poverty Indicators](visualizations/04_poverty_decline.png)

Time series showing economic growth and inequality metrics for developing nations, capturing important development stories of poverty reduction.

### Visualization 5: Climate & CO₂ Emissions
![Climate Emissions](visualizations/05_climate_emissions.png)

Comparison of CO₂ emissions and climate metrics across major economies, revealing environmental costs of industrialization and recent sustainability efforts.

### Visualization 6: Digital Infrastructure Development
![Infrastructure Development](visualizations/06_infrastructure_development.png)

Two-panel visualization showing broadband/internet infrastructure growth (2000-2020) and current digital access comparison, demonstrating the digital divide.

---

**Submission Date:** November 14, 2025  
**Course:** DSC 209R - Data Visualization

