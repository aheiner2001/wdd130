# No one under 36 inches may ever ride, either by themselves or with another rider.

# Normally, two riders sit in the car together. A single rider can only ride if they are at least 18 years old and are at least 62 inches tall.

# If there are two riders and one of them is at least 18 years old, they may ride together.

# Defined Variables
rider = "first"


# FUNCTIONS
def no():
    print("You may not ride")

def questions():
    global rider
    global age
    global height
    age = int(input(f"What is the age of the {rider} rider? "))
    height = int(input(f"What is the height of the {rider} rider in inches? "))
   
def yes():
    print("Welcome to the ride. Please be safe and have fun!")
def questions2():
    global rider
    global age2
    global height2
    age2 = int(input(f"What is the age of the {rider} rider? "))
    height2 = int(input(f"What is the height of the {rider} rider? "))
    if height < 36:
        no()
    
def one_rider():
    if age >=12 and age <=17
        responde= input("Do you have a golden passport? ")
        if responde == "yes":
            age = 18
    if height < 36:
        no()
    elif height < 62 or age < 18:
        no()
    else:
        yes() 



def two_rider():
    
    if age >= 18 or age2 >=18 and (height >=  36 and height2 >= 36 ):
        yes()
    if age >=12 and age <=17:
        responde= input("Doesyou have a golden passport? ")
        if responde == "yes":
            age = 18
    elif age >= 12 and age2 >=12 and height >=52 and height2 >=52:
        yes()
    
    else:
        no()
both at least 12 years old and at least 52 inches tall.

If a person is age 12–17, ask if that person has a golden passport. If they do, they should be treated as if they were 18 years old for the sake of all rules. (Don't forget to apply this to the single rider case.)

If there are two riders, but neither one is at least 18 years old, they may still ride if one rider is at least 16 years old and the other is at least 14. (Keep in mind that the first rider may be the younger of the two or they may be the older of the two.)





# Running the code

questions()
answer = input("Is there a second rider (yes/no)? ")
if answer == "yes":
    rider = "second"
    questions2()
    two_rider()
else:
    one_rider()





# Sorry, you may not ride.
# Welcome to the ride. Please be safe and have fun!
