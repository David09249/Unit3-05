# Created by: David Wang
# Created on: 14-Oct-2017
# Created for: ICS3U
# Daily Assignment - Unit 3-05
# This program calculates the factorial of a number

import ui

def calculate_factorial_touch_up_inside(sender):
    
    # constants
    integer = 1
    number = 1
    
    # input 
    user = int(view['user_input_textbox'].text)
   
    # process 
    if user < 0:
    	 # output
       view['answer_label'].text = "Please enter a non negative value."
       return
       
    while integer <= user:
          number = integer * number     
          integer = integer + 1
    #output          
    view['answer_label'].text = "The factorial is: " + str(number)

view = ui.load_view()
view.present('full_screen')
