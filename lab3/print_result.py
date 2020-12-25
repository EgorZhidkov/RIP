def print_result(func, *arg):
    def wrapper(*arg):

        n = func(*arg)
        if type(n) == list:
            print(func.__name__)
            for i in range(len(n)):
                print(n[i])
        elif type(n) == dict:
            print(func.__name__)
            for key in n:
                print(key, ' = ', n[key])
        elif type(n) == int:
            print(func.__name__)
            print(n)
        else:
            print(func.__name__)
            print(n)

        return n

        print('')
    return wrapper
    

@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()