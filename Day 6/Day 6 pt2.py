Input=open("Day 6\Input.txt", "r")
Signal=Input.readline()
def In_Sector(Start,End):
    Sector=Signal[Start:End]
    for Character in Sector:
        if Sector.count(Character) > 1:
            return True
    return False

for i in range(0,(len(Signal)-14)):
    if not In_Sector(0+i,14+i):
        print(f"There is a message detected after {i+14} characters")