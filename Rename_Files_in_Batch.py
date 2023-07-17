#!/usr/bin/env python

# IMPORTING LIBRARIES
# import all classes / functions from the tkinter, easygui and os
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
import os
from screeninfo import get_monitors
# from functools import partial

# FUNCTIONS USED
# Function to add path of the files to be renamed.


def add_path():
    dir_name_in = filedialog.askdirectory()
    dir_name.insert(tk.END, dir_name_in)

# Function to populate the array from user input that contains the dash locations


def populate_dash_loc():
    global dash_content
    dash_content = []
    total_dash = int(number_dashes.get())
    for i in range(total_dash):
        # position_dashes = Entry(second_frame, font=("Times New Roman", 12), justify='center')
        dash_content.append(Entry(second_frame, width=40, font=("Times New Roman", 12), justify='center'))
        dash_content[i].grid(sticky=W, row=27 + i, column=2, padx=10, pady=10)


def populate_word_remove():
    global word_remove_content
    word_remove_content = []
    total_remove = int(remove_word_number.get())
    for i in range(total_remove):
        # position_dashes = Entry(second_frame, font=("Times New Roman", 12), justify='center')
        word_remove_content.append(Entry(second_frame, width=40, font=("Times New Roman", 12), justify='center'))
        word_remove_content[i].grid(sticky=W, row=19 + i, column=2, padx=10, pady=10)

# Function for clearing the contents of all entry boxes


def clear_all():
    # whole content of entry boxes and radio buttons is deleted
    dir_name.delete("1.0", "end")
    want_split.set(None)
    split_word.delete(0, END)
    space_absent.set(None)
    copies_present.set(None)
    number_copy.delete(0, END)
    want_sentence.set(None)
    position_sentence.delete(0, END)
    insert_sentence.delete(0, END)
    remove_word.set(None)
    remove_word_number.delete(0, END)
    capitalize.set(None)
    insert_dashes.set(None)
    number_dashes.delete(0, END)
    insert_definitions.set(None)
    definition_val.delete(0, END)
    string_splitting_character.delete(0, END)
    filename_final.delete("1.0", "end")

    for j in range(len(dash_content)):
        dash_content[j].delete(0, END)

    for k in range(len(word_remove_content)):
        dash_content[k].delete(0, END)

    # set focus on the principle_field entry box
    # dir_name.focus_set()

# Function to clear only the results, so that the program can run on slightly modified initial conditions


def clear_results():
    # contents of the result box is deleted
    filename_final.delete("1.0", "end")

# Function which resets all the data and removes the extra dash content boxes too


def restart():
    dir_name.delete("1.0", "end")
    split_word.delete(0, END)
    space_absent.set(None)
    copies_present.set(None)
    number_copy.delete(0, END)
    want_sentence.set(None)
    position_sentence.delete(0, END)
    insert_sentence.delete(0, END)
    remove_word.set(None)
    remove_word_number.delete(0, END)
    capitalize.set(None)
    insert_dashes.set(None)
    number_dashes.delete(0, END)
    insert_definitions.set(None)
    definition_val.delete(0, END)
    string_splitting_character.delete(0, END)
    filename_final.delete("1.0", "end")

    for j in range(len(dash_content)):
        dash_content[j].destroy()

    for k in range(len(word_remove_content)):
        word_remove_content[k].destroy()


# Function to rename files


