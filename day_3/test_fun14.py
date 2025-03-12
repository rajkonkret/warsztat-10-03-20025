# pip install pytest
# cd .\day_3\
# # pytest .\fun_14.py
import fun_14 as f14

transactions = [
    {"id": 1, "type": "income", "amount": 500, "currency": "USD"},
    {"id": 2, "type": "expense", "amount": 200, "currency": "USD"},
    {"id": 3, "type": "income", "amount": 500, "currency": "USD"},
    {"id": 4, "type": "expense", "amount": 300, "currency": "USD"},
    {"id": 5, "type": "income", "amount": 700, "currency": "USD"},
    {"id": 6, "type": "expense", "amount": 400, "currency": "EUR"},
    {"id": 7, "type": "income", "amount": 100, "currency": "EUR"},
]


def test_transaction_processing():
    assert f14.map_tranactions(f14.filter_transactions(transactions, "income"), "USD") == [500, 500, 700, 0]
    # Launching pytest with arguments C:\Users\CSComarch\PycharmProjects\warsztat-10-03-20025\day_3\fun_14.py --no-header --no-summary -q in C:\Users\CSComarch\PycharmProjects\warsztat-10-03-20025\day_3
    #
    # ============================= test session starts =============================
    # collecting ... collected 1 item
    #
    # fun_14.py::test_transaction_processing PASSED                            [100%]
    #
    # ============================== 1 passed in 0.03s ==============================
    #
    # Process finished with exit code 0
    assert f14.reduce_transactions([1000, 500, 700, 0]) == 2200

    print("All test passed")


def test_process():
    assert f14.process_transactions(transactions, "expense", "EUR") == 400
