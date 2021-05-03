def FizzBuzz(input):
    for i in range(input):
        if (i+1) % 5 == 0 and (i+1) % 3 == 0:
            print(i+1, 'FizzBuzz')
        elif (i+1) % 5 == 0:
            print(i+1, 'Buzz')
        elif (i+1) % 3 == 0:
            print(i+1, 'Fizz')

FizzBuzz(100)


def fizzbuzz(input):
    for i in range(1, input+1):
        output = ''
        if (i) % 3 == 0:
            output = output + 'Fizz'
        if (i) % 5 == 0:
            output += 'Buzz'
        print(i, output)

fizzbuzz(100)