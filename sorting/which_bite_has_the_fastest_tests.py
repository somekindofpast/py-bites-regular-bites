import os
from collections import defaultdict
from pathlib import Path
from urllib.request import urlretrieve

tmp = Path(os.getenv("TMP", "/tmp"))
timings_log = tmp / 'pytest_timings.out'
if not timings_log.exists():
    urlretrieve(
        'https://bites-data.s3.us-east-2.amazonaws.com/pytest_timings.out',
        timings_log
    )


def get_bite_with_fastest_avg_test(timings: list[str]) -> str:
    """Return the bite which has the fastest average time per test"""
    test_speeds = defaultdict(float)
    for row in timings:
        if "passed" not in row:
            continue
        bite = row.split(" =")[0]
        passed = int(row.split("= ")[1].split(" passed")[0])
        seconds = float(row.split("in ")[1].split(" seconds")[0])
        test_speeds[bite] = seconds / passed
    return sorted(test_speeds.items(), key=lambda x: x[1])[0][0]