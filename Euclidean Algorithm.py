print("Welcome to my first Python program!")

#This is just to get the hang of things on Python and programming in general
#I coded this after seeing a rectangular visualization of the Euclidean Algorithm in a documentary

#LargerNumber is the larger side of the rectangle
#SmallerNumber is the smaller side of the rectangle

def EuclideanAlgorithm():

    print("")
    print("Time for some GCFing!")
    print("")
    
    N1 = int(input("Enter a first number:"))

    N2 = int(input("Enter a second number:"))

    if N1 > N2:
        LargerNumber = N1
        SmallerNumber = N2
    else:
        LargerNumber = N2
        SmallerNumber = N1

    if LargerNumber % SmallerNumber == 0:
        Remainder = SmallerNumber


    while LargerNumber % SmallerNumber!= 0:
        Remainder = LargerNumber % SmallerNumber
        LargerNumber = SmallerNumber
        SmallerNumber = Remainder

    GCF = Remainder
    
    print("The GCF is:" , GCF)
    print("")

EuclideanAlgorithm()

Answer = input("Thanks for GCFing! Try again? (Y/N)")

while Answer == "Y":
    EuclideanAlgorithm()
    Answer = input("Thanks for GCFing! Try again? (Y/N)")
    
if Answer == "N":
    print("Fine. Bye, loser.")
else:
    print("Screw you!")

print ("")



