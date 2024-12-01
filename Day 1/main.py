from collections import Counter
# PART 1
list1 = open("Day 1\Inputs1.txt", "r")
list2 = open("Day 1\Inputs2.txt", "r")
sorted1 = sorted(list1)
sorted2 = sorted(list2)
total = 0
for i in range(1000):
    total = total + abs(int(sorted1[i]) - int(sorted2[i]))
print(total)
# PART 2
similarty = 0
print(Counter(sorted1))

for i in range(1000):
    count = 0
    for j in range(1000):
        count += int(sorted1[i]) == int(sorted2[j])
    similarty += int(sorted1[i]) * count
print(similarty)

    