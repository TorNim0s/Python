shop_list = []

def MainMenu():
    print("חנות וירטואלית | לחץ על המקש הרצוי\n")
    print(" 1. רשימת המוצרים")
    print(" 2. מספר המוצרים ברשימה")
    print(" 3. בדיקת מוצר ברשימה")
    print(" 4. בדיקת כמות מוצר ברשימה")
    print(" 5. מחיקת מוצר")
    print(" 6. הוספת מוצר לרשימה")
    print(" 7. מוצרים לא חוקיים")
    print(" 8. הסרת כל הכפילויות הקיימות ברשימה")
    print(" 9. יציאה")
    clinetinput = int(input("הכנס מספר בין 1-9: "))

    MenuHandle(clinetinput)

def checkvaliditem(item):
    if item.isalpha():
        return True
    else:
        return False

def MenuHandle(clientinput):
    global shop_list
    if clientinput == 1:
        for item in shop_list:
            print(item)
        MainMenu()
    elif clientinput == 2:
        print ("מספר המוצרים ברשימה הינו: ", len(shop_list))
        MainMenu()
    elif clientinput == 3:
        checkitem = input("הכנס מוצר לבדיקה: ")
        for item in shop_list:
            if checkitem == item:
                print ("מוצר נמצא ברשימה")
                MainMenu()
        print("מוצר לא נמצא ברשימה")
        MainMenu()
    elif clientinput == 4:
        checkitem = input("הכנס מוצר לבדיקה: ")
        counter = 0;
        for item in shop_list:
            if checkitem == item:
                counter += 1;
        print ("המוצר", checkitem, "נמצא", counter, "פעמים ברשימה")
        MainMenu()
    elif clientinput == 5:
        delitem = input("הכנס מוצר למחיקה: ")
        for item in shop_list:
            if delitem == item:
                shop_list.remove(item)
                print("מוצר נמחק ברשימה")
                MainMenu()
        print("המוצר לא נמחק מכיוון שאינו נמצא ברשימה")
        MainMenu()
    elif clientinput == 6:
        additem = input("הכנס מוצר להוספה: ")
        shop_list.append(additem)
        print("המוצר", additem, "נוסף לרשימת המוצרים")
        MainMenu()
    elif clientinput == 7:
        for item in shop_list:
            if (checkvaliditem(item)):
                print (item)
        MainMenu()
    elif clientinput == 8:
        shop_list = list(dict.fromkeys(shop_list))
        print("כפילויות נמחקו")
        MainMenu()

def main():
    MainMenu()


if __name__ == "__main__":
    main()


"""
def try_update_letter_guessed(letter_guessed, old_letter_guessed):
    if (len(letter_guessed) == 1 and letter_guessed.isalpha() and letter_guessed not in old_letter_guessed):
        old_letter_guessed += [letter_guessed]
        print (old_letter_guessed)
        return True, old_letter_guessed
    elif (letter_guessed in old_letter_guessed):
        notvalidletter(old_letter_guessed)
        return False, old_letter_guessed
    elif len(letter_guessed) > 1 and letter_guessed.isalpha():
        notvalidletter(old_letter_guessed)
        return False, old_letter_guessed
    elif len(letter_guessed) == 1 and not letter_guessed.isalpha():
        notvalidletter(old_letter_guessed)
        return False, old_letter_guessed
    elif len(letter_guessed) > 1 and not letter_guessed.isalpha():
        notvalidletter(old_letter_guessed)
        return False, old_letter_guessed

def notvalidletter(old_letters):
    print ("X")
    print(" -> ".join(sorted(old_letters)))

def main():
    old_letters = []
    newletter = input("Enter a valid letter: ")
    status , old_letters = try_update_letter_guessed(newletter, old_letters)
    newletter = input("Enter a valid letter: ")
    status, old_letters = try_update_letter_guessed(newletter, old_letters)
    newletter = input("Enter a valid letter: ")
    status, old_letters = try_update_letter_guessed(newletter, old_letters)


if __name__ == "__main__":
    main()

"""