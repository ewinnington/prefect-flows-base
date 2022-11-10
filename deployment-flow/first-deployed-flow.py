import sys
import prefect
from prefect import flow, task, get_run_logger
import requests

@task
def log_task(name):
    logger = get_run_logger()
    logger.info("Hello %s!", name)
    logger.info("Prefect Version = %s 🚀", prefect.__version__)
    api_result = call_api("http://time.jsontest.com/")
    logger.info("Time is %s", api_result)

def call_api(url):
    return requests.get(url).json()

@flow()
def log_flow(name: str):
    log_task(name)


if __name__ == "__main__":
    name = sys.argv[1]
    log_flow(name)