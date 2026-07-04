def ft_recursive_helper(n) -> None:
    if (n > 0):
        ft_recursive_helper(n - 1)
        print("Day", n)


def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))
    ft_recursive_helper(days)