def change_filename():
    global COUNT
    COUNT = 1
    try:
        # dir_name = input("Enter the path of the file that you want to rename:")
        dir_name_final = r'{}'.format(dir_name.get("1.0", 'end-1c')).replace('\\', '//')
        os.chdir(dir_name_final)

        # Function to increment count to make the files sorted.
        def increment():
            global COUNT
            COUNT = COUNT + 1

        # Traversing through all the files in the same directory
        for f in os.listdir():
            # getting the path
            f_name, f_ext = os.path.splitext(f)

            if bool(int(want_split.get())):
                words = f_name.split(split_word.get())
                word1_str = words[0].split()
            else:
                word1_str = f_name.split()

            # Removing Copies
            if bool(int(copies_present.get())):
                words = word1_str[2*int(number_copy.get()):]
            else:
                words = word1_str

            words_imp = [' '.join(i) for i in [words]]

            # Cleansing the filename string from non space demarcations
            if bool(int(space_absent.get())):
                words_new = words_imp[0].split(str(string_splitting_character.get()))
                words_new = words_new[:-1]
            else:
                words_new = words_imp[0].split()

            # Inserting the sentence name at the required position if the user asks for it
            if bool(int(want_sentence.get())):
                words_new.insert(int(position_sentence.get()), insert_sentence.get())

            # Removing words if required
            if bool(int(remove_word.get())):
                for i in range(int(remove_word_number.get())):
                    words_new.remove(word_remove_content[i].get())

            # Capitalizing the complete string
            words_new_final = []
            if bool(int(capitalize.get())):
                for element in words_new:
                    element_mod = element.capitalize()
                    words_new_final.append(element_mod)
            else:
                words_new_final = words_new

            # Inserting definitions if required
            if bool(int(insert_definitions.get())):
                words_new_final.insert(len(words_new_final), '[' + definition_val.get() + ']')

            # Inserting dashes if required
            if bool(int(insert_dashes.get())):
                for i in range(int(number_dashes.get())):
                    words_new_final.insert(int(dash_content[i].get()), '-')

            # Joining the sentences with spaces to make the final string
            sentences = [' '.join(i) for i in [words_new_final]]
            f_name = sentences[0]
            filename_final.insert(tk.END, f_name + '\n')
            increment()

            # Comment these two lines whenever testing the program
            new_name = '{} {}'.format(f_name, f_ext)
            os.rename(f, new_name)

    except:
        messagebox.showerror("Invalid Input", "Enter a valid number/string/path")

# Driver code
# CREATING THE GUI WINDOWS AND SETTING THEIR VISUAL ELEMENTS


root = Tk()

# Set the background colour of GUI window
root.configure(background='gray5')

# Set the configuration of GUI window
m = get_monitors()
height_disp = m[0].height
width_disp = m[0].width
res = str(width_disp) + "x" + str(height_disp) 
root.geometry(res)

# set the name of tkinter GUI window
root.title("Modify Filenames in Batch")

# Icon for the program
root.iconbitmap('./Icon/Icon.ico')

# Create A Main Frame
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)
main_frame.configure(background='gray5')

# Create A Canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Add Vertical Scrollbar To The Canvas
my_scrollbar1 = ttk.Scrollbar(main_frame, orient='vertical', command=my_canvas.yview)
my_scrollbar1.pack(side=RIGHT, fill=Y)

# Configure The Canvas
my_canvas.configure(background='gray5')
my_canvas.configure(yscrollcommand=my_scrollbar1.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))


def _on_mouse_wheel(event):
    my_canvas.yview_scroll(-1 * int((event.delta / 100)), "units")


my_canvas.bind_all("<MouseWheel>", _on_mouse_wheel)

# You can lower the 120 to increase scroll speed.

# Create ANOTHER Frame INSIDE the Canvas

second_frame = Frame(my_canvas)
second_frame.configure(background='gray5')
# Add that New frame To a Window In The Canvas

my_canvas.create_window((0, 0), window=second_frame, anchor="sw")

# ADDING DESCRIPTION LABELS
# Grid method is used for placing the widgets at respective positions in table like structure.

title_label = Label(second_frame, text="MODIFY FILENAMES IN BATCH", font=("Times New Roman", 16, "bold", "underline"),
                    fg='white', bg='gray5').grid(sticky=N, row=1, column=1, padx=1, pady=1)
# Path of the file : label
dir_name_label = Label(second_frame, text="Path of the File :", font=("Times New Roman", 12),
                       fg='white', bg='gray5').grid(sticky=W, row=7, column=0, padx=1, pady=1)
# Do you need to split the string (after some particular word) : label
want_split_label = Label(second_frame, text="Do you wish to split the original string/filename? :",
                         font=("Times New Roman", 12),
                         fg='white', bg='gray5').grid(sticky=W, row=8, column=0, padx=1, pady=1)
# Split Word Input : label
split_word_label = Label(second_frame, text="If yes,enter the word where you want to split the original string :",
                         font=("Times New Roman", 12),
                         fg='white', bg='gray5').grid(sticky=W, row=9, column=0, padx=1, pady=1)
