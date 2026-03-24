from random import randint

def get_color(color_number=4):
    # Making sure is a number and not a string
    color_number = int(color_number)

    switcher = {
                  0:'red',
                  1:'yellow',
                  2:'blue',
                  3:'green',
                  4:'black'
              }
    
    return switcher.get(color_number,"Invalid Color Number")

# ❌ ⬆ DON'T CHANGE THE CODE ABOVE ⬆ ❌

def get_allStudentColors():
    example_color = get_color(1)
    students_array = []
    # ✅ ↓ your loop here ↓ ✅
    #for i in range(10):
    return [get_color(randint(0,3)) for i in range(10)]

print(get_allStudentColors())
