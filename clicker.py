import time
import pyautogui as auto
import keyboard
import random
import threading

'''
pip install pyautogui keyboard
base speed of 19.2 CPS with two threads - https://www.rapidtables.com/
'''
class clicker:
    def __init__(self):
        self.clicker = False
        self.base = 0

    def toggle(self):
        self.clicker = not self.clicker

    def number_generate(self):               
        self.base = random.uniform(0.00025, 0.0005)  # generates a random float between 0.25 ms and 0.5 ms
        return self.base                             # adding zeros will increase cps
                                                     # removing will decrease cps 
    def auto_clicker(self):
        while 1:
            if self.clicker:
                random_sleep = self.number_generate()
                auto.click()
                time.sleep(random_sleep)
                print(random_sleep)
            else:
                time.sleep(0.1) # cpu saver -_-

# main runner
if __name__ == '__main__':
    c = clicker()
    # hotkey to toggle on and off
    keyboard.add_hotkey("9", c.toggle)

    # start clicker one
    one = threading.Thread(target=c.auto_clicker)
    one.start()

    # start clicker two
    two = threading.Thread(target=c.auto_clicker)
    two.start()