import os
import urllib.request

# data provided
tmp = os.getenv("TMP", "/tmp")
drive_file = os.path.join(tmp, 'drive.txt')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/driving.py',
    drive_file
)

def wc(file_):
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""
    with open(file_) as f:
        file_name = f.name.split('\\')[-1]
        content = f.read()
    return ' '.join([str(len(content.splitlines())), str(len(content.split())), str(len(content)), file_name])


if __name__ == '__main__':
    print(wc(drive_file))


