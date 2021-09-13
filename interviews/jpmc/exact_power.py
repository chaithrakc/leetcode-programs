if __name__ == '__main__':
    line = 1024
    num = int(line)
    exact_power = False
    while num > 2:
        num, rem = divmod(num, 2)
        if rem != 0:
            break
    if num == 2:
        exact_power = True
    print(exact_power)


