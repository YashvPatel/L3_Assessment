from tkinter import *


class QuizApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Animal Youth Quiz")

        # Common format for all buttons
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

        self.temp_entry = Entry(self.intro_frame,
                                font=("Arial", "14"))
        self.temp_entry.grid(row=2, padx=10, pady=10)

        # Error message label, initially hidden
        self.error_label = Label(self.intro_frame, text="", fg="#9C0000")
        self.error_label.grid(row=3)

        # Submit button
        self.button_frame = Frame(self.intro_frame)
        self.button_frame.grid(row=4)

        self.submit_button = Button(self.button_frame,
                                    text="Start Quiz",
                                    bg="#990099",
                                    fg=button_fg,
                                    font=button_font,
                                    command=self.start_quiz)
        self.submit_button.grid(row=0, column=0)

    def start_quiz(self):
        try:
            num_questions = int(self.temp_entry.get())
            if 1 <= num_questions <= 100:
                self.show_quiz(num_questions)  # Start the quiz with the specified number of questions
            else:
                self.error_label.config(text="Please enter a number between 1 and 100")
        except ValueError:
            self.error_label.config(text="Please enter a valid number")  # Show error message

    def show_quiz(self, how_many):
        self.intro_frame.destroy()  # Remove the initial frame

        # Set up quiz frame
        self.quiz_frame = Frame(self.root, padx=10, pady=10)
        self.quiz_frame.grid()

        rounds_heading = f"Question 1 of {how_many}"
        self.choose_heading = Label(self.quiz_frame, text=rounds_heading,
                                    font=("Arial", "16", "bold"))
        self.choose_heading.grid(row=0)

        self.control_frame = Frame(self.quiz_frame)
        self.control_frame.grid(row=6)

        self.start_over_button = Button(self.control_frame, text="Start Over",
                                        command=self.reset_app)
        self.start_over_button.grid(row=0, column=2)

    def reset_app(self):
        self.quiz_frame.destroy()
        self.__init__(self.root)  # Reinitialize the app to show the initial input frame


# main routine
if __name__ == "__main__":
    root = Tk()
    app = QuizApp(root)
    root.mainloop()
