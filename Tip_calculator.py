print("| Calculator |")
print("+------------+")
print("| 7  8  9  ÷ |")
print("| 4  5  6  × |")
print("| 1  2  3  - |")
print("| 0  .  =  + |")
print("+------------+")

print("Welcome to the tip calculator !")
bill=float(input("""What was the total bill🃏? \n $"""))
tip=int(input("How much tip💵 would you like to give? 10, 12 or 15?  "))
div=int(input("How many people to split➗ the bill?  "))
result=bill+tip/div
total_bill=(round(result,2))
print(f"Each person should pay: ${total_bill}")