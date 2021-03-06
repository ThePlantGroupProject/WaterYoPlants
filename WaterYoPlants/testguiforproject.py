from tkinter import *
import sqlite3


root = Tk()
root.title('WaterYoPlants, Where You Get All The Info About Yo Plants')
root.geometry("1024x685")


#backgroud image
bg = PhotoImage(file="plants.png")
lbl=Label(root, image=bg)
lbl.place(x=0, y=0, relwidth=1, relheight=1)


# connecting to the database
conn = sqlite3.connect("WaterYoPlants.db")
# creating the cursor
c = conn.cursor()


# creating a query function
def query():
    conn = sqlite3.connect("WaterYoPlants.db")
    c = conn.cursor()
    #querying the database
    c.execute("SELECT * FROM WaterYoPlants")
    plantinfo = c.fetchall()
    
    # loop through the results
    print_plantinfo = ""
    for allplants in plantinfo:
        print_plantinfo += str(allplants[0]) + "\n"
        
    allplants_label = Label(root, text=print_plantinfo)
    allplants_label.place(x=0, y=250)
    
    #print(allplants[0:3])
    
    conn.close()
    
    


# Title name on the GUI
lbl=Label(root, text='WATER YO PLANTS', fg='green', font=("Helvetica", 20))
lbl.place(x=300, y=25)


# textbox label next to the entry box
lbl1=Label(root, text='What is yo plants name?', fg='black', font=('Helvetica', 10))
lbl1.place(x=250, y=100)


#######################################################################################################################
###                                          CURRENT ISSUES                                                         ###
###                                                                                                                 ###
### HOW TO QUERRY JUST ONE SPECIFIC ROW BASED OFF THE FILTERS???                                                    ###
### HOW TO USE THE SEARCH BAR AS THE POINT OF FETCHING THE DATA FROM THE DATABASE???                                ###
### HOW TO CHECK USER INPUT AGAINST THE DATABASE AND GIVE A MESSAGE BACK SAYING YOU SPELLED THE PLANT NAME WRONG??? ###
#######################################################################################################################


# querying from data base based on the search entry
def entrysearch():
    conn = sqlite3.connect("WaterYoPlants.db")
    c = conn.cursor()
    #getentry = c.execute("SELECT Plant FROM WaterYoPlants WHERE Plant = ?'"+ str(search.get()) +"' ")
    getentry = c.execute("SELECT Plant FROM WaterYoPlants WHERE Plant = str(search.get())")
    plantname = str(getentry)
    for searchedname in plantname:
        print(searchedname)
    
    conn.close()


# Input entrybox for search of the plants
search=Entry(root, bd=5, bg="light green")
search.place(x=500, y=100)
search.focus()


# filter for all the info
def queryall():
    alllabel = Label(root, text=v0.get())
    alllabel.place(x=0, y=250)
    conn = sqlite3.connect("WaterYoPlants.db")
    c = conn.cursor()
    #querying the database
    c.execute("SELECT * FROM WaterYoPlants")
    origininfo = c.fetchall()    
    # loop through the results
    print_allinfo = ""
    for allplants in allinfo:
        print_allinfo += str(allplants[1:]) + "\n"
            
    conn.close()
    
    
def queryorigin():
    originlabel = Label(root, text=v1.get())
    originlabel.place(x=0, y=250)
    conn = sqlite3.connect("WaterYoPlants.db")
    c = conn.cursor()
    #querying the database
    c.execute("SELECT Origin FROM WaterYoPlants")
    origininfo = c.fetchone()    
    # loop through the results
    print_origininfo = ""
    for originplants in origininfo:
        print_origininfo += str(originplants[1]) + "\n"
            
    conn.close()
    
    
def queryheight():
    heightlabel = Label(root, text=v2.get())
    heightlabel.place(x=0, y=250)
    conn = sqlite3.connect("WaterYoPlants.db")
    c = conn.cursor()
    #querying the database
    c.execute("SELECT Height FROM WaterYoPlants")
    info = c.fetchall()    
    # loop through the results
    print_heightinfo = ""
    for heightplants in heightinfo:
        print_heightinfo += str(heightplants[2]) + "\n"
            
    conn.close()
    

def querylight():
    lightlabel = Label(root, text=v3.get())
    lightlabel.place(x=0, y=250)
    conn = sqlite3.connect("WaterYoPlants.db")
    c = conn.cursor()
    #querying the database
    c.execute("SELECT Light FROM WaterYoPlants")
    lightinfo = c.fetchall()    
    # loop through the results
    print_lightinfo = ""
    for lightplants in lightinfo:
        print_lightinfo += str(lightplants[3]) + "\n"
            
    conn.close()
    

