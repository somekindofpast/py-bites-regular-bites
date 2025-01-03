import pandas as pd

data = "https://s3.us-east-2.amazonaws.com/bites-data/menu.csv"
# load the data in once, functions will use this module object
df = pd.read_csv(data)

pd.options.mode.chained_assignment = None  # ignore warnings


def get_food_most_calories(df=df):
    """Return the food "Item" string with most calories"""
    return df[(df["Calories"] == df["Calories"].max())]["Item"].values[0]


def get_bodybuilder_friendly_foods(df=df, excl_drinks=False):
    """Calulate the Protein/Calories ratio of foods and return the
       5 foods with the best ratio.

       This function has a excl_drinks switch which, when turned on,
       should exclude 'Coffee & Tea' and 'Beverages' from this top 5.

       You will probably need to filter out foods with 0 calories to get the
       right results.

       Return a list of the top 5 foot Item stings."""
    df_drinks_filtered = df[(df["Category"] != "Coffee & Tea") & (df["Category"] != "Beverages")] if excl_drinks else df
    df_cal_filtered = df_drinks_filtered[(df_drinks_filtered["Calories"] != 0)]
    df_prot_cal = df_cal_filtered.assign(prot_cal = df_cal_filtered["Protein"] / df_cal_filtered["Calories"])
    df_prot_cal = df_prot_cal.sort_values(by="prot_cal", ascending=False)
    return df_prot_cal.head(5)["Item"].values


if __name__ == '__main__':
    print(get_food_most_calories())
    print(get_food_most_calories(df[df['Category'] == 'Breakfast']))
    print(get_bodybuilder_friendly_foods())
    print(get_bodybuilder_friendly_foods(excl_drinks=True))