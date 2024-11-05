from collections import Counter

data = [{"id":1,"automaker":"Dodge","model":"Ram Van 1500","year":1999},
   {"id":2,"automaker":"Chrysler","model":"Town & Country","year":2002},
   {"id":3,"automaker":"Porsche","model":"Cayenne","year":2008},
  ]


# your turn:
def most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
       the highest number of new car models"""
    automakers = []
    for dictionary in data:
        if dictionary["year"] == year:
            automakers.append(dictionary["automaker"])
    return Counter(automakers).most_common(1)[0][0]


def get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""
    result_set = set()
    for dictionary in data:
        if dictionary["automaker"] == automaker and dictionary["year"] == year:
            result_set.add(dictionary["model"])
    return result_set


if __name__ == '__main__':
    print(most_prolific_automaker(1999))
    print(get_models("Chrysler", 2002))