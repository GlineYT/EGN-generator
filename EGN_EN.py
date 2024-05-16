#Imports
from tkinter import * 
#!This is the english version of the GUI, actual calculations happend in the EGN_calculator.py file
#^Utility
#set TK() as tk
tk = Tk()
#Title, window size and background
tk.title("EGN GENERATOR - EN VERSION // ЕГН ГЕНЕРАТОР - АНГЛИЙСКА ВЕРСИЯ")
tk.geometry("1920x1080")
tk.configure(bg="#333")

#!GUI elements start from here
#^About
About = Label(tk, text = "EGN/UCN GENERATOR",
    fg="#FFDB51", 
    bg="#216CEC", 
    font=" Arial, 50",
    width=100,
      )
#Placement
About.grid()
About.place(
    relx = 0.5,
    rely = 0.03,
    anchor="center"
)

#^The exit button
#destroys the window upon invoked (button clicked)
def exit_clicked():
    tk.destroy()

#The graphical definitions for the exit button
exit = Button(
    tk, 
    text="QUIT", 
    command=exit_clicked,
    activebackground="#444", 
    activeforeground="#F00",
    anchor="center",
    justify="center",
    bg="#222",
    cursor="hand2",
    fg="#E94A4A",
    font=("Arial", 30),
    highlightbackground="#444",
    padx=10,
    pady=5,
    width=15,
    )

#graphical placement
exit.grid()
#bottom left
exit.place(
    relx=0.001,
    rely=0.995,
    anchor="sw"
)

#^The definitions for the button responsible for getting the datas, and sending them over to EGN_Calculator
def Submit():
    global year
    year = EnterYear.get()
    global month
    month = EnterMonth.get()
    global day
    day = EnterDay.get()
    global Province
    Province = EnterProvince.get()

    #!debug print commands. Delete later
    print(year)
    print(month)
    print(day)
    print("Female", Female)
    print("Male", Male)
    print(Province)


#^D.O.B input
#*The definitons for the variables that will store the strings for the D.O.B
#*(will be converted to int later in the EGN_Calculator.py file)
EnterYear = StringVar()
EnterMonth = StringVar()
EnterDay = StringVar()
#year
EnterYear = Entry(  
    tk,
    bg="#222",
    fg="#FFDB51",
    font=("arial", 30),
    width=30,
    textvariable= EnterYear,
)

#month
EnterMonth = Entry(  
    tk,
    bg="#222",
    fg="#FFDB51",
    font=("arial", 30),
    width=30,
    textvariable= EnterMonth,
)

#day
EnterDay = Entry(  
    tk,
    bg="#222",
    fg="#FFDB51",
    font=("arial", 30),
    width=30,
    textvariable= EnterDay,
)

#^The button for submitting
Submit = Button(
    tk, 
    text="GENERATE", 
    command=Submit,
    activebackground="#444", 
    activeforeground="#FFFF00",
    anchor="center",
    justify="center",
    bg="#222",
    cursor="hand2",
    disabledforeground="black",
    fg="#FFDB51",
    font=("Arial", 30),
    highlightbackground="#444",
    padx=10,
    pady=5,
    width=15,
     )

#The placement for the submit button
Submit.grid()
Submit.place(
    relx=0.5,
    rely= 0.965,
    anchor="center",
)

#^Input placements for the D.O.B
#Input field for the Year
EnterYear.grid()
EnterYear.place(
    relx=0.001,
    rely= 0.075,
    anchor="nw"
)

#Input field for the Month
EnterMonth.grid()
EnterMonth.place(
    relx=0.001,
    rely= 0.125,
    anchor="nw"
)

#The input field for the Day
EnterDay.grid
EnterDay.place(
    relx=0.001,
    rely=0.175,
    anchor="nw",    #! Debug print command, delete later
)
#^ The labels for the D.O.B 
#* Label for the year
YearLabel = Label(
    tk, 
    text = "YEAR OF BIRTH",
    fg="#216CEC", 
    bg="#333", 
    font=" Arial, 30" )
#Placement
YearLabel.grid()
YearLabel.place(
    relx=0.35,
    rely=0.075,
    anchor="nw"
)
#*Label for the month
MonthLabel = Label(
    tk, 
    text = "MONTH OF BIRTH",
    fg="#216CEC", 
    bg="#333", 
    font=" Arial, 30" )
MonthLabel.grid()
MonthLabel.place(
    relx=0.35,
    rely=0.125,
    anchor="nw"
)

#Label for the month
DayLabel = Label(
    tk, 
    text = "DAY OF BIRTH",
    fg="#216CEC", 
    bg="#333", 
    font=" Arial, 30" )
DayLabel.grid()
DayLabel.place(
    relx=0.35,
    rely=0.175,
    anchor="nw"
)

#^Gender selection
#Variables for the genders, by default set to "False"
Male = False
Female = False

#*definitions for the buttons

#definiton for male
def MaleButton():
    global Male
    Male = True
    global Female
    Female = False
    #! Debug print commands, delete later
    print("Male", Male)
    print("Female", Female)

#definitons for female
def FemaleButton():
    Female = True
    Male = False
#&Buttons for genders
#*Male
MaleButton = Button(
    tk, 
    text="MALE", 
    command=MaleButton,
    activebackground="#444", 
    activeforeground="#FFFF00",
    anchor="center",
    justify="center",
    bg="#222",
    cursor="hand2",
    disabledforeground="black",
    fg="#FFDB51",
    font=("Arial", 30),
    highlightbackground="#444",
    padx=10,
    pady=5,
    width=15,
)

#placement
MaleButton.grid()
MaleButton.place(
    relx=0.001,
    rely=0.275,
    anchor="nw",
)

#*Female
FemaleButton = Button(
    tk, 
    text="FEMALE", 
    command=FemaleButton,
    activebackground="#444", 
    activeforeground="#FFFF00",
    anchor="center",
    justify="center",
    bg="#222",
    cursor="hand2",
    disabledforeground="black",
    fg="#FFDB51",
    font=("Arial", 30),
    highlightbackground="#444",
    padx=10,
    pady=5,
    width=15,
)

#placement
FemaleButton.grid()
FemaleButton.place(
    relx=0.1870,
    rely=0.275,
    anchor="nw",
)
#* Label
GenderLabel = Label(
    tk, 
    text = "SELECT GENDER",
    fg="#216CEC", 
    bg="#333", 
    font=" Arial, 30" )
#Placement
GenderLabel.grid()
GenderLabel.place(
    relx=0.375,
    rely=0.28,
    anchor="nw"
)
#^ Button for the randomization
#* Definition
def RandomizeButton():
    global Random
    Random =  False
    #! Debug print command. Delete later
    print("Randomize Button")

#* Button
RandomizeButton = Button(
    tk, 
    text="RANDOMIZE", 
    command=RandomizeButton,
    activebackground="#444", 
    activeforeground="#FFFF00",
    anchor="center",
    justify="center",
    bg="#222",
    cursor="hand2",
    disabledforeground="black",
    fg="#FFDB51",
    font=("Arial", 30),
    highlightbackground="#444",
    padx=10,
    pady=5,
    width=15,
)
#Placement
RandomizeButton.grid()
RandomizeButton.place(
    relx = 0.814,
    rely = 0.995,
    anchor="sw"
)
#^ The inputs for the province
#* The variable
Province = StringVar()
#*Text field
EnterProvince = Entry(  
    tk,
    bg="#222",
    fg="#FFDB51",
    font=("arial", 30),
    width=30,
    textvariable= Province,
)
#Placement
EnterProvince.grid()
EnterProvince.place(
    relx=0.001,
    rely=0.380,
    anchor="nw",
)
#^The labels for the province
#* Label
ProvinceLabel = Label(
    tk, 
    text = "SELECT PROVINCE - BULGARIAN/ENGLISH VERSION  ",
    fg="#216CEC", 
    bg="#333", 
    font=" Arial, 30" )
#Placement
ProvinceLabel.grid()
ProvinceLabel.place(
    relx=0.375,
    rely=0.38,
    anchor="nw"
)

tk.mainloop()
