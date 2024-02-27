import dlt
import pandas as pd

car_data = ""

df = pd.read_csv(car_data)
data = df.to_dict(orient="records")

pipeline = dlt.pipeline(
    pipeline_name="csv_to_duckdb",
    destination="duckdb",
    dataset_name="mydata",
)

load_info = pipeline.run(data, table_name="cars")