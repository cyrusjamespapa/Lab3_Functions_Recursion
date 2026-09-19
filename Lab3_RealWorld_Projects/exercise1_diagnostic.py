# Exercise 1 - Equipment Diagnostic System

LAST_NAME = "Papa"
FAVORITE_ARTIST = "MAKI"
SEED_NUM = 7


def generate_readings(last_name, seed_num, artist):
    voltage = 220 + seed_num
    current = len(last_name) + seed_num
    temperature = 25 + len(artist)

    return {
        "Voltage": voltage,
        "Current": current,
        "Temperature": temperature
    }


def validate_readings(readings):
    try:
        if not 200 <= readings["Voltage"] <= 240:
            raise ValueError("Voltage is out of range.")

        if not 0 < readings["Current"] <= 20:
            raise ValueError("Current is out of range.")

        if not 0 <= readings["Temperature"] <= 100:
            raise ValueError("Temperature is out of range.")

        return "VALID"

    except (KeyError, TypeError, ValueError) as error:
        return f"INVALID: {error}"


def calculate_readings(readings):
    power = readings["Voltage"] * readings["Current"]
    temperature_f = (readings["Temperature"] * 9 / 5) + 32

    return {
        "Power": power,
        "Temperature_F": temperature_f
    }


def classify_equipment(validation, calculated_data):
    if validation != "VALID":
        return "FAULT"

    power = calculated_data["Power"]
    temperature_f = calculated_data["Temperature_F"]

    if power <= 2500 and temperature_f <= 100:
        return "NORMAL"
    elif power <= 3000 and temperature_f <= 140:
        return "WARNING"
    else:
        return "CRITICAL"


def diagnostic_logger(func):
    def wrapper(*args, **kwargs):
        print("Starting diagnostic process...")
        result = func(*args, **kwargs)
        print("Diagnostic process completed.")
        return result

    return wrapper


@diagnostic_logger
def run_diagnostic(readings):
    validation = validate_readings(readings)

    if validation != "VALID":
        return {
            "Validation": validation,
            "Condition": "FAULT"
        }

    calculated = calculate_readings(readings)
    condition = classify_equipment(validation, calculated)

    return {
        "Validation": validation,
        "Calculated": calculated,
        "Condition": condition
    }


readings = generate_readings(
    LAST_NAME,
    SEED_NUM,
    FAVORITE_ARTIST
)

result = run_diagnostic(readings)

print("\nEQUIPMENT DIAGNOSTIC SUMMARY")
print("=" * 40)
print("Student:", LAST_NAME)
print("Favorite Artist:", FAVORITE_ARTIST)
print("Seed Number:", SEED_NUM)
print("Readings:", readings)
print("Diagnostic Result:", result)