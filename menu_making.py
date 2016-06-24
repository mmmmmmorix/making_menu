# coding: utf-8

import random

menu_category = ["Drill", "Kick", "Pull", "Swim"]
menu_time = [5,10,15]

def menu(training_time):
    contents = []
    total_time = 0

    print("-----TODAY\'S TRAINING MENU-----\n")

    timeWup = random.choice([5,10])
    total_time += timeWup
    print("W-up " + random.choice(["100m ", "200m "]) +"--"+str(timeWup)+ "min\n")

    while total_time < training_time - 5:
        time = random.choice(menu_time)
        total_time += time
        if total_time <= training_time - 5:
            content = random.choice(menu_category)
            if "Drill" in contents and content == "Drill":
                total_time -= time
            else:
                contents.append(content)
                print(content +" --"+ str(time) + "min")
        elif total_time > training_time - 5:
            total_time -= time

    print("\nDown")
    print("-------TotalTime: " +str(total_time)+ " min-------")

menu(30)
