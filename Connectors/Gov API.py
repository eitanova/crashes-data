import requests
import pandas as pd
from DataRetriever import DataRetriever as dr
import seaborn as sns
import matplotlib.pyplot as plt


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


# Return's all data that extract from Gov as DataFrame
def get_gov_data():
    # Gov variables for API requests
    gov_url = "https://data.gov.il/api/3/action/datastore_search?resource_id="

    # Gov variables for extract from .zip files
    gov_csv_files = {
        "2016.zip": "H20161332Accdatamekuzar.csv",
        "2017.zip": "H20171332AccdataMEKUZAR.csv",
        "2020.zip": "H20201331Data.csv"
    }
    gov_zip_file_prefix = "קבצים להורדה - תאונות מקוצר "
    gov_zip_path = "https://www.cbs.gov.il/he/publications/DocLib1/2015/PUF/%D7%AA%D7%97%D7%91%D7%95%D7%A8%D7%94/%D7" \
                   "%A7%D7%91%D7%A6%D7%99%D7%9D%20%D7%9C%D7%94%D7%95%D7%A8%D7%93%D7%94%20-%20%D7%AA%D7%90%D7%95%D7%A0" \
                   "%D7%95%D7%AA%20%D7%9E%D7%A7%D7%95%D7%A6%D7%A8%20"

    # General Gov variables
    gov_resources = {
        'area': ['b17b1634-c001-4d37-96c6-a661b2ecd98c'],
        'year': ['ecf37201-e71a-4af5-99a5-062fdf07a38d', 'f372a398-e2c1-408c-8333-e758cf2124c5'],
        'zip': ['2016.zip', '2017.zip', '2020.zip']
    }
    gov_resources_params = {
        'year': ['MEZEG_AVIR', 'SEMEL_YISHUV', "SHNAT_TEUNA", "HODESH_TEUNA", "SUG_YOM", "YOM_LAYLA",
                 "YOM_BASHAVUA", "HUMRAT_TEUNA", "SUG_TEUNA", "KVISH1"],
        'area': ['CITYCODE', 'YEARMONTH'],
        'zip': ['MEZEG_AVIR', 'SEMEL_YISHUV', "SHNAT_TEUNA", "HODESH_TEUNA", "SUG_YOM", "YOM_LAYLA",
                "YOM_BASHAVUA", "HUMRAT_TEUNA", "SUG_TEUNA", "KVISH1"]

    }
    gov_new_params_name = {
        'MEZEG_AVIR': 'weather',
        'SEMEL_YISHUV': 'city',
        'SHNAT_TEUNA': "year",
        'HODESH_TEUNA': 'month',
        'SUG_YOM': 'day_type',
        'YOM_LAYLA': 'day_time',
        'YOM_BASHAVUA': 'day',
        'HUMRAT_TEUNA': 'accident_severity',
        'SUG_TEUNA': 'accident_type',
        'CITYCODE': 'city',
        'KVISH1': 'road',
        'YEARMONTH': 'year'
    }
    gov_data = dr(url=gov_url)
    # END OF GOV VARIABLES #

    # Request all data from Gov API & store in 'gov_data' DF
    for key in gov_resources.keys():

        print(key)

        if key == 'area':
            for gov_resource in gov_resources[key]:
                temp = dr(url=gov_url)
                temp.retrieve_records(gov_resource, gov_resources_params[key])
                temp.rename_data(new_params=gov_new_params_name)

                # todo: think how to change the two following code lines
                temp.set_col_data(col_name='month', col=temp.get_col_data('year').str[4:])
                temp.set_col_data(col_name='year', col=temp.get_col_data('year').str[:4])

                gov_data.merge_data(df_data=temp.get_data())
                del temp

        elif key == 'year':
            for gov_resource in gov_resources[key]:
                gov_data.retrieve_records(gov_resource, gov_resources_params[key])

        elif key == 'zip':
            for gov_zip in gov_resources[key]:
                gov_data.extract_data_zip(zip_path=f"{gov_zip_path}{gov_zip}",
                                          zip_name=f"{gov_zip_file_prefix}{gov_zip}",
                                          csv_file=gov_csv_files[gov_zip],
                                          selected_params=gov_resources_params[key])

    gov_data.rename_data(new_params=gov_new_params_name)
    # gov_data.replace_data(new_data=(convert_to_city_name('city', gov_data.get_data())))
    return gov_data.get_data()


# Visualization functions
def show_top_values(df, amount, plot_type=None):

    top_values = df.value_counts().head(amount).sort_values(ascending=False)

    plt.figure(figsize=(10, 6))
    plt.xlabel(top_values.name)
    plt.ylabel('Count')
    plt.title(f'Top {amount} Values in {top_values.name} column')

    if plot_type == 'line':
        sns.lineplot(x=top_values.index, y=top_values.values)
    else:
        sns.barplot(x=top_values.index, y=top_values.values, order=top_values.index)

    plt.show()


if __name__ == '__main__':
    # gov_df = get_gov_data()
    gov_df = pd.read_csv("C:\\Users\\2eita\\Desktop\\b.csv")

    # Visualization
    '''
        todo: add visualizations
            1. sns.kdeplot
            2. sns.relplot()
            3. sns.regplot() # to Maor
    '''