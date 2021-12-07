while True:
    firs_number = int(input())
    second_number = int(input())
    if firs_number < second_number:
        cache = firs_number
        firs_number = second_number
        second_number = cache
    cache = 1
    while cache != 0:
        while firs_number >= second_number:
            firs_number = firs_number - second_number
        cache = firs_number
        firs_number = second_number
        second_number = cache
    print(firs_number)