from login import username, token
import os
import textscroller.textscroller as text

available_apps = [
    (text.app_name, text)
]

select = ""
while select != 'q' and not (select.isnumeric() and int(select) > 0 and int(select) <= len(available_apps)):
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Welcome to the YoLighthouse Launcher, which of the following you want to launch?")
    print("Enter one of the preceding index numbers to continue or 'q' to quit!\n")

    count = 1
    for a in available_apps:
        print(f"({count}) {a[0]}")

        count += 1

    print("")
    select = input("Select: ")

if select == 'q':
    os.system('cls' if os.name == 'nt' else 'clear')
    print("bye bye :)")
    exit()
else:
    available_apps[int(select) - 1][1].execute(username, token)
