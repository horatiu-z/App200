""" For this program we don't need to impot any libraries"""

""" To make it interesting, we won't just do it for 200$, we'll ask the user for the sum they want to check out and set a default to 200"""

def insert_value():
    x = input("Please enter the value you want to check. If you want to check for 200$ just press enter ")
    try:
        x = int(x)
        return x
    except:
        x = 200
        return x

"""Now for the main program, we want to divide the number to 2 as many times as posible, and substract 1 only when it's not possible to divide by 2"""

def moves_to_make(sum):
    """Create a list of stept so take, and reverse it at the end"""
    list_of_steps=[]
    count = 0
    while sum > 1:
        if sum % 2 == 0:
            sum = sum / 2
            list_of_steps.append("Multiply {}$ with 2 = {}$".format(sum,sum*2))
            count += 1
        else:
            sum = sum-1
            list_of_steps.append("Added 1$ to {}$ = {}$".format(sum,sum+1))
            count += 1
    return count, reversed(list_of_steps)

""" Now, let's just execute the program"""

if __name__ == '__main__':
    sum = insert_value()
    steps, moves = moves_to_make(sum)
    print("{} steps as follows:".format(steps))
    y = 1
    for move in moves:
        print("step {}. {}".format(y,move))
        y += 1
