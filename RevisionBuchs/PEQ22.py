def square_wave(width, height, n):
    """DS"""
    i = 1
    while i <= n:
        j = 0
        if i % 2 != 0:
            while j < height:
                print(' ' * (width - 1) + '*')
                j += 1
        else:
            while j < height:
                print('*' + ' ' * (width - 1))
                j += 1
        if i < n:
            print('*' * width)

        i += 1


square_wave(10, 5, 22)