Input=open("Day 2\stratergy guide.txt" , "r")
Input=Input.readlines()
Score=0
for n in range (len(Input)):
    line=Input[n]
    if "X" in line:
        Score+=1
        if "A" in line:
            Score+=3
        elif "C" in line:
            Score+=6
    elif "Y" in line:
        Score+=2
        if "A" in line:
            Score+=6
        elif "B" in line:
            Score+=3
    elif "Z" in line:
        Score+=3
        if "B" in line:
            Score+=6
        elif "C" in line:
            Score+=3
print(Score)