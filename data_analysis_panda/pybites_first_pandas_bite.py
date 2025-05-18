import pandas as pd

data = "https://bites-data.s3.us-east-2.amazonaws.com/summer.csv"


def athletes_most_medals(data: str = data) -> pd.Series:
    df = pd.read_csv(data)
    men = df.loc[(df["Gender"] == "Men")]
    women = df.loc[(df["Gender"] == "Women")]
    men = men.groupby("Athlete").size().sort_values(ascending=False).head(1)
    women = women.groupby("Athlete").size().sort_values(ascending=False).head(1)
    return pd.concat([men, women]).sort_values(ascending=False).iloc[:]


if __name__ == '__main__':
    print(athletes_most_medals())