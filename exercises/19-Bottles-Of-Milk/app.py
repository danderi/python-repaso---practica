# ✅↓ Write your code here ↓✅
def number_of_botles():
    count = 99
    while count >= 0:
        if count == 1:
            print(f'{count} bottles of milk on the wall, {count} bottles of milk. Take one down and pass it around, no bottles of milk on the wall.')
        elif count == 0:
            print("No more bottles of milk on the wall, no more bottles of milk. Go to the store and buy some more, 99 bottles of milk on the wall.")    
        else:   
            print(f'{count} bottles of milk on the wall, {count} bottles of milk. Take one down and pass it around, {count-1} bottles of milk on the wall.')
        count-=1

number_of_botles()