# Are Spaces absent - Yes or No : label
space_absent_label = Label(second_frame, text="Does the filename have fullstops/underscores \n or any other character instead of spaces? :",
                           font=("Times New Roman", 12),
                           fg='white', bg='gray5').grid(sticky=W, row=10, column=0, padx=1, pady=1)
# What character is to be replaced by spaces : label
string_splitting_character_label = Label(second_frame, text="If yes, then type in the character \n that is to be replaced by spaces? :",
                                         font=("Times New Roman", 12),
                                         fg='white', bg='gray5').grid(sticky=W, row=11, column=0, padx=1, pady=1)
# Does the Filename have the word Copy - Yes or No : label
copy_present_label = Label(second_frame, text="Do the filenames contain 'Copy of'? :",
                           font=("Times New Roman", 12),
                           fg='white', bg='gray5').grid(sticky=W, row=12, column=0, padx=1, pady=1)
# If yes then how many times does the word Copy occur : label
number_copy_label = Label(second_frame,
                          text="If yes, then enter the number of 'Copy of'(s) that you need :",
                          font=("Times New Roman", 12),
                          fg='white', bg='gray5').grid(sticky=W, row=13, column=0, padx=1, pady=1)

# Any additional sentences/strings required : label
want_sentence_label = Label(second_frame, text="Do you want to insert a sentence/string into the filename? :",
                            font=("Times New Roman", 12),
                            fg='white', bg='gray5').grid(sticky=W, row=14, column=0, padx=1, pady=1)
# If yes, the position of the sentence/string : label
position_sentence_label = Label(second_frame,
                                text="If yes, then enter position of the string with \n respect to positions of the desired string  :",
                                font=("Times New Roman", 12),
                                fg='white', bg='gray5').grid(sticky=W, row=15, column=0, padx=1, pady=1)

# Enter the string which is to be inserted : label
insert_sentence_label = Label(second_frame,
                              text="Enter the sentence/string that is to be inserted :",
                              font=("Times New Roman", 12),
                              fg='white', bg='gray5').grid(sticky=W, row=16, column=0, padx=1, pady=1)

# Any additional sentences/strings required : label
remove_word_label = Label(second_frame, text="Do you want to remove any word from the string? :",
                          font=("Times New Roman", 12),
                          fg='white', bg='gray5').grid(sticky=W, row=17, column=0, padx=1, pady=1)
# If yes, the position of the sentence/string : label
remove_word_number_label = Label(second_frame, text="If yes, then enter the number of words that are to be removed :",
                                 font=("Times New Roman", 12),
                                 fg='white', bg='gray5').grid(sticky=W, row=18, column=0, padx=1, pady=1)
# Word to be Removed : Label
word_to_be_removed_label = Label(second_frame, text="Enter the word to be removed :",
                                 font=("Times New Roman", 12),
                                 fg='white', bg='gray5').grid(sticky=W, row=19, column=0, padx=1, pady=1)
# Capitalize the String : Label
capitalize_label = Label(second_frame, text="Do you want to capitalize the string",
                         font=("Times New Roman", 12),
                         fg='white', bg='gray5').grid(sticky=W, row=24, column=0, padx=1, pady=1)

# Do you want to Insert a dash : label
insert_dash_label = Label(second_frame, text="Are dashes required? :",
                          font=("Times New Roman", 12),
                          fg='white', bg='gray5').grid(sticky=W, row=25, column=0, padx=1, pady=1)
# If yes then how many times does the dash or '-' needs to be inserted : label
number_dash_label = Label(second_frame,
                          text="If yes, then enter the number of dashes you need :",
                          font=("Times New Roman", 12),
                          fg='white', bg='gray5').grid(sticky=W, row=26, column=0, padx=1, pady=1)
# If yes then how many times does the dash or '-' needs to be inserted : label
position_dash_label = Label(second_frame,
                            text="If yes, then enter the positions of the dashes that you need :",
                            font=("Times New Roman", 12),
                            fg='white', bg='gray5').grid(sticky=W, row=27, column=0, padx=1, pady=1)
# Do you want to Insert Video Definition : label
insert_definition_label = Label(second_frame, text="Is definition (e.g. 720p) required? :",
                                font=("Times New Roman", 12),
                                fg='white', bg='gray5').grid(sticky=W, row=32, column=0, padx=1, pady=1)
