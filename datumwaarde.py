import tkinter as tk
from tkinter import messagebox
import datetime
import csv
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def open_main_window():
    #main_window = tk.Tk()
    #date_entry = tk.Entry(main_window)
    #value_entry = tk.Entry(main_window)
    main_window.title("Main Window")
    main_window.geometry("500x320")

    date_label = tk.Label(main_window, text="Datum:")
    date_label.pack(padx=20, pady=5)
   
    #date_entry = tk.Entry(main_window)
    date_entry.pack(padx=20, pady=5)
    
    #insert_date_button = tk.Button(main_window, text="   I   ", command=lambda: insert_current_datetime(date_entry))#def insert_current_datetime(date_entry) moet later voorkomen. insert_current_datetime() betekent geen input.
    insert_date_button = tk.Button(main_window, text="   I   ", command=lambda: insert_current_datetime())
    insert_date_button.pack(padx=20, pady=5)
   
    value_label = tk.Label(main_window, text="Meetwaarde:")
    value_label.pack(padx=20, pady=5)
   
    #value_entry = tk.Entry(main_window)
    value_entry.pack(padx=20, pady=5)

    process_button = tk.Button(main_window, text="Verwerk", command= save_to_csv) #?? plot graph Nee deze button moet de nieuwe csv file creeren OF de csv file updaten met nieuwe waarden. De volgende knop maakt de Grafiek met matplotlib.
    process_button.pack(padx=20, pady=5)
   
    graph_button = tk.Button(main_window, text="Grafiek", command= plot_graph_window)
    graph_button.pack(padx=20, pady=5)

    main_window.mainloop()

def insert_current_datetime():#date_entry):
    #global date_entry #Dit werkt niet in python. Niet zomaar.
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    date_entry.delete(0, tk.END)
    date_entry.insert(0, current_datetime)
    datetime.datetime.strptime(date_entry,"%Y-%m-%d %H:%M:%S")
    #if __name__ == "__main__":
    #    open_main_window()        dit moet op het einde helemaal in the root level

def save_to_csv():
    date = date_entry.get()
    value = value_entry.get()
    #check if data is valid
    fail = False
    try:
        test =int(value)+1        
    except:
        messagebox.showerror("Onjuiste waarde!", "Graag de waarde in numerieke formaat invoeren.")
        fail = True
    try:
        datetime.datetime.strptime(date,"%Y-%m-%d %H:%M:%S")
    except:
        messagebox.showerror("Onjuiste datum formaat!", "Graag de waarde in de juiste datum formaat invoeren. \njjjj-mm-dd hh:mm:ss.")
        fail = True
    
    if not(fail):
        if not os.path.isfile('data.csv'):
            with open('data.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Date", "Value"])
                
        with open('data.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([date, value])
        

#def process_data(date, value):
#    if date and value:
#        with open("data.csv", "a", newline="") as csvfile:
#            csv_writer = csv.writer(csvfile)
#            csv_writer.writerow([date, value])

def plot_graph():
    dates = []
    values = []
    
    #data.csv bestaat nog niet. Check die file die we door AI gemaakt hebben. je moet eerst checken of de file wel bestaat.
    #Daarna moet je appenden met "a" in die file de nieuwe waarden. Thats it. Geen grafiek nog.
    with open("data.csv", "r") as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)

        for row in csv_reader:
            dates.append(row[0])
            values.append(float(row[1]))

    fig, ax = plt.subplots()
    ax.plot(dates, values, marker='o')
    ax.set_xlabel('Datum')
    ax.set_ylabel('Meetwaarde')
    ax.set_title('Grafiek')

    return fig

def plot_graph_window():
    #hier moet die csv file in "r" mode geopend worden en de 2 kollomen geplot worden. Het mag open gaan in een nieuw window hoor, hoeft niet perse gepacked worden in dezelfde window.
    fig = plot_graph()
   
    graph_window = tk.Toplevel()
    graph_window.title("Grafiek")

    canvas = FigureCanvasTkAgg(fig, master=graph_window)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()

#open_main_window()

main_window = tk.Tk()
date_entry = tk.Entry(main_window)
value_entry = tk.Entry(main_window)
#     open_main_window()        
#global main_window, date_entry, 
def init():
    
    open_main_window()        
    
if __name__ == "__main__":
    init()