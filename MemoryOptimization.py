from tkinter import * 

class MemoryOptimization:
    def __init__(self, master):
        self.master = master
        self.master.title("Memory Optimization Calculator")

        self.system_var = StringVar()
      
        self.basic_opt_1_var = StringVar()
        self.basic_opt_2_var = StringVar()
        self.basic_opt_3_var = StringVar()
            
        self.advance_opt_1_var = StringVar()
        self.advance_opt_2_var = StringVar()
        self.advance_opt_3_var = StringVar()
        


        self.system_label = Label(self.master, text="Computer Class:")
        self.system_label.pack()
        self.system_dropdown = OptionMenu(self.master, self.system_var, "PMDs", "Desktop", "Server", "Warehouse scale", "Embeded")
        self.system_dropdown.pack()

      
        self.basic_opt_1_label = Label(self.master, text="Basic Optimization 1:")
        self.basic_opt_1_label.pack()
        self.basic_opt_1_dropdown = OptionMenu(self.master, self.basic_opt_1_var, "Larger block size", "Larger total cache", "Higher associativity", "Higher number of cache levels", "Giving priority to read misses over writes", "Avoiding address translation in cache indexing", "None")
        self.basic_opt_1_dropdown.pack()
      
        self.basic_opt_2_label = Label(self.master, text="Basic Optimization 2:")
        self.basic_opt_2_label.pack()
        self.basic_opt_2_dropdown = OptionMenu(self.master, self.basic_opt_2_var, "Larger block size", "Larger total cache", "Higher associativity", "Higher number of cache levels", "Giving priority to read misses over writes", "Avoiding address translation in cache indexing", "None")
        self.basic_opt_2_dropdown.pack()

            
        self.basic_opt_3_label = Label(self.master, text="Basic Optimization 3:")
        self.basic_opt_3_label.pack()
        self.basic_opt_3_dropdown = OptionMenu(self.master, self.basic_opt_3_var, "Larger block size", "Larger total cache", "Higher associativity", "Higher number of cache levels", "Giving priority to read misses over writes", "Avoiding address translation in cache indexing", "None")
        self.basic_opt_3_dropdown.pack()

  
        self.advance_opt_1_label = Label(self.master, text="Advanced Optimization 1:")
        self.advance_opt_1_label.pack()
        self.advance_opt_1_dropdown = OptionMenu(self.master, self.advance_opt_1_var, "Small and simple first level caches", "Way Prediction", "Pipelining Cache", "Nonblocking Caches", "Multibanked Caches", "Critical Word First, Early Restart", "Merging Write Buffer", "Compiler Optimizations", "Hardware Prefetching", "Compiler Prefetching", "None")
        self.advance_opt_1_dropdown.pack()

        self.advance_opt_2_label = Label(self.master, text="Advanced Optimization 2:")
        self.advance_opt_2_label.pack()
        self.advance_opt_2_dropdown = OptionMenu(self.master, self.advance_opt_2_var, "Small and simple first level caches", "Way Prediction", "Pipelining Cache", "Nonblocking Caches", "Multibanked Caches", "Critical Word First, Early Restart", "Merging Write Buffer", "Compiler Optimizations", "Hardware Prefetching", "Compiler Prefetching", "None")
        self.advance_opt_2_dropdown.pack()

        self.advance_opt_3_label = Label(self.master, text="Advanced Optimization 3:")
        self.advance_opt_3_label.pack()
        self.advance_opt_3_dropdown = OptionMenu(self.master, self.advance_opt_3_var, "Small and simple first level caches", "Way Prediction", "Pipelining Cache", "Nonblocking Caches", "Multibanked Caches", "Critical Word First, Early Restart", "Merging Write Buffer", "Compiler Optimizations", "Hardware Prefetching", "Compiler Prefetching", "None")
        self.advance_opt_3_dropdown.pack()
       
        
        self.calculate_button = Button(self.master, text="Calculate", command=self.calculate)
        self.calculate_button.pack()
        
        self.result_label = Label(self.master, text="")
        self.result_label.pack()

             

      
    def calculate(self):

        self.power = 0
        self.cost = 0
        self.performance = 0
      
        system_var = self.system_var.get()
        basic_opt_1 = self.basic_opt_1_var.get()
        basic_opt_2 = self.basic_opt_2_var.get()
        basic_opt_3 = self.basic_opt_3_var.get()
        advance_opt_1 = self.advance_opt_1_var.get()
        advance_opt_2 = self.advance_opt_2_var.get()
        advance_opt_3 = self.advance_opt_3_var.get()

        if system_var == "PMDs":
          self.power_bdgt = 20
          self.cost_bdgt = 25
          self.performance_bdgt = 30
        elif system_var == "Desktop":
          self.power_bdgt = 35
          self.cost_bdgt = 50
          self.performance_bdgt = 50
        elif system_var == "Server":
          self.power_bdgt = 80
          self.cost_bdgt = 70
          self.performance_bdgt = 80
        elif system_var == "Warehouse scale":
          self.power_bdgt = 40
          self.cost_bdgt = 50
          self.performance_bdgt = 40
        elif system_var == "Embeded" :
          self.power_bdgt = 10
          self.cost_bdgt = 10
          self.performance_bdgt = 20
        else :
          self.power_bdgt = 0
          self.cost_bdgt = 0
          self.performance_bdgt = 0

        for x in range(3):
          if(x == 1):
            basic_opt = basic_opt_1
          elif (x == 2):
            basic_opt = basic_opt_2
          else:
            basic_opt = basic_opt_3

          if basic_opt == "Larger block size":
            self.power += 0
            self.cost += 0
            self.performance += 5
          elif basic_opt == "Larger total cache":
            self.power += 15
            self.cost += 15
            self.performance += 15
          elif(basic_opt == "Higher associativity"):
            self.power += 5
            self.cost += 0
            self.performance += 10
          elif(basic_opt == "Higher number of cache levels"):
            self.power += 10
            self.cost += 10
            self.performance += 15
          elif(basic_opt == "Giving priority to read misses over writes"):
            self.power += 0
            self.cost += 0
            self.performance += 5
          elif(basic_opt == "Avoiding address translation in cache indexing"):
            self.power += 0
            self.cost += 0
            self.performance += 10
          else: #None
            self.power += 0
            self.cost += 0
            self.performance += 0

        for x in range(3):
          if(x == 1):
            advance_opt = advance_opt_1
          elif (x == 2):
            advance_opt = advance_opt_2
          else:
            advance_opt = advance_opt_3
            
          if advance_opt == "Small and simple first level caches":
            self.power += -5
            self.cost += -5
            self.performance += 5
          elif advance_opt == "Way Prediction":
            self.power += -5
            self.cost += 0
            self.performance += 5            
          elif advance_opt == "Pipelining Cache":            
            self.power += 0
            self.cost += 0
            self.performance += 10            
          elif advance_opt == "Nonblocking Caches":            
            self.power += 5
            self.cost += 5
            self.performance += 5            
          elif advance_opt == "Multibanked Caches":            
            self.power += -5
            self.cost += 0
            self.performance += 10            
          elif advance_opt == "Critical Word First, Early Restart":            
            self.power += 3
            self.cost += 5
            self.performance += 5            
          elif advance_opt == "Merging Write Buffer":            
            self.power += 0
            self.cost += 0
            self.performance += 5            
          elif advance_opt == "Compiler Optimizations":            
            self.power += 3
            self.cost += 0
            self.performance += 10            
          elif advance_opt == "Hardware Prefetching":            
            self.power += 5
            self.cost += 5
            self.performance += 10            
          elif advance_opt == "Compiler Prefetching":
            self.power += 2
            self.cost += 0
            self.performance += 5            
          else: #None 
            self.power += 0
            self.cost += 0
            self.performance += 0            

        self.power = self.power_bdgt - self.power
        self.cost = self.cost_bdgt - self.cost
        self.performance = self.performance - self.performance_bdgt
              
        self.result = "Power: {} Cost: {} Performance: {}"
        self.result_label.config(text=   self.result.format(self.power,self.cost, self.performance) )

root = Tk()
app = MemoryOptimization(root)
root.mainloop()
