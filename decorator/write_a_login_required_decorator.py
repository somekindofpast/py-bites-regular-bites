from functools import wraps

known_users = ['bob', 'julian', 'mike', 'carmen', 'sue']
loggedin_users = ['mike', 'sue']


def login_required(func):
    @wraps(func)
    def wrapper(user):
        if user in loggedin_users:
            return func(user)
        elif user in known_users:
            return "please login"
        else:
            return "please create an account"

    return wrapper


@login_required
def welcome(user):
    '''Return a welcome message if logged in'''
    return f"welcome back {user}"


if __name__ == '__main__':
    print(welcome('anonymous'))
    print(welcome('julian'))
    print(welcome('sue'))
    print(welcome.__doc__)