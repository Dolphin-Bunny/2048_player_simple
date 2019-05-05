import pyautogui,time,random,sys

can_go_up=pyautogui.prompt('\ncan computer press up? (t or f): \nPressing up decreases the final score, but allows the game to not get stuck.')
if can_go_up=='t':
    can_go_up==True
elif can_go_up=='f':
    can_go_up=False
else:
    sys.exit('input error')

print('\n')

pyautogui.alert('PLEASE NOTE:\n- press ctrl+c in the console/terminal/cmd window to end program\n- this program may do unwanted things on other websites or in other programs\n- program will not start playing until OK is pressed\n\npress ok and click into your 2048 tab after reading this message')

print('\npress ctrl+c in this window to quit program')

while True:#main loop
    pyautogui.typewrite(['LEFT'])
    time.sleep(0.23)
    pyautogui.typewrite(['DOWN'])
    time.sleep(0.23)
    pyautogui.typewrite(['RIGHT'])
    time.sleep(0.23)
    pyautogui.typewrite(['DOWN'])
    time.sleep(0.23)

    if can_go_up:# going up prevents getting stuck, but lowers score
        if random.randint(1,60)==2:
            pyautogui.typewrite(['UP'])
