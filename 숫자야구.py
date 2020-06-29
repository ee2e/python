from random import randint


def generate_numbers():
	numbers = []
	while len(numbers) < 3:
		random = randint(0,9)
		if random not in numbers:
			numbers.append(random)
	print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.")
	return numbers


def take_guess():
	print("숫자 3개를 하나씩 차례대로 입력하세요.")

	new_guess = []
	while len(new_guess) < 3:
		num = int(input(f'{len(new_guess)+1}번째 숫자를 입력하세요: '))
		if 0 <= num <= 9:
			if num in new_guess:
				print('중복되는 숫자입니다. 다시 입력하세요.')
			else:
				new_guess.append(num)
		else:
			print('범위를 벗어나는 숫자입니다. 다시 입력하세요.')

	return new_guess


def get_score(guesses, solution):
	strike_count = 0
	ball_count = 0

	for i in range(len(guesses)):
		if guesses[i] in solution:
			if guesses[i] == solution[i]:
				strike_count += 1
			else:
				ball_count += 1

	return strike_count, ball_count


# 여기서부터 게임 시작!
ANSWER = generate_numbers()
tries = 0

while True:
	guesses = take_guess()
	s, b = get_score(guesses, ANSWER)
	print(f'{s}S {b}B')
	tries += 1
	if s == 3: break

print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))
