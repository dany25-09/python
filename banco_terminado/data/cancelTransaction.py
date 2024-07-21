# Define a custom exception
class CancelTransaction(Exception):
    """raise this exception to cancel a bank transaction"""
    pass