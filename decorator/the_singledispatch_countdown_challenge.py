from functools import singledispatch


@singledispatch
def count_down(data_type):
    raise ValueError("Invalid data type")

@count_down.register(str)
@count_down.register(int)
@count_down.register(float)
def _(data_type):
    data_type = str(data_type)
    for i in range(len(data_type)):
        print(data_type) if i == 0 else print(data_type[:-i])

@count_down.register(list)
@count_down.register(tuple)
@count_down.register(set)
@count_down.register(range)
def _(data_type):
    data_str = ""
    for item in data_type:
        data_str += str(item)
    count_down(data_str)

@count_down.register(dict)
def _(data_type):
    data_str = ""
    for item in data_type.items():
        data_str += str(item[0])
    count_down(data_str)


if __name__ == '__main__':
    print("string:")
    count_down('1234')
    print()

    print("int:")
    count_down(1234)
    print()

    print("float:")
    count_down(12.34)
    print()

    print("num_list:")
    count_down([1, 2, 3, 4])
    print()

    print("str_list:")
    count_down(['1', '2', '3', '4'])
    print()

    print("num_tuple:")
    count_down((1, 2, 3, 4))
    print()

    print("str_tuple:")
    count_down(('1', '2', '3', '4'))
    print()

    print("num_dict:")
    count_down({1: 'one', 2: 'two', 3: 'three', 4: 'four'})
    print()

    print("str_dict:")
    count_down({'1': 'one', '2': 'two', '3': 'three', '4': 'four'})
    print()

    print("range:")
    count_down(range(1, 5))
    print()

    print("set:")
    count_down({x for x in range(1, 5)})
    print()