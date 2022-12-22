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

    def Find_Folders_For_Deletion(self,TargetSize):
        Folders=[]
        if self.Folder:
            for Child in self.Children:
                if Child.Folder:
                    if Child.Get_Folder_Size() >= TargetSize:
                        Folders_in_Child=Child.Find_Folders_For_Deletion(TargetSize)
                        for Folder in Folders_in_Child:
                            Folders.append(Folder)
            if self.Get_Folder_Size() >= TargetSize:
                Folders.append(self)
            return Folders

    def Select_Folder_For_Deletion(self,Folders):
        Sorted_Folders = sorted(Folders, key=lambda x: x.Size)
        Folder_To_Delete=Sorted_Folders[0]
        return Folder_To_Delete

    def Free_Up_Space(self,TargetSize):
        Potential_Target_Folders=self.Find_Folders_For_Deletion(TargetSize)
        Folder=self.Select_Folder_For_Deletion(Potential_Target_Folders)
        print(f"Delete directory named : {Folder.Name} to free up {Folder.Size}")

#Setting up Root node (/)
Root=Directory_Node('Root',None,True)
Root.Is_Folder()
Root.Set_Name("/")
Parent=Root

#Adding all nodes to the Tree
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

#Calculating the Size of all the folders
Root.Calculate_Folder_Size()


Root.Print_File_Structure()
Free_Storage=70000000-Root.Get_Folder_Size()
Storage_Needed=-(Free_Storage-30000000)
Root.Free_Up_Space(Storage_Needed)