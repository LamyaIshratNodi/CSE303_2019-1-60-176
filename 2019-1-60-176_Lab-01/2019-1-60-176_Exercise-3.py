#Exercise-03


def compound_interest_2019_1_60_176(p, r, t):
    return float(p * ((1 + r/100)**t))

principleAmount = float(input("Enter principle amount: ")) 
interest = float(input("Enter interest amount: ")) 
time = float(input("Enter time (in years): ")) 
print("The compound interest is: %.2f" %compound_interest_2019_1_60_176(principleAmount, 
                                                                        interest, time))
