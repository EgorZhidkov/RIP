data = [2, -123, -34, 232, 0, 23, 5, -4, 34]

if __name__=='__main__':
    result = sorted(data)
    print(result)
    result_with_lambda = lambda data: sorted(data)
    print(result_with_lambda(data))