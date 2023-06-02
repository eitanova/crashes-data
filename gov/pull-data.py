import requests
import pandas as pd


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
    url = "https://data.gov.il/api/3/action/datastore_search?" \
          "resource_id=5c78e9fa-c2e2-4771-93ff-7f400a12f7ba" \
          "&limit=99999"
    response = requests.get(url)

    if response.status_code == 200:
        # Create dict with requested values (City code, city name)
        records = response.json()['result']['records']
        gov_cities_dict = {rec['סמל_ישוב'].strip(): rec['שם_ישוב_לועזי'] for rec in records}

        df[row_name] = df[row_name].map(gov_cities_dict)

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

    gov_new_params_name = {
       'MEZEG_AVIR': 'wheater',
        'SEMEL_YISHUV': 'city',
        'SHNAT_TEUNA': "year",
        'HODESH_TEUNA': 'month',
        'SUG_YOM': 'day_type',
        'YOM_LAYLA': 'day_time',
        'YOM_BASHAVUA': 'day',
        'HUMRAT_TEUNA': 'accident_severity',
        'SUG_TEUNA': 'accident_type',
        'MEHIRUT_MUTERET': 'speed'
    }
    merged_df = pd.DataFrame()

    for gov_resource in gov_resources['year']:
        df = retrieve_records(gov_url, gov_resource, gov_resources_params['year'])
        merged_df = pd.concat([merged_df, df], ignore_index=True)

    merged_df = convert_to_city_name('SEMEL_YISHUV', merged_df)
    merged_df = merged_df.rename(columns=gov_new_params_name)
    print(merged_df.columns)


if __name__ == '__main__':
    main()
