####################  IMPORTS  #######################
from tkinter import *
from tkinter import ttk

####################  Class Code  #######################
# Create the account class
class Spell_Info:
    """The spell info class stores information about each individual day and has methods to determine if spell 5 is on"""
 
    def __init__(self, subject, teacher_name, teacher_code, start_time , end_time):
        self._subject = subject
        self._start_time = start_time
        self._end_time = end_time
        self._teacher_name = teacher_name
        self._teacher_code = teacher_code
    
    # initializer/constructor
    @property
    def subject(self) -> str:
        return self._subject
    @property
    def start_time(self):
        return self._start_time
    @property
    def end_time(self):
        return self._end_time
    @property
    def teacher_name(self):
        return self._teacher_name
    @property
    def teacher_code(self):
        return self._teacher_code
    @property
    def day(self):
        return self._day

    def __str__(self):
        info = self._subject + "\n" + self._teacher_name + "\n" + self._teacher_code + "\n" + self._start_time + "\n" + self._end_time
        return info
        
      

####################  Functions And Setup  #######################
monday_spells = [Spell_Info("Biology", "Jan Sydlowski", "SJA", "8:45", "9:45"), Spell_Info("English", "Grace Howarth", "HGR", "9:45", "10:45"), Spell_Info("Math", "Alex Marull", "MAL", "11:15", "12:15"), Spell_Info("Free", "N/A", "N/A", "12:15", "1:15"), Spell_Info("Free", "N/A", "N/A", "2:10", "3:10")]

tuesday_spells = [Spell_Info("Business", "Te Mahia Millanta", "MTE", "9:30", "10:25"), Spell_Info("Biology", "Jan Sydlowski", "SJA", "10:25", "11:20"), Spell_Info("Digital", "Tatiana Voropaeva", "VTA", "11:45", "12:40"), Spell_Info("English", "Grace Howarth", "HGR", "12:40", "1:35"), Spell_Info("English", "Grace Howarth", "HGR", "2:15", "3:10")]

wednesday_spells = [Spell_Info("Free", "N/A", "N/A", "8:45", "9:40"), Spell_Info("Digital", "Tatiana Voropaeva", "VTA", "9:40", "10:35"), Spell_Info("Digital", "Tatiana Voropaeva", "VTA", "11:00", "11:55"), Spell_Info("Math", "Alex Marull", "MAL", "12:30", "1:25"), Spell_Info("Free", "N/A", "N/A", "2:15", "3:15")]

thursday_spells =[Spell_Info("English", "Grace Howarth", "HGR", "8:45", "9:45"), Spell_Info("Business", "Te Mahia Millanta", "MTE", "9:45", "10:45"), Spell_Info("Business", "Te Mahia Millanta", "MTE", "11:15", "12:15"), Spell_Info("Biology", "Jan Sydlowski", "SJA", "12:15", "1:15"), Spell_Info("Biology", "Jan Sydlowski", "SJA", "2:10", "3:10")]

friday_spells = [Spell_Info("Free", "N/A", "N/A", "8:45", "9:40"), Spell_Info("Math", "Alex Marull", "MAL", "9:40", "10:35"), Spell_Info("Math", "Alex Marull", "MAL", "11:00", "11:55"), Spell_Info("Business", "Te Mahia Millanta", "MTE", "12:30", "1:25"), Spell_Info("Digital","Tatiana Voropaeva", "VTA", "2:15", "3:10")]

time_table = {"Monday":monday_spells, "Tuesday":tuesday_spells, "Wednesday":wednesday_spells, "Thursday":thursday_spells, "Friday":friday_spells}


#################### GUI Code  #######################
root = Tk()
root.title("Timetable")
global spell_one_text
global spell_two_text
global spell_three_text
global spell_four_text
global spell_five_text

def day_clicked(day):
    if day == "Monday":
        spell_one_text.set("Spell One:\n" + str(time_table["Monday"][0]))
        spell_two_text.set("Spell Two:\n" + str(time_table["Monday"][1]))
        spell_three_text.set("Spell Three:\n" + str(time_table["Monday"][2]))
        
        spell_four_text.set("Spell Four:\n" + str(time_table["Monday"][3]))
        
        spell_five_text.set("Spell Five:\n" + str(time_table["Monday"][4]))
        
    elif day == "Tuesday":
        spell_one_text.set("Spell One:\n" + str(time_table["Tuesday"][0]))
        spell_two_text.set("Spell Two:\n" + str(time_table["Tuesday"][1]))
        spell_three_text.set("Spell Three:\n" + str(time_table["Tuesday"][2]))
        
        spell_four_text.set("Spell Four:\n" + str(time_table["Tuesday"][3]))
        
        spell_five_text.set("Spell Five:\n" + str(time_table["Tuesday"][4]))

    elif day == "Wednesday":
        spell_one_text.set("Spell One:\n" + str(time_table["Wednesday"][0]))
        spell_two_text.set("Spell Two:\n" + str(time_table["Wednesday"][1]))
        spell_three_text.set("Spell Three:\n" + str(time_table["Wednesday"][2]))
        
        spell_four_text.set("Spell Four:\n" + str(time_table["Wednesday"][3]))
        
        spell_five_text.set("Spell Five:\n" + str(time_table["Wednesday"][4]))

    elif day == "Thursday":
        spell_one_text.set("Spell One:\n" + str(time_table["Thursday"][0]))
        spell_two_text.set("Spell Two:\n" + str(time_table["Thursday"][1]))
        spell_three_text.set("Spell Three:\n" + str(time_table["Thursday"][2]))
        
        spell_four_text.set("Spell Four:\n" + str(time_table["Thursday"][3]))
        
        spell_five_text.set("Spell Five:\n" + str(time_table["Thursday"][4]))

    elif day == "Friday":
        spell_one_text.set("Spell One:\n" + str(time_table["Friday"][0]))
        spell_two_text.set("Spell Two:\n" + str(time_table["Friday"][1]))
        spell_three_text.set("Spell Three:\n" + str(time_table["Friday"][2]))
        
        spell_four_text.set("Spell Four:\n" + str(time_table["Friday"][3]))
        
        spell_five_text.set("Spell Five:\n" + str(time_table["Friday"][4]))
