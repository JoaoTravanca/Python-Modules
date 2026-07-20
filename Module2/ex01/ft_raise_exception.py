def input_temperature(temp_str) -> int:
    temp = int(temp_str)
    if (temp < 0 or temp > 40):
        if (temp < 0):
            raise ValueError(f"Caught input_temperature error: {temp}"
                             f" is too cold for plants (min 0°C)")
        elif (temp > 40):
            raise ValueError(f"Caught input_temperature error: {temp}"
                             f" is too hot for plants (max 40°C)")
    return temp


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    value = "25"
    try:
        print(f"input data is {value}")
        temp = input_temperature(value)
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    value = "abc"
    try:
        print(f"input data is '{value}'")
        temp = input_temperature(value)
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    value = "100"
    try:
        print(f"input data is '{value}'")
        temp = input_temperature(value)
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    value = "-50"
    try:
        print(f"input data is '{value}'")
        temp = input_temperature(value)
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
