classs student:

  def __init__(self, name, id):
      self.name = name
      self.id = id
      self.computer = self.Laptop()
       
  def __show__(self):
        print(self.name, self.id)
        self.computer.show()
       
  class Laptop:
     def __init__(self):
        self.brand = 'HP'
        self.cpu = 'i7'
        self.ram = 8
        
    def __show__(self):
        print(self.brand, self.cpu, self.ram)
       
    student_one = student ('Palash', 65302)
    student_two = student ('Anu', 30267)
    
   student_one.show()
   
   student_one.computer.brand()
   
   // or we can create a variable 
   
   computerOne = student_one.computer
   computerTwo = student_two.computer
   
/// you can create object of inner class inside the outer calss or you can create obhect of inner class outside the outer class provide you use outer class name to call

   
   student_one.show // will print the info and computer details of the particular student.
   
   
   
   
   
   
   
   
   
   
   
   
   
