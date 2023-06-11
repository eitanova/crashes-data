import requests
import pandas as pd

class DataRetriever:

    # Constructor
    def __init__(self, url):
        self.url = url