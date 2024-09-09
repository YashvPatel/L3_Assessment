from tkinter import *


class Converter:

    def __init__(self):

        # common format for all buttons
        # Arial size 14 bold, with white text7/48970*84*
        button_font = ("Arial", "14", "bold")
        button_fg = "#FFFFFF"

        # Set up GUI Frame
        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame,
                                  text="Animal Quiz",
                                  font=("Arial", "16", "bold")
                                  )
        self.temp_heading.grid(row=0)

        instructions = "Please enter a number of questions " \
                       "you will be answering about information " \
                       "related to Animals youth names"
        self.temp_instructions = Label(self.temp_frame,
                                       text=instructions,
                                       wrap=250, width=40,
                                       justify="left")
        self.temp_instructions.grid(row=1)

        self.temp_entry = Entry(self.temp_frame,
                                font=("Arial", "14")
                                )
        self.temp_entry.grid(row=2, padx=10, pady=10)

        error = "Please enter a number"
        self.output_label = Label(self.temp_frame, text=error,
                                  fg="#9C0000")
        self.output_label.grid(row=3)

        # Conversion, help, and history / export buttons
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        self.to_celsius_button = Button(self.button_frame,
                                        text="Submit",
                                        bg="#990099",
                                        fg=button_fg,
                                        font=button_font)
        self.to_celsius_button.grid(row=0, column=0)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Animal Youth Quiz")
    Converter()
    root.mainloop()
