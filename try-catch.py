try:
    num=int(input('Enter an integer: '))
    print(num)
except ValueError:
    print('Something went wrong')
else:
    print('Nothing went wrong')