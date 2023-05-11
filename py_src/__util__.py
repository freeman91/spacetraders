import os
from datetime import datetime
from dotenv import load_dotenv
import requests

load_dotenv()


TOKEN = os.getenv("TOKEN")
API_URL = "https://api.spacetraders.io/v2/"


def log_message(message: str):
    print("[" + datetime.now().isoformat()[:19] + "] :: " + message)


def get_system(location: str):
    first_split = location.split("-", 1)
    second_split = first_split[1].split("-", 1)
    return first_split[0] + "-" + second_split[0]


def get_request(path):
    try:
        response = requests.get(
            API_URL + path, headers={"Authorization": f"Bearer {TOKEN}"}, timeout=30
        )

        if response.status_code == 204:
            return {}

        return response.json().get("data")

    except Exception as err:
        log_message(f"ERROR :: {err}")
        return {}


def post_request(path, body=None):
    if not body:
        body = {}

    try:
        response = requests.post(
            API_URL + path,
            body,
            headers={"Authorization": f"Bearer {TOKEN}"},
            timeout=30,
        )

        return response.json().get("data")

    except Exception as err:
        log_message(f"ERROR :: {err}")
        return {}
