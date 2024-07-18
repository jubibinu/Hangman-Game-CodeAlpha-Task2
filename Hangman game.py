import tkinter as tk
import random


root = tk.Tk()
root.title="Hangman game"
root.config(bg="#E7FFFF")


word_list=["root","city","python","queue","flower","chocolate","plan","ghost","syntax"]
randomword=random.choice(word_list)
guessed_word = ["_"] * len(randomword)

hangman_art = [
    "   +---+\n   |   |\n       |\n       |\n       |\n       |\n==========",
    "   +---+\n   |   |\n   O   |\n       |\n       |\n       |\n==========",
    "   +---+\n   |   |\n   O   |\n   |   |\n       |\n       |\n==========",
    "   +---+\n   |   |\n   O   |\n  /|   |\n       |\n       |\n==========",
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n       |\n       |\n==========",
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n  /    |\n       |\n==========",
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n  / \\  |\n       |\n=========="
]


def update_hangman(wrong):
    hangman_label.config(text=hangman_art[wrong],bg="#E7FFFF")

def clear_entry_field():
    guess_entry.delete(0, tk.END)
    
def reset_game():
    global randomword, guessed_word, wrong
    randomword = random.choice(word_list)
    guessed_word = ["_"] * len(randomword)
    update_hangman(0)
    word_label.config(text=guessed_word, bg="#E7FFFF")
    result_label.config(text="", bg="#E7FFFF")
    guess_entry.config(state="normal")
    guess_button.config(state="normal")
    wrong = 0


def check_guess(guess):
    clear_entry_field()
    global guessed_word
    if guess in randomword:
        for i in range(len(randomword)):
            if  randomword[i] == guess:
                guessed_word=guessed_word[:i]+list(guess)+guessed_word[i+1:]
        word_label.config(text=guessed_word,bg="#E7FFFF")
        if '_' not in guessed_word:
            end_game("Win")
    else:
        global wrong
        wrong+=1
        update_hangman(wrong)
        if wrong==6:
            end_game("Lose")
                
def end_game(result):
    if result == "Win":
        result_text = "Congratulations! You guessed the word correctly."
    else:
        result_text = "You Lose. The word was: " + randomword
    result_label.config(text=result_text, bg="#E7FFFF")
    guess_entry.config(state="disabled")
    guess_button.config(state="disabled")

hangman_label=tk.Label(root,font=("CourierK", 16),bg="#E7FFFF" )
hangman_label.grid(row=0,column=0)
word_label= tk.Label(root,text=guessed_word,font=("Ariel",25),bg="#E7FFFF")
word_label.grid(row=1,column=0)

guess_entry=tk.Entry(root,width=9,font=("Ariel",20),bg="white")
guess_entry.grid(row=2,column=0)
guess_button=tk.Button(root,text="Guess",width=7,command=lambda: check_guess(guess_entry.get()))
guess_button.grid(row=2,column=1)

result_label=tk.Label(root,font=("Arial",20),bg="#E7FFFF")
result_label.grid(row=3,column=0)

reset_button = tk.Button(root, text="Reset", width=7, command=reset_game)
reset_button.grid(row=3, column=1)


wrong=0
update_hangman(wrong)
root.mainloop()