class User:
    """A User class
       (Django's User model inspired us)
    """

    def __init__(self, first_name, last_name):
        """Constructor, base values"""
        self.first_name = first_name
        self.last_name = last_name

    @property
    def get_full_name(self):
        """Return first and last name separated by a whitespace
           and using title case for both.
        """
        return f"{self.first_name} {self.last_name}".title()

    @property
    def username(self):
        """A username consists of the first char of
           the user's first_name and the first 7 chars
           of the user's last_name, both lowercased.

           If this is your first property, check out:
           https://pybit.es/articles/property-decorator/
        """
        return f"{self.first_name[:1]}{self.last_name[:7]}".lower()

    # add a __str__ and a __repr__
    # see: https://stackoverflow.com/a/1438297
    # "__repr__ is for devs, __str__ is for customers"
    #
    # see also TESTS for required output

    def __str__(self):
        return f"{self.get_full_name} ({self.username})"

    def __repr__(self):
        """Don't hardcode the class name, hint: use a
           special attribute of self.__class__ ...
        """
        return f"{type(self).__name__}('{self.first_name}', '{self.last_name}')"


if __name__ == '__main__':
    user = User("first", "last56789")
    print(user.get_full_name)
    print(user.username)
    print(user)
    print(repr(user))