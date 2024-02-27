import dlt
from dlt.sources.helpers import requests

# URL of the API endpoint
url = "https://github.com/Samuel-Njoroge/data-load-tool/blob/main/datasets/Maji_Ndogo_farm_survey_small.db"

# Make a request & Check
response = requests.get(url)
response.raise_for_status()

pipeline = dlt.pipeline(
    pipeline_name="api_sqlite_pipeline",
    destination="",
    dataset_name="",
)

# Response contains a list of "Maji Ndogo Farm " data.
