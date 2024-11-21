from collections import namedtuple
import datetime

import pandas as pd

DATA_FILE = "https://bites-data.s3.us-east-2.amazonaws.com/weather-ann-arbor.csv"
STATION = namedtuple("Station", "ID Date Value")

start_date = datetime.datetime(2005, 1, 1)
end_date = datetime.datetime(2016, 1, 1)


def high_low_record_breakers_for_2015():
    """Extract the high and low record breaking temperatures for 2015

    The expected value will be a tuple with the highest and lowest record
    breaking temperatures for 2015 as compared to the temperature data
    provided.

    NOTE:
    The date values should not have any timestamps, should be a
    datetime.date() object. The temperatures in the dataset are in tenths
    of degrees Celsius, so you must divide them by 10

    Possible way to tackle this challenge:

    1. Create a DataFrame from the DATA_FILE dataset.

    2. Manipulate the data to extract the following:
       * Extract highest temperatures for each day / station pair between 2005-2015
       * Extract lowest temperatures for each  day / station  between 2005-2015
       * Remove February 29th from the dataset to work with only 365 days

    3. Separate data into two separate DataFrames:
       * high/low temperatures between 2005-2014
       * high/low temperatures for 2015

    4. Iterate over the 2005-2014 data and compare to the 2015 data:
       * For any temperature that is higher/lower in 2015 extract ID,
         Date, Value

    5. From the record breakers in 2015, extract the high/low of all the
       temperatures
       * Return those as STATION namedtuples, (high_2015, low_2015)
    """
    df = pd.read_csv(DATA_FILE)
    df['Date'] = pd.to_datetime(df['Date'])
    df = df[
        (start_date <= df["Date"]) &
        (df["Date"] < end_date) &
        ~((df["Date"].dt.month == 2) & (df["Date"].dt.day == 29))
    ]
    df_2005_2014 = df[
        (start_date <= df["Date"]) &
        (df["Date"] < datetime.datetime(end_date.year - 1, end_date.month, end_date.day))
    ]
    df_2015 = df[(df["Date"].dt.year == 2015)]
    df_low = df_2015[(df_2015["Element"] == "TMIN") & (df_2015["Data_Value"] == df_2015["Data_Value"].min())]
    df_high = df_2015[(df_2015["Element"] == "TMAX") & (df_2015["Data_Value"] == df_2015["Data_Value"].max())]
    return (
        STATION(
            df_high.iloc[0]["ID"],
            datetime.date(df_high.iloc[0]["Date"].year, df_high.iloc[0]["Date"].month, df_high.iloc[0]["Date"].day),
            float(df_high.iloc[0]["Data_Value"] / 10)
        ),
        STATION(
            df_low.iloc[0]["ID"],
            datetime.date(df_low.iloc[0]["Date"].year, df_low.iloc[0]["Date"].month, df_low.iloc[0]["Date"].day),
            float(df_low.iloc[0]["Data_Value"] / 10)
        )
    )


if __name__ == '__main__':
    print(high_low_record_breakers_for_2015())