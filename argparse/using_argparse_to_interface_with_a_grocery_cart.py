import argparse
from collections import namedtuple

Item = namedtuple('Item', 'product price craving')


class Groceries:

    def __init__(self, items=None):
        """This cart can be instantiated with a list of namedtuple
           items, if not provided use an empty list"""
        self._items = items if items is not None else []

    def show(self, items=None):
        """Print a simple table of cart items with total at the end"""
        items = items if items is not None else self
        for item in items:
            product = f'{item.product}'
            if item.craving:
                product += ' (craving)'
            print(f'{product:<30} | {item.price:>3}')
        self._print_total(items)

    def _print_total(self, items):
        """Calculate and print total price of cart"""
        total = sum(item.price for item in items)
        print('-' * 36)
        print(f'{"Total":<30} | {total:>3}')

    def add(self, new_item):
        """Add a new item to cart, exceptions left out for simplicity"""
        self._items.append(new_item)
        self.show()

    def delete(self, product):
        """Delete item matching 'product', raises IndexError
           if no item matches"""
        for i, item in enumerate(self):
            if item.product == product:
                self._items.pop(i)
                break
        else:
            raise IndexError(f'{product} not in cart')
        self.show()

    def search(self, search):
        """Filters items matching insensitive 'contains' search, and passes
           them to show for printing"""
        items = [item for item in self if search.lower()
                 in item.product.lower()]
        self.show(items)

    @property
    def due(self):
        return sum(item.price for item in self)

    def __len__(self):
        """The len of cart"""
        return len(self._items)

    def __getitem__(self, index):
        """Making the class iterable (cart = Groceries() -> cart[1] etc)
           without this dunder I would get 'TypeError: 'Cart' object does
           not support indexing' when trying to index it"""
        return self._items[index]


def create_parser():
    """TODO 1
       Create an ArgumentParser object giving it the required options,
       note that the options are mutually exclusive.
       Returns a argparse.ArgumentParser object"""
    _parser = argparse.ArgumentParser()
    group = _parser.add_mutually_exclusive_group()
    group.add_argument("--list", "-l", action='store_true')
    group.add_argument("--search", "-s", nargs=1)
    group.add_argument("--add", "-a", nargs=3)
    group.add_argument("--delete", "-d", nargs=1)
    return _parser


def handle_args(args=None, cart=None):
    """TODO 2
       Receives args and cart and performs the add/delete/list/search
       operations on cart:
       - If args not provided create a parser object and retrieve the args
       - If cart not provided make a Groceries object with 0 or more items
       Modifies the cart object, no return"""
    if args is None:
        parser = create_parser()
        args = parser.parse_args()

    if cart is None:
        cart = Groceries()

    # different crud operations - please complete ...
    if args.list:
        cart.show()
    elif args.search:
        cart.search(args.search[0])
    elif args.add:
        cart.add(Item(product=args.add[0], price=int(args.add[1]), craving=(args.add[2] == 'True')))
    elif args.delete:
        cart.delete(args.delete[0])