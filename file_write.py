# with open('data/new_file.txt', 'w') as f:   # 'w': 덮어쓰기
# 	f.write('Hello world!\n')
# 	f.write('My name is Codeit.\n')

with open('data/new_file.txt', 'a') as f:   # 'a'(append): 파일 있으면 생성, 없으면 추가
	f.write('Hello world!\n')
	f.write('My name is Codeit.\n')