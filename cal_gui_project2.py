from tkinter import *
from tkcalendar import *
def Date():
    selected_date.set(mycal.get_date())  # Update the selected_date StringVar with the selected date
    DateLabel.config(text="Selected Date: " + selected_date.get())  # Update the Label text with the selected date
m = Tk()
mycal = Calendar(m, selectmode='day', date_pattern='D/M/Y') # calendar widget
mycal.pack(padx=15, pady=15)  #  calendar widget window
selected_date = StringVar() # StringVar to store the selected date
DateLabel = Label(m, text="")  # Label to display the selected date
DateLabel.pack(padx=2, pady=2)
bro_cal = Button(m, text="Select Date", command=Date)  # Creating a button to select the date and linked it to the Date() function
bro_cal.pack(padx=15, pady=15)
m.geometry("400x400")  # window size
m.title("GUI Calendar")  # Setting the title for the root window
m.configure(bg="lightpink")  # background color window
m.mainloop()  # Start the main event loop for the application