# If yes, then Definition Value : label
definition_val_label = Label(second_frame, text="If yes, enter the value of definition \n that you need (appended at the end) :",
                             font=("Times New Roman", 12),
                             fg='white', bg='gray5').grid(sticky=W, row=33, column=0, padx=1, pady=1)

# Final filenames in the folder : label

filename_final_label = Label(second_frame, text="Final names of renamed files :", font=("Times New Roman", 12),
                             fg='white', bg='gray5').grid(sticky=W, row=34, column=0, padx=1, pady=1)

# Instructions : labels
instructions_label_header = Label(second_frame, text="INSTRUCTIONS", font=("Times New Roman", 14, "underline"),
                                  fg='white', bg='gray5').grid(row=2, column=1, padx=10, pady=0)
instructions_label1 = Label(second_frame, text="1. Keep the maximum number of 'words to remove' and 'inserted dashes' to 5.", font=("Times New Roman", 12),
                            fg='white', bg='gray5').grid(sticky=W, row=3, column=1, padx=1, pady=0)
instructions_label2 = Label(second_frame, text="2. Follow the top to bottom flow and use full-screen view for best experience.", font=("Times New Roman", 12),
                            fg='white', bg='gray5').grid(sticky=W, row=4, column=1, padx=1, pady=0)
instructions_label3 = Label(second_frame, text="3. Restart button removes boxes with dash positions and clears all the other boxes.", font=("Times New Roman", 12),
                            fg='white', bg='gray5').grid(sticky=W, row=5, column=1, padx=1, pady=0)
instructions_label4 = Label(second_frame, text="4. If the sentence/string is inserted before any of the dashes, "
                                               "then account for it while entering \n dash positions. "
                                               "Same applies for words being removed.", font=("Times New Roman", 12),
                            fg='white', bg='gray5').grid(sticky=W, row=6, column=1, padx=1, pady=0)

dash_marker_label = Label(second_frame,
                          text="The dash positions are to be put in the \n boxes  that appear below this line.",
                          font=("Times New Roman", 12),
                          fg='white', bg='gray5').grid(sticky=W, row=26, column=2, padx=1, pady=0)

word_remove_marker_label = Label(second_frame,
                                 text="The words to be removed are to be put in the \n boxes  that appear below this line.",
                                 font=("Times New Roman", 12),
                                 fg='white', bg='gray5').grid(sticky=W, row=18, column=2, padx=1, pady=0)

thanks_label = Label(second_frame, text="Thank You!", font=("Times New Roman", 12),
                     fg='white', bg='gray5').grid(row=39, column=1, padx=10, pady=10)

# ADDING ENTRY BOXES, TEXT BOXES AND INTEGER VARIABLES (RADIO BUTTON) FOR FILLING AND DISPLAYING INFORMATION.

dir_name = tk.Text(second_frame, width=70, height=2, font=("Times New Roman", 12))
want_split = IntVar()
split_word = tk.Entry(second_frame, font=("Times New Roman", 12), justify='center')
space_absent = IntVar()
string_splitting_character = tk.Entry(second_frame, font=("Times New Roman", 12), justify='center')
copies_present = IntVar()
number_copy = tk.Entry(second_frame, font=("Times New Roman", 12), justify='center')
want_sentence = IntVar()
position_sentence = tk.Entry(second_frame, font=("Times New Roman", 12), justify='center')
insert_sentence = tk.Entry(second_frame, width=70, font=("Times New Roman", 12), justify='center')
remove_word = IntVar()
remove_word_number = tk.Entry(second_frame, font=("Times New Roman", 12), justify='center')
capitalize = IntVar()
insert_dashes = IntVar()
number_dashes = tk.Entry(second_frame, font=("Times New Roman", 12), justify='center')
insert_definitions = IntVar()
definition_val = tk.Entry(second_frame, font=("Times New Roman", 12), justify='center')
filename_final = tk.Text(second_frame, width=50, height=5, font=("Times New Roman", 12))

# Radio buttons set to none by default

want_split.set(None)
space_absent.set(None)
copies_present.set(None)
insert_dashes.set(None)
insert_definitions.set(None)
want_sentence.set(None)
remove_word.set(None)
capitalize.set(None)

# grid method is used for placing the widgets at respective positions in table like structure.

# padx keyword argument used to set padding along x-axis.
# ipadx keyword argument used to set padding within the entry box along x-axis.
# pady keyword argument used to set padding along y-axis.
# ipady keyword argument used to set padding within the entry box along y-axis.

# ADDING RADIO BUTTONS, ENTRY AND TEXT-BOXES

dir_name.grid(row=7, column=1, padx=10, pady=10, sticky=W)

button1_want_split = Radiobutton(second_frame, text="Yes", variable=want_split, value=1, padx=10, pady=10,
                                 activeforeground='white', activebackground='gray5', fg='white', bg='gray5',
                                 selectcolor='black', highlightbackground='black').grid(row=8, column=1, padx=10, pady=10, sticky=W)
button0_want_split = Radiobutton(second_frame, text="No", variable=want_split, value=0, padx=10, pady=10,
                                 activeforeground='white', activebackground='gray5', fg='white', bg='gray5',
                                 selectcolor='black', highlightbackground='black').grid(row=8, column=1, padx=10, pady=10)
split_word.grid(row=9, column=1, padx=10, pady=10, sticky=W)

button1_space_absent = Radiobutton(second_frame, text="Yes", variable=space_absent, value=1, padx=10, pady=10,
                                   activeforeground='white', activebackground='gray5', fg='white', bg='gray5',
                                   selectcolor='black', highlightbackground='black').grid(row=10, column=1, padx=10, pady=10, sticky=W)
button0_space_absent = Radiobutton(second_frame, text="No", variable=space_absent, value=0, padx=10, pady=10,
                                   activeforeground='white', activebackground='gray5', fg='white', bg='gray5',
                                   selectcolor='black', highlightbackground='black').grid(row=10, column=1, padx=10, pady=10)

string_splitting_character.grid(row=11, column=1, padx=10, pady=10, sticky=W)
button1_copies = Radiobutton(second_frame, text="Yes", variable=copies_present, value=1, padx=10, pady=10,
                             activeforeground='white', activebackground='gray5', fg='white', bg='gray5',
                             selectcolor='black', highlightbackground='black').grid(row=12, column=1, padx=10, pady=10, sticky=W)
button0_copies = Radiobutton(second_frame, text="No", variable=copies_present, value=0, padx=10, pady=10,
                             activeforeground='white', activebackground='gray5', fg='white', bg='gray5',
                             selectcolor='black', highlightbackground='black').grid(row=12, column=1, padx=10, pady=10)

number_copy.grid(row=13, column=1, padx=10, pady=10, sticky=W)

button1_want_sentence = Radiobutton(second_frame, text="Yes", variable=want_sentence, value=1, padx=10, pady=10,
                                    activeforeground='white', activebackground='gray5', fg='white', bg='gray5',
                                    selectcolor='black', highlightbackground='black').grid(row=14, column=1, padx=10, pady=10, sticky=W)
button0_want_sentence = Radiobutton(second_frame, text="No", variable=want_sentence, value=0, padx=10, pady=10,
                                    activeforeground='white', activebackground='gray5', fg='white', bg='gray5',
                                    selectcolor='black', highlightbackground='black').grid(row=14, column=1, padx=10, pady=10)

position_sentence.grid(row=15, column=1, padx=10, pady=10, sticky=W)
insert_sentence.grid(row=16, column=1, padx=10, pady=10, sticky=W)

button1_remove = Radiobutton(second_frame, text="Yes", variable=remove_word, value=1, padx=10, pady=10,
                             activeforeground='white', activebackground='gray5', fg='white', bg='gray5',
                             selectcolor='black', highlightbackground='black').grid(row=17, column=1, padx=10, pady=10, sticky=W)
button0_remove = Radiobutton(second_frame, text="No", variable=remove_word, value=0, padx=10, pady=10,
                             activeforeground='white', activebackground='gray5', fg='white', bg='gray5',
                             selectcolor='black', highlightbackground='black').grid(row=17, column=1, padx=10, pady=10)

remove_word_number.grid(row=18, column=1, padx=10, pady=10, sticky=W)

button1_capitalize = Radiobutton(second_frame, text="Yes", variable=capitalize, value=1, padx=10, pady=10,
                                 activeforeground='white', activebackground='gray5', fg='white', bg='gray5',
                                 selectcolor='black', highlightbackground='black').grid(row=24, column=1, padx=10, pady=10, sticky=W)
button0_capitalize = Radiobutton(second_frame, text="No", variable=capitalize, value=0, padx=10, pady=10,
                                 activeforeground='white', activebackground='gray5', fg='white', bg='gray5',
                                 selectcolor='black', highlightbackground='black').grid(row=24, column=1, padx=10, pady=10)


button1_dashes = Radiobutton(second_frame, text="Yes", variable=insert_dashes, value=1, padx=10, pady=10,
                             activeforeground='white', activebackground='gray5', fg='white', bg='gray5',
                             selectcolor='black', highlightbackground='black').grid(row=25, column=1, padx=10, pady=10, sticky=W)
button0_dashes = Radiobutton(second_frame, text="No", variable=insert_dashes, value=0, padx=10, pady=10,
                             activeforeground='white', activebackground='gray5', fg='white', bg='gray5',
                             selectcolor='black', highlightbackground='black').grid(row=25, column=1, padx=10, pady=10)

number_dashes.grid(row=26, column=1, padx=10, pady=10, sticky=W)

button1_def = Radiobutton(second_frame, text="Yes", variable=insert_definitions, value=1, padx=10, pady=10,
                          activeforeground='white', activebackground='gray5', fg='white', bg='gray5',
                          selectcolor='black', highlightbackground='black').grid(row=32, column=1, padx=10, pady=10, sticky=W)
button0_def = Radiobutton(second_frame, text="No", variable=insert_definitions, value=0, padx=10, pady=10,
                          activeforeground='white', activebackground='gray5', fg='white', bg='gray5',
                          selectcolor='black', highlightbackground='black').grid(row=32, column=1, padx=10, pady=10)

definition_val.grid(row=33, column=1, padx=10, pady=10, sticky=W)
filename_final.grid(row=34, column=1, padx=10, pady=10, sticky=W)

# ADDING THE BUTTONS

# Create a File path button
button1 = Button(second_frame, text="Select Folder", bg="azure4", fg="black",
                 font=("Times New Roman", 12), command=add_path).grid(row=7, column=2, padx=10, pady=10, ipadx=5,
                                                                      ipady=0, sticky=W)
# Create a Submit Button
button2 = Button(second_frame, text="Submit", bg="azure4", fg="black",
                 font=("Times New Roman", 12), command=change_filename).grid(row=35, column=1, padx=10, pady=10, ipadx=5,
                                                                             ipady=0, sticky=W)
# Create a Remove Word Button
button3 = Button(second_frame, text="Remove Word", bg="azure4", fg="black",
                 font=("Times New Roman", 12), command=populate_word_remove).grid(row=19, column=1, padx=10, pady=10, ipadx=5,
                                                                                  ipady=0, sticky=W)
# Create a Insert Dash Locations
button4 = Button(second_frame, text="Insert Dash Locations", bg="azure4", fg="black",
                 font=("Times New Roman", 12), command=populate_dash_loc).grid(row=27, column=1, padx=10, pady=10, ipadx=5,
                                                                               ipady=0, sticky=W)
# Create a Clear Button just to clear the outputs
button5 = Button(second_frame, text="Clear Results", bg="azure4", fg="black",
                 font=("Times New Roman", 12), command=clear_results).grid(row=36, column=1, padx=10, pady=10, ipadx=5,
                                                                           ipady=0, sticky=W)
# Create a Clear All Button
button6 = Button(second_frame, text="Clear All", bg="azure4", fg="black",
                 font=("Times New Roman", 12), command=clear_all).grid(row=37, column=1, padx=10, pady=10, ipadx=5,
                                                                       ipady=0, sticky=W)
# Create a Button to Remove dash and word remove entry boxes as well as clearing everything
button7 = Button(second_frame, text="Restart", bg="azure4", fg="black",
                 font=("Times New Roman", 12), command=restart).grid(row=38, column=1, padx=10, pady=10, ipadx=5,
                                                                     ipady=0, sticky=W)

# Starting the GUI
root.mainloop()
