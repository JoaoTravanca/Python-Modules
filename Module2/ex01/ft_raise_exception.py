def input_temperature(temp_str) -> int:
    return int(temp_str)


def test_temperature(temp) -> None:
    try:
        print(f"Input data is '{temp}'")
        temp = input_temperature(temp)
        print(f"Temperature is now {temp}°C")
    except ValueError:
        print(f"Caught input_temperature error: invalid literal for int() "
              f"with base 10: {temp}")


if __name__ == "__main__":
    print("=== Garden Temperature checker ===")
