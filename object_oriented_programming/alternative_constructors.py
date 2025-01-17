import re


class DomainException(Exception):
    """Raised when an invalid is created."""


class Domain:

    def __init__(self, name):
        # validate a current domain (r'.*\.[a-z]{2,3}$' is fine)
        # if not valid, raise a DomainException
        if re.match(r'.*\.[a-z]{2,3}$', name) is None:
            raise DomainException
        self.name: str = name

    # next add a __str__ method and write 2 class methods
    # called parse_url and parse_email to construct domains
    # from an URL and email respectively

    def __str__(self):
        return self.name

    @classmethod
    def parse_url(cls, url: str):
        url_parts = url.split("://")
        if len(url_parts) == 2:
            url = url_parts[1]
        return cls(url.split("/")[0])

    @classmethod
    def parse_email(cls, email: str):
        email_parts = email.split("@")
        if len(email_parts) == 2:
            email = email_parts[1]
        return cls(email)

if __name__ == '__main__':
    print(Domain("stuff.en"))
    domain = Domain.parse_url("https://stuff.en/aa/bb/cc.txt")
    print(type(domain))
    print(str(domain))
    domain = Domain.parse_email("suff@hotmail.co.uk")
    print(type(domain))
    print(str(domain))