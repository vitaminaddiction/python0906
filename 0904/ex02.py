def sum_range():
    x, y = try_int()
    large_num = max(x, y)
    small_num = min(x, y)
    total = 0
    for i in range(small_num, large_num + 1):
        total += i
    print(f'{small_num} 부터 {large_num} 까지의 합은 : {total}')


def try_int():
    while True:
        try:
            x, y = input("두 수를 입력해주세요.(공백기준)").split()
            x = int(x)
            y = int(y)
            return x, y
        except ValueError:
            print("정수를 입력해주세요.")


sum_range()

