from datetime import datetime, timedelta
import os
import urllib.request
import re
from typing import Union

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
tmp = os.getenv("TMP", "/tmp")
logfile = os.path.join(tmp, 'log')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/messages.log',
    logfile
)

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:

def convert_to_datetime(line: str) -> Union[datetime, None]:
    """Extract timestamp from logline and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
    """
    if len(line.split()) < 2:
        return None
    date_parts = re.sub(r'[-T:]', r' ', line.split()[1]).split()
    if not date_parts or len(date_parts) != 6:
        return None
    return datetime(int(date_parts[0]), int(date_parts[1]), int(date_parts[2]), int(date_parts[3]), int(date_parts[4]), int(date_parts[5]))



def time_between_shutdowns(loglines_) -> timedelta:
    """Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """
    shutdown_lines = [logline for logline in loglines_ if "shutdown initiated" in logline.lower()]
    if not shutdown_lines or len(shutdown_lines) < 2:
        return timedelta(0)
    first_date = convert_to_datetime(shutdown_lines[0])
    last_date = convert_to_datetime(shutdown_lines[-1])
    if first_date is None or last_date is None:
        return timedelta(0)
    return last_date - first_date



if __name__ == "__main__":
    new_date = convert_to_datetime("INFO 2014-07-03T23:27:51 supybot Shutdown complete")
    print("The result of a valid string is a datetime:", type(new_date) == datetime, new_date)
    wrong_date = convert_to_datetime("gibberish text")
    print("The result of an invalid string is None:", wrong_date is None)
    print(time_between_shutdowns([]))
    print(time_between_shutdowns(loglines))