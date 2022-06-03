#If below program does not work, you are missing the library sympy. To fix, simply download the library in your ide/debugger.
#If using cs50 ide, type python example.py <-- example is whatever filename you named it

import sympy as a

equation = 0
numerator = 0
denominator = 0
print("This Program is a Calculator Used For Definite or Indefinite Integrals")
print("Presented and Created by: Munahim Ahmed\n")

ifDivision = input("Is your equation being divided? (yes or no)\n").lower()

choice = input("[Definite or Indefinite?]\n").lower()
x = a.Symbol("x")

#Code for definite
if (choice == "definite"):
    toFTerm = input("Is there a term in your equation? (yes or no)\n").lower()

    if (ifDivision == "yes"):

        temp = 0

        while (toFTerm == "yes"):

            typeFraction = input("Numerator or denominator (n or d)?\n")
            coefficient = int(input("What's the coefficient?\n"))
            print("\nOnly input one of these options.")
            specialVar = input("Is there a variable (x), euler's number (e), trig (tan, cos, sin, arctan, arccos, arcsin), constant (input as no) ?\n").lower()
            value = int(input("What's the exponent (variable or euler) or value (value for trig and logarithms)? Only numerical numbers?\n"))


            if (specialVar == "x"):
                temp = coefficient*(x**value)
                nTerm = input("Is there another term? (yes or no)\n").lower()
                toFTerm = nTerm

            if (specialVar == "e"):
                v = a.exp(value)
                temp = coefficient*(v)
                nTerm = input("Is there another term? (yes or no)\n").lower()
                toFTerm = nTerm

            if (specialVar == "tan"):
                v = a.tan(value)
                temp = coefficient*(v)
                nTerm = input("Is there another term? (yes or no)\n").lower()
                toFTerm = nTerm

            if (specialVar == "sin"):
                v = a.sin(value)
                temp = coefficient*(v)
                nTerm = input("Is there another term? (yes or no)\n").lower()
                toFTerm = nTerm

            if (specialVar == "cos"):
                v = a.cos(value)
                temp = coefficient*(v)
                nTerm = input("Is there another term? (yes or no)\n").lower()
                toFTerm = nTerm

            if (specialVar == "arctan"):
                v = a.atan(value)
                temp = coefficient*(v)
                nTerm = input("Is there another term? (yes or no)\n").lower()
                toFTerm = nTerm

            if (specialVar == "arcsin"):
                v = a.asin(value)
                temp = coefficient*(v)
                nTerm = input("Is there another term? (yes or no)\n").lower()
                toFTerm = nTerm

            if (specialVar == "arccos"):
                v = a.acos(value)
                temp = coefficient*(v)
                nTerm = input("Is there another term? (yes or no)\n").lower()
                toFTerm = nTerm

            if (specialVar == "no"):
                temp = coefficient
                nTerm = input("Is there another term? (yes or no)\n").lower()
                toFTerm = nTerm

            if (typeFraction == "n"):
                numerator += temp

            if (typeFraction == "d"):
                denominator += temp


        if (denominator == 0):
            print("Nothing can be done with the equation, it is undefined.")

        else:
            a1 = int(input("What value is your a (lower limit)? "))
            b1 = int(input("What's value is your b (upper limit)? "))

            def f(x):
                return numerator
            def g(x):
                return denominator

            print("::LOADING::")
            print("Here's your solution to the integral of the equation ["+str(numerator)+ "/" + str(denominator)+ "] from "+str(a1)+ " to " +str(b1)+ ":")
            print(a.integrate(f(x)/g(x), (x, a1, b1)))

    elif (ifDivision == "no"):
        temp = 0

        while (toFTerm == "yes"):

            coefficient = int(input("What's the coefficient?\n"))
            print("\nOnly input one of these options.")
            specialVar = input("Is there a variable (x), euler's number (e), trig (tan, cos, sin, arctan, arccos, arcsin), constant (input as no) ?\n").lower()
            value = int(input("What's the exponent (variable or euler) or value (value for trig and logarithms)? Only numerical numbers?\n"))


            if (specialVar == "x"):
                equation += coefficient*(x**value)
                nTerm = input("Is there another term? (yes or no)\n").lower()
                toFTerm = nTerm

            if (specialVar == "e"):
                v = a.exp(value)
                equation += coefficient*(v)
                nTerm = input("Is there another term? (yes or no)\n").lower()
                toFTerm = nTerm

            if (specialVar == "tan"):
                v = a.tan(value)
                equation += coefficient*(v)
                nTerm = input("Is there another term? (yes or no)\n").lower()
                toFTerm = nTerm

            if (specialVar == "sin"):
                v = a.sin(value)
                equation += coefficient*(v)
                nTerm = input("Is there another term? (yes or no)\n").lower()
                toFTerm = nTerm

            if (specialVar == "cos"):
                v = a.cos(value)
                equation += coefficient*(v)
                nTerm = input("Is there another term? (yes or no)\n").lower()
                toFTerm = nTerm

            if (specialVar == "arctan"):
                v = a.atan(value)
                equation += coefficient*(v)
                nTerm = input("Is there another term? (yes or no)\n").lower()
                toFTerm = nTerm

            if (specialVar == "arcsin"):
                v = a.asin(value)
                equation += coefficient*(v)
                nTerm = input("Is there another term? (yes or no)\n").lower()
                toFTerm = nTerm

            if (specialVar == "arccos"):
                v = a.acos(value)
                equation += coefficient*(v)
                nTerm = input("Is there another term? (yes or no)\n").lower()
                toFTerm = nTerm

            if (specialVar == "no"):
                equation += coefficient
                nTerm = input("Is there another term? (yes or no)\n").lower()
                toFTerm = nTerm



        a1 = int(input("What value is your a (lower limit)? "))
        b1 = int(input("What's value is your b (upper limit)? "))

        def f(x):
            return equation

        print("::LOADING::")
        print("Here's your solution to the integral of the equation ["+str(equation)+"] from "+str(a1)+ " to " +str(b1)+ ":")
        print(a.integrate(f(x), (x, a1, b1)))

    else:
        print("Invalid Input")

