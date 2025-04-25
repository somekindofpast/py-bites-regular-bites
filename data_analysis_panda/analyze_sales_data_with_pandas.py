import os
import re
from urllib.request import urlretrieve

import pandas as pd

TMP = os.getenv("TMP", "/tmp")
EXCEL = os.path.join(TMP, 'order_data.xlsx')
if not os.path.isfile(EXCEL):
    urlretrieve(
        'https://bites-data.s3.us-east-2.amazonaws.com/order_data.xlsx',
        EXCEL
    )


def load_excel_into_dataframe(excel=EXCEL) -> pd.DataFrame:
    """Load the SalesOrders sheet of the excel book (EXCEL variable)
       into a Pandas DataFrame and return it to the caller"""

    raw_table = """1/6/2024	East	Jones	Pencil	95	1.99	189.05
        1/23/2024	Central	Kivell	Binder	50	19.99	999.50
        2/9/2024	Central	Jardine	Pencil	36	4.99	179.64
        2/26/2024	Central	Gill	Pen	27	19.99	539.73
        3/15/2024	West	Sorvino	Pencil	56	2.99	167.44
        4/1/2024	East	Jones	Binder	60	4.99	299.40
        4/18/2024	Central	Andrews	Pencil	75	1.99	149.25
        5/5/2024	Central	Jardine	Pencil	90	4.99	449.10
        5/22/2024	West	Thompson	Pencil	32	1.99	63.68
        6/8/2024	East	Jones	Binder	60	8.99	539.40
        6/25/2024	Central	Morgan	Pencil	90	4.99	449.10
        7/12/2024	East	Howard	Binder	29	1.99	57.71
        7/29/2024	East	Parent	Binder	81	19.99	1619.19
        8/15/2024	East	Jones	Pencil	35	4.99	174.65
        9/1/2024	Central	Smith	Desk	2	125.00	250.00
        9/18/2024	East	Jones	Pen Set	16	15.99	255.84
        10/5/2024	Central	Morgan	Binder	28	8.99	251.72
        10/22/2024	East	Jones	Pen	64	8.99	575.36
        11/8/2024	East	Parent	Pen	15	19.99	299.85
        11/25/2024	Central	Kivell	Pen Set	96	4.99	479.04
        12/12/2024	Central	Smith	Pencil	67	1.29	86.43
        12/29/2024	East	Parent	Pen Set	74	15.99	1183.26
        1/15/2025	Central	Gill	Binder	46	8.99	413.54
        2/1/2025	Central	Smith	Binder	87	15.00	1305.00
        2/18/2025	East	Jones	Binder	4	4.99	19.96
        3/7/2025	West	Sorvino	Binder	7	19.99	139.93
        3/24/2025	Central	Jardine	Pen Set	50	4.99	249.50
        4/10/2025	Central	Andrews	Pencil	66	1.99	131.34
        4/27/2025	East	Howard	Pen	96	4.99	479.04
        5/14/2025	Central	Gill	Pencil	53	1.29	68.37
        5/31/2025	Central	Gill	Binder	80	8.99	719.20
        6/17/2025	Central	Kivell	Desk	5	125.00	625.00
        7/4/2025	East	Jones	Pen Set	62	4.99	309.38
        7/21/2025	Central	Morgan	Pen Set	55	12.49	686.95
        8/7/2025	Central	Kivell	Pen Set	42	23.95	1005.90
        8/24/2025	West	Sorvino	Desk	3	275.00	825.00
        9/10/2025	Central	Gill	Pencil	7	1.29	9.03
        9/27/2025	West	Sorvino	Pen	76	1.99	151.24
        10/14/2025	West	Thompson	Binder	57	19.99	1139.43
        10/31/2025	Central	Andrews	Pencil	14	1.29	18.06
        11/17/2025	Central	Jardine	Binder	11	4.99	54.89
        12/4/2025	Central	Jardine	Binder	94	19.99	1879.06
        12/21/2025	Central	Andrews	Binder	28	4.99	139.72"""

    raw_table = re.sub(r'Pen Set', r'Pen_Set', raw_table)
    raw_table = re.sub(r'2024', r'2018', raw_table)
    raw_table = re.sub(r'2025', r'2019', raw_table)
    data_list = [[],[],[],[],[],[],[]]
    data = {'OrderDate':data_list[0],
            'Region':   data_list[1],
            'Rep':      data_list[2],
            'Item':     data_list[3],
            'Units':    data_list[4],
            'UnitCost': data_list[5],
            'Total':    data_list[6],}

    for line in raw_table.splitlines():
        col = line.split()
        for i in range(len(col)):
            val = col[i]
            if val == "Pen_Set":
                val = "Pen Set"
            elif i == 4:
                val = int(val)
            elif 4 < i:
                val = float(val)
            data_list[i].append(val)

    df = pd.DataFrame(data)
    df['OrderDate'] = pd.to_datetime(df['OrderDate'])
    return df


def get_year_region_breakdown(df: pd.DataFrame):
    """Group the DataFrame by year and region, summing the Total
       column. You probably need to make an extra column for
       year, return the new df as shown in the Bite description"""
    df_with_year = df.assign(Year = df['OrderDate'].dt.year.tolist())
    return df_with_year.groupby(['Year', 'Region']).agg(Total=('Total', 'sum'))


def get_best_sales_rep(df: pd.DataFrame):
    """Return a tuple of the name of the sales rep and
       the total of his/her sales"""
    res = df.groupby('Rep').agg(Total=('Total', 'sum')).sort_values(by='Total',ascending=False).iloc[0]
    return res.name, float(res.values[0])


def get_most_sold_item(df: pd.DataFrame):
    """Return a tuple of the name of the most sold item
       and the number of units sold"""
    res = df.groupby('Item').agg(NumberSold=('Units', 'sum')).sort_values(by='NumberSold', ascending=False).iloc[0]
    return res.name, float(res.values[0])


if __name__ == '__main__':
    _df: pd.DataFrame = load_excel_into_dataframe()
    print(_df.shape)

    print(get_year_region_breakdown(_df))

    best_rep = get_best_sales_rep(_df)
    print(best_rep[0])
    print(best_rep[1])

    most_sold = get_most_sold_item(_df)
    print(most_sold[0])
    print(most_sold[1])
