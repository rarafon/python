#! python3
# countdown.py - A simple countdown script.

import time, subprocess

timeLeft = 5
while timeLeft > 0:
    print(timeLeft, end='')
    time.sleep(1)
    timeLeft = timeLeft - 1

subprocess.Popen(['C:\\Windows\\notepad.exe'])
