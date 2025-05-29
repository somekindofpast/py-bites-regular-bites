import math


def check_split(item_total, tax_rate, tip, people):
    """Calculate check value and evenly split.

       :param item_total: str (e.g. '$8.68')
       :param tax_rate: str (e.g. '4.75%)
       :param tip: str (e.g. '10%')
       :param people: int (e.g. 3)

       :return: tuple of (grand_total: str, splits: list)
                e.g. ('$10.00', [3.34, 3.33, 3.33])
    """
    grand_total = float(item_total.strip('$'))
    grand_total += grand_total * (0.01 * float(tax_rate.strip('%')))
    grand_total += grand_total * (0.01 * float(tip.strip('%')))
    grand_total = math.floor(grand_total * 100) / 100

    split = round(grand_total / people, 2)
    split_list = [split for _ in range(people)]
    split_list[0] += grand_total - (split * people)

    return "${:.{}f}".format(grand_total, 2), split_list


if __name__ == "__main__":
    print(check_split('$8.68', '4.75%', '10%', 3)) #'$10.00'
    print(check_split('$9.99', '3.25%', '10%', 2)) #'$11.34'
    print(check_split('$186.70', '6.75%', '18%', 6))  # '$235.17'
    print(check_split('$191.57', '6.75%', '15%', 6))  # '$235.18'