"""
I've made the assumption assumptions:
- Moving starts after the first BEGIN, even if integers or directions are input before
- If there is an integer after BEGIN but before the first direction, this gets ignored
    e.g. [BEGIN, 3, LEFT, 3...]
- If consecutive integers are listed after a direction, these get added up 
    e.g. [.., LEFT, 3, 4, 1, RIGHT, 2...] -> We move 8 to the left and 2 to the right
"""
from math import sqrt

def robot_x_y(input_list):
    x, y = 0, 0
    i = input_list.index('BEGIN')+1
    print("Started")
    while i<len(input_list):
        if input_list[i] == 'LEFT':
            j = 1
            while type(input_list[i+j])==int:
                x=x-input_list[i+j]
                print(f"Moved {input_list[i+j]} left")
                j+=1
            i=i+j
        elif input_list[i] == 'RIGHT':
            j = 1
            while type(input_list[i+j])==int:
                x=x+input_list[i+j]
                print(f"Moved {input_list[i+j]} right")
                j+=1
            i=i+j
        elif input_list[i] == 'DOWN':
            j = 1
            while type(input_list[i+j])==int:
                y=y-input_list[i+j]
                print(f"Moved {input_list[i+j]} down")
                j+=1
            i=i+j
        elif input_list[i] == 'UP':
            j = 1
            while type(input_list[i+j])==int:
                y=y+input_list[i+j]
                print(f"Moved {input_list[i+j]} up")
                j+=1
            i=i+j
        elif input_list[i] == 'STOP':
            print("Stopped")
            break
    return(sqrt(x**2 + y**2))


input_list = [1, 'LEFT', 3, 4, 'BEGIN', 'LEFT', 4, 5, 3, 'RIGHT', 6, 'DOWN', 4, 6, 'UP', 'STOP', 4]

robot_distance = robot_x_y(input_list)
print(f"Total distance traveled from (0,0) is {robot_distance} units")