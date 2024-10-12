import math

sin = math.sin
pi  = math.pi

for i in range(41) :
    x = int(((sin(float(i) / 40.0 * 2 * pi))+1)*40)
    character_count_per_line = x # Change this line to print out sine curve correctly.
    
    output_str = ' ' * character_count_per_line + '*'
    print (output_str)