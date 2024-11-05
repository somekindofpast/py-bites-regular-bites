from collections import defaultdict

# fake data from https://www.mockaroo.com
data = """last_name,first_name,country_code
Watsham,Husain,ID
Harrold,Alphonso,BR
Apdell,Margo,CN
Tomblings,Deerdre,RU
Wasielewski,Sula,ID
Jeffry,Rudolph,TD
Brenston,Luke,SE
Parrett,Ines,CN
Braunle,Kermit,PL
Halbard,Davie,CN"""


def group_names_by_country(_data: str = data) -> defaultdict:
    countries = defaultdict(list)
    lines = _data.splitlines()

    header = "last_name,first_name,country_code"
    if header in lines:
        lines.remove(header)

    for line in lines:
        items = line.split(',')
        value = "{} {}".format(items[1], items[0])
        if countries.get(items[2]):
            countries.get(items[2]).append(value)
        else:
            countries[items[2]] = [value]
    return countries


if __name__ == '__main__':
    print(group_names_by_country())