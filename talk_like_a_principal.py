
def madlib():
    print()
    print ("Please enter the following parts of speech: -")
    print()
    year = input("Year: ")
    number = input ("Number: ")
    number2 = input("Number: ")
    adj1 = input("Adjective: ")
    adj2 = input("Adjective: ")
    adj3 = input("Adjective: ")
    adj4 = input("Adjective: ")
    past_simple_verb = input("Past Simple Verb: ")
    present_continous_verb = input("Present Contonius Verb: ")
    noun = input("Noun: ")
    noun_plural = input("Noun (plural): ")
  


    madlib=f"I sincerely welcome you all to this {adj1} occasion when we are {present_continous_verb } the {year} Kenya Certificate of \
Primary Education (KCPE) examination results . I feel {adj2} that we have managed to have the results ready \
just {number} days after the {number2} {noun_plural} sat the examinations . I wish to sincerely thank everyone -- \
the examination officials , examiners , monitors and the backroom staff at the Kenya National \
Examinations Council (KNEC) -- who has {past_simple_verb} this exercise {adj3} . It is proof that with commitment , \
Government officials can deliver {adj4} services."

    print(madlib)

if __name__ == '__main__':
    madlib()