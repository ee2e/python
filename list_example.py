# # 리스트 (list)
# numbers = [2, 3, 5, 7, 11, 13]
# names = ['윤수', '혜린', '태호', '영훈']
#
# # numbers[0] = 7
# # print(numbers)
# numbers[0] = numbers[0] + numbers[1]
# print(numbers)


# # 인덱싱 (indexing)
# print(names[1])
# print(numbers[1] + numbers[3])
# num_1 = numbers[1]
# num_2 = numbers[3]
# print(num_1 + num_2)
# # print(numbers[6])   # IndexError: list index out of range
# print(numbers[-1])
# print(numbers[-2])
# print(numbers[-6])


# # 리스트 슬라이싱 (list slicing)
# print(numbers[0:3])
# print(numbers[2:])
# print(numbers[:3])
# new_list = numbers[:3]  # [2, 3, 5]
# print(new_list[2])


# numbers = []
# print(len(numbers))
# numbers.append(5)
# numbers.append(8)
# print(numbers)
# print(len(numbers))


# numbers = [2, 3, 5, 7, 11, 13, 17, 19]
# # del numbers[3]
# # print(numbers)
# numbers.insert(4, 37)
# print(numbers)


numbers = [19, 13, 2, 5, 3, 11, 7, 17]
# # sorted : 기존 리스트는 건드리지 않고, 정렬된 새로운 리스트를 리턴
# new_list = sorted(numbers)
# print(new_list)
# new_list = sorted(numbers, reverse=True)
# print(new_list)
# print(numbers)
# sort : 아무것도 리턴하지 않고, 기존 리스트를 정렬
# print(numbers.sort())   # .sort()는 아무것도 return 하지 않음
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)