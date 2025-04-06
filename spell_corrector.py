#Python program to create a Spell Corrector GUI using Tkinter in Python  
# importing all the required modules into our program   
from tkinter import *  
from textblob import TextBlob  
  
# Creating a method to clear all the data from the entry boxes  
def clrAll() :  
   
 # Deleting all the data inside the entry boxes  
 word1_place.delete(0, END)  
 word2_place.delete(0, END)  
  
# Creating a new method to get the corrected word in the box  
def crction() :  
  
 # getting the word as input from the user in the entry box  
 input_wrd = word1_place.get()  
  
 # creating a new TextBlob obj.  
 blob_objct = TextBlob(input_wrd)  
  
 # getting the corrected word for the incorrect word  
 crctd_word = str(blob_objct.correct())  
  
 # applying the insert method for the insertion of any value into  
 # the data entry box.  
 word2_place.insert(10, crctd_word)  
  
  
# Main code  
if __name__ == "__main__" :  
  
 # Creating a new Graphical User Interface(GUI) window with Tkinter instance  
 base = Tk()  
  
 # Setting the colour of the background for the GUI window  
 base.configure(background = 'light green')  
   
 # Setting the dimensions of the GUI window as < Width x Height >  
 base.geometry("400x150")  
  
 # Alotting a name to the GUI window  
 base.title("Spell Corrector")  
   
 # Creating the heading label as Welcome to Spell Corrector Application :  
 headlbl = Label(base , text = 'Welcome to Spell Corrector Application' ,  
     fg = 'black' , bg = "red")  
   
# Creating another label for the word to be entered, as "Input Word" :  
 lbl1 = Label(base , text = "Input Word" ,  
    fg = 'black' , bg = 'dark green')  
    
 # Creating another label for the corrected word to be shown, as "Corrected Word" :  
 lbl2 = Label(base , text = "Corrected Word" ,  
    fg = 'black' , bg = 'dark green')  
   
   
 # grid functions is used for positioning  
 # the widgets at certain places  
 # in a tabular arrangement .  
 # padx keyword is used for setting the padding along x-axis .  
 headlbl.grid(row = 0 , column = 1)  
 lbl1.grid(row = 1 , column = 0)  
 lbl2.grid(row = 3 , column = 0 , padx = 10)  
  
    
 # Creating the entry boxes for entering the words  
 # or the required text .  
 word1_place = Entry()  
 word2_place = Entry()  
    
 # padx keyword is used for setting the padding along x-axis .  
 # pady keyword is used for setting the padding along y-axis .  
 word1_place.grid(row = 1, column = 1, padx = 10, pady = 10)  
 word2_place.grid(row = 3, column = 1, padx = 10, pady = 10)  
  
    
# Creating a new variable for the Correction Button to work on   
# getting clicked y calling the correction method  
 btn1 = Button(base , text = "Correction" , bg = "red" , fg = "black" ,  
        command = crction)  
    
 btn1.grid(row = 2 , column = 1)  
   
 # Creating another button to clear the existing text by being   
 # called using the clrAll method  
 btn2 = Button(base , text = "Clear" , bg = "red" ,  
     fg = "black" , command = clrAll)  
   
 btn2.grid(row = 4 , column = 1)  
   
 # Running the GUI  
 base.mainloop()  
