Input=open("Day 3\Rucksacks.txt" , "r")
Rucksacks=Input.readlines()
Sum=0
Index=0
while Index != len(Rucksacks):
    Rucksack_1=Rucksacks[Index]
    Rucksack_2=Rucksacks[Index+1]
    Rucksack_3=Rucksacks[Index+2]
    for letter1 in Rucksack_1:
        if letter1.strip():
            for letter2 in Rucksack_2:
                if letter2.strip():
                    if letter1==letter2:
                        for letter3 in Rucksack_3:
                            if letter1==letter3:
                                Group_letter=letter3
                                if Group_letter.isupper():
                                    Priority=(ord(Group_letter))-38
                                elif not Group_letter.isupper():
                                    Priority=(ord(Group_letter))-96
    Sum=Sum+Priority
    Index+=3
print(Sum)