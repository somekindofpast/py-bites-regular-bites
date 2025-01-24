import re
from typing import Dict, Optional

EMAIL_HEADER = """Return-Path: <bounces+5555-7602-redacted-info>
...
Received: by 10.8.49.86 with SMTP id mf9.22328.51C1E5CDF
    Wed, 19 Jun 2013 17:09:33 +0000 (UTC)
Received: from NzI3MDQ (174.37.77.208-static.reverse.softlayer.com [174.37.77.208])
by mi22.sendgrid.net (SG) with HTTP id 13f5d69ac61.41fe.2cc1d0b
for <redacted-info>; Wed, 19 Jun 2013 12:09:33 -0500 (CST)
Content-Type: multipart/alternative;
boundary="===============8730907547464832727=="
MIME-Version: 1.0
From: redacted-address
To: redacted-address
Subject: A Test From SendGrid
Message-ID: <1371661773.974270694268263@mf9.sendgrid.net>
Date: Wed, 19 Jun 2013 17:09:33 +0000 (UTC)
X-SG-EID: P3IPuU2e1Ijn5xEegYUQ...
X-SendGrid-Contentd-ID: {"test_id":"1371661776"}"""  # noqa E501


def get_email_details(header: str) -> Optional[Dict[str, str]]:
    """User re.search or re.match to capture the from, to, subject
       and date fields. Return the groupdict() of matching object, see:
       https://docs.python.org/3.7/library/re.html#re.Match.groupdict
       If not match, return None
    """
    match_obj = re.search(r"From: (?P<from>.+?)\n.*To: (?P<to>.+?)\n.*Subject: (?P<subject>.+?)\n.*Date: (?P<date>\w{3}, \d{1,2} \w{3} \d{4} \d{2}:\d{2}:\d{2})", header, re.DOTALL)
    if not match_obj:
        return None
    return match_obj.groupdict()


if __name__ == "__main__":
    print(get_email_details(EMAIL_HEADER))

    OTHER_HEADER = """
    Return-Path: <info@pybit.es>
    From: Bob & Julian from PyBites (info@pybit.es)
    To: pybites@ninja.com
    Subject: New regex learning path!
    Date: Sun, 18 Aug 2019 17:16:10 -0700 (PDT)
    Envelope-To: pybites@ninja.com
    ...
    X-SendGrid-Contentd-ID: {"test_id":"1371661776"}
    """

    print(get_email_details(OTHER_HEADER))