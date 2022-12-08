Input=open("Day 3\Rucksacks.txt" , "r")
Rucksacks=Input.readlines()
Sum=0
for Rucksack in Rucksacks:
    Num_of_items=len(Rucksack) 
    Midpoint=(Num_of_items-1)//2
    Compartment1=Rucksack[:Midpoint]
    Compartment2=Rucksack[Midpoint:]
    for letter1 in range(Midpoint):
        for letter2 in range(Midpoint):
            if Compartment1[letter1]==Compartment2[letter2]:
                Common_element=Compartment1[letter1]
                if Common_element.isupper():
                    Priority=(ord(Common_element))-38
                else:
                    Priority=(ord(Common_element))-96
    Sum=Sum+Priority 
print(Sum)