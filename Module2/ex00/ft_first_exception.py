def input_temperature(temp_str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    input = "25"
    try:
        print(f"input data is {input}")
        temp = input_temperature(input)
        print(f"Temperature is now {temp}°C")
    except ValueError:
        print(f"Caught input_temperature error: invalid literal for int() "
              f"with base 10: {temp}")
    input = "abc"
    try:
        print(f"input data is '{input}'")
        temp = input_temperature(input)
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
