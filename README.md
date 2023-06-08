# Data Science Project - car accidents

### Motivation
In the realm of Data Science, a comprehensive project focused on car accidents unfolds, leveraging the power of data analysis and predictive modeling.
This endeavor aims to delve into the intricate patterns and underlying factors contributing to vehicular accidents. This Data Science project seeks to extract valuable insightsand pave the way for effective accident prevention strategies.
Through a meticulous exploration of extensive accident data, this undertaking aims to provide a deeper understanding of the complex dynamics at play, ultimately fostering safer roadways and improving the well-being of individuals and communities.


## Gov API
> Main API: https://data.gov.il/

The provided API data originates from a government database that is publicly accessible. Within the database section (מאגרי מידע), you have the option to select the specific data you intend to utilize. By utilizing the search bar, you can explore and retrieve data pertaining to your desired subject.

In this particular scenario, I utilized this database to obtain information related to accidents in Israel, categorized by year. Following the retrieval of data through the public API and performing necessary data manipulations, I stored the acquired data in a DataFrame object.

### Parameters table
|  Parameter name   | Parameter value |                    Description                     |
|:-----------------:|:---------------:|:--------------------------------------------------:|
|      weather      |     Integer     |           weather when accident occurred           |
|       city        |     string      |                     City name                      |
|       year        |     Integer     |                      The year                      |
|       month       |     Integer     |                     The month                      |
|     day_type      |     Integer     |  The type of day referred to holiday for example   | 
|     day_time      |     Integer     |   If the accident occurred in day(1) or night(5)   |
|        day        |     Integer     |                The day of the week                 |
| accident_severity |     Integer     | Severity of the accident, from 1(worst) to 3(easy) |
|   accident_type   |     Integer     |             Which type of the accident             |


#### weather values & meaning table
| value |  meaning  |
|:-----:|:---------:|
|   1   |   Sunny   | 
|   2   |   Rainy   |
|   3   | Extra hot |
|   4   |   Foggy   |
|   5   |   Other   | 
|   9   |  Unknown  |

#### day_type values & meaning table
| value |    meaning    |
|:-----:|:-------------:|
|   1   |    Holiday    |
|   2   | Holiday night |
|   3   | Jewish retual |
|   4   |     Other     |

#### accident_type values & meaning table
| value |          meaning           |
|:-----:|:--------------------------:|
|   1   |      Hit with walker       |
|   8   |      Hit with object       |
|   9   |  Went down from the road   |
|  10   |          Rollover          |
|  11   |            Slip            |
|  14   |            Burn            |
|  19   |      Hit with animal       |
|  20   | Injury from a vehicle load |
| Other |   Accident with vehicle    |

