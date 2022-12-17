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
        if self.Parent:
            return self.Parent
        else:
            return None

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
            Size=0
            for Child in self.Children:
                Size=Size+(Child.Get_File_Size())
            return Size
        return 0

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
            if self.File:
                print(prefix , self.Name , " " , self.Size)
            elif self.Folder:
                print(prefix + self.Name)
                for Child in self.Children:
                    Child.Print_File_Structure()


Root=Directory_Node('Root',None,True)
Root.Is_Folder()
Root.Set_Name("/")
Parent=Root
for i in range (1,(len(CMD))):
    line=CMD[i]
    line=line.replace("\n","")
    if "dir" in line:
            Folder_Name=line[4:]
            if Folder_Name not in Names: 
                if Names[Folder_Name] not in (Parent).Children:
                    Names[Folder_Name]=Directory_Node(Name,Parent,True)
                    (Parent).Add_Children((Names[Folder_Name]))
    elif "$" in line:
        if "cd" in line:
            if ".." in line:
                Parent=(Names[Name]).Get_Parent()
            else:
                Name=line[5:]
                Names[Name]=Directory_Node(Name,Parent,True)
                (Parent).Add_Children((Names[Name]))
                Parent=Names[Name]
    else:
        Size=line.split(" ")[0]
        File_Name=line.split(" ")[1]
        Names[File_Name]=Directory_Node(File_Name,Parent,False)
        (Parent).Add_Children(Names[File_Name])
        (Names[File_Name]).Set_Size(Size)
Root.Print_File_Structure()