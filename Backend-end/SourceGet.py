import json
from sourceAPI import *


def initialisation(url):
    try:
        with open('data.json', 'r') as f:
            dic = json.loads(f)
    except TypeError:
        dic = get_data_from_API_with_head(url)
        print()
    with open('data.json', 'w') as f:
        json.dump(dic,f)

url = 'https://opendata.paris.fr/api/records/1.0/search/?dataset=que-faire-a-paris-&rows=10000&facet=category&facet=tags&facet=address_zipcode&facet=address_city&facet=pmr&facet=blind&facet=deaf&facet=access_type&facet=price_type'
initialisation(url)


