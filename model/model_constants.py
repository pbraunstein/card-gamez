TYPE_ERROR_MESSAGE = 'A {} is not comparable to a {}'
THIS_SHOULD_NEVER_HAPPEN = 'THIS_SHOULD_NEVER_HAPPEN'

class DoubleDealtDeckError(Exception):
    """
    Raised when the deal method is called on a Deck more than once.
    """
    pass
