number_of_non_zeros = 0
survivor = []
class Generation:
    def __init__(self,col,row):
         
        self.col = col
        self.row = row

    

    def create_2D_array(self):
        """creating a 2D array of zeros"""

        myArray = [[0 for x in range(self.col)] for y in range(self.row)]
        return myArray

    def create_generation(self,myArray,value,postion):
        """creating a new game by inserting non-zero values in random position"""
        myArray.insert(postion,value)
        return myArray

    def get_position_of_elements(self,myArray):
        """getting postion of each non_zero elemet in my 2D array"""
        for i in myArray:
            for k in i:
                non_zero_position = [myArray.index(i),i.index(k)]
        return non_zero_position
    
    def neighbourhood_of_non_zeros(self,non_zero_position,myArray):
        """getting postions of non_zeros; horizontally,vertically and diagonally"""

        horizontal_neighbours_right = non_zero_position[0],non_zero_position[1]+1
        horizontal_neighbours_left = non_zero_position[0],non_zero_position[1]-1

        vertical_neighbours_newtop = non_zero_position[0] - 1,non_zero_position[1]
        vertical_neighbours_bottom = non_zero_position[0] + 1,non_zero_position[1]

        diagonally_neighbours_a = non_zero_position[0] - 1,non_zero_position[1]-1
        diagonally_neighbours_a1 = non_zero_position[0] + 1,non_zero_position[1]+1


        diagonally_neighbours_b = non_zero_position[0] + 1,non_zero_position[1]-1
        diagonally_neighbours_b1 = non_zero_position[0] - 1,non_zero_position[1]+1

        non_zero_neighbours_list = [horizontal_neighbours_right, horizontal_neighbours_left,
                                    vertical_neighbours_newtop, vertical_neighbours_bottom,
                                    diagonally_neighbours_a, diagonally_neighbours_a1,
                                    diagonally_neighbours_b,diagonally_neighbours_b1]
        return non_zero_neighbours_list


    def game_rules(self,non_zero_neighbours_list,non_zero_position,myArray):
        for i in non_zero_neighbours_list:
            if myArray[i[0]][i[1]] != 0:
                number_of_non_zeros +=1

            if 2 >= number_of_non_zeros >= 3: 
                return survivor.append(non_zero_position)  

            elif number_of_non_zeros == 0:
                myArray[non_zero_position[0]][non_zero_position[1]] = 0
                return myArray

            elif number_of_non_zeros >= 4:
                myArray[non_zero_position[0]][non_zero_position[1]] = 0
                return myArray
        return survivor

                    


                  



