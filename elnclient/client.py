import os, requests
from dotenv import load_dotenv

class ElnClient:
    def __init__(self, api_key: str):
        self.api_key = api_key