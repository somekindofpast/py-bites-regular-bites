from collections import Counter
from datetime import datetime
from dateutil.parser import parse
from typing import List


def get_srt_section_ids(text: str) -> List[int]:
    """Parse a caption (srt) text passed in and return a
       list of section numbers ordered descending by
       highest speech speed
       (= ratio of "time past:characters spoken")

       e.g. this section:

       1
       00:00:00,000 --> 00:00:01,000
       let's code

       (10 chars in 1 second)

       has a higher ratio then:

       2
       00:00:00,000 --> 00:00:03,000
       code

       (4 chars in 3 seconds)

       You can ignore milliseconds for this exercise.
    """
    text += "\n   "
    section_id = -1
    from_date: datetime
    to_date: datetime
    caption = ""
    counter = Counter()
    for line in text.splitlines():
        if len(line.strip()) == 0:
            if section_id != -1:
                diff = (to_date.second - from_date.second)
                counter[section_id] = int(len(caption) / diff)
                section_id = -1
                caption = ""
        elif section_id == -1:
            section_id = int(line)
        elif "-->" in line:
            from_date = parse(line.split("-->")[0].strip())
            to_date = parse(line.split("-->")[1].strip())
        else:
            caption += line
    return [element[0] for element in counter.most_common()]


if __name__ == '__main__':
    text1 = """
    1
    00:00:00,498 --> 00:00:02,827
    Beautiful is better than ugly.

    2
    00:00:02,827 --> 00:00:06,383
    Explicit is better than implicit.

    3
    00:00:06,383 --> 00:00:09,427
    Simple is better than complex.
    """
    text2 = """
    18
    00:01:12,100 --> 00:01:17,230
    If you want a bit more minimalistic view, you can actually hide the sidebar.

    19
    00:01:18,200 --> 00:01:19,500
    If you go to Settings

    20
    00:01:23,000 --> 00:01:26,150
    scroll down to 'Focus Mode'.

    21
    00:01:28,200 --> 00:01:35,180
    You can actually hide the sidebar and have only the description and the code editor.
    """
    text3 = '\n'.join(text1.splitlines()[:9])
    text4 = '\n'.join(text2.splitlines()[5:])
    # testing hours as well
    text5 = """
    32
    00:59:45,000 --> 00:59:48,150
    talking quite normal here

    33
    01:00:00,000 --> 01:00:07,000
    he is talking slooooow

    34
    02:04:28,000 --> 02:04:30,000
    she is talking super fast here!
    """
    print(get_srt_section_ids(text1))
    print(get_srt_section_ids(text2))
    print(get_srt_section_ids(text3))
    print(get_srt_section_ids(text4))
    print(get_srt_section_ids(text5))