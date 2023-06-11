import requests
import pandas as pd
import DataRetriever as dr


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
    # Gov variables
    gov_url = "https://data.gov.il/api/3/action/datastore_search?resource_id="
    gov_resources = {
        'area': ['b17b1634-c001-4d37-96c6-a661b2ecd98c'],
        'year': ['ecf37201-e71a-4af5-99a5-062fdf07a38d', 'f372a398-e2c1-408c-8333-e758cf2124c5']
    }
    gov_resources_params = {
        'year': ['MEZEG_AVIR', 'SEMEL_YISHUV', "SHNAT_TEUNA", "HODESH_TEUNA", "SUG_YOM", "YOM_LAYLA",
                 "YOM_BASHAVUA", "HUMRAT_TEUNA", "SUG_TEUNA"],
        'area': ['CITYCODE', 'YEARMONTH']
    }
    gov_new_params_name = {
        'year':
            {
                'MEZEG_AVIR': 'weather',
                'SEMEL_YISHUV': 'city',
                'SHNAT_TEUNA': "year",
                'HODESH_TEUNA': 'month',
                'SUG_YOM': 'day_type',
                'YOM_LAYLA': 'day_time',
                'YOM_BASHAVUA': 'day',
                'HUMRAT_TEUNA': 'accident_severity',
                'SUG_TEUNA': 'accident_type'
            },
        'area':
            {
                'CITYCODE': 'city',
                'YEARMONTH': 'year'
            }
    }

    gov_data = pd.DataFrame()

    # Request all data from Gov API & store in 'gov_data' DF
    for key in gov_resources.keys():
        for gov_resource in gov_resources[key]:
            df = retrieve_records(gov_url, gov_resource, gov_resources_params[key])
            df = df.rename(columns=gov_new_params_name[key])

            print(df.shape)
            # Data manipulation & adjustment for all requests from 'area'
            if key == 'area':
                df['month'] = df['year'].str[4:]
                df['year'] = df['month'].str[:4]

            gov_data = pd.concat([gov_data, df], ignore_index=True)

    gov_data = convert_to_city_name('city', gov_data)
    print(gov_data.shape)


if __name__ == '__main__':
    main()
