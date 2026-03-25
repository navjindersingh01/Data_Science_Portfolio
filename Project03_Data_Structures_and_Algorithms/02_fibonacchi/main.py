import Method_iterative as mi

def main():
    print("~" * 20)
    num = int(input("Enter the number: "))
    print("")

    series = mi.fibonacci_optimized(num)
    sum_series = mi.fibonacci_sum(series)
    size_series = mi.fibonacci_size(num)

    print("Serial:", end=" |")
    for i in range(num):
        print(str(i+1) + (" " * (size_series[i] - len(str(i+1)))), end=" | ")
    print("")

    print("")
    
    print("Series:", end=" |")
    for i in series:
        print(i, end=" | ")
    print("")

    print("")

    print("Sum:   ", end=" |")
    print(f"{sum_series} |")


if __name__ == "__main__":
    main()