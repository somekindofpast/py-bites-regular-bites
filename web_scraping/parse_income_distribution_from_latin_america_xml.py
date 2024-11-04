import os
from collections import defaultdict
from pathlib import Path
from urllib.request import urlretrieve
import xml.etree.ElementTree as ET

# import the countries xml file
tmp = Path(os.getenv("TMP", "/tmp"))
countries = tmp / 'countries.xml'

if not countries.exists():
    urlretrieve(
        'https://bites-data.s3.us-east-2.amazonaws.com/countries.xml',
        countries
    )


def get_income_distribution(xml=countries):
    """
    - Read in the countries xml as stored in countries variable.
    - Parse the XML
    - Return a dict of:
      - keys = incomes (wb:incomeLevel)
      - values = list of country names (wb:name)
    """
    tree = ET.parse(countries)
    root = tree.getroot()
    income_dict = defaultdict(list)
    for country in root:
        name_elem = country.find("{http://www.worldbank.org}name")
        income_elem = country.find("{http://www.worldbank.org}incomeLevel")
        income_dict[income_elem.text].append(name_elem.text)
    return income_dict


print(get_income_distribution())