class my_2d_Array:
    def __init__(self,col,row):
        """initializing"""
        self.col = col
        self.row = row

    def create_2d_array(self):
        """creating a 2D array"""
        my_2d_array = [[0]*self.col in range(self.row)]
        return my_2d_array

    def shape(self):
        """return number of columns and rows"""
        return self.col, self.row
    
    def clear_array(self,my_2d_array):
        """replace values with "k" or anything else"""

        my_2d_array = [["a" for _ in range(self.col)]for _ in range(self.row)]
        return my_2d_array

   
    def get_element(self,my_2d_array):
        """get a specified row and column value"""
        try:
             return my_2d_array[self.row][self.col]
        except:
            raise ValueError("unknown index")

    def set_element(self,my_2d_array,get_element,new_value):
        """update element"""

        my_2d_array = get_element = new_value
        return (my_2d_array)

    def remove_item(self,get_element,my_2d_array):
        """remove value"""    

        return my_2d_array.pop(get_element)


