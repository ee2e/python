# 사전 (dictionary)
# key-value pair (키-값 쌍)

# my_dictionary = {
# 	5: 25,
# 	2: 4,
# 	3: 9
# }
# print(type(my_dictionary))
# print(my_dictionary[3])
# my_dictionary[9] = 81
# print(my_dictionary)

my_family = {
	'엄마': '김자옥',
	'아빠': '이석진',
	'아들': '이동민',
	'딸': '이지영'
}

# print(my_family['아빠'])

# print(my_family.values())
# print('이지영' in my_family.values())
# print('성태호' in my_family.values())
# for value in my_family.values():
# 	print(value)

# print(my_family.keys())
# for key in my_family.keys():
# 	print(key)

for key in my_family.keys():
	value = my_family[key]
	print(key, value)

for key, value in my_family.items():
	print(key, value)