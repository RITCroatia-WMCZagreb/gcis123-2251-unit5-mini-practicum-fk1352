'''
@ASSESSME.USERID: fk1352
@ASSESSME.AUTHOR: Faris Karić
@ASSESSME.DESCRIPTION: MiniPractical
@ASSESSME.ANALYZE: YES
'''

# The  thecima values of PI
PI_VALUE = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"

def pi_tester():
    correct_pi = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
    counter = 0
    for i in range(100):
        user_input = input(f"Enter the ",{i+1}," digit of PI: ")
        if user_input == correct_pi[i]:
            counter+=1
        else:
            print("Incorrect digit, the correct digit is",correct_pi[i]) 
            break
        return counter

def display_score(score):
    if score >100:
        title = "PI Imposter"
    elif score >=97 and score<=100:
        title = "PI Expert"
    elif score >=50 and score<=96:
        title = "PI Connoiseur"
    elif score >=25 and score<=49:
        title = "PI Enthusiast"
    elif score >=10 and score<=24:
        title = "PI Journeyman"
    elif score >=5 and score<=9:
        title = "PI Novice"
    elif score >=0 and score<=4:
        title = "PI Neophyte"
    print("Number of correct decimal digits: ",{score})
    print("Your title: ",{title})

def main():
    
    display_score(score)
    score = pi_tester()

if __name__ == "__main__":
    main()