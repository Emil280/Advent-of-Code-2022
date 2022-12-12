Input=open("Day 4\Input.txt", "r")
Pairs=Input.readlines()
Overlaps=0
for Pair in Pairs:
    Overlap=0
    Pair=Pair.replace("\n","")
    Seperated_Pair=Pair.split(',')
    Elf_1_range=Seperated_Pair[0].split('-')
    Elf_2_range=Seperated_Pair[1].split('-')
    Elf_1=[]
    Elf_2=[]
    for x in range(int(Elf_1_range[0]),int(Elf_1_range[1])+1):
        Elf_1.append(x)
    for x in range(int(Elf_2_range[0]),int(Elf_2_range[1])+1):
        Elf_2.append(x)
    for task1 in Elf_1:
        for task2 in Elf_2:
            if task1==task2: 
                Overlap+=1
    if Overlap != 0:
        Overlaps+=1
    
print(Overlaps)
