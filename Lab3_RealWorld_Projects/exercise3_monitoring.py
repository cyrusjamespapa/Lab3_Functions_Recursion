# Exercise 3 - Intelligent Equipment Monitoring Pipeline

import telemetry_utils
import diagnostic_utils


LAST_NAME = "Papa"
FAVORITE_ARTIST = "MAKI"
SEED_NUM = 7


def diagnostic_logger(func):
    def wrapper(*args, **kwargs):
        print("\n--- Diagnostic Process Started ---")
        result = func(*args, **kwargs)
        print("--- Diagnostic Process Completed ---")
        return result

    return wrapper


@diagnostic_logger
def run_monitoring_pipeline(data):
    results = []

    for reading in data:
        try:
            diagnostic_utils.validate_reading(reading)
            condition = diagnostic_utils.classify_reading(reading)

            results.append({
                "Reading": reading,
                "Status": "VALID",
                "Condition": condition
            })

        except (TypeError, ValueError) as error:
            results.append({
                "Reading": reading,
                "Status": "INVALID",
                "Condition": str(error)
            })

    return results


telemetry_data = telemetry_utils.generate_telemetry(
    LAST_NAME,
    SEED_NUM,
    FAVORITE_ARTIST
)

monitoring_results = run_monitoring_pipeline(telemetry_data)

print("\nINTELLIGENT EQUIPMENT MONITORING REPORT")
print("=" * 45)
print("Student:", LAST_NAME)
print("Favorite Artist:", FAVORITE_ARTIST)
print("Seed Number:", SEED_NUM)

print("\nTelemetry Readings:")
for result in monitoring_results:
    print(result)

print("=" * 45)