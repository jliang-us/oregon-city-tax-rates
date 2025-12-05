# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "marimo>=0.17.0",
#     "numpy==2.3.5",
#     "pandas==2.3.3",
#     "pyzmq",
# ]
# ///

import marimo

__generated_with = "0.18.3"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import numpy as np
    return mo, pd


@app.cell
def _(mo):
    mo.md("""
    # Property Tax Data Analysis with City Population Data

    This notebook explores the FY 2024-25 Property Tax Statistics and identifies data sources for merging city population data.
    """)
    return


@app.cell
def _(pd):
    import os as _os

    # Load the Excel file using relative path
    _base_dir = _os.path.dirname(_os.path.abspath(__file__))
    file_path = _os.path.join(_base_dir, "FY 2024-25 Property Tax Statistics Supplement.xlsx")

    # Read with proper header row
    df_raw = pd.read_excel(file_path, sheet_name='City Code Areas FY 2024-25', header=1)

    # Display basic info
    print(f"Shape: {df_raw.shape}")
    print(f"\nColumns: {df_raw.columns.tolist()}")
    df_raw.head(10)
    return (df_raw,)


@app.cell
def _(df_raw, pd):
    # Clean up the data
    df_clean = df_raw.copy()

    # Rename columns for easier access
    df_clean.columns = [
        'City',
        'County',
        'Code_Area',
        'M5V',
        'Assessed_Value',
        'Tax_Rate_County',
        'Tax_Rate_City',
        'Tax_Rate_School',
        'Tax_Rate_Districts_Other',
        'Tax_Rate_Total'
    ]

    # Convert numeric columns
    numeric_cols = ['M5V', 'Assessed_Value', 'Tax_Rate_County', 'Tax_Rate_City',
                    'Tax_Rate_School', 'Tax_Rate_Districts_Other', 'Tax_Rate_Total']

    for col in numeric_cols:
        df_clean[col] = pd.to_numeric(df_clean[col], errors='coerce')

    # Remove rows with all NaN values
    df_clean = df_clean.dropna(how='all')

    # Extract unique cities
    unique_cities = df_clean['City'].str.replace(' City', '').unique()

    print(f"Total rows: {len(df_clean)}")
    print(f"Unique cities: {len(unique_cities)}")
    print(f"\nFirst few unique cities: {sorted(unique_cities)[:10]}")

    df_clean.head(10)
    return (df_clean,)


@app.cell
def _(mo):
    mo.md("""
    ## Available Population Data Sources for Oregon Cities (2024)

    Below are the main data sources we can use to obtain 2024 population estimates for Oregon cities:
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ### 1. **U.S. Census Bureau API** (Recommended Primary Source)

    **Pros:**
    - Official, authoritative data
    - Free API access with key
    - Multiple vintages and geographic levels
    - Programmatic access via Python libraries

    **Cons:**
    - 2024 estimates may not be released yet (typically lag by 1-2 years)
    - May need to use 2023 or 2022 estimates
    - Requires API key (free registration)

    **Python Libraries:**
    - `census` - Official Census API wrapper
    - `cenpy` - Alternative Census data access

    **Datasets:**
    - Population Estimates Program (PEP) - Annual city/town estimates
    - American Community Survey (ACS) - 5-year estimates

    **Example API endpoint:**
    ```
    https://api.census.gov/data/2023/pep/population
    ```
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ### 2. **Portland State University Population Research Center**

    **Pros:**
    - Oregon-specific population estimates
    - Certified by State of Oregon
    - More timely than federal estimates
    - Direct Excel/CSV downloads available

    **Cons:**
    - Manual download process
    - May require web scraping for automation
    - Less structured than Census API

    **Website:**
    - https://www.pdx.edu/population-research/population-estimates
    - Annual Certified Population Estimates for Oregon cities

    **Data Format:**
    - Excel spreadsheets
    - CSV files
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ### 3. **OpenDataSoft - US Cities Dataset**

    **Pros:**
    - Free, open API
    - No authentication required
    - JSON/CSV/GeoJSON formats
    - Easy to query

    **Cons:**
    - May not have 2024 data
    - Less official than Census
    - Population data might be outdated

    **API Example:**
    ```python
    import requests
    url = "https://public.opendatasoft.com/api/records/1.0/search/"
    params = {
        'dataset': 'us-cities-demographics',
        'q': 'state:Oregon',
        'rows': 1000
    }
    ```
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ### 4. **World Population Review**

    **Pros:**
    - Aggregates multiple sources
    - User-friendly format
    - Current year projections

    **Cons:**
    - No official API
    - Requires web scraping
    - Less reliable for official use

    **Website:**
    - https://worldpopulationreview.com/us-cities/states/or
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ### 5. **SimpleMaps - US Cities Database**

    **Pros:**
    - Comprehensive city database
    - Includes lat/long coordinates
    - Relatively up-to-date

    **Cons:**
    - Free version has limitations
    - Commercial license for full data
    - Not as authoritative as Census

    **Website:**
    - https://simplemaps.com/data/us-cities
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Recommended Approach

    ### Primary Strategy: PSU Population Research Center + Census Bureau

    1. **Use PSU PRC data** as primary source since it's:
       - Oregon-specific
       - State-certified
       - Most likely to have 2024 estimates

    2. **Use Census Bureau API** as backup for:
       - Validation
       - Historical comparisons
       - Any cities missing from PSU data

    ### Implementation Steps:

    1. Download PSU Population Research Center's latest certified estimates
    2. Clean and standardize city names (remove "City" suffix, handle variations)
    3. Match on city name (and county if needed for disambiguation)
    4. For unmatched cities, query Census API
    5. Handle edge cases (merged cities, name changes, etc.)

    ### Data Quality Considerations:

    - **Name matching challenges**: Cities may have different spellings or formats
    - **Multiple code areas per city**: Your tax data has multiple entries per city (by county or district)
    - **Population assignment**: Decide whether to use city-wide population for all code areas or proportion by assessed value
    """)
    return