# Create the top frame
top_frame = ttk.LabelFrame(root, text = "Ethan's Timetable")
top_frame.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

# Create and set the text variable
welcome_text = StringVar()
welcome_text.set("Welcome!\nClick on a day to display that days timetable.")

# Create a frame for welcoming
welcome_label =ttk.Label(top_frame, textvariable=welcome_text, wraplength=200)
welcome_label.grid(row=10, column=10, columnspan=2, padx=10, pady=10)


button_frame = ttk.Frame(root)
button_frame.grid(row=0, column=10)
#Create text for monday
monday_text = StringVar()
monday_text.set("Monday")

#create a monday button
monday_button = Button(button_frame, textvariable=monday_text, width =8, height=3, bg="orange", fg="black",command = lambda: day_clicked(monday_text.get()))
monday_button.grid(row=10, column=30)

# Create text for tuesday
tuesday_text = StringVar()
tuesday_text.set("Tuesday")

#create a tuesday button
tuesday_button = Button(button_frame, textvariable=tuesday_text, width =8, height=3, bg="orange", fg="black", command = lambda: day_clicked(tuesday_text.get()))
tuesday_button.grid(row=10, column=40)

# Create text for the wednesday button
wednesday_text = StringVar()
wednesday_text.set("Wednesday")

#Create a wednesday button
wednesday_button = Button(button_frame, textvariable=wednesday_text, width =8, height=3, bg="orange", fg="black", command = lambda: day_clicked(wednesday_text.get()))
wednesday_button.grid(row=10, column=50)

# Create text for the thursday button
thursday_text = StringVar()
thursday_text.set("Thursday")

#Create a thursday button
thursday_button = Button(button_frame, textvariable=thursday_text, width =8, height=3, bg="orange", fg="black", command = lambda: day_clicked(thursday_text.get()))
thursday_button.grid(row=10, column=60)

# Create text for the friday button
friday_text = StringVar()
friday_text.set("Friday")

#Create a friday button
friday_button = Button(button_frame, textvariable=friday_text, width =8, height=3, bg="orange", fg="black", command = lambda: day_clicked(friday_text.get()))
friday_button.grid(row=10, column=70)

spell_frame = ttk.Frame(root)
spell_frame.grid(row=30, column=10)

spell_one_frame = Frame(spell_frame, width=8, height=1, borderwidth=5, bg="black")
spell_one_frame.grid(row=1, column=1)
spell_one_text = StringVar()
spell_one_text.set("Spell One:")
spell_one_title = Label(spell_one_frame, textvariable=spell_one_text)
spell_one_title.grid(row=35, column=5)

spell_two_frame = Frame(spell_frame, width=8, height=1, borderwidth=5, bg="black")
spell_two_frame.grid(row=1, column=5)
spell_two_text = StringVar()
spell_two_text.set("Spell Two:")
spell_two_title = Label(spell_two_frame, textvariable=spell_two_text)
spell_two_title.grid(row=30, column=11)

spell_three_frame = Frame(spell_frame, width=8, height=1, borderwidth=5, bg="black")
spell_three_frame.grid(row=1, column=10)
spell_three_text = StringVar()
spell_three_text.set("Spell Three:")
spell_three_title = Label(spell_three_frame, textvariable=spell_three_text)
spell_three_title.grid(row=1, column=10)

spell_four_frame = Frame(spell_frame, width=8, height=1, borderwidth=5, bg="black")
spell_four_frame.grid(row=1, column=15)
spell_four_text = StringVar()
spell_four_text.set("Spell Four:")
spell_four_title = Label(spell_four_frame, textvariable=spell_four_text)
spell_four_title.grid(row=1, column=10)

spell_five_frame = Frame(spell_frame, width=8, height=1, borderwidth=5, bg="black")
spell_five_frame.grid(row=1, column=20)
spell_five_text = StringVar()
spell_five_text.set("Spell Five:")
spell_five_title = Label(spell_five_frame, textvariable=spell_five_text)
spell_five_title.grid(row=1, column=10)
# Run the mainloop
root.mainloop()
