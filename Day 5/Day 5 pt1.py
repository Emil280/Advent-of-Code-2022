Input=open("Day 5\Input.txt", "r")
Input=Input.readlines()
Initial=Input[0:8]
Instructions=Input[10:]
Stacks=[[],[],[],[],[],[],[],[],[]]
Moves=[]

def Invert(Queue):
    Stack=[]
    for x in range(0,len(Queue)):
        Stack.append(Queue.pop())
    return Stack

def Fetch_Stacks():
    Index=1
    for line in Initial:
        while Index<34:
            if line[Index] != " ":
                Stacks[((Index-1)//4)].append(line[Index])
            Index+=4
        Index=1
    for x in range(0,9):
        Stacks[x]=Invert(Stacks[x])

def Interpret_Moves():
    for Instruction in Instructions:
        No_of_items=(Instruction.split("from"))[0]
        Movement=(Instruction.split("from"))[1]
        No_of_items=No_of_items.replace("move ","")
        From=(Movement.split("to"))[0]
        Destination=Movement.split("to")[1]
        Destination=Destination.replace("\n","")
        Key_info=[int(No_of_items),int(From),int(Destination)]
        Moves.append(Key_info)

def Do_Moves():
    for Move in Moves:
        for x in range(Move[0]):
            Stacks[Move[2]-1].append(Stacks[Move[1]-1].pop())

def Get_Message():
    Top_letters=[]
    for Stack in Stacks:
        Top_letters.append(Stack[len(Stack)-1])
    Message=''.join(Top_letters)
    return Message

Fetch_Stacks()
Interpret_Moves()
Do_Moves()
print(Get_Message())