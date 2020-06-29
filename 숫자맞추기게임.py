import random

# 코드를 작성하세요.
number = random.randint(1, 20)
result = 0; opportunity = 4
while opportunity > 0:
    user_num = int(input(f'기회가 {opportunity}번 남았습니다. 1-20 사이의 숫자를 맞춰보세요: '))
    if user_num > number:
        print('Down')
    elif user_num < number:
        print('Up')
    else:
        print(f'축하합니다. {5-opportunity}번만에 숫자를 맞추셨습니다.')
        break
    opportunity -= 1
if not opportunity:
    print(f'아쉽습니다. 정답은 {number}였습니다.')