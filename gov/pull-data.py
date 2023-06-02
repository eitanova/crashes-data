import requests
import pandas as pd
import os

# Create API request and returns answer as DataFrame with the selected parameters
def retrieve_records(url, resource, selected_params):

    uri = f"{url}{resource}&limit=20000"
    response = requests.get(uri)

    if response.status_code == 200:
        data = response.json()['result']['records']
        selected_data = [{param: item[param] for param in selected_params} for item in data]
        return pd.DataFrame(selected_data)

    return None

# Replace all cities numbers to cities names
def convert_to_city_name(row_name, df):

    url = "https://data.gov.il/api/3/action/datastore_search?resource_id=5c78e9fa-c2e2-4771-93ff-7f400a12f7ba&limit" \
          "=99999"
    response = requests.get(url)

    if response.status_code == 200:
        govCities = pd.DataFrame(response.json()['result']['records'])

    else:
        return df




def main():
    gov_url = "https://data.gov.il/api/3/action/datastore_search?resource_id="
    gov_resources = {
        'area': '57c5aef9-70f9-4b71-82fa-52304cfbd031',
        'year': ['ecf37201-e71a-4af5-99a5-062fdf07a38d', 'f372a398-e2c1-408c-8333-e758cf2124c5']
    }
    gov_resources_params = {
        'year': ['MEZEG_AVIR', 'SEMEL_YISHUV', "SHNAT_TEUNA", "HODESH_TEUNA", "SUG_YOM", "YOM_LAYLA",
                 "YOM_BASHAVUA", "HUMRAT_TEUNA", "SUG_TEUNA", "MEHIRUT_MUTERET"]
    }

    merged_df = pd.DataFrame()
    for gov_resource in gov_resources['year']:
        df = retrieve_records(gov_url, gov_resource, gov_resources_params['year'])
        print(df.shape)
        merged_df = pd.concat([merged_df, df], ignore_index=True)

    print(merged_df.shape)


if __name__ == '__main__':
    main()
