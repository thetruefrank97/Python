import time


i = 0
def HelloWorldWithTime():
    while True:
        global i
        time.sleep(i)
        i += 1
        print("Hello")
        if i > 3:
            print("End of loop")
            break


HelloWorldWithTime()
