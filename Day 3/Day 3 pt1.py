Input=open("Day 3\Rucksacks.txt" , "r")
Rucksacks=Input.readlines()
Sum=0
for Rucksack in Rucksacks:
    Num_of_items=len(Rucksack) 
    Midpoint=Num_of_items//2
    Compartment1=Rucksack[:Midpoint]
    Compartment2=Rucksack[Midpoint:]
    for letter1 in Compartment1:
        for letter2 in Compartment2:
            if letter1==letter2:
                Common_element=letter1
                if Common_element.isupper():
                    Priority=(ord(Common_element))-38
                else:
                    Priority=(ord(Common_element))-96
    Sum=Sum+Priority 
print(Sum)