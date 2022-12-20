Input=open("Day 7\Input.txt", "r")
CMD=Input.readlines()
Names={}

class Directory_Node():
    def __init__(self,name,parent,Folder):
        setattr(self,name,name)
        self.Parent=parent 
        self.Children=[]
        self.Name=name
        self.Size=0
        if Folder: 
            self.Folder=True
            self.File=False
        elif not Folder:
            self.Folder=False 
            self.File=True

    def Set_Parent(self,parent):
        self.Parent=parent 

    def Get_Parent(self):
        return self.Parent

    def Add_Children(self,Child):
        self.Children.append(Child)
    
    def Get_Children(self):
        if self.Children:
            return self.Children
        else:
            return None

    def Is_File(self):
        self.File=True

    def Is_Folder(self):
        self.Folder=True

    def Set_Size(self,Size):
        self.Size=Size

    def Get_File_Size(self):
        if self.Size and self.File:
            return self.Size

    def Get_Folder_Size(self):
        if self.Folder:
            return self.Size

    def Calculate_Folder_Size(self):
        if self.Folder:
            Size=0
            for Child in self.Children:
                if Child.File:
                    Size=Size+(Child.Get_File_Size())
                elif Child.Folder:
                    Size=Size+(Child.Calculate_Folder_Size())
            self.Set_Size(Size)
            return Size

    def Set_Name(self,Name):
        self.Name=Name

    def Get_Name(self):
        return self.Name

    def Get_level(self):
        level=0
        Parent=self.Parent
        while Parent:
            level+=1
            Parent=Parent.Parent
        return level

    def Print_File_Structure(self):
            spaces=" " * self.Get_level()
            prefix=spaces + "--" if self.Parent else ""
            if self.Folder:
                print(prefix, self.Name, "(Dir)", self.Size)
                for Child in self.Children:
                    Child.Print_File_Structure()
            elif self.File:
                print(prefix , self.Name , " " , self.Size)

    def Sum_of_Folders_Under_100000(self):
        Total=0
        if self.Folder:
            for Child in self.Children:
                if Child.Folder:
                    Total=Total+(Child.Sum_of_Folders_Under_100000())
            if self.Get_Folder_Size() <= 100000:
                Total=Total+self.Get_Folder_Size()
            return Total


Root=Directory_Node('Root',None,True)
Root.Is_Folder()
Root.Set_Name("/")
Parent=Root
for i in range (1,(len(CMD))):
    line=CMD[i]
    line=line.replace("\n","")
    if "$" in line:
        if "cd" in line:
            if ".." in line:
                Parent=((Parent).Get_Parent())
            else:
                Name=line[5:]
                Names[Name]=Directory_Node(Name,Parent,True)
                (Parent).Add_Children((Names[Name]))
                Parent=(Names[Name])
    elif "dir" not in line:
        Size=int(line.split(" ")[0])
        File_Name=line.split(" ")[1]
        Names[File_Name]=Directory_Node(File_Name,Parent,False)
        (Parent).Add_Children(Names[File_Name])
        (Names[File_Name]).Set_Size(Size)
Root.Calculate_Folder_Size()
Root.Print_File_Structure()
No_of_Folders=Root.Sum_of_Folders_Under_100000()
print(No_of_Folders)