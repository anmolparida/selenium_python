
def check_traingle(side1, side2, side3):

    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        print('Enter Valid Inputs')
    elif (side1 > side2 + side3) or (side2 > side1 + side3) or (side1 > side2 + side1):
        print('Given lengths wont form a triangle')
    elif (side1 == side2 + side3) or (side2 == side1 + side3) or (side1 == side2 + side1):
        print('yes, it can form a degenerated triangle : formed by 3 colinear points')
    else:
        print('Yes, a triangle can be formed out of it')


check_traingle(-14, -11, -12)
