#To enter two angle and using function third angle (angle1,angle2) calculate the 3rd angle.

angle1= int (input ("enter the 1st angle:"))
angle2=int(input("enter the 2nd angle:"))

def angle3(angle_x,angle_y):
    angle3 = angle_x +angle_y
    print (angle3)

c = angle3(angle_x,angle_y)
print(c)