#Code for indefinite
elif (choice == "indefinite"):
    toFTerm = input("Is there a term in your equation? (yes or no)\n").lower()

    if (ifDivision == "yes"):

        temp = 0

        while (toFTerm == "yes"):

            typeFraction = input("Numerator or denominator (n or d)?\n")
            coefficient = int(input("What's the coefficient?\n"))
            print("\nOnly input one of these options.")
            specialVar = input("Is there a variable (x), euler's number (e), trig (tan, cos, sin, arctan, arccos, arcsin), constant (input as no) ?\n").lower()
            value = int(input("What's the exponent (variable or euler) or value (value for trig and logarithms)? Only numerical numbers?\n"))


            if (specialVar == "x"):
                temp = coefficient*(x**value)
                nTerm = input("Is there another term? (yes or no)\n").lower()
                toFTerm = nTerm

            if (specialVar == "e"):
                v = a.exp(value)
                temp = coefficient*(v)
                nTerm = input("Is there another term? (yes or no)\n").lower()
                toFTerm = nTerm

            if (specialVar == "tan"):
                v = a.tan(value)
                temp = coefficient*(v)
                nTerm = input("Is there another term? (yes or no)\n").lower()
                toFTerm = nTerm

            if (specialVar == "sin"):
                v = a.sin(value)
                temp = coefficient*(v)
                nTerm = input("Is there another term? (yes or no)\n").lower()
                toFTerm = nTerm

            if (specialVar == "cos"):
                v = a.cos(value)
                temp = coefficient*(v)
                nTerm = input("Is there another term? (yes or no)\n").lower()
                toFTerm = nTerm

            if (specialVar == "arctan"):
                v = a.atan(value)
                temp = coefficient*(v)
                nTerm = input("Is there another term? (yes or no)\n").lower()
                toFTerm = nTerm

            if (specialVar == "arcsin"):
                v = a.asin(value)
                temp = coefficient*(v)
                nTerm = input("Is there another term? (yes or no)\n").lower()
                toFTerm = nTerm

            if (specialVar == "arccos"):
                v = a.acos(value)
                temp = coefficient*(v)
                nTerm = input("Is there another term? (yes or no)\n").lower()
                toFTerm = nTerm

            if (specialVar == "no"):
                temp = coefficient ** value
                nTerm = input("Is there another term? (yes or no)\n").lower()
                toFTerm = nTerm

            if (typeFraction == "n"):
                numerator += temp

            if (typeFraction == "d"):
                denominator += temp

        if (denominator == 0):
            print("Nothing can be done with the equation, it is undefined.")

        else:

            def f(x):
                return numerator
            def g(x):
                return denominator

            print("::LOADING::")
            print("Here's your solution to the integral of the equation ["+str(numerator)+ "/" + str(denominator)+ "]:")
            print(a.integrate(f(x)/g(x), (x)))

    if (ifDivision == "no"):
        temp = 0

        while (toFTerm == "yes"):

            coefficient = int(input("What's the coefficient?\n"))
            print("\nOnly input one of these options.")
            specialVar = input("Is there a variable (x), euler's number (e), trig (tan, cos, sin, arctan, arccos, arcsin), constant (input as no) ?\n").lower()
            value = int(input("What's the exponent (variable or euler) or value (value for trig and logarithms)? Only numerical numbers?\n"))

            if (specialVar == "x"):
                equation += coefficient*(x**value)
                nTerm = input("Is there another term? (yes or no)\n").lower()
                toFTerm = nTerm

            if (specialVar == "e"):
                v = a.exp(value)
                equation += coefficient*(v)
                nTerm = input("Is there another term? (yes or no)\n").lower()
                toFTerm = nTerm

            if (specialVar == "tan"):
                v = a.tan(value)
                equation += coefficient*(v)
                nTerm = input("Is there another term? (yes or no)\n").lower()
                toFTerm = nTerm

            if (specialVar == "sin"):
                v = a.sin(value)
                equation += coefficient*(v)
                nTerm = input("Is there another term? (yes or no)\n").lower()
                toFTerm = nTerm

            if (specialVar == "cos"):
                v = a.cos(value)
                equation += coefficient*(v)
                nTerm = input("Is there another term? (yes or no)\n").lower()
                toFTerm = nTerm

            if (specialVar == "arctan"):
                v = a.atan(value)
                equation += coefficient*(v)
                nTerm = input("Is there another term? (yes or no)\n").lower()
                toFTerm = nTerm

            if (specialVar == "arcsin"):
                v = a.asin(value)
                equation += coefficient*(v)
                nTerm = input("Is there another term? (yes or no)\n").lower()
                toFTerm = nTerm

            if (specialVar == "arccos"):
                v = a.acos(value)
                equation += coefficient*(v)
                nTerm = input("Is there another term? (yes or no)\n").lower()
                toFTerm = nTerm

            if (specialVar == "no"):
                equation += coefficient
                nTerm = input("Is there another term? (yes or no)\n").lower()
                toFTerm = nTerm

        def f(x):
            return equation

        print("::LOADING::")
        print("Here's your solution to the indefinite integral of the equation ["+str(equation)+"] :")
        print(a.integrate(f(x), (x)))

else:
    print("Invalid Input!")
