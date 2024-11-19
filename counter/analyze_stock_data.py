from collections import Counter

import requests

STOCK_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/stocks.json'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(STOCK_DATA).json()


# your turn:

def _cap_str_to_mln_float(cap):
    """If cap = 'n/a' return 0, else:
       - strip off leading '$',
       - if 'M' in cap value, strip it off and return value as float,
       - if 'B', strip it off, multiply by 1,000 and return
         value as float"""
    if cap == "n/a":
        return 0
    cap = cap.lstrip('$')
    if 'M' in cap:
        return float(cap.rstrip('M'))
    if 'B' in cap:
        return int(float(cap.rstrip('B')) * 1000)
    return 0


def get_industry_cap(industry):
    """Return the sum of all cap values for given industry, use
       the _cap_str_to_mln_float to parse the cap values,
       return a float with 2 digit precision"""
    industry_cap = 0
    for dictionary in data:
        if dictionary["industry"] == industry:
            industry_cap += _cap_str_to_mln_float(dictionary["cap"])
    return float(f"{industry_cap:.2f}")


def get_stock_symbol_with_highest_cap():
    """Return the stock symbol (e.g. PACD) with the highest cap, use
       the _cap_str_to_mln_float to parse the cap values"""
    counter = Counter()
    for dictionary in data:
        counter[dictionary["symbol"]] = _cap_str_to_mln_float(dictionary["cap"])
    return counter.most_common(1)[0][0]


def get_sectors_with_max_and_min_stocks():
    """Return a tuple of the sectors with most and least stocks,
       discard n/a"""
    counter = Counter()
    for dictionary in data:
        if dictionary["sector"] != "n/a":
            counter[dictionary["sector"]] += 1
    return counter.most_common()[0][0], counter.most_common()[-1][0]


if __name__ == '__main__':
    print(_cap_str_to_mln_float("n/a"))
    print(_cap_str_to_mln_float("$100.45M"))
    print(_cap_str_to_mln_float("$20.9B"))
    print(get_industry_cap("Business Services"))
    print(get_industry_cap("Real Estate Investment Trusts"))
    print(get_stock_symbol_with_highest_cap())
    print(get_sectors_with_max_and_min_stocks())