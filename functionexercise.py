homework = int(input("Please enter homework mark max 25: "))
assessment = int(input("Please enter assessment mark max 50: "))
finalexam = int(input("Please enter final exam mark max 100: "))

def grade(homework, assessment, finalexam):
    result = (homework + assessment + finalexam) 
    if result <= 86:
        print("Unclassified")
        return result 
    elif result <= 95:
        print("E")
        return result
    elif result <= 115:
        print("D")
        return result
    elif result <= 130:
        print("C")
        return result
    elif result <=145:
        print ("B")
        return (result)
    else:
            print ("A")
            return (result)


print(grade(homework, assessment, finalexam,))


