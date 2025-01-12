import statistics
from decimal import Decimal


class IntList(list):
    def __init__(self, numbers: list):
        super().__init__()
        self.extend(numbers)

    def append(self, num):
        if not isinstance(num, int) and not isinstance(num, float) and not isinstance(num, Decimal):
            raise TypeError
        if isinstance(num, Decimal):
            num = float(num)
        super().append(num)

    def extend(self, numbers):
        for num in numbers:
            self.append(num)

    @property
    def mean(self):
        if len(self) == 0:
            return None
        return statistics.mean(self)

    @property
    def median(self):
        if len(self) == 0:
            return None
        return statistics.median(self)

    def __add__(self, other):
        new_list = IntList(self)
        if isinstance(other, list):
            new_list.extend(other)
        else:
            new_list.append(other)
        return new_list

    def __iadd__(self, other):
        if isinstance(other, list):
            self.extend(other)
        else:
            self.append(other)
        return self


if __name__ == '__main__':
    nums = IntList([2, 3])
    nums.append(4)
    nums.extend([5, 7])
    print(nums)
    print(nums.mean)
    print(nums.median)

    nums.append(9.0)
    nums.append(Decimal(11))
    print(nums)
    print(round(nums.mean, 2))
    print(nums.median)

    print(nums + 33)
    print(nums)
    print(nums + [44, 55])
    print(nums)
    nums += 66
    print(nums)
    nums += [77.7, Decimal(88.88)]
    print(nums)