from datetime import datetime
import os
from pathlib import Path
from zipfile import ZipFile

TMP = Path(os.getenv("TMP", "/tmp"))
LOG_DIR = TMP / 'logs'
ZIP_FILE = 'logs.zip'


def zip_last_n_files(directory: Path = LOG_DIR,
                     zip_file: str = ZIP_FILE, n: int = 3):
    file_paths = []
    now = datetime.now().strftime("%Y-%m-%d")
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    sorted_file_paths = sorted(file_paths, key=lambda x: os.path.getctime(x))[-n:]
    with ZipFile(zip_file,'w') as zipped:
        for file in sorted_file_paths:
            file_name = file.split('/')[-1]
            zipped.write(file, arcname=file_name.split('.')[0] + '_' + str(now) + '.' + file_name.split('.')[1])