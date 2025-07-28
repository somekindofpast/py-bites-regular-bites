import re

def pair_files(filenames):
    """
    Function that pairs filenames

    filenames: list[str] containing filenames
    returns: list[tuple[str, str]] containing filename pairs
    """
    res = []
    for i in range(len(filenames)):
        r1_sample = filenames[i].lower().split('_')
        if not _is_valid_sample(r1_sample) or r1_sample[-2] != "r1":
            continue

        for j in range(len(filenames)):
            if i == j:
                continue
            r2_sample = filenames[j].lower().split('_')
            if not _is_valid_sample(r2_sample) or r2_sample[-2] != "r2" or len(r2_sample) != len(r1_sample):
                continue

            is_match = True
            for k in range(len(r2_sample)-2):
                if r2_sample[k] != r1_sample[k]:
                    is_match = False
                    break

            if is_match:
                res.append((filenames[i], filenames[j]))
                break
    return res


def _is_valid_sample(sample: list[str]) -> bool:
    if len(sample) < 5:
        return False
    if sample[-1] != "001.fastq.gz":
        return False
    if not (sample[-2] == "r1" or sample[-2] == "r2"):
        return False
    if re.match(r"l\d{3}$", sample[-3]) is None:
        return False
    if re.match(r"s\d{1,2}$", sample[-4]) is None:
        return False

    return True


# Set up for your convenience during testing
if __name__ == "__main__":
    filenames = [
        "Sample1_S1_L001_R1_001.FASTQ.GZ",
        "Sample1_S1_L001_R2_001.fastq.gz",
        "Sample2_S2_L001_R1_001.fastq.gz",
        "sample2_s2_l001_r2_001.fastq.gz",
    ]
    # ('Sample1_S1_L001_R1_001.FASTQ.GZ', 'Sample1_S1_L001_R2_001.fastq.gz')
    # ('Sample2_S2_L001_R1_001.fastq.gz', 'sample2_s2_l001_r2_001.fastq.gz')

    for pair in pair_files(filenames):
        print(pair)