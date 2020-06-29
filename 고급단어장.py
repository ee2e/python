with open('data/vocabulary.txt', 'r', encoding='UTF-8') as f:
	word_dict = {}; num = 1
	for line in f:
		data = line.strip().split(': ')
		word_dict[num] = data
		num += 1

import random

while True:
	random_num = random.randint(1,num-1)
	data = word_dict[random_num]
	english = input(f'{data[1]}: ')
	if english == 'q':
		break
	elif english == data[0]:
		print('맞았습니다!\n')
	else:
		print(f'아쉽습니다. 정답은 {data[0]}입니다.\n')