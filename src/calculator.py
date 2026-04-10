"""
Ominakavsar's Calculator Module
Numeric operations for cloud-based arithmetic.
"""

def add(a: float, b: float) -> float:
    return float(a + b)

def subtract(a: float, b: float) -> float:
    return float(a - b)

def multiply(a: float, b: float) -> float:
    return float(a * b)

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Division by zero is mathematically undefined.")
    return float(a / b)
