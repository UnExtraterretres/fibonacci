from datetime import datetime


def calc_fibonacci(iteration=100):
    try:
        fibonacci_series = open("fibo.txt", "r").read().split(",")
        open("log.txt", "a").write("fibo.txt loaded\n")
    except FileNotFoundError:
        fibonacci_series = [0, 1]
        open("log.txt", "a").write("fibo.txt FileNotFoundError\n")

    [fibonacci_series.append(fibonacci_series[-1] + fibonacci_series[-2]) for i in range(iteration)]
    open("log.txt", "a").write("calculations completed\n")

    f = open("fibo.txt", "w")
    [f.write(f",{i}") for i in fibonacci_series]
    open("log.txt", "a").write("fibonacci_series saved in fibo.txt\n")


if __name__ == "__main__":
    open("log.txt", "a").write(f"{datetime.now()}\n")
    calc_fibonacci()
    open("log.txt", "a").write("\n")
