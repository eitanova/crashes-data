# Data Science Project - car accidents

## Motivation
We used this platform to analyse data related to accident and to come with 
the follow conclusions:
>    1. Which city / area is the most dangerous place to drive
>    2. On which age you must likely to be involved in accident


# API's

## Gov api - accident data
> Main API: https://data.gov.il/

The given API data is from government database that is open for the public.
Under database section (מאגרי מידע) you can choose which data you want to use.
In the searchbar you can search the requested subject you wish to explore / pull data.
I used this database to get data regarding accident in israel by year's.

After pulling data using this public API and making some data manipulation's,
I store the data in DataFrame object.

### Parameters table
|  Parameter name   | Parameter value |                    Description                     |
|:-----------------:|:---------------:|:--------------------------------------------------:|
|      wheater      |     Integer     |           wheater when accident occured            |
|       city        |     string      |                     City name                      |
|       year        |     Integer     |                      The year                      |
|       month       |     Integer     |                     The month                      |
|     day_type      |     Integer     |   The type of day refered to holiday for example   | 
|     day_time      |     Integer     |   If the accident occured in day(1) or night(5)    |
|        day        |     Integer     |                The day of the week                 |
| accident_severity |     Integer     | Severity of the accident, from 1(worst) to 3(easy) |
|   accident_type   |     Integer     |             Which type of the accident             |
|       speed       |     Integer     |         Range of the speed in the accident         | 
