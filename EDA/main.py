import pandas as pd
import seaborn as sns
import requests
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
        gov_cities_dict = {int(rec['סמל_ישוב'].strip()): rec['שם_ישוב_לועזי'] for rec in records}

        # Custom from knowledge
        gov_cities_dict.update({0: 'INTER CITY'})

        df[row_name] = df[row_name].map(gov_cities_dict)

    return df


# Display top value for given column in DF
def display_top_values(col, amount, drop_values=None):

    if drop_values:
        col = col[col != drop_values]

    top_values = col.value_counts().head(amount).sort_values(ascending=False)

    plt.figure(figsize=(10, 6))
    plt.xlabel(top_values.name)
    plt.ylabel('Count')
    plt.title(f'Top {amount} Values in {top_values.name} column')

    sns.barplot(x=top_values.index, y=top_values.values, order=top_values.index)
    plt.show()


def display_cut_line(col):
    col = col.value_counts()
    plt.figure(figsize=(10, 6))
    plt.xlabel(col.name)
    plt.ylabel('Count')
    sns.lineplot(x=col.index, y=col.values)
    plt.show()


def display_heatmap(df):
    # Create a pivot table to aggregate the data
    heatmap_table = df.pivot_table(index=df.columns[0], columns=df.columns[1], aggfunc=len, fill_value=0)

    sns.heatmap(heatmap_table, annot=True, cmap='YlGnBu', fmt='d', linewidth=.5)
    plt.title(f'{df.columns[0]} by {df.columns[1]}')
    plt.ylabel(df.columns[1])
    plt.xlabel(df.columns[0])
    plt.show()


if __name__ == '__main__':
    gov_df = pd.read_csv("C:\\Users\\2eita\\Desktop\\b.csv")
    gov_df = convert_to_city_name('city', gov_df)

    '''
    # PREREQUISITES - change city number to name
    gov_df = convert_to_city_name('city', gov_df)

    # Display top values of following columns
    display_top_values(gov_df['city'], 10, 'INTER CITY')
    display_top_values(gov_df['day_time'], 2)

    # Display accidents mapping by months
    display_cut_line(gov_df['month'])   
    display_cut_line(gov_df['weather'])

    # Display heatmap
    display_heatmap(gov_df[['month', 'accident_severity']])
    '''