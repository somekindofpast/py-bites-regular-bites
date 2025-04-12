import json
import os
from pathlib import Path
from ipaddress import IPv4Network
from urllib.request import urlretrieve

import pytest

from ips import (ServiceIPRange, parse_ipv4_service_ranges,
                 get_aws_service_range)

URL = "https://bites-data.s3.us-east-2.amazonaws.com/ip-ranges.json"
TMP = os.getenv("TMP", "/tmp")
PATH = Path(TMP, "ip-ranges.json")
IP = IPv4Network('192.0.2.8/29')


@pytest.fixture(scope='module')
def json_file():
    """Import data into tmp folder"""
    urlretrieve(URL, PATH)
    return PATH


# write your pytest code ...

def test_service_ip_range_class():
    service = "AMAZON",
    region = "eu-west-1",
    cidr = IPv4Network("13.248.118.0/24")
    service_ip_range = ServiceIPRange(
        service=service,
        region=region,
        cidr=cidr,
    )
    assert str(service_ip_range) == f"{cidr} is allocated to the {service} service in the {region} region"


def test_parse_ipv4_service_ranges(json_file):
    prefixes = json.loads(json_file.read_text())["prefixes"]
    service_ranges = parse_ipv4_service_ranges(json_file)

    assert service_ranges is not None and len(service_ranges) == len(prefixes)

    assert service_ranges[0].service    == prefixes[0]["service"]
    assert service_ranges[0].region     == prefixes[0]["region"]
    assert str(service_ranges[0].cidr)  == str(IPv4Network(prefixes[0]["ip_prefix"]))

    assert service_ranges[-1].service   == prefixes[-1]["service"]
    assert service_ranges[-1].region    == prefixes[-1]["region"]
    assert str(service_ranges[-1].cidr) == str(IPv4Network(prefixes[-1]["ip_prefix"]))


def test_get_aws_service_range(json_file):
    service_ranges = parse_ipv4_service_ranges(json_file)

    with pytest.raises(ValueError):
        get_aws_service_range("not an address", service_ranges)

    _ranges = get_aws_service_range("99.82.170.0", service_ranges)

    assert len(_ranges) == 2
    assert _ranges[0].service == "AMAZON"
    assert _ranges[1].service == "GLOBALACCELERATOR"