
#Design a creative UI using Python's tkinter module to calculate the total cost of a pizza. The UI should have (at least) each widget that was covered in class:

#Frames
#Labels
#input box
#buttons
#radio buttons
#check boxes
#You can use check boxes for for selecting toppings (each with a different cost), radio buttons for the type of crust selected (each with a different cost), buttons for calculation and quit. The input box can be used to record the name of the person placing the order. Use a message box to display the total cost of the pizza along with the name of the person placing the order.

#Make sure your design is well laid out and intuitive to the user. Take account of spacing and packing so that everything is properly aligned and professional looking. Be creative with font, color, size, etc.



import tkinter
import tkinter.messagebox

##### main screen #####

class pizza_cost:
    def __init__(self):
      self.main_window = tkinter.Tk()

      self.main_window.geometry("200x200")
      self.main_window.title("Enter order name")
      self.main_window.configure(bh = "gray")

      self.top_frame = tkinter.Frame(self.main_window)
      self.bottom_frame = tkinter.Frame(self.main_window)

      self.prompt_label = tkinter.label(self.name_frame, text = "Enter order name")
      self.crust_label = tkinter.label(self.middle_frame,text='Select Crust')
      self.toppings_label = tkinter.label(self.bottom_frame,text='Select Toppings')
      self.name_entry = tkinter.entry(self.name_frame,width=50)

      self.prompt_label.pack(side='left')
      self.name_entry.pack(side='right')
      self.crust_label.pack(side='left')
      self.toppings_label.pack(side='left')

      ##### Crust - radio boxes #####

      self.rv = tkinter.intvar()

      self.rb_c1 = tkinter.checkbutton(self.middle_frame,text='Stuffed Crust', variable = self.rv, value=1)
      self.rb_c2 = tkinter.checkbutton(self.middle_frame,text='New York', variable = self.rv, value=2)
      self.rb_c3 = tkinter.checkbutton(self.middle_frame,text='Sicilian', variable = self.rv, value=3)

      ##### Toppings - check boxes #####

      self.cb_t1 = tkinter.intvar()
      self.cb_t2 = tkinter.intvar()
      self.cb_t3 = tkinter.intvar()
      self.cb_t4 = tkinter.intvar()
      self.cb_t5 = tkinter.intvar()

      self.cb_t1.set(0)
      self.cb_t2.set(0)
      self.cb_t3.set(0)
      self.cb_t4.set(0)
      self.cb_t5.set(0)

      self.cb1 = tkinter.checkbutton(self.top_frame,text="Pepperoni",variable=self.cb_t1)
      self.cb1 = tkinter.checkbutton(self.top_frame,text="Sausage",variable=self.cb_t2)
      self.cb1 = tkinter.checkbutton(self.top_frame,text="Bacon",variable=self.cb_t3)
      self.cb1 = tkinter.checkbutton(self.top_frame,text="Pineapple",variable=self.cb_t4)
      self.cb1 = tkinter.checkbutton(self.top_frame,text="Cannadian Bacon",variable=self.cb_t5)

      ##### Calculation - buttons #####

      self.rb_c1.pack(side = 'left')
      self.rb_c2.pack(side = 'left')
      self.rb_c3.pack(side = 'left')

      self.cb_t1.pack(side = 'left')
      self.cb_t2.pack(side = 'left')
      self.cb_t3.pack(side = 'left')
      self.cb_t4.pack(side = 'left')
      self.cb_t5.pack(side = 'left')

      self.calc_button = tkinter.button(self.main_window,text='Calculate Pizza Cost',command=self.calc)
      self.quit_button = tkinter.button(self.main_window,text='Quit',comand=self.main_window.destroy)

      self.name_frame.pack(side='top')
      self.middle_frame.pack(side='top')
      self.bottom_frame.pack(side='top')

      self.quit_button.pack(side='bottom')
      self.calc_buttton.pack(side='bottom')

      tkinter.mainloop()

    def calc(self):
        self.message = 'Crust:' '\n' + 'Toppings:'
        self.total = 0

        if self.cb_t1.get() == 1:
            self.message += 'Pepperoni \n'
            self.total = 5

        
        if self.cb_t1.get() == 1:
            self.message += 'Sausage \n'
            self.total += 5

        if self.cb_t1.get() == 1:
            self.message += 'Bacon \n'
            self.total += 5

        if self.cb_t1.get() == 1:
            self.message += 'Pineapple \n'
            self.total += 5

        if self.cb_t1.get() == 1:
            self.message += 'Canadian Bacon \n'
            self.total += 5

        if self.rv.get() == 1:
            self.message += 'Stuffed Crust \n'

        if self.rv.get() == 2:
            self.message += 'New York \n'

        if self.rv.get() == 3:
            self.message += 'Sicilian \n'




calc_cost = pizza_cost()
    