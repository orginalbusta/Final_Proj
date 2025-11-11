"""
Fix visualization 4 with better data - use GDP/population data instead of sparse poverty data
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import warnings
warnings.filterwarnings('ignore')

plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

def viz4_population_growth():
    """Visualization 4: Population Growth & Development"""
    df = pd.read_csv('../data/health.csv')
    
    plt.figure(figsize=(12, 6))
    
    # Use population growth rate
    pop_col = 'average_value_Population growth (annual %)'
    
    print(f"Using column: {pop_col}")
    
    # Select diverse countries with interesting development stories
    countries = ['China', 'India', 'Brazil', 'Nigeria', 'Bangladesh', 'Mexico']
    
    colors = sns.color_palette("husl", len(countries))
    
    for i, country in enumerate(countries):
        country_data = df[df['Country Name'] == country].copy()
        if len(country_data) > 0:
            country_data = country_data.sort_values('Year')
            years = country_data['Year'].values
            values = pd.to_numeric(country_data[pop_col], errors='coerce')
            
            mask = ~values.isna()
            if mask.sum() > 10:  # Need at least 10 points
                plt.plot(years[mask], values[mask], marker='o', markersize=2,
                        linewidth=2.5, label=country, alpha=0.85, color=colors[i])
                print(f"  {country}: {mask.sum()} data points")
    
    plt.title('Population Growth Trends in Major Developing Nations (1960-2020)', 
              fontsize=14, fontweight='bold')
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Annual Population Growth (%)', fontsize=12)
    plt.legend(loc='best', frameon=True, fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.axhline(y=0, color='gray', linestyle='--', linewidth=0.8, alpha=0.5)
    plt.tight_layout()
    plt.savefig('../visualizations/04_poverty_decline.png', dpi=300, bbox_inches='tight')
    print("\n[OK] Saved visualization 4: Population Growth")
    plt.close()

if __name__ == "__main__":
    print("Regenerating visualization 4 with population growth data...")
    print()
    viz4_population_growth()
    print("\n[SUCCESS] Visualization 4 fixed!")

