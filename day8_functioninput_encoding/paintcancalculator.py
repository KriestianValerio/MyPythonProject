import math

def paint_calc(height,width,coverage):
    num_cans = (height*width)/coverage
    round_up_cans = math.ceil(num_cans)
    print(f"you will need {round_up_cans} cans")

inputtedheight = int(input())
inputtedwidth = int(input())
inputtedcoverage = 5

paint_calc(height=inputtedheight,width=inputtedwidth,coverage=inputtedcoverage)



