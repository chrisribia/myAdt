class pyArray:
    def __init__(self,myArray):
        self.myArray = []
        self.myLen = 5

    def get_element(self,index):
        return self.myArray[index]

    def get_array_size(self):
        array_size = len(self.myArray)
        return array_size

   def add_element(self,element,array_size):   
        try:         
            if array_size < self.myLen:
                return self.myArray.append(element)
        except:
            raise ValueError("python array must maintain the size of {}".format(self.myLen))
            
    


        
