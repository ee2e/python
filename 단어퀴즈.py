with open('data/vocabulary.txt', 'r', encoding='UTF-8') as f:
	for line in f:
		data = line.strip().split(': ')
		english = input(f'{data[1]}: ')
		if english == data[0]:
			print('맞았습니다!')
		else:
			print(f'아쉽습니다. 정답은 {data[0]}입니다.')