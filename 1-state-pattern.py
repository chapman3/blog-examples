class App(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.setting = None
        self.initGUI()

    def initGUI(self):
        self.parent.title("Shopify Product Updating")
        self.pack(fill=BOTH, expand=1)
        self.parent.addCButton = Checkbutton(self, text="Add Product", command=self.addCB)
        self.parent.addCButton.place(relx=0.2, rely=0.5, anchor=CENTER)
        self.parent.editCButton = Checkbutton(self, text="Edit Product", command=self.editCB)
        self.parent.editCButton.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.parent.deleteCButton = Checkbutton(self, text="Delete Product", command=self.deleteCB)
        self.parent.deleteCButton.place(relx=0.8, rely=0.5, anchor=CENTER)

    def addCB(self):
        if(self.setting == None):
            self.setting = "Add"
        elif(self.setting is not "Add"):
            self.parent.deleteCButton.deselect()
            self.parent.editCButton.deselect()
            self.setting = "Add"
        else:
            self.setting = None
        print(self.setting)

    def editCB(self):
        if(self.setting == None):
            self.setting = "Edit"
        elif(self.setting is not "Edit"):
            self.parent.addCButton.deselect()
            self.parent.deleteCButton.deselect()
            self.setting = "Edit"
        else:
            self.setting = None
        print(self.setting)

    def deletCB(self):
        if(self.setting == None):
            self.setting = "Delete"
        elif(self.setting is not "Delete"):
            self.parent.addCButton.deselect()
            self.parent.editCButton.deselect()
            self.setting = "Delete"
        else:
            self.setting = None
        print(self.setting)
