from os import getenv

import mlflow
from mlflow import MlflowClient

mlflow.set_tracking_uri(getenv("MLFLOW_TRACKING_URI", "http://localhost:5000"))

client = MlflowClient()
