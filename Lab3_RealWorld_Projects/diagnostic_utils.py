# diagnostic_utils.py

def validate_reading(value):
    if not isinstance(value, (int, float)):
        raise
    TypeError("Telemetry reading must be numeric.")

    if value < 0:
        raise
    ValueError("Telemetry reading cannot be negative.")

    return True

def classify_reading(value):
    if value <= 100:
        return "NORMAL"
    elif value <= 150:
        return "WARNING"
    else:
        return "CRITICAL"

def recursive_check(value):
    if value <= 1:
        return 1

    return value + recursive_check(value - 1)