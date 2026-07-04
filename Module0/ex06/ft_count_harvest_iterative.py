def ft_count_harvest_iterative() -> None:
    time = int(input("Days until harvest: "))
    x = range(1, time + 1)
    for i in x:
        print("Day", i)
