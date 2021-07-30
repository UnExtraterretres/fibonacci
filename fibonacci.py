from datetime import datetime
import time


def calc_fibonacci(iteration=100):
    open("log.txt", "a").write(f"{datetime.now()}\n")

    try:
        fibonacci_series = open("fibo.txt", "r").read().split(",")
        open("log.txt", "a").write("fibo.txt loaded\n")
    except FileNotFoundError:
        fibonacci_series = [0, 1]
        open("log.txt", "a").write("fibo.txt FileNotFoundError\n")

    calculation_time = time.time()
    [fibonacci_series.append(fibonacci_series[-1] + fibonacci_series[-2]) for i in range(iteration)]
    open("log.txt", "a").write(f"calculations completed : {time.time()-calculation_time}sec\n")
    open("log.txt", "a").write(f"iteration = {iteration}\n")
    open("log.txt", "a").write(f"len = {len(fibonacci_series)}\n")

    f = open("fibo.txt", "w")
    [f.write(f",{i}") for i in fibonacci_series]
    open("log.txt", "a").write("fibonacci_series saved in fibo.txt\n")

    open("log.txt", "a").write("\n")


if __name__ == "__main__":
    calc_fibonacci()
