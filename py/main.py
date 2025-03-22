import keyboard  # using module keyboard
print("if you are experiencing issues please run the script with sudo")
print("press 1 to print hello world")
while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('1'):  # if key 'q' is pressed 
            import helloworld
            break  # finishing the loop
    except:
        break  # if user pressed a key other than the given key the loop will break

