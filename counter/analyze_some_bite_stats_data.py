from collections import Counter
from csv import DictReader
import os
from urllib.request import urlretrieve

TMP = os.getenv("TMP", "/tmp")
LOGS = 'bite_output_log.txt'
DATA = os.path.join(TMP, LOGS)
S3 = 'https://bites-data.s3.us-east-2.amazonaws.com'
if not os.path.isfile(DATA):
    urlretrieve(f'{S3}/{LOGS}', DATA)


class BiteStats:

    def __init__(self, data=DATA):
        self.rows = []
        with open(DATA, newline='', encoding='UTF-8') as csvfile:
            self.rows = list(DictReader(csvfile))

    @property
    def number_bites_accessed(self) -> int:
        """Get the number of unique Bites accessed"""
        bite_set = set()
        [bite_set.add(row["bite"]) for row in self.rows]
        return len(bite_set)

    @property
    def number_bites_resolved(self) -> int:
        """Get the number of unique Bites resolved (completed=True)"""
        bite_set = set()
        [bite_set.add(row["bite"]) for row in self.rows if row["completed"] == "True"]
        return len(bite_set)

    @property
    def number_users_active(self) -> int:
        """Get the number of unique users in the data set"""
        bite_set = set()
        [bite_set.add(row["user"]) for row in self.rows]
        return len(bite_set)

    @property
    def number_users_solving_bites(self) -> int:
        """Get the number of unique users that resolved
           one or more Bites"""
        bite_set = set()
        [bite_set.add(row["user"]) for row in self.rows if row["completed"] == "True"]
        return len(bite_set)

    @property
    def top_bite_by_number_of_clicks(self) -> str:
        """Get the Bite that got accessed the most
           (= in most rows)"""
        counter = Counter()
        for row in self.rows:
            counter[row["bite"]] += 1
        return counter.most_common(1)[0][0]

    @property
    def top_user_by_bites_completed(self) -> str:
        """Get the user that completed the most Bites"""
        counter = Counter()
        for row in self.rows:
            if row["completed"] == "True":
                counter[row["user"]] += 1
        return counter.most_common(1)[0][0]


if __name__ == '__main__':
    bite_stats = BiteStats()
    print(bite_stats.number_bites_accessed)
    print(bite_stats.number_bites_resolved)
    print(bite_stats.number_users_active)
    print(bite_stats.number_users_solving_bites)
    print(bite_stats.top_bite_by_number_of_clicks)
    print(bite_stats.top_user_by_bites_completed)