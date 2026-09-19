# Exercise 2 - Recursive Fault Trace

LAST_NAME = "Papa"
FAVORITE_ARTIST = "MAKI"
SEED_NUM = 7


def generate_fault_code(last_name, seed_num, artist):
    return (seed_num * len(last_name)) + len(artist)


fault_trace = []
recursive_calls = 0


def trace_fault(code):
    global recursive_calls

    recursive_calls += 1
    fault_trace.append(code)

    if code <= 1:
        return code

    return trace_fault(code // 2)


FAULT_CODE = generate_fault_code(
    LAST_NAME,
    SEED_NUM,
    FAVORITE_ARTIST
)

final_result = trace_fault(FAULT_CODE)

print("RECURSIVE FAULT TRACE")
print("=" * 40)
print("Student:", LAST_NAME)
print("Favorite Artist:", FAVORITE_ARTIST)
print("Seed Number:", SEED_NUM)
print("Generated Fault Code:", FAULT_CODE)
print("Recursive Trace:", fault_trace)
print("Number of Recursive Calls:", recursive_calls)
print("Final Result:", final_result)
