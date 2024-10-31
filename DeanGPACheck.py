#This is a program that will accept the student's name and GPA to determine if they can get
#onto the Dean's list and or Honor roll. the program will ask the a student's last name,
#quit processing records if the last name is "ZZZ", ask for an accept student's first name,
#ask for the GPA as a float, ask if the GPA is 3.5 or greater, and printa  message if so,
#stating they have made the dean's list. if it's 3.25 or higher, they made the honor roll.
#test the app with five students. this program was made my elijah gonzalez, the program is 
#called DeanGPACheck.py.

#we begin by setting ZZZtoQuit to false, we have to set it here so the program can continue.
#it is a boolean
toQuit = False

#we also set HonorCheck and DeanCheck to false, as later if someone's GPA is higher than 3.25
#or 3.5, it is set to true. 
honorCheck = False
deanCheck = False

#the entire program is a while loop, it will keep asking the user the questions and deliver
#the information they seek until ZZZ is inputed.
while toQuit == False:

    #we ask the user their last name, if they input ZZZ, toQuit is set to true, and the
    #program ends, as the while loop is set to false. otherwise, we just take the user's
    #last name, and uise it later.
    lastName = str(input("What is your last name? Please input it, or 'ZZZ' to quit: "))

    #if lastName is set to ZZZ, the application closes.
    if lastName == ("ZZZ"):

        #we tell the user what they inputed, and tell them the application has ended, and ask them
        #to close the window.
        print("ZZZ inputed. End of application, please close the window.")

        #the program ends because ZZZtoQuit is set to True, as the while loop only continues if
        #the loop is set to False.
        toQuit = True

    #if anything else aside from ZZZ is inputed, the following happens:
    else:

        #we set a variable called firstName, and use it to store the user's first name. we use it
        #later
        firstName = str(input("What is your first name? Please input it: "))

        #we then ask for the user's GPA, and set it to a float, as we need to include decimals, which
        #integers do not. we set it to studentGPA
        studentGPA = float(input("What is your GPA? Please input it: "))

        #if studentGPA is greater or equal to 3.5, we set deanCheck and honorCheck to True. you need
        #3.5 or more to achieve the dean's list.
        if studentGPA >= 3.50:

            #we set deanCheck to true here.
            deanCheck = True

        #we do the same as above, but only with studentGPA if it is 3.25, if it is above, but less than 3.50, we do the following:
        elif studentGPA >= 3.25:

            #set honorCheck to true, as that is true, but not deanCheck, as does not meet the requirements.
            honorCheck = True

        #if deanCheck is set to true, it is first in line in the logic so it will skip elif and else. so, it prints the following:
        if deanCheck == True:

            #this here, we use firstName, lastName, so it tells the user their name to tell them they've made the Dean's List, but if you make the Dean's List
            #you also make the honor's roll, so it is included in the message.
            print(firstName, lastName, "has made the Dean's list, as well as the honor roll.")

        #we do the same here, but instead if it's less than 3.5 but more than 3.25 or equal to it.
        elif honorCheck == True:

            #if it meets the requirements, we tell them they have made the honor's roll, but not the Dean's list.
            print(firstName, lastName, "has made the honor roll, but not the Dean's list.")

        #else, if it not more than 3.5, or less than 3.5 but more than or equal to 3.25, we tell them they have not made either.
        else:

            #we tell them that here.
            print(firstName, lastName, "has not made either the Dean's list, or the honor's roll.")

        #finally, we have to set deanCheck and honorCheck to false, so that the variables are ready and fresh for the next loop around.
        deanCheck = False
        honorCheck = False
