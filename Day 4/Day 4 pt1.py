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
    Elf_1_start=Elf_1_range[0]
    Elf_1_end=Elf_1_range[1]
    Elf_2_start=Elf_2_range[0]
    Elf_2_end=Elf_2_range[1]
    if Elf_1_start < Elf_2_start and Elf_1_end > Elf_2_end:
        Overlaps+=1
        print(f"Overlap in pair: {Pair}")
    elif Elf_2_start < Elf_1_start and Elf_2_end > Elf_1_end:
        Overlaps+=1
        print(f"Overlap in pair: {Pair}")
    elif Elf_1_start == Elf_1_end:
        if Elf_1_start > Elf_2_start:
            Overlaps+=1
            print(f"Overlap in pair: {Pair}")
        elif Elf_1_start == Elf_2_start:
            Overlaps+=1
            print(f"Overlap in pair: {Pair}")
        elif Elf_1_end == Elf_2_end:
            Overlaps+=1
            print(f"Overlap in pair: {Pair}")
    elif Elf_2_start == Elf_2_end:
        if Elf_2_start > Elf_1_start:
            Overlaps+=1
            print(f"Overlap in pair: {Pair}")
        elif Elf_2_start == Elf_1_start:
            Overlaps+=1
            print(f"Overlap in pair: {Pair}")
        elif Elf_2_end == Elf_1_end:
            Overlaps+=1
            print(f"Overlap in pair: {Pair}")
    elif Elf_1_start == Elf_2_start:
        if Elf_1_end > Elf_2_end:
            Overlaps+=1
            print(f"Overlap in pair: {Pair}")
        elif Elf_2_end > Elf_1_end:
            Overlaps+=1
            print(f"Overlap in pair: {Pair}")
    elif Elf_1_end == Elf_2_end:
        if Elf_1_start < Elf_2_start:
            Overlaps+=1
            print(f"Overlap in pair: {Pair}")
        elif Elf_2_start < Elf_1_start:
            Overlaps+=1
            print(f"Overlap in pair: {Pair}")
print(Overlaps)