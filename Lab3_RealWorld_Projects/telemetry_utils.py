# telemetry_utils.py

def generate_telemetry(last_name, seed_num, artist):
    base = seed_num + len(last_name) + len(artist)

    return [
        base + 10,
        base + 20,
        base + 30,
        base + 40,
        base + 50
    ]

def telemetry_generator(data):
    for value in data:
        yield value

square_reading = lambda x: x**2