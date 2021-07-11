num_list = []
while True:
    num = int(input())
    if num == 55:
        break
    num_list.append(num)
print(len(num_list))
print(sum(num_list))
print(round(sum(num_list) / len(num_list)))
