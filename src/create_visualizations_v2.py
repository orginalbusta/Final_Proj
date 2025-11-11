"""
Create static visualizations for the project proposal
(Updated version to handle actual World Bank data format)
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

def viz1_global_gdp_trends():
    """Visualization 1: Global GDP Growth Trends (1960-2020)"""
    df = pd.read_csv('../data/economy-and-growth.csv')
    
    plt.figure(figsize=(12, 6))
    
    # Get GDP related column (find the first column with 'GDP' in it)
    gdp_cols = [col for col in df.columns if 'GDP' in col or 'income' in col.lower()]
    if not gdp_cols:
        print("[WARNING] No GDP column found, using first numeric column")
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            gdp_col = numeric_cols[0]
        else:
            print("[ERROR] No numeric columns found in economy data")
            return
    else:
        gdp_col = gdp_cols[0]
    
    print(f"Using column: {gdp_col}")
    
    # Select major economies
    countries = ['United States', 'China', 'Germany', 'Japan', 'India', 'Brazil']
    
    for country in countries:
        country_data = df[df['Country Name'] == country].copy()
        if len(country_data) > 0:
            # Sort by year
            country_data = country_data.sort_values('Year')
            years = country_data['Year'].values
            values = pd.to_numeric(country_data[gdp_col], errors='coerce')
            
            # Plot non-null values
            mask = ~values.isna()
            if mask.sum() > 0:
                plt.plot(years[mask], values[mask], marker='o', markersize=2, 
                        linewidth=1.5, label=country, alpha=0.8)
    
    plt.title('Economic Growth Trends: Major Economies (1960-2020)', fontsize=14, fontweight='bold')
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Economic Indicator Value', fontsize=12)
    plt.legend(loc='best', frameon=True)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('../visualizations/01_gdp_trends.png', dpi=300, bbox_inches='tight')
    print("[OK] Saved visualization 1: GDP Trends")
    plt.close()

def viz2_life_expectancy_comparison():
    """Visualization 2: Life Expectancy Evolution by Region"""
    df = pd.read_csv('../data/health.csv')
    
    plt.figure(figsize=(14, 7))
    
    # Find life expectancy or age-related column
    health_cols = [col for col in df.columns if 'age' in col.lower() or 'life' in col.lower() or 'population ages' in col.lower()]
    if not health_cols:
        print("[WARNING] No health indicator found")
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            health_col = numeric_cols[0]
        else:
            print("[ERROR] No numeric columns found")
            return
    else:
        # Prefer working-age population as a proxy
        health_col = [col for col in health_cols if 'working-age' in col.lower() or '15-64' in col]
        if not health_col:
            health_col = health_cols[0]
        else:
            health_col = health_col[0]
    
    print(f"Using column: {health_col}")
    
    # Select countries from different regions
    regions_countries = {
        'North America': 'United States',
        'Europe': 'Germany',
        'East Asia': 'Japan',
        'South Asia': 'India',
        'Africa': 'Nigeria',
        'Latin America': 'Brazil'
    }
    
    for region, country in regions_countries.items():
        country_data = df[df['Country Name'] == country].copy()
        if len(country_data) > 0:
            country_data = country_data.sort_values('Year')
            years = country_data['Year'].values
            values = pd.to_numeric(country_data[health_col], errors='coerce')
            
            mask = ~values.isna()
            if mask.sum() > 0:
                plt.plot(years[mask], values[mask], marker='o', markersize=2,
                        linewidth=2, label=region, alpha=0.8)
    
    plt.title('Health Indicator Evolution by Region (1960-2020)', fontsize=14, fontweight='bold')
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Health Indicator Value', fontsize=12)
    plt.legend(loc='best', frameon=True)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('../visualizations/02_life_expectancy.png', dpi=300, bbox_inches='tight')
    print("[OK] Saved visualization 2: Health Indicators")
    plt.close()

def viz3_education_progress():
    """Visualization 3: Education Progress"""
    df = pd.read_csv('../data/education.csv')
    
    plt.figure(figsize=(12, 6))
    
    # Get education-related column
    edu_cols = [col for col in df.columns if 'enrollment' in col.lower() or 'school' in col.lower() or 'education' in col.lower()]
    if not edu_cols:
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            edu_col = numeric_cols[0]
        else:
            print("[ERROR] No numeric columns found")
            return
    else:
        edu_col = edu_cols[0]
    
    print(f"Using column: {edu_col}")
    
    countries = ['China', 'India', 'Brazil', 'South Africa', 'Egypt, Arab Rep.', 'Indonesia']
    
    for country in countries:
        country_data = df[df['Country Name'] == country].copy()
        if len(country_data) > 0:
            country_data = country_data.sort_values('Year')
            years = country_data['Year'].values
            values = pd.to_numeric(country_data[edu_col], errors='coerce')
            
            mask = ~values.isna()
            if mask.sum() > 0:
                plt.plot(years[mask], values[mask], marker='o', markersize=2,
                        linewidth=2, label=country, alpha=0.8)
    
    plt.title('Education Indicator Trends in Developing Nations (1960-2020)', fontsize=14, fontweight='bold')
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Education Indicator Value', fontsize=12)
    plt.legend(loc='best', frameon=True)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('../visualizations/03_education_progress.png', dpi=300, bbox_inches='tight')
    print("[OK] Saved visualization 3: Education Progress")
    plt.close()

def viz4_poverty_decline():
    """Visualization 4: Poverty Indicator Trends"""
    df = pd.read_csv('../data/poverty.csv')
    
    plt.figure(figsize=(12, 6))
    
    # Get poverty-related column
    poverty_cols = [col for col in df.columns if 'poverty' in col.lower() or 'income' in col.lower() or 'gini' in col.lower()]
    if not poverty_cols:
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            poverty_col = numeric_cols[0]
        else:
            print("[ERROR] No numeric columns found")
            return
    else:
        poverty_col = poverty_cols[0]
    
    print(f"Using column: {poverty_col}")
    
    countries = ['China', 'India', 'Vietnam', 'Bangladesh', 'Indonesia', 'Brazil']
    
    for country in countries:
        country_data = df[df['Country Name'] == country].copy()
        if len(country_data) > 0:
            country_data = country_data.sort_values('Year')
            years = country_data['Year'].values
            values = pd.to_numeric(country_data[poverty_col], errors='coerce')
            
            mask = ~values.isna()
            if mask.sum() > 0:
                plt.plot(years[mask], values[mask], marker='o', markersize=2,
                        linewidth=2, label=country, alpha=0.8)
    
    plt.title('Poverty Indicator Trends (1960-2020)', fontsize=14, fontweight='bold')
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Poverty Indicator Value', fontsize=12)
    plt.legend(loc='best', frameon=True)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('../visualizations/04_poverty_decline.png', dpi=300, bbox_inches='tight')
    print("[OK] Saved visualization 4: Poverty Indicators")
    plt.close()

def viz5_climate_emissions():
    """Visualization 5: Climate/Environmental Indicators"""
    df = pd.read_csv('../data/climate-change.csv')
    
    plt.figure(figsize=(12, 6))
    
    # Get climate-related column
    climate_cols = [col for col in df.columns if 'co2' in col.lower() or 'emission' in col.lower() or 'climate' in col.lower()]
    if not climate_cols:
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            climate_col = numeric_cols[0]
        else:
            print("[ERROR] No numeric columns found")
            return
    else:
        climate_col = climate_cols[0]
    
    print(f"Using column: {climate_col}")
    
    countries = ['United States', 'China', 'Germany', 'India', 'Brazil', 'Saudi Arabia']
    
    for country in countries:
        country_data = df[df['Country Name'] == country].copy()
        if len(country_data) > 0:
            country_data = country_data.sort_values('Year')
            years = country_data['Year'].values
            values = pd.to_numeric(country_data[climate_col], errors='coerce')
            
            mask = ~values.isna()
            if mask.sum() > 0:
                plt.plot(years[mask], values[mask], marker='o', markersize=2,
                        linewidth=2, label=country, alpha=0.8)
    
    plt.title('Climate & Environmental Indicators (1960-2020)', fontsize=14, fontweight='bold')
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Climate Indicator Value', fontsize=12)
    plt.legend(loc='best', frameon=True)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('../visualizations/05_climate_emissions.png', dpi=300, bbox_inches='tight')
    print("[OK] Saved visualization 5: Climate Indicators")
    plt.close()

def viz6_infrastructure_development():
    """Visualization 6: Infrastructure Development Indicators"""
    df = pd.read_csv('../data/infrastructure.csv')
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    # Get infrastructure-related column
    infra_cols = [col for col in df.columns if 'internet' in col.lower() or 'mobile' in col.lower() or 'broadband' in col.lower() or 'cellular' in col.lower()]
    if not infra_cols:
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            infra_col = numeric_cols[0]
        else:
            print("[ERROR] No numeric columns found")
            return
    else:
        infra_col = infra_cols[0]
    
    print(f"Using column: {infra_col}")
    
    countries = ['United States', 'South Korea', 'Brazil', 'India', 'Nigeria']
    
    # Left plot - trend over time
    for country in countries:
        country_data = df[df['Country Name'] == country].copy()
        if len(country_data) > 0:
            country_data = country_data.sort_values('Year')
            # Focus on years 2000+
            country_data = country_data[country_data['Year'] >= 2000]
            years = country_data['Year'].values
            values = pd.to_numeric(country_data[infra_col], errors='coerce')
            
            mask = ~values.isna()
            if mask.sum() > 0:
                ax1.plot(years[mask], values[mask], marker='o', markersize=3,
                        linewidth=2, label=country, alpha=0.8)
    
    ax1.set_title('Digital Infrastructure Growth (2000-2020)', fontsize=12, fontweight='bold')
    ax1.set_xlabel('Year', fontsize=11)
    ax1.set_ylabel('Infrastructure Indicator Value', fontsize=11)
    ax1.legend(loc='best', frameon=True)
    ax1.grid(True, alpha=0.3)
    
    # Right plot - latest year comparison
    latest_values = []
    country_names = []
    
    for country in countries:
        country_data = df[df['Country Name'] == country].copy()
        if len(country_data) > 0:
            # Get most recent non-null value
            country_data = country_data.sort_values('Year', ascending=False)
            for _, row in country_data.iterrows():
                val = pd.to_numeric(row[infra_col], errors='coerce')
                if pd.notna(val):
                    latest_values.append(val)
                    country_names.append(country)
                    break
    
    if country_names:
        colors = sns.color_palette("husl", len(country_names))
        ax2.barh(country_names, latest_values, color=colors, alpha=0.8)
        ax2.set_title('Digital Access Comparison (Latest Year)', fontsize=12, fontweight='bold')
        ax2.set_xlabel('Indicator Value', fontsize=11)
        ax2.grid(True, alpha=0.3, axis='x')
    
    plt.tight_layout()
    plt.savefig('../visualizations/06_infrastructure_development.png', dpi=300, bbox_inches='tight')
    print("[OK] Saved visualization 6: Infrastructure Development")
    plt.close()

def main():
    """Generate all visualizations"""
    print("Loading datasets and generating visualizations...")
    print()
    
    try:
        print("1. Creating GDP/Economic Trends visualization...")
        viz1_global_gdp_trends()
        print()
        
        print("2. Creating Health Indicators visualization...")
        viz2_life_expectancy_comparison()
        print()
        
        print("3. Creating Education Progress visualization...")
        viz3_education_progress()
        print()
        
        print("4. Creating Poverty Indicators visualization...")
        viz4_poverty_decline()
        print()
        
        print("5. Creating Climate Indicators visualization...")
        viz5_climate_emissions()
        print()
        
        print("6. Creating Infrastructure Development visualization...")
        viz6_infrastructure_development()
        print()
        
        print("[SUCCESS] All visualizations created successfully!")
        print("Check the 'visualizations' folder for outputs.")
        
    except FileNotFoundError as e:
        print(f"[ERROR] Could not find data file. Please run download_data.py first.")
        print(f"Details: {e}")
    except Exception as e:
        print(f"[ERROR] Error creating visualizations: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()

