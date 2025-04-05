import math as mt
import os
import requests

current_version = "1.0.0"

def check_for_updates():

    repo_url = "https://api.github.com/repos/egdmte/pyrow/releases/latest"
    response = requests.get(repo_url)
    if response.status_code == 200:
        latest_version = response.json()["tag_name"]
        if latest_version != current_version:
            print(f"[WARNING] You are using an old version of PyRow.")
            print("Even though it is possible to bypass this requirement, you are missing new features and potential bug fixes.")
            print("If you have 'git' installed, run 'git clone https://github.com/egdmte/pyrow for the latest version of PyRow.'")
            input("Press enter to continue...")
            exit()  # Stops the app from running
    else:
        print("Application could not fetch the latest version of PyRow. Try again with internet connection or bypass this requirement by\nchanging PyRow's source code, removing the 'check_for_updates' function.")
        exit()

check_for_updates()

os.environ['TERM'] = 'xterm'

u_age_spesification = (15, 17, 19, 21, 23)
gender = ("male", "female", "mix")
gender_s = None
boat_member = (1, 2, 4, 8)
academic = False
master = False
i = 0

inputs = []

def clean():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")


for i in range(int(input("How many times do you want to run this program?"))):

    def findAppropriate(data):
        global age
        global age_raw
        age_raw = data
        if data in u_age_spesification:  # U means "Under", which means 'data' cannot be the same as spesification. Add 1 to data, so user input is directed to correct spesification.
            data += 1
            if data > 23:
                print(
                    "Maximum U spesification treshold exceeded while trying to find the nearest class. Assuming user as a Master."
                )
                master = True
                age = "Master"
                return
        elif data > 23 or data == 23:
            print(
                f"This individual is not suitable for U categorization - user age ({data}) exceeds maximum U limitation (Under23). Assuming user as a Master.")
            master = True
            return

        while data not in u_age_spesification:  # Add 1 to numbers between spesifications, e.g 15 < 16(+1) < 17
            data += 1

        age = "U" + str(data)  # Data is the age part of the combination.
        print("Automatically transformed to U" + str(u_age_spesification[u_age_spesification.index(data)]))


    def genderDetect(data):
        while data.strip().lower() not in gender:
            data = (input("Enter a valid (Male, Female, Mix) gender.").lower()).strip()

        global gender_data
        if data.strip().lower() == "male":
            return "M"
        elif data.strip().lower() == "female":
            return "F"
        else:
            return "Mix"


    def boatDetect(data, gender_s):
        if data < 0:
            data = abs(data)
            print("Your input was a negative number. Automatically transformed into positive number.")

        gender_s = genderDetect(input("Enter gender (Male, Female, Mix): "))

        if gender_s == None:
            genderDetect(input("Enter a valid (Male, Female, Mix) gender: "))

        while data not in boat_member:
            data = int(input("This boat type does not exist - enter 1, 2, 4, or 8 as input: "))

        while data < 3 and gender_s == "Mix":
            print(
                "Mix status cannot be used for boats having less than 4 athletes - gender categorization impossible on single and double. Re-enter gender.")
            gender_s = genderDetect(input("Enter gender (Male, Female, Mix): "))

        while age == "U15" and data == 8:
            print("Under15 category is not allowed to use this boat - too dangerous to replicate.")
            data = int(input("Enter 1, 2, or 4 as input: "))

        global gender_data
        gender_data = gender_s
        global boat_num
        boat_num = data


    def scullsweep():
        global sweep_data
        if int(boat_num) == 8:
            print("8 athletes detected, automatically enabled sweep.")
            sweep_data = ""
            return
        if int(boat_num) == 2:
            print("2 athletes detected, automatically enabled scull.")
            sweep_data = "X"
            return
        if int(boat_num) == 1:
            print("1 athlete detected, automatically enabled scull")
            sweep_data = "X"
            return

        else:
            print(
                f"Select sweep (one oar per person) and scull (two oar per person).\n1. Sweep({boat_num})\n2. Scull({boat_num}X)")
            data = int(input())
            i = 0
            while i == 0:
                if data == 1:
                    if int(boat_num) == 4:
                        sweep_data = ""
                        return 4
                elif data == 2:
                    if int(boat_num) == 4:
                        sweep_data = "X"
                        return "X"
                else:
                    i = 0

    def coxswain():
        global coxswain_data
        i = 0
        if int(boat_num) == 4:
            while i == 0:
             print("Coxswain may be added or removed for this boat type.\n1.Add\n2.Remove")
             choice = int(input())
             if choice == 1:
                 coxswain_data = "+"
                 return
             else:
                 coxswain_data = "-"
                 return
        elif int(boat_num) == 8:
            coxswain_data = "+"
            print("8 athletes detected, coxswain required.")
        else:
            coxswain_data = ""




    i = 0
    try:
        clean()
        findAppropriate(int(input("Please enter age: ")))
        i = 1
    except:
        while i == 0:
            print("Invalid input type. Expected number, text returned.")
            try:
                findAppropriate(int(input("Please enter age: ")))
                i = 1
            except:
                i = 0

    boatDetect(int(input("Please enter athlete amount in the boat:  ")), 0)
    scullsweep()
    coxswain()

    a = (f"{age}{gender_data}{boat_num}{sweep_data}{coxswain_data}")
    inputs.append(a); print(f"{a}\n\n")

print("\nAll outputs:")
for i in inputs:
    print(i)
input("Press Enter to terminate (YOUR OUTPUTS ARE NOT SAVED IF YOU DON'T COPY THEM NOW)")