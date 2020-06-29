from random import randint


def generate_numbers(n):
	numbers = []
	while len(numbers) < n:
		random = randint(1, 45)
		if random not in numbers:
			numbers.append(random)
	return numbers


def draw_winning_numbers():
	winning_numbers = generate_numbers(7)
	return sorted(winning_numbers[:6]) + winning_numbers[6:]


def count_matching_numbers(numbers, winning_numbers):
	cnt = 0
	for n in numbers:
		if n in winning_numbers:
			cnt += 1
	return cnt


def check(numbers, winning_numbers):
	count = count_matching_numbers(numbers, winning_numbers[:6])
	bonus_count = count_matching_numbers(numbers, winning_numbers[6:])
	if count == 6:
		return 1000000000
	elif count == 5:
		if bonus_count:
			return 50000000
		else:
			return 1000000
	elif count == 4:
		return 50000
	elif count == 3:
		return 5000
	else:
		return 0


# 테스트
print(check([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6]))
print(check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25]))