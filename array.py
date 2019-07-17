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
        if array_size < self.myLen:
            return self.myArray.append(element)
        else:
            return "python array size cannot be expanded beyond {}".format(self.myLen)
    


        