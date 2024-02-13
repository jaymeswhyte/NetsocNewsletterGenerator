import tkinter
import customtkinter
import datetime

eventCounter = 1

class MyNewsFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.gamingLabel = customtkinter.CTkLabel(self, fg_color="gray12", font=('Roboto', 18), text="This Week In Gaming")
        self.gamingLabel.pack()

        self.gamingTitleField = customtkinter.CTkEntry(master=self, width=250, height=10, placeholder_text="Article Title")
        self.gamingTitleField.pack(pady=2)

        self.gamingImageField = customtkinter.CTkEntry(master=self, width=250, height=10, placeholder_text="Article Image Link")
        self.gamingImageField.pack(pady=2)

        self.gamingArticleLinkField = customtkinter.CTkEntry(master=self, width=250, height=10, placeholder_text="Article URL")
        self.gamingArticleLinkField.pack(pady=2)

        self.gamingArticleDescriptionField = customtkinter.CTkTextbox(master=self, width=300, height=200, fg_color="gray15", border_color="gray25", border_width=2.5)
        self.gamingArticleDescriptionField.pack(pady=2)
        self.gamingArticleDescriptionField.insert(index="0.0", text="Article One-Liner")

        self.techLabel = customtkinter.CTkLabel(self, fg_color="gray12", font=('Roboto', 18), text="This Week In Tech")
        self.techLabel.pack(pady=(30, 0))

        self.techTitleField = customtkinter.CTkEntry(master=self, width=250, height=10, placeholder_text="Article Title")
        self.techTitleField.pack(pady=2)

        self.techImageField = customtkinter.CTkEntry(master=self, width=250, height=10, placeholder_text="Article Image Link")
        self.techImageField.pack(pady=2)

        self.techArticleLinkField = customtkinter.CTkEntry(master=self, width=250, height=10, placeholder_text="Article URL")
        self.techArticleLinkField.pack(pady=2)

        self.techArticleDescriptionField = customtkinter.CTkTextbox(master=self, width=300, height=200, fg_color="gray15", border_color="gray25", border_width=2.5)
        self.techArticleDescriptionField.pack(pady=2)
        self.techArticleDescriptionField.insert(index="0.0", text="Article One-Liner")

class MyEventsFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.dateFields = []
        self.titleFields = []
        self.imageFields = []
        self.descriptionFields = []

        self.eventsLabel = customtkinter.CTkLabel(self, fg_color="gray12", font=('Roboto', 18), text="This Week's Events")
        self.eventsLabel.pack()

    def addEventFields(self):
        self.newDateField = customtkinter.CTkEntry(master=self, width=250, height=10, placeholder_text=f"Event #{eventCounter} Date")
        self.dateFields.append(self.newDateField)

        self.newTitleField = customtkinter.CTkEntry(master=self, width=250, height=10, placeholder_text=f"Event #{eventCounter} Title")
        self.titleFields.append(self.newTitleField)

        self.newImageField = customtkinter.CTkEntry(master=self, width=250, height=10, placeholder_text=f"Event #{eventCounter} Image Link")
        self.imageFields.append(self.newImageField)

        self.newDescriptionField = customtkinter.CTkTextbox(master=self, width=300, height=200, fg_color="gray15", border_color="gray25", border_width=2.5)
        self.newDescriptionField.insert("0.0", text="Event Description")
        self.descriptionFields.append(self.newDescriptionField)

    def refresh(self):
        for i in range(0, eventCounter):
            yPad = 2
            if i != 0:
                yPad=50
            self.dateFields[i].pack(pady=(yPad, 2))
            self.titleFields[i].pack(pady=2)
            self.imageFields[i].pack(pady=2)
            self.descriptionFields[i].pack(pady=2)
    
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.eventsFrame = MyEventsFrame(master=self, width=500, height=500, corner_radius=10, fg_color="gray12")
        self.eventsFrame.place(anchor='ne', relx=0.48, rely=0.1)

        self.newsFrame = MyNewsFrame(master=self, width=500, height=500, corner_radius=10, fg_color="gray12")
        self.newsFrame.place(anchor='nw', relx=0.52, rely=0.1)

def load():
    for widget in app.winfo_children():
        widget.destroy

    dateField = customtkinter.CTkEntry(app, height=10, placeholder_text="Date")
    dateField.place(anchor="ne", relx=0.48, rely=0.02)
    gifField = customtkinter.CTkEntry(app, height=10, width=340, placeholder_text="Gif of the week Link")
    gifField.place(anchor="nw", relx=0.52, rely=0.02)

    submitButton = customtkinter.CTkButton(app, text="Generate")
    submitButton.place(anchor="se", rely=0.98, relx=0.926)

    addEventButton = customtkinter.CTkButton(app, text="New Event", command=addEvent)
    addEventButton.place(anchor="ne", relx=0.48, rely=0.85)
    app.eventsFrame.addEventFields()
    app.eventsFrame.refresh()

def addEvent():
    global eventCounter
    eventCounter = eventCounter+1
    app.eventsFrame.addEventFields()
    app.eventsFrame.refresh()

if __name__ == "__main__":
    # Settings
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")

    # Run
    app=App()
    load()

    # Display
    app.geometry("1280x720")
    app.title("Netsoc Newsletter")
    app.mainloop()