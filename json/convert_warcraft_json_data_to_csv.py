import os
from pathlib import Path
import csv
import json
from json.decoder import JSONDecodeError

EXCEPTION = 'exception caught'
TMP = Path(os.getenv("TMP", "/tmp"))


def convert_to_csv(json_file):
    """Read/load the json_file (local file downloaded to /tmp) and
       convert/write it to defined csv_file.
        The data is in mounts > collected

       Catch bad JSON (JSONDecodeError) file content, in that case print the defined
       EXCEPTION string ('exception caught') to stdout reraising the exception.
       This is to make sure you actually caught this exception.

       Example csv output:
       creatureId,icon,isAquatic,isFlying,isGround,isJumping,itemId,name,qualityId,spellId
       32158,ability_mount_drake_blue,False,True,True,False,44178,Albino Drake,4,60025
       63502,ability_mount_hordescorpionamber,True,...
       ...
    """  # noqa E501

    try:
        csv_file = TMP / json_file.name.replace('.json', '.csv')
        with open(json_file, 'r') as file:
            data = json.load(file)

        with open(csv_file, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=list(data["mounts"]["collected"][0].keys()))
            writer.writeheader()
            writer.writerows(data["mounts"]["collected"])
    except:
        print(EXCEPTION)
        raise JSONDecodeError(msg="Invalid control character", doc="", pos=0)