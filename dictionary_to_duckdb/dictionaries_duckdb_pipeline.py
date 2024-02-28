import dlt
import pandas as pd

# Create the dictionary with African countries
african_countries = {
    "name": ["Kenya", "Uganda", "Tanzania", "Rwanda", "Burundi", "Nigeria", "Egypt", "South Africa", "Ethiopia", "Morocco"],
    "capital_city": ["Nairobi", "Kampala", "Dodoma", "Kigali", "Gitega", "Abuja", "Cairo", "Pretoria", "Addis Ababa", "Rabat"],
    "population": [56000000, 48000000, 65000000, 13000000, 12000000, 220000000, 108000000, 60000000, 120000000, 38000000],
    "gross_domestic_product": [120000000000, 40000000000, 75000000000, 11000000000, 40000000000, 500000000000, 450000000000, 430000000000, 130000000000, 140000000000],
    "year_of_independence": [1963, 1962, 1961, 1962, 1962, 1960, 1922, 1910, 1941, 1956]
}

# Convert the dictionary to a pandas DataFrame
df = pd.DataFrame(african_countries)

# Create a dlt pipeline specifying destination and dataset name
pipeline = dlt.pipeline(
    pipeline_name="african_countries",
    destination="duckdb",
    dataset_name="countries_data"
)

# Load the data into DuckDB table named "countries"
load_info = pipeline.run(df.to_dict(orient="records"), table_name="african_countries_data")

# Print the load information
print(load_info)
