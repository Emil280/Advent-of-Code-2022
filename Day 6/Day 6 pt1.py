Input=open("Day 6\Input.txt", "r")
Signal=Input.readline()
Found=False
Index=3
while not Found and Index != (len(Signal)-1):
        if Signal[Index] != Signal[Index-1] and Signal[Index] != Signal[Index-2] and Signal[Index] != Signal[Index-3]:
            if Signal[Index-1] != Signal[Index-2] and Signal[Index-1] != Signal[Index-3]:
                if Signal[Index-2] != Signal[Index-3]:
                    Characters_searched=Index+1
                    print(Characters_searched)
                    Found=True
        Index+=1