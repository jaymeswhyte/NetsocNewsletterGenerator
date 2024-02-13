import tkinter
from tkinter import filedialog
import customtkinter
from generator import generate

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

        self.dateField = customtkinter.CTkEntry(master=self, height=10, placeholder_text="Date")
        self.dateField.place(anchor="ne", relx=0.48, rely=0.02)
        self.gifField = customtkinter.CTkEntry(master=self, height=10, width=340, placeholder_text="Gif of the week Link")
        self.gifField.place(anchor="nw", relx=0.52, rely=0.02)

        self.submitButton = customtkinter.CTkButton(master=self, text="Generate", command=submit)
        self.submitButton.place(anchor="se", rely=0.98, relx=0.926)

        self.addEventButton = customtkinter.CTkButton(master=self, text="New Event", command=addEvent)
        self.addEventButton.place(anchor="ne", relx=0.48, rely=0.85)

def load():
    for widget in app.winfo_children():
        widget.destroy

    app.eventsFrame.addEventFields()
    app.eventsFrame.refresh()

def addEvent():
    global eventCounter
    eventCounter = eventCounter+1
    app.eventsFrame.addEventFields()
    app.eventsFrame.refresh()

def submit():
    eventTitleFields = app.eventsFrame.titleFields
    eventDateFields = app.eventsFrame.dateFields
    eventImageFields = app.eventsFrame.imageFields
    eventDescriptionFields = app.eventsFrame.descriptionFields

    titles = []
    dates = []
    images = []
    descriptions = []

    for i in range(eventCounter):
        titles.append(eventTitleFields[i].get())
        dates.append(eventDateFields[i].get())
        images.append(eventImageFields[i].get())
        descriptions.append(eventDescriptionFields[i].get(1.0, "end-1c"))
    
    gamingTitle = app.newsFrame.gamingTitleField.get()
    gamingImage = app.newsFrame.gamingImageField.get()
    gamingLink = app.newsFrame.gamingArticleLinkField.get()
    gamingText = app.newsFrame.gamingArticleDescriptionField.get(1.0, "end-1c")

    techTitle = app.newsFrame.techTitleField.get()
    techImage = app.newsFrame.techImageField.get()
    techLink = app.newsFrame.techArticleLinkField.get()
    techText = app.newsFrame.techArticleDescriptionField.get(1.0, "end-1c")

    date = app.dateField.get()
    gifLink = app.gifField.get()

    html = generate(date=date, gifLink=gifLink, eventDates=dates, eventTitles=titles,
                    eventImages=images, eventDescriptions=descriptions,
                    gamingTitle=gamingTitle, gamingLink=gamingLink,
                    gamingImage=gamingImage, gamingDescription=gamingText,
                    techTitle=techTitle, techLink=techLink,
                    techImage=techImage, techDescription=techText)
    
    filePath = filedialog.asksaveasfilename(defaultextension=".html", filetypes=[("HTML", "*.html"), ("Text file", "*.txt"), ("All files", "*.*")])
    if filePath:
        try:
            with open(filePath, 'w') as file:
                file.write(html)
        except Exception as e:
            app.submitButton._text = e
            


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