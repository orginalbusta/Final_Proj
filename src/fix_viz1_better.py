"""
Fix visualization 1 with GDP constant data for better comparison
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import warnings
warnings.filterwarnings('ignore')

plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

def viz1_gdp_growth():
    """Visualization 1: GDP Growth using constant 2010 US$"""
    df = pd.read_csv('../data/economy-and-growth.csv')
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    # Use GDP constant 2010 US$ for fair comparison
    gdp_col = 'average_value_GDP (constant 2010 US$)'
    
    print(f"Using column: {gdp_col}")
    
    countries = ['United States', 'China', 'Germany', 'Japan', 'India', 'Brazil']
    colors = sns.color_palette("husl", len(countries))
    
    # Left plot: Absolute GDP
    for i, country in enumerate(countries):
        country_data = df[df['Country Name'] == country].copy()
        if len(country_data) > 0:
            country_data = country_data.sort_values('Year')
            years = country_data['Year'].values
            values = pd.to_numeric(country_data[gdp_col], errors='coerce')
            
            mask = ~values.isna()
            if mask.sum() > 5:
                # Convert to trillions for readability
                values_trillions = values / 1e12
                ax1.plot(years[mask], values_trillions[mask], marker='o', markersize=2,
                        linewidth=2, label=country, alpha=0.85, color=colors[i])
                values_masked = values[mask].values
                print(f"  {country}: {mask.sum()} data points, latest GDP: ${values_masked[-1]/1e12:.2f}T")
    
    ax1.set_title('GDP Growth: Major Economies (1960-2020)', fontsize=13, fontweight='bold')
    ax1.set_xlabel('Year', fontsize=11)
    ax1.set_ylabel('GDP (Trillion US$, constant 2010)', fontsize=11)
    ax1.legend(loc='best', frameon=True, fontsize=9)
    ax1.grid(True, alpha=0.3)
    
    # Right plot: Indexed growth (1960 = 100)
    for i, country in enumerate(countries):
        country_data = df[df['Country Name'] == country].copy()
        if len(country_data) > 0:
            country_data = country_data.sort_values('Year')
            years = country_data['Year'].values
            values = pd.to_numeric(country_data[gdp_col], errors='coerce')
            
            mask = ~values.isna()
            if mask.sum() > 5:
                # Index to first year = 100
                values_masked = values[mask].values
                base_value = values_masked[0]
                indexed_values_array = (values_masked / base_value) * 100
                
                ax2.plot(years[mask], indexed_values_array, marker='o', markersize=2,
                        linewidth=2, label=country, alpha=0.85, color=colors[i])
    
    ax2.set_title('GDP Growth Indexed (Base Year = 100)', fontsize=13, fontweight='bold')
    ax2.set_xlabel('Year', fontsize=11)
    ax2.set_ylabel('GDP Index (Base Year = 100)', fontsize=11)
    ax2.legend(loc='best', frameon=True, fontsize=9)
    ax2.grid(True, alpha=0.3)
    ax2.set_yscale('log')
    
    plt.tight_layout()
    plt.savefig('../visualizations/01_gdp_trends.png', dpi=300, bbox_inches='tight')
    print("\n[OK] Saved visualization 1: GDP Growth")
    plt.close()

if __name__ == "__main__":
    print("Regenerating visualization 1 with GDP data...")
    print()
    viz1_gdp_growth()
    print("\n[SUCCESS] Visualization 1 fixed!")

