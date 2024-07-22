import customtkinter
import json
from textProcessing import returnPatientDataAsList, processjson
import sys
sys.path.append("/Users/micahbassett/Desktop/testingUI/backend")
from engine.engine import Engine

"""
This class will be a container class and controller for the pages. Each frame class will be initialised 
so that the controller is assigned to this mainApp class. The showPage method will allow pages to be called to user. 
"""

class MainApp(customtkinter.CTk):

    def __init__(self, *args, **kwargs):
        customtkinter.CTk.__init__(self, *args, **kwargs)

        self.title("Davinci Testing Suite")
        self.geometry("600x450")

        # container to store pages of the gui
        container = customtkinter.CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # dictionary to store the pages
        self.frames = {}

        # adding frames

        self.frames["StartPage"] = StartPage(parent=container, controller=self)
        self.frames["StartPage"].grid(row=0, column=0, sticky="nsew")

        self.frames["RunTests"] = RunTests(parent=container, controller=self)
        self.frames["RunTests"].grid(row=0,column=0,sticky="nsew")

        self.showPage("StartPage")

    def showPage(self, pageName):
        frame = self.frames[pageName]
        frame.tkraise()

class StartPage(customtkinter.CTkFrame):

    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)

        self.grid_columnconfigure(0, weight=1)
        #self.grid_rowconfigure(0, weight=1)

        self.controller = controller

        # BUTTONS
        RunTests = customtkinter.CTkButton(self, text="Run New Tests", command=lambda: controller.showPage("RunTests"))

        # packing buttons
        RunTests.grid(row=0,column=0,padx=10,pady=(10,10),sticky="")

# TODO Add code to display results and logic for checkbuttons
class RunTests(customtkinter.CTkFrame):

    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        
        # the number of checkbox options
        self.options = 6

        # setting row and column configurations
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1,weight=1)
        
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2,weight=1)

        # set the controller (the parent window passed in)
        self.controller = controller

        self.DAISY = Engine()

        """
        PATIENT TEXTBOX
        """

        # label for patient data textbox
        self.patientDataLabel = customtkinter.CTkLabel(self, text="Patient Data")
        self.patientDataLabel.grid(row=0, column=0,padx=10,pady=(10,10),sticky="nsew")        

        # TODO get this richtextbox functional 
        # patient data textbox
        self.patientDataTextbox = RichTextbox(self)
        self.patientDataTextbox.grid(row=1,column=0,rowspan=self.options,padx=10,pady=(10,10), sticky="nsew")

        """
        DAVINCI OUTPUT
        """

        # label for output
        self.davinciOutputLabel = customtkinter.CTkLabel(self, text="Davinci Output")
        self.davinciOutputLabel.grid(row=0, column=1,padx=10,pady=(10,10),sticky="nsew")

        # output textbox for davinci
        self.davinciOutputTextbox = RichTextbox(self)
        self.davinciOutputTextbox.grid(row=1,column=1,rowspan=self.options,padx=10,pady=(10,10),sticky="nsew")

        """
        CHECKBOXES AND BUTTONS
        """

        self.resultsLabel = customtkinter.CTkLabel(self, text="Options")
        self.resultsLabel.grid(row=0,column=2,padx=10,pady=(10,10), sticky="nsew")

        # TODO
        # OPTION 1
        self.stableCheckbox = customtkinter.CTkCheckBox(self,text="Check this box if the test is valid")
        self.stableCheckbox.grid(row=1,column=2,padx=10,pady=(10,10),sticky="ew")

        # TODO
        # OPTION 2
        self.saveTestCheckbox = customtkinter.CTkCheckBox(self, text="Check to save test")
        self.saveTestCheckbox.grid(row=2,column=2,padx=10,pady=(10,10),sticky="ew")

        # TODO
        # OPTION 3
        self.runDAISYButton = customtkinter.CTkButton(self, text="Run DAISY")
        self.runDAISYButton.grid(row=3,column=2,padx=10,pady=(10,10),sticky="nsew")

        # OPTION 4
        self.nextTestButton = customtkinter.CTkButton(self,text="Next Test")
        self.nextTestButton.grid(row=4,column=2,padx=10,pady=(10,10),sticky="nsew")

        # OPTION 5
        self.previousTestButton = customtkinter.CTkButton(self,text="Previous Test")
        self.previousTestButton.grid(row=5,column=2,padx=10,pady=(10,10),sticky="nsew")

        # OPTION 6
        self.exitButton = customtkinter.CTkButton(self,text="Exit",command=lambda: controller.showPage("StartPage"))
        self.exitButton.grid(row=6,column=2,padx=10,pady=(10,10), sticky="nsew")
 
"""
This class inherits from Textbox and provides additional methods to process and format text to be displayed
"""
# TODO finish implementing this class
class RichTextbox(customtkinter.CTkTextbox):
    def __init__(self,parent):
        customtkinter.CTkTextbox.__init__(self, parent)

        # here we configure and add the tags needed for formatting the text

    # takes a list of text
    def insertText(self,text):
        for info in text:
            self.insert("end", info + "\n")
            # this is a heading
            if ":" not in info:
                self.insert("end", "\n")

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()