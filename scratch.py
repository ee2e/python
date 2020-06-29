print('Hello\n')
print('Hello')

# strip : 화이트 스페이스(' ', '\t', '\n')를 없애줌
print('           abc   def    '.strip())
print('       \t   \n   abc   def\n\n\n'.strip())


# split
my_string = '1. 2. 3. 4. 5. 6'
print(my_string.split('. '))

full_name = 'Kim, Yuna'
name_data = full_name.split(', ')
last_name = name_data[0]
first_name = name_data[1]
print(first_name, last_name)

numbers = '    \n\n   2    \t    3   \n  5 7 11   \n\n'.split()
print(numbers[0] + numbers[1])  # split을 이용하면 문자로 저장됨
print(int(numbers[0]) + int(numbers[1]))