@app.cell
def _(df_clean):
    # Analyze city distribution across counties
    city_county_dist = df_clean.groupby('City').agg({
        'County': 'nunique',
        'Code_Area': 'count',
        'Assessed_Value': 'sum'
    }).sort_values('County', ascending=False)

    city_county_dist.head(20)
    return


@app.cell
def _(mo):
    mo.md("""
    ## PSU Population Data Integration

    Loading the 2024 Certified Population Estimates from Portland State University Population Research Center.
    """)
    return


@app.cell
def _(pd):
    import os as _os2

    # Load PSU population file using relative path
    _base_dir2 = _os2.path.dirname(_os2.path.abspath(__file__))
    psu_file_path = _os2.path.join(_base_dir2, "PSU_2024_Certified_Population_Estimates.xlsx")

    # PSU data is in "Cities and Towns" sheet with header in row 2
    df_pop_raw = pd.read_excel(psu_file_path, sheet_name='Cities and Towns', header=1)

    print(f"Population data shape: {df_pop_raw.shape}")
    print(f"\nColumns: {df_pop_raw.columns.tolist()[:10]}")
    df_pop_raw.head(10)
    return (df_pop_raw,)


@app.cell
def _(df_pop_raw, pd):
    # PSU data has 5 sections in wide format - need to reshape to long format
    # Each section has a city name column followed by population columns

    # The 2024 population columns contain "Certified Estimate" and "2024"
    # Column names may have newlines, so we need to check both parts
    pop_2024_cols = [col for col in df_pop_raw.columns
                     if 'Certified Estimate' in str(col) and '2024' in str(col)]

    print(f"Found {len(pop_2024_cols)} population columns")

    # Extract all city-population pairs from the 5 sections
    all_cities = []

    for pop_col in pop_2024_cols:
        # Find the city name column (should be 1 column before the population column)
        city_col_idx = df_pop_raw.columns.get_loc(pop_col) - 1
        city_col = df_pop_raw.columns[city_col_idx]

        # Extract city and population data for this section
        section_data = df_pop_raw[[city_col, pop_col]].copy()
        section_data.columns = ['City_Name', 'Population_2024']

        # Remove empty rows
        section_data = section_data.dropna(subset=['City_Name'])

        all_cities.append(section_data)

    # Combine all sections
    df_pop_clean = pd.concat(all_cities, ignore_index=True)

    # Convert population to numeric
    df_pop_clean['Population_2024'] = pd.to_numeric(df_pop_clean['Population_2024'], errors='coerce')

    # Remove any remaining NaN rows
    df_pop_clean = df_pop_clean.dropna()

    print(f"Total cities found: {len(df_pop_clean)}")
    print(f"\nFirst 10 cities:")
    df_pop_clean.head(10)
    return (df_pop_clean,)


@app.cell
def _(df_clean, df_pop_clean):
    # Standardize city names for merging
    # Remove " City" suffix from tax data city names
    df_tax_for_merge = df_clean.copy()
    df_tax_for_merge['City_Clean'] = df_tax_for_merge['City'].str.replace(' City', '', regex=False).str.strip()

    # Create clean population dataframe - data is already cleaned from previous cell
    df_pop_for_merge = df_pop_clean.copy()
    df_pop_for_merge['City_Clean'] = df_pop_for_merge['City_Name'].str.strip()

    print(f"Tax data cities: {df_tax_for_merge['City_Clean'].nunique()}")
    print(f"Population data cities: {df_pop_for_merge['City_Clean'].nunique()}")

    df_pop_for_merge.head(10)
    return df_pop_for_merge, df_tax_for_merge


@app.cell
def _(df_pop_for_merge, df_tax_for_merge):
    # Merge tax data with population data
    df_merged = df_tax_for_merge.merge(
        df_pop_for_merge[['City_Clean', 'Population_2024']],
        on='City_Clean',
        how='left'
    )

    # Check match rate
    match_rate = (df_merged['Population_2024'].notna().sum() / len(df_merged)) * 100
    print(f"Match rate: {match_rate:.1f}%")
    print(f"Matched rows: {df_merged['Population_2024'].notna().sum()} / {len(df_merged)}")

    # Show cities without population data
    unmatched = df_merged[df_merged['Population_2024'].isna()]['City_Clean'].unique()
    print(f"\nUnmatched cities ({len(unmatched)}): {sorted(unmatched)[:10]}")

    df_merged.head(10)
    return (df_merged,)


@app.cell
def _(mo):
    mo.md("""
    ## Final Table: Cities with Tax Rates and Population

    This table shows each city with their property tax rates and 2024 population estimates.
    """)
    return


@app.cell
def _(df_merged):
    # Create final summary table
    # Group by city to get one row per city with average tax rates
    final_table = df_merged.groupby('City_Clean').agg({
        'County': 'first',
        'Tax_Rate_County': 'mean',
        'Tax_Rate_City': 'mean',
        'Tax_Rate_School': 'mean',
        'Tax_Rate_Districts_Other': 'mean',
        'Tax_Rate_Total': 'mean',
        'Population_2024': 'first',
        'Assessed_Value': 'sum'
    }).reset_index()

    # Rename columns for clarity
    final_table.columns = [
        'City',
        'County',
        'Avg_Tax_Rate_County',
        'Avg_Tax_Rate_City',
        'Avg_Tax_Rate_School',
        'Avg_Tax_Rate_Districts_Other',
        'Avg_Tax_Rate_Total',
        'Population_2024',
        'Total_Assessed_Value'
    ]

    # Sort by population (largest first)
    final_table = final_table.sort_values('Population_2024', ascending=False)

    # Round tax rates for readability
    tax_cols = ['Avg_Tax_Rate_County', 'Avg_Tax_Rate_City', 'Avg_Tax_Rate_School',
                'Avg_Tax_Rate_Districts_Other', 'Avg_Tax_Rate_Total']
    final_table[tax_cols] = final_table[tax_cols].round(4)

    print(f"Final table shape: {final_table.shape}")
    print(f"Cities with population data: {final_table['Population_2024'].notna().sum()}")

    final_table.head(20)
    return (final_table,)


@app.cell
def _(final_table):
    # Display summary statistics
    print("Summary Statistics:")
    print(f"Total cities: {len(final_table)}")
    print(f"Cities with population data: {final_table['Population_2024'].notna().sum()}")
    print(f"\nAverage tax rate (all cities): {final_table['Avg_Tax_Rate_Total'].mean():.4f}")
    print(f"Median tax rate (all cities): {final_table['Avg_Tax_Rate_Total'].median():.4f}")
    print(f"\nLargest city: {final_table.iloc[0]['City']} (pop: {final_table.iloc[0]['Population_2024']:,.0f})")
    print(f"Total population covered: {final_table['Population_2024'].sum():,.0f}")

    # Show the full table
    final_table
    return


if __name__ == "__main__":
    app.run()
