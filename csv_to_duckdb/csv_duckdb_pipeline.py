import dlt
import pandas as pd

car_data = "https://github.com/Samuel-Njoroge/data-load-tool/blob/main/datasets/car_prices.csv"

df = pd.read_csv(car_data, sep=None, header=None, engine='python')
data = df.to_dict(orient="records")

pipeline = dlt.pipeline(
    pipeline_name="csv_duckdb",
    destination="duckdb",
    dataset_name="cars_data",
)

load_info = pipeline.run(data, table_name="cars")
print(load_info)