import os

DEBUG = os.getenv('DEBUG_MODE', 'false').lower() == 'true'


def add(a, b):
    result = a + b
    if DEBUG:
        print(f"[DEBUG] add({a}, {b}) = {result}")
    return result


def subtract(a, b):
    result = a - b
    if DEBUG:
        print(f"[DEBUG] subtract({a}, {b}) = {result}")
    return result


def multiply(a, b):
    result = a * b
    if DEBUG:
        print(f"[DEBUG] multiply({a}, {b}) = {result}")
    return result


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    result = a / b
    if DEBUG:
        print(f"[DEBUG] divide({a}, {b}) = {result}")
    return result


def power(a, b):
    result = a ** b
    if DEBUG:
        print(f"[DEBUG] power({a}, {b}) = {result}")
    return result
