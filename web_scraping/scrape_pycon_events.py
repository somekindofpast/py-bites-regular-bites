import json
from collections import namedtuple
from typing import List

import requests
from bs4 import BeautifulSoup
from datetime import datetime

PYCON_DATA = "https://bites-data.s3.us-east-2.amazonaws.com/pycons.html"

PyCon = namedtuple("PyCon", "name city country start_date end_date url")

country_lookup = {
    "Africa": [
        "Algeria", "Angola", "Benin", "Botswana",
        "Burkina Faso", "Burundi", "Cameroon", "Cape Verde",
        "Central African Republic", "Chad", "Comoros",
        "Democratic Republic of the Congo",
        "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea",
        "Ethiopia", "Gabon", "Ghana", "Guinea", "Guinea-Bissau",
        "Ivory Coast", "Kenya", "Lesotho", "Liberia",
        "Libya", "Madagascar", "Malawi", "Mali",
        "Mauritania", "Mauritius", "Morocco", "Mozambique",
        "Namibia", "Niger", "Nigeria", "Republic of the Congo",
        "Rwanda", "São Tome and Principe", "Senegal", "Seychelles",
        "Sierra Leone", "Somalia", "South Africa", "South Sudan",
        "Sudan", "Swaziland", "Tanzania", "The Gambia",
        "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe",
    ],
    "Asia": [
        "Afghanistan", "Armenia", "Azerbaijan", "Bahrain",
        "Bangladesh", "Bhutan", "Brunei", "Cambodia",
        "China", "East Timor", "Georgia", "India",
        "Indonesia", "Iran", "Iraq", "Israel",
        "Japan", "Jordan", "Kazakhstan", "Kuwait",
        "Kyrgyzstan", "Laos", "Lebanon", "Malaysia",
        "Maldives", "Mongolia", "Myanmar", "Nepal",
        "North Korea", "Oman", "Pakistan", "Palestinian territories",
        "Philippines", "Qatar", "Saudi Arabia", "Singapore",
        "South Korea", "Sri Lanka", "Syria", "Taiwan",
        "Tajikistan", "Thailand", "Turkey", "Turkmenistan",
        "United Arab Emirates", "Uzbekistan", "Vietnam",
        "Yemen",
    ],
    "Australia and Oceania": [
        "Australia", "Federated States of Micronesia", "Fiji",
        "Kiribati", "Marshall Islands", "Nauru", "New Zealand",
        "Palau", "Papua New Guinea", "Samoa", "Solomon Islands",
        "Tonga", "Tuvalu", "Vanuatu",
    ],
    "Europe": [
        "Albania", "Andorra", "Austria", "Belarus", "Belgium",
        "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Cyprus",
        "Czech Republic", "Denmark", "Estonia", "Finland",
        "France", "Germany", "Greece", "Hungary", "Iceland",
        "Italy", "Latvia", "Liechtenstein", "Lithuania",
        "Luxembourg", "Malta", "Moldova", "Monaco",
        "Montenegro", "Netherlands", "Norway", "Poland",
        "Portugal", "Republic of Ireland", "Republic of Macedonia",
        "Romania", "Russia", "San Marino", "Serbia", "Slovakia",
        "Slovenia", "Spain", "Sweden", "Switzerland",
        "Ukraine", "United Kingdom", "U.K.", "Vatican City",
    ],
    "North America": [
        "Antigua and Barbuda", "Barbados", "Belize",
        "Canada", "Costa Rica", "Cuba", "Dominica",
        "Dominican Republic", "El Salvador", "Grenada",
        "Guatemala", "Haiti", "Honduras", "Jamaica",
        "Mexico", "Nicaragua", "Panama", "Saint Kitts and Nevis",
        "Saint Lucia", "Saint Vincent and the Grenadines",
        "The Bahamas", "Trinidad and Tobago",
        "United States of America", "U.S.A.",
    ],
    "South America": [
        "Argentina", "Bolivia", "Brazil", "Chile",
        "Colombia", "Ecuador", "Guyana", "Paraguay",
        "Peru", "Suriname", "Uruguay", "Venezuela",
    ],
}


def get_continent(country: str) -> str:
    """
    Given a country name returns the associated continent of the country.

    :param country: The name of the country
    :type country: str
    :returns: The continent of the country
    :rtype: str
    """
    for continent, countries in country_lookup.items():
        for c in countries:
            if country.lower() in c.lower():
                return continent


def _get_pycon_data():
    """Helper function that retrieves the required PyCon data"""
    with requests.Session() as session:
        return session.get(PYCON_DATA).content.decode("utf-8")


def get_pycon_events(data=_get_pycon_data()) -> List[PyCon]:
    """
    Scrape the PyCon events from the given website data and
    return a list of PyCon namedtuples. Pay attention to the
    application/ld+json data structure website data.
    """
    soup = BeautifulSoup(data, "html.parser")
    scripts = soup.find_all("script", type="application/ld+json")
    pycon_events: List[PyCon] = []
    for script in scripts:
        event_dict = json.loads("".join(script.contents))
        if "pycon" not in event_dict["name"].lower():
            continue
        address_dict = event_dict["location"]["address"]
        start_date = event_dict["startDate"].split('-')
        end_date = event_dict["endDate"].split('-')
        event = PyCon(event_dict["name"], address_dict["addressLocality"], address_dict["addressCountry"],
                      datetime(int(start_date[0]), int(start_date[1]), int(start_date[2])),
                      datetime(int(end_date[0]), int(end_date[1]), int(end_date[2])),
                      event_dict["url"])
        pycon_events.append(event)
    return pycon_events


def filter_pycons(pycons: List[PyCon],
                  year: int = 2019,
                  continent: str = "Europe") -> List[PyCon]:
    """
    Given a list of PyCons a year and a continent return
    a list of PyCons that take place in that year and on
    that continent.
    """
    return [pycon for pycon in pycons if pycon.start_date.year == year and get_continent(pycon.country) == continent]


if __name__ == '__main__':
    events = get_pycon_events()
    print(f'total pycon events: {len(events)}')
    print({event.city for event in events})
    filtered_events = filter_pycons(events)
    print(f'filtered pycon events: {len(filtered_events)}')
    print({event.city for event in filtered_events})