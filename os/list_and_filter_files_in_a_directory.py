import os

ONE_KB = 1024


def get_files(dirname, size_in_kb):
    """Return files in dirname that are >= size_in_kb"""
    obj = os.scandir(dirname)
    res = []
    for entry in obj:
        if entry.is_file() and size_in_kb <= float(os.path.getsize(entry.path)) / 1024.0:
            res.append(entry.name)
    return res