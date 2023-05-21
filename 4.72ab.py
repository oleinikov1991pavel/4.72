number1 = int(input('Введите первое число\Т'))
number2 = int(input('Введите второе число\Т'))
number3 = int(input('Введите третье число\Т'))

if number1 > number2 and number1 > number3:
    print('первое число')
elif number2 > number3 and number2 > number1:
    print('второе число')
elif number3 > number1 and number3 > number2:
    print('третьте число')
else:
    print('равны')
