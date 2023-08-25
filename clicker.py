import time as t
import pyautogui
import keyboard
import random
import threading

'''
pip install pyautogui keyboard
Base speed of 18.8CPS
'''
class clicker:
    def __init__(self):
        self.clicker = False
        self.interval = 0

    def toggle_auto_clicker(self):
        self.clicker = not self.clicker

    def random_number(self):
        self.interval = random.uniform(0, 0.01) # this will effect you cps
        return self.interval                    # adding zeros will increase 
                                                # removing will decrease
    def auto_clicker(self):
        while 1:
            if self.clicker:
                r = self.random_number()
                pyautogui.click()
                t.sleep(r)
                print(r)
            else:
                t.sleep(0.1) # cpu saver -_-

# main runner
if __name__ == '__main__':
    c = clicker()
    # hotkey to toggle on and off
    keyboard.add_hotkey("9", c.toggle_auto_clicker)
    # start number gen
    n_gen = threading.Thread(target=c.auto_clicker)
    n_gen.start()
    # start clicker
    c_one = threading.Thread(target=c.auto_clicker)
    c_one.start()