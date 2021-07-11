a = int(input())
b = int(input())
sum_ = 0
n = 0
for i in range(a, b + 1):
    if not i % 3:
        sum_ += i
        n += 1
print(sum_ / n)
