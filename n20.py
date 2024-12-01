#20 შექმენით calculator ფუნქცია რომელსაც ექნება ყველა მათემატიკური მოქმედება მაგალითად:+,-,*,/. ფუნქციას გადაეცით 3 არგუმენტი. პირველი იქნება პირველი რიცხვი, მეორე მეორე რიცხვი და მესამე მათემატიკური ოპერაციის ოპერატორი (+,-...).												


oper = input("+" "-" "*" "//")
person = int(input("enter your num?"))
person1 = int(input("enter your num?"))

def name ():
    if oper == "+":
        print(person + person1)
    elif oper == "-":
        print(person - person1)
    elif oper == "*":
        print(person * person1)
    elif oper =="/":
        print(person // person1)        
    else:
        print("error")    

name()        