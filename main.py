import tkinter as tk
from tkinter import messagebox
import random

# Reading questions and answers from files
with open('questions.txt', 'r') as q_file:
    questions = q_file.readlines()

with open('answers.txt', 'r') as a_file:
    answers = a_file.readlines()

# Pairing questions and answers
quiz_data = list(zip(questions, answers))
random.shuffle(quiz_data)

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Quiz App')
        self.score = 0
        self.current_q = 0

        self.question_label = tk.Label(root, text='', wraplength=400, font=('Arial', 14))
        self.question_label.pack(pady=20)

        self.options = []
        for i in range(4):
            btn = tk.Button(root, text='', width=20, command=lambda i=i: self.check_answer(i+1))
            btn.pack(pady=5)
            self.options.append(btn)

        self.next_question()

    def next_question(self):
        if self.current_q < len(quiz_data):
            q, a = quiz_data[self.current_q]
            self.correct_answer = int(a.strip())

            q_parts = q.split(';')
            self.question_label.config(text=q_parts[0])
            for i in range(4):
                self.options[i].config(text=q_parts[i+1])
        else:
            messagebox.showinfo('Quiz Complete', f'Your final score is: {self.score}/{len(quiz_data)}')
            self.root.quit()

    def check_answer(self, selected):
        if selected == self.correct_answer:
            self.score += 1
        self.current_q += 1
        self.next_question()

if __name__ == '__main__':
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
