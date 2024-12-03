# for each thing
# check for mul( 
# look for comma split and create 2 vars a and b
# add a*b to counter
import re
counter = 0
shouldCount = True
with open("Day_3\input.txt") as f:
    for text in f:
        for i in range(len(text)): 
            if shouldCount:      
                x = re.search("^mul\((\d+),(\d+)\)", text[i:i+12])
                if(not x==None):
                    # print(x.group())
                    l = ((re.findall("\d{1,3}", x.group())))
                    counter += int(l[0]) * int(l[1])
                # PART 2
            newX = re.search("don't\(\)", text[i:i+7])
            if(newX):
                shouldCount = False
            superNewX = not re.search("do\(\)", text[i:i+4])==None
            if(superNewX):
                shouldCount = True
print(counter)