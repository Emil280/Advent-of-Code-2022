Input=open("Day 2\stratergy guide.txt" , "r")
Totaled=False
Index=1
Score=0
while not Totaled:
    line=Input.readline()
    if "X" in line:
        Score+=1
        if "A" in line:
            Score+=3
        elif "C":
            Score+=6
    elif "Y" in line:
        Score+=2
        if "A" in line:
            Score+=6
        elif "B":
            Score+=3
    elif "Z" in line:
        Score+=3
        if "B" in line:
            Score+=6
        elif "C" in line:
            Score+=3
    Index+=1
    if Index==len(Input.readlines()):
        Totaled=True
print(Score)