input=open("Day 1\elf_calories.txt", "r")
Totaled=False
index=0
Elf_calories=[]
Sum=0
Elf_num=1
Highest_calorie_elf=[0,0]
while Totaled==False:
    line=input.readline()
    if line.strip():
        Sum+=int(line)
    else:
        Elf_calories.insert(Elf_num,[Elf_num,Sum])
        Elf_num+=1
        Sum=0
    index+=1
    if index==2255:
        Totaled=True

for x in range(0,len(Elf_calories)):
    if Elf_calories[x][1] > Highest_calorie_elf[1]:
        Highest_calorie_elf=Elf_calories[x]

print(Highest_calorie_elf[1])