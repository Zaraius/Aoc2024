# go through each line
# if 2nd is > 1 ... check if all are >
# if 2nd is < 1 .. check if all are < AND check if less than 3

# list = open("Day_2\input.txt", "r")
# print("hi")
# # print(list.read())
counter = 0
with open("Day_2\input.txt") as f:
    for line in f:
        number_list = line.split()
        number_list = list(map(int, number_list))
        shouldCount = True
        shouldCountpt2 = True
        mistakes = 0
        if (number_list[0] > number_list[1]):
            for i in range(len(number_list) - 1):
                a = (number_list[i] < number_list[i+1] or ((abs(number_list[i] - number_list[i+1]) > 3) or (abs(number_list[i] - number_list[i+1]) < 1)))
                if (a and shouldCount == False):
                    shouldCountpt2 = False
                if (a):
                    shouldCount = False
                    mistakes +=1
        else:
            for i in range(len(number_list) - 1):
                a = ((number_list[i] > number_list[i+1] or ((abs(number_list[i] - number_list[i+1]) > 3) or (abs(number_list[i] - number_list[i+1]) < 1))))
                if (a and shouldCount == False):
                    shouldCountpt2 = False
                if (a):
                    shouldCount = False
                    mistakes +=1
        if(shouldCountpt2):
            counter += 1

print(counter)
# 290
