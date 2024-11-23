cold = input("Do you have cold? ")
if cold == "yes":
    print("That is sad!")
    fever = input("Do you have fever too? ")
    if fever == "yes":
        print("Sounds bad!")
        cough = input("Do you have cough? ")
        if cough == "yes":
            print("Get these tests done. I will suggest medication based on the reports.")
        else:
            print("Take these medicines for 3 days and you will be fine.")
    else:
        print("Could be normal cold because of climate change. Take rest, you will be ok.")
else:
    print("Glad you are fine! Please take care of yourself.")