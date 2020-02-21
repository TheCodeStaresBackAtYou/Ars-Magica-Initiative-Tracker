#Health Monitor

#uses tkinter for gui elements
import tkinter as TK
from tkinter import *
import Dice as DC
import random
import ArsData as ARS


class Creature(TK.Toplevel):
    def simple_dice(self,initial_bonus):
        #calculate bonus on dice
        final_bonus = initial_bonus
        wound_penalty = 1
        for row_bonus in range(0,3):
            for colum_bonus in range(len(self.wounds[row_bonus])):
                if self.wounds[row_bonus][colum_bonus].get() == 1:
                    final_bonus -= wound_penalty
                
            wound_penalty += 2

        #roll and get results 
        result = DC.roll(1,final_bonus)
        roll_window = Toplevel()
        roll_window.title("Your Roll")

        rolled_Var = StringVar() 
        rolled_Label = Label(roll_window, textvariable=rolled_Var).grid(row=3,column=3,columnspan=2,rowspan=2)
        if self.wounds[4][0].get() == 1:
            rolled_Var.set("DEAD")
        elif self.wounds[3][0].get() == 1:
            rolled_Var.set("INCAPACITATED")
        else:
            rolled_Var.set("You rolled a " + str(result))


    def stress_dice(self,initial_bonus):
        #calculate bonus on dice
        final_bonus = initial_bonus
        wound_penalty = 1
        for row_bonus in range(0,3):
            for colum_bonus in range(len(self.wounds[row_bonus])):            
                if self.wounds[row_bonus][colum_bonus].get() == 1:
                    final_bonus -= wound_penalty
                
            wound_penalty += 2

         #roll and get results 
        result = DC.roll(0,final_bonus)
        roll_window = Toplevel()
        roll_window.title("Your Roll")

        
            
        rolled_Var = StringVar() 
        rolled_Label = Label(roll_window, textvariable=rolled_Var,justify=LEFT  ).grid(row=3,column=3,columnspan=2,rowspan=2)

        botch_starting_point = IntVar()

        #is called on a botch to run botch dice
        def check_botch():
            botch_botch_counter = 0
            for x in range(0,botch_starting_point.get()):
               if random.randint(0,9) == 0:
                   botch_botch_counter += 1
            botch_counter_Var = StringVar() 
            botch_counter_Label = Label(roll_window, textvariable=botch_counter_Var)
            rolled_Var.set("You rolled " + str(botch_botch_counter) + " botches.")    


        #setting display
        if self.wounds[4][0].get() == 1:
            rolled_Var.set("DEAD")
        elif self.wounds[3][0].get() == 1:
            rolled_Var.set("INCAPACITATED")    
        elif result == "Botch" :
            rolled_Var.set("You rolled a " + str(result) + "\n" + ARS.Ars_Data.botch_chance )
            botchButton = TK.Button(roll_window, text = "Botch Roll.", command = check_botch)
            botchButton.grid(row=0,column=4)
            botch_starting_point = IntVar()
            botch_spin = TK.Spinbox(roll_window, from_=1, to=10,textvariable=botch_starting_point,width=6).grid(row=0,column=3)
            botch_starting_point.set(1)
        else:
            rolled_Var.set("You rolled a " + str(result))


         


            
        

    def __init__(self, parent,name,size,soak,turn, *args, **kwargs):

        #Data and intialization
        TK.Toplevel.__init__(self, parent, *args, **kwargs)
        self.title(name)
        self.parent = parent    
        self.wounds = [[IntVar(),IntVar(),IntVar(),IntVar(),IntVar()],\
                       [IntVar(),IntVar(),IntVar(),IntVar(),IntVar()],\
                       [IntVar(),IntVar(),IntVar(),IntVar(),IntVar()],\
                       [IntVar()],\
                       [IntVar()]]
        self.name = name
        self.size = size
        self.soak = soak
        self.turn = turn


            #checkbuttons
        for row_I in range(len(self.wounds)):
             for colum_I in range(len(self.wounds[row_I])):
                Checkbutton(self, offvalue=0, onvalue=1, \
                           var=self.wounds[row_I][colum_I]).grid(row=row_I,column=colum_I +1)
      
          #Light label
        lightVar = StringVar()
        lightVar.set("1-" + str(5 + self.size))
        lightLabel = Label(self, textvariable=lightVar ).grid(row=0,column=0)

          #Medium label
        mediumVar = StringVar() 
        mediumLabel = Label(self, textvariable=mediumVar ).grid(row=1)
        mediumVar.set(str(6 + int(self.size))+ "-" + str(10 + self.size))

          #Heavy label 
        hardVar = StringVar() 
        hardLabel = Label(self, textvariable=hardVar ).grid(row=2)
        hardVar.set(str(11 + int(self.size))+ "-" + str(15 + self.size))
    

          #incapacitating label
        incVar = StringVar() 
        incLabel = Label(self, textvariable=incVar ).grid(row=3)
        incVar.set(str(16 + int(self.size))+ "-" + str(21 + self.size))
      
      
          #Dead label 
        deadVar = StringVar() 
        deadLabel = Label(self, textvariable=deadVar ).grid(row=4)
        deadVar.set(str(21 + self.size) + "+" )

          #Soak Label
        soak_output = StringVar() 
        soak_label = Label(self, textvariable=soak_output ).grid(row=3,column=2,columnspan=2)
        soak_output.set("Soak: " + str(self.soak))

          #Size Label
        size_Var = StringVar() 
        size_Label = Label(self, textvariable=size_Var ).grid(row=4,column=2,columnspan=2)
        size_Var.set("Size: " + str(self.size))

          #Turn Label
        turn_Var = StringVar() 
        turn_Label = Label(self, textvariable=turn_Var ).grid(row=3,column=4,columnspan=2)
        turn_Var.set("Turn: " + str(self.turn))

          #Roll Label
        roll_Var = StringVar() 
        roll_Label = Label(self, textvariable=turn_Var ).grid(row=3,column=4,columnspan=2)
        roll_Var.set("Roll: " + str(self.turn))

          #Modifier Information
        starting_point = IntVar()
        bonus_spin = TK.Spinbox(self, from_=-50, to=50,textvariable=starting_point,width=6).grid(row=4,column=4,columnspan=2)
        starting_point.set(0)


            #dice reroute functions. If this is not here starting_point variable can't be reached by _dice functions
        def simple_re_dice():
            self.simple_dice(starting_point.get())
        
        def stress_re_dice():
            self.stress_dice(starting_point.get())



          #Dice buttons
        simpleButton = TK.Button(self, text = "Simple Roll.", command = simple_re_dice)
        simpleButton.grid(row = 5,column=0, columnspan=2)

        stressButton = TK.Button(self, text = "Stress Roll.", command = stress_re_dice)
        stressButton.grid(row = 5,column=2, columnspan=2)

        
        
    






    #simple function to make creating a creature more easy
def new_creature(parent,name,size,soak,turn):
        new_CR = Creature(parent,name,size,soak,turn)
        return new_CR
    
