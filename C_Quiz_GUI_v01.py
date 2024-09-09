from tkinter import *


class QuizApp:

    def __init__(self):
        self.root = root
        self.root.title("Animal Youth Quiz")

        # Code below triggers to_quiz function to automatically launch quiz with
        # 3 questions <useful for when we develop the quiz component>
        # self.to_quiz(3)

        # Format for all buttons
        button_font = ("Arial", "14", "bold")
        button_fg = "#FFFFFF"

        # Set up GUI Frame
        self.intro_frame = Frame(root, padx=10, pady=10)
        self.intro_frame.grid()

        self.intro_heading_label = Label(self.intro_frame, text="Animal Quiz",
                                         font=("Arial", "16", "bold"))
        self.intro_heading_label.grid(row=0)

        choose_instructions_txt = "Please enter the number of questions you want to answer (1-100), then press 'Start " \
                                  "Quiz' to begin."
        self.choose_instructions_label = Label(self.intro_frame,
                                               text=choose_instructions_txt,
                                               wraplength=300, justify="left")
        self.choose_instructions_label.grid(row=1)

        self.quiz_entry = Entry(self.intro_frame,
                                font=("Arial", "14"))
        self.quiz_entry.grid(row=2, padx=10, pady=10)

        # Error message label, initially hidden
        self.error_label = Label(self.intro_frame, text="",
                                 fg="#9C0000")
        self.error_label.grid(row=3)

        # Submit button
        self.button_frame = Frame(self.intro_frame)
        self.button_frame.grid(row=4)

        self.submit_button = Button(self.button_frame,
                                    text="Start Quiz",
                                    bg="#990099",
                                    fg=button_fg,
                                    font=button_font, width=20,
                                    command=self.to_submit)
        self.submit_button.grid(row=0, column=0)

    def check_quiz(self, min_value):
        error = "Enter a number that is more than 1 & less than 100" \
            .format(min_value)

        try:
            response = self.quiz_entry.get()
            response = float(response)

            if response < 1 or response > 100:
                self.error_label.config(text=error)
            else:
                return response

        except ValueError:
            self.error_label.config(text=error)

    # check if number is over 1-100
    def to_submit(self):

        self.check_quiz(-100)


class Quiz:

    def __init__(self, how_many):
        # sets up question / answer GUI
        self.quiz_box = Toplevel()
        print("you have started the quiz", how_many)


# main routine
if __name__ == "__main__":
    root = Tk()
    app = QuizApp()
    root.mainloop()
