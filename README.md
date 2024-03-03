# Data Load Tool (dlt)
[dlt](https://dlthub.com/docs) - An open-source library added in Python scripts to load data from various and often messy data sources into well-structured, live datasets.

## Overview
![dlt](data_load_tool_overview.svg)

![dlt](dataloadtool.drawio(1).svg)
![dlt](dataloadtool.drawio(2).svg)
## Installation.
```sh
pip install dlt
```

## Run the pipeline.
```sh
python pipeline_file_name.py
```
This is the name of your python file.

## Inspect the created dataset using a Streamlit app.
```sh
dlt pipeline pipeline_name show
```
This is the name of your pipeline defined in your python file. 

Example : The pipeline `african_countries` loads data from a defined `source` to `DuckDB`.
```sh
# Create a pipeline.
pipeline = dlt.pipeline(
    pipeline_name="african_countries",
    destination="duckdb",
    dataset_name="countries" # Database schema "countries".
)
```
