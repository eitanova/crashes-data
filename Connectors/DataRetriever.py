import requests
import pandas as pd


class DataRetriever:
    # Constructor
    def __init__(self, url):
        self.url = url
        self.df_data = pd.DataFrame()

    def retrieve_records(self, resource, selected_params=None, filters="limit=99999"):
        uri = f"{self.url}{resource}&{filters}"
        response = requests.get(uri)

        if response.status_code == 200:
            data = response.json()['result']['records']

            if selected_params:
                data = [{param: item[param] for param in selected_params} for item in data]

            self.df_data = pd.concat([self.df_data, pd.DataFrame(data)], ignore_index=True)
            return 200

        return 500
