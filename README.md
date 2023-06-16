# Data Science Project - car accidents

### Motivation
In the realm of Data Science, a comprehensive project focused on car accidents unfolds, leveraging the power of data analysis and predictive modeling.
<<<<<<< HEAD

This endeavor aims to delve into the intricate patterns and underlying factors contributing to vehicular accidents.

This Data Science project seeks to extract valuable insightsand pave the way for effective accident prevention strategies. 
Through a meticulous exploration of extensive accident data, this undertaking aims to provide a deeper understanding of the complex dynamics at play, ultimately fostering safer roadways and improving the well-being of individuals and communities.

### Research questions
In this section, we aim to explore the significance and value of our project.
By addressing this question, we can subsequently progress towards elucidating the appropriate methods and strategies to effectively reduce car accidents.
Our objective is to leverage knowledge and insights gained from this research to implement proactive measures and promote safety on the roads.
 1. What are the primary causes of car accidents in a specific region?
 2. How do weather conditions contribute to car accidents?
 3. How does the time of day or day of the week influence the likelihood of car accidents?
 5. Are there more accidents that occur during holidays?
=======
This endeavor aims to delve into the intricate patterns and underlying factors contributing to vehicular accidents. This Data Science project seeks to extract valuable insightsand pave the way for effective accident prevention strategies.
Through a meticulous exploration of extensive accident data, this undertaking aims to provide a deeper understanding of the complex dynamics at play, ultimately fostering safer roadways and improving the well-being of individuals and communities.
>>>>>>> origin


### Data acquistion
All data is sourced from formal databases, which are based on real events.
> API Gov: https://https://data.gov.il/api/3/action/datastore_search?<query>
```python
 # Sample code
def get_data_from_gov():
    
    import requests
    
    uri = "https://data.gov.il/api/3/action/datastore_search" 
    query = "resource_id=5c78e9fa-c2e2-4771-93ff-7f400a12f7ba"  # query by resource_id
    query.append("&limit=99999") # set a records limit (by default: 1000)
    
    url = uri + query
    
    response = requests.get(url)

    if response.status_code == 200:
        records = response.json()['result']['records']
    
    return records
```
