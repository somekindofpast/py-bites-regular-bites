import re


def validate_license(key: str) -> bool:
    """Write a regex that matches a PyBites license key
       (e.g. PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4)
    """
    return re.match(r"^PB-[A-Z0-9]{8}-[A-Z0-9]{8}-[A-Z0-9]{8}-[A-Z0-9]{8}$", key) is not None


if __name__ == "__main__":
    print(validate_license("PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4"))