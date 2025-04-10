import pytest

from account import Account

# write your pytest functions below, they need to start with test_

def test_account_creation():
    owner = "Owner"
    amount = 150
    acc = Account(owner, amount)
    assert str(acc) == f"Account of {owner} with starting amount: {amount}"
    assert repr(acc) == f"Account('{owner}', {amount})"
    assert len(acc) == 0


def test_transactions():
    owner = "Owner"
    start_amount = 29
    first_transaction = 41
    second_transaction = -5
    third_transaction = -13
    acc = Account(owner, start_amount)

    with pytest.raises(ValueError):
        acc.add_transaction("not integer")
    assert len(acc) == 0

    acc.add_transaction(first_transaction)
    assert acc[0] == first_transaction
    assert acc.balance == start_amount + first_transaction
    assert len(acc) == 1

    acc.add_transaction(second_transaction)
    assert acc[1] == second_transaction
    assert acc.balance == start_amount + first_transaction + second_transaction
    assert len(acc) == 2

    acc.add_transaction(third_transaction)
    assert acc[2] == third_transaction
    assert acc.balance == start_amount + first_transaction + second_transaction + third_transaction
    assert len(acc) == 3


def test_multiple_accounts():
    acc1_owner = "Owner1"
    acc1_start = 0
    acc1_first = 15
    acc1 = Account(acc1_owner, acc1_start)
    acc1.add_transaction(acc1_first)

    acc2_owner = "Owner2"
    acc2_start = 7
    acc2_first = -6
    acc2_second = 14
    acc2 = Account(acc2_owner, acc2_start)
    acc2.add_transaction(acc2_first)
    acc2.add_transaction(acc2_second)

    acc3_owner = "Owner3"
    acc3_start = 14
    acc3 = Account(acc3_owner, acc3_start)

    acc4_owner = "Owner4"
    acc4_start = 16
    acc4 = Account(acc4_owner, acc4_start)

    assert acc1 == acc2
    assert acc3 < acc1
    assert not acc4 < acc1

    acc_combined = acc1 + acc2
    assert str(acc_combined) == f"Account of {acc1_owner}&{acc2_owner} with starting amount: {acc1_start + acc2_start}"
    assert repr(acc_combined) == f"Account('{acc1_owner}&{acc2_owner}', {acc1_start + acc2_start})"
    assert acc_combined[0] == acc1_first
    assert acc_combined[1] == acc2_first
    assert acc_combined[2] == acc2_second

