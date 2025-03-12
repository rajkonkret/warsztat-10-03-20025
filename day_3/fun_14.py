from functools import reduce

transactions = [
    {"id": 1, "type": "income", "amount": 1000, "currency": "USD"},
    {"id": 2, "type": "expense", "amount": 200, "currency": "USD"},
    {"id": 3, "type": "income", "amount": 500, "currency": "USD"},
    {"id": 4, "type": "expense", "amount": 300, "currency": "USD"},
    {"id": 5, "type": "income", "amount": 700, "currency": "USD"},
    {"id": 6, "type": "expense", "amount": 400, "currency": "EUR"},
    {"id": 7, "type": "income", "amount": 100, "currency": "EUR"},
]


def filter_transactions(transactions, transaction_type):
    return list(filter(lambda x: x['type'] == transaction_type, transactions))


def map_tranactions(transactions, currency):
    return list(map(lambda x: x['amount'] if x['currency'] == currency else 0, transactions))


def reduce_transactions(transactions):
    return reduce(lambda x, y: x + y, transactions, 0)


def process_transactions(transactions, transaction_type, currency):
    filtered = filter_transactions(transactions, transaction_type)
    mapped = map_tranactions(filtered, currency)
    total = reduce_transactions(mapped)
    return total


# pip install pytest
# cd .\day_3\
# result = process_transactions(transactions, "income", "EUR")
# print("Result:", result) # Result: 100
# pytest .\fun_14.py

# def test_transaction_processing():
#     assert map_tranactions(filter_transactions(transactions, "income"), "USD") == [1000, 500, 700, 0]
# # Launching pytest with arguments C:\Users\CSComarch\PycharmProjects\warsztat-10-03-20025\day_3\fun_14.py --no-header --no-summary -q in C:\Users\CSComarch\PycharmProjects\warsztat-10-03-20025\day_3
# #
# # ============================= test session starts =============================
# # collecting ... collected 1 item
# #
# # fun_14.py::test_transaction_processing PASSED                            [100%]
# #
# # ============================== 1 passed in 0.03s ==============================
# #
# # Process finished with exit code 0
#     assert reduce_transactions([1000, 500, 700, 0]) == 2200
#
#     print("All test passed")