def querywater():
    waterlabel = Label(root, text=v4.get())
    waterlabel.place(x=0, y=250)
    conn = sqlite3.connect("WaterYoPlants.db")
    c = conn.cursor()
    #querying the database
    c.execute("SELECT Water FROM WaterYoPlants")
    waterinfo = c.fetchall()    
    # loop through the results
    print_waterinfo = ""
    for waterplants in waterinfo:
        print_waterinfo += str(waterplants[4]) + "\n"
            
    conn.close()
    
    
def queryhumidity():
    humiditylabel = Label(root, text=v5.get())
    humiditylabel.place(x=0, y=250)
    conn = sqlite3.connect("WaterYoPlants.db")
    c = conn.cursor()
    #querying the database
    c.execute("SELECT Humidity FROM WaterYoPlants")
    humidityinfo = c.fetchall()    
    # loop through the results
    print_humidityinfo = ""
    for humidityplants in humidityinfo:
        print_humidityinfo += str(humidityplants[5]) + "\n"
            
    conn.close()


def querytemperature():
    temperaturelabel = Label(root, text=v6.get())
    temperaturelabel.place(x=0, y=250)
    conn = sqlite3.connect("WaterYoPlants.db")
    c = conn.cursor()
    #querying the database
    c.execute("SELECT Temperature FROM WaterYoPlants")
    temperatureinfo = c.fetchall()    
    # loop through the results
    print_temperatureinfo = ""
    for temperatureplants in temperatureinfo:
        print_temperatureinfo += str(temperatureplants[6]) + "\n"
            
    conn.close()



def querysoil():
    soillabel = Label(root, text=v7.get())
    soillabel.place(x=0, y=250)
    conn = sqlite3.connect("WaterYoPlants.db")
    c = conn.cursor()
    #querying the database
    c.execute("SELECT * FROM WaterYoPlants")
    soilinfo = c.fetchall()    
    # loop through the results
    print_soilinfo = ""
    for soilplants in soilinfo:
        print_soilinfo += str(soilplants[7]) + "\n"
            
    conn.close()


def queryfertilizer():
    fertilizerlabel = Label(root, text=v8.get())
    fertilizerlabel.place(x=0, y=250)
    conn = sqlite3.connect("WaterYoPlants.db")
    c = conn.cursor()
    #querying the database
    c.execute("SELECT * FROM WaterYoPlants")
    fertilizerinfo = c.fetchall()    
    # loop through the results
    print_fertilizerinfo = ""
    for fertilizerplants in fertilizerinfo:
        print_fertilizerinfo += str(fertilizerplants[8]) + "\n"
            
    conn.close()

def querypropagation():
    propagationlabel = Label(root, text=v9.get())
    propagationlabel.place(x=0, y=250)
    conn = sqlite3.connect("WaterYoPlants.db")
    c = conn.cursor()
    #querying the database
    c.execute("SELECT * FROM WaterYoPlants")
    propagationinfo = c.fetchall()    
    # loop through the results
    print_propagationinfo = ""
    for propagationplants in propagationinfo:
        print_propagationinfo += str(propagationplants[9]) + "\n"
            
    conn.close()


# check boxes to filter the plant info search
v0 = StringVar()
v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
v4 = StringVar()
v5 = StringVar()
v6 = StringVar()
v7 = StringVar()
v8 = StringVar()
v9 = StringVar()

# check box labels and variable assignments
C0 = Checkbutton(root, text = "All", variable = v0, onvalue=queryall)
C0.deselect()
C1 = Checkbutton(root, text = "Origin", variable = v1, onvalue=queryorigin)
C1.deselect()
C2 = Checkbutton(root, text = "Height", variable = v2, onvalue=queryheight)
C2.deselect()
C3 = Checkbutton(root, text = "Light", variable = v3, onvalue=querylight)
C3.deselect()
C4 = Checkbutton(root, text = "Water", variable = v4, onvalue=querywater)
C4.deselect()
C5 = Checkbutton(root, text = "Humidity", variable = v5, onvalue=queryhumidity)
C5.deselect()
C6 = Checkbutton(root, text = "Temperature", variable = v6, onvalue=querytemperature)
C6.deselect()
C7 = Checkbutton(root, text = "Soil", variable = v7, onvalue=querysoil)
C7.deselect()
C8 = Checkbutton(root, text = "Fertilizer", variable = v8, onvalue=queryfertilizer)
C8.deselect()
C9 = Checkbutton(root, text = "Propagation", variable = v9, onvalue=querypropagation)
C9.deselect()

# checkbox locations on the GUI
C0.place(x=25, y=150)
C1.place(x=80, y=150)
C2.place(x=165, y=150)
C3.place(x=255, y=150)
C4.place(x=335, y=150)
C5.place(x=420, y=150)
C6.place(x=530, y=150)
C7.place(x=670, y=150)
C8.place(x=740, y=150)
C9.place(x=850, y=150)

# button for querying the information
B1=Button(root, text='SubmitYoPlant', command=entrysearch)
B1.place(x=400, y=200)


root.mainloop()