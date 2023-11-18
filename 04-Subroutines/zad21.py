import mykeyboard 
import mymath


num = mykeyboard.read_number()
numc = mymath.generate_number()
print(f"Computer number: {numc}")

if num == numc:
    print("You won the game!!")