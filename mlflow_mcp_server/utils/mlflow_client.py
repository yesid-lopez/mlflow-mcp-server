import mlflow
from mlflow import MlflowClient
from os import getenv

mlflow.set_tracking_uri(getenv("MLFLOW_TRACKING_URI"))

client = MlflowClient()
