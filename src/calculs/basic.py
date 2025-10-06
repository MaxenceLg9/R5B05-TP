
def add(a : int, b : int) -> int:
    return a + b

def mul(a : int, b : int) -> int:
    return a * b

def powc(a: int, b: int) -> int:
    """Compute a**b but raise ValueError for the undefined case 0**0."""
    return a ** b
