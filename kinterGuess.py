import tkinter
from random import randint
from tkinter import W, E, END

class Guesser:

    def __init__(self, master):
        self.master = master
        master.title = 'Guess the number!'

        self.min_value = tkinter.IntVar()
        self.max_value = tkinter.IntVar()
        
        self.min_value.set(1)
        self.max_value.set(100)

        self.number = self.generateNumber()
        self.entered_number = 0
        self.counter = 0

        self.label = tkinter.Label(master=master, text='Guess the number!')

        self.guess_text = tkinter.StringVar()
        self.guess_text.set('Input your guess!')
        self.guess_label = tkinter.Label(master, textvariable=self.guess_text)
        
        self.guess_num = tkinter.IntVar()
        self.guess_num_label = tkinter.Label(master, textvariable=self.guess_num)
        
        self.prompt = tkinter.StringVar()
        self.prompt_label = tkinter.Label(master, textvariable=self.prompt)

        self.count_text = tkinter.StringVar()
        self.count_text.set('# of guesses:')
        self.count_label = tkinter.Label(master, textvariable=self.count_text)

        self.count_num = tkinter.IntVar()
        self.count_num_label = tkinter.Label(master, textvariable=self.count_num)

        master.bind("<Return>", self.guess)
        self.submit_button = tkinter.Button(master, text='Make a guess!', command=self.guess)
        self.generate_button = tkinter.Button(master, text='Generate New', command=self.generate)

        vcmd = master.register(self.validate)
        self.entry = tkinter.Entry(master, validate="key", validatecommand=(vcmd, '%P'))
        
        #LAYOUT
        self.label.grid(row=0, column=0, columnspan=2, sticky=W+E)
        self.entry.grid(row=1, column=0, columnspan=2, sticky=W+E)
        
        self.submit_button.grid(row=2, column=0, sticky=W)
        self.generate_button.grid(row=2, column=1, sticky=E)

        self.guess_label.grid(row=3, column=0, sticky=W)
        self.guess_num_label.grid(row=3, column=1, sticky=E)
        
        self.prompt_label.grid(row=4, columnspan=2, sticky=W+E)

        self.count_label.grid(row=5, column=0, sticky=W)
        self.count_num_label.grid(row=5, column=1, sticky=E)


    def guess(self, event=None):
        if self.entered_number==0:
            return
        elif self.entered_number > self.number:
            self.prompt.set('Too high')
        elif self.entered_number < self.number:
            self.prompt.set('Too low')
        else:
            self.prompt.set('On point!')
        self.counter += 1

        self.guess_text.set('Your guess:')
        self.guess_num.set(self.entered_number)

        self.count_num.set(self.counter)
        self.entry.delete(0, END)

    def generateNumber(self):
        return randint(self.min_value.get(), self.max_value.get())
        
    def generate(self):
        self.number = self.generateNumber()
        self.counter = 0
        self.prompt.set('')
        self.guess_text.set('Input your guess!')
        self.counter = 0
        self.count_num.set(self.counter)
        self.guess_num.set(0)


    def validate(self, new_text):
        if not new_text:
            self.entered_number = 0
            return True
        
        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False

if __name__ == "__main__":
    root = tkinter.Tk()
    my_gui = Guesser(root)
    root.mainloop()
        
    