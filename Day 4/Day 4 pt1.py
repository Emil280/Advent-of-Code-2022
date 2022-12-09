Input=open("Day 4\Input.txt", "r")
Pairs=Input.readlines()
Overlaps=0
for Pair in Pairs:
    Pair=Pair.replace("\n","")
    Seperated_Pair=Pair.split(',')
    Elf_1=Seperated_Pair[0]
    Elf_2=Seperated_Pair[1]
    Elf_1_range=Elf_1.split('-')
    Elf_2_range=Elf_2.split('-')
    Elf_1=[]
    Elf_2=[]
    for x in range(int(Elf_1_range[0]),int(Elf_1_range[1])+1):
        Elf_1.append(x)
    for x in range(int(Elf_2_range[0]),int(Elf_2_range[1])+1):
        Elf_2.append(x)
    if Elf_2[0] in Elf_1 and Elf_2[-1] in Elf_1:
        Overlaps+=1
    elif Elf_1[0] in Elf_2 and Elf_1[-1] in Elf_2:
        Overlaps+=1
    else:
        pass
    
print(Overlaps)
