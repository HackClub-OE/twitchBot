import socket
import pyautogui
import pynput
import ctypes
import time


SendInput = ctypes.windll.user32.SendInput

def PressKeyPynput(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = pynput._util.win32.INPUT_union()
    ii_.ki = pynput._util.win32.KEYBDINPUT(0, hexKeyCode, 0x0008, 0, ctypes.cast(ctypes.pointer(extra), ctypes.c_void_p))
    x = pynput._util.win32.INPUT(ctypes.c_ulong(1), ii_)
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKeyPynput(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = pynput._util.win32.INPUT_union()
    ii_.ki = pynput._util.win32.KEYBDINPUT(0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.cast(ctypes.pointer(extra), ctypes.c_void_p))
    x = pynput._util.win32.INPUT(ctypes.c_ulong(1), ii_)
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def PressAndHoldKey(hexKeyCode, seconds):
    PressKeyPynput(hexKeyCode)
    time.sleep(seconds)
    ReleaseKeyPynput(hexKeyCode)


Q = 0x10
W = 0x11
E = 0x12
R = 0x13
T = 0x14
Y = 0x15
U = 0x16
I = 0x17
O = 0x18
P = 0x19
A = 0x1E
S = 0x1F
D = 0x20
F = 0x21
G = 0x22
H = 0x23
J = 0x24
K = 0x25
L = 0x26
Z = 0x2C
X = 0x2D
C = 0x2E
V = 0x2F
B = 0x30
N = 0x31
M = 0x32
ESC = 0x01
ONE = 0x02
TWO = 0x03
THREE = 0x04
FOUR = 0x05
FIVE = 0x06
SIX = 0x07
SEVEN = 0x08
EIGHT = 0x09
NINE = 0x0A
ZERO = 0x0B
MINUS = 0x0C
EQUALS = 0x0D
BACKSPACE = 0x0E
SEMICOLON = 0x27
TAB = 0x0F
CAPS = 0x3A
ENTER = 0x1C
LEFT_CONTROL = 0x1D
LEFT_ALT = 0x38
LEFT_SHIFT = 0x2A
SPACE = 0x39
DELETE = 0x53
COMMA = 0x33
PERIOD = 0x34
BACKSLASH = 0x35
NUMPAD_0 = 0x52
NUMPAD_1 = 0x4F
NUMPAD_2 = 0x50
NUMPAD_3 = 0x51
NUMPAD_4 = 0x4B
NUMPAD_5 = 0x4C
NUMPAD_6 = 0x4D
NUMPAD_7 = 0x47
NUMPAD_8 = 0x48
NUMPAD_9 = 0x49
NUMPAD_PLUS = 0x4E
NUMPAD_MINUS = 0x4A
LEFT_ARROW = 0xCB
RIGHT_ARROW = 0xCD
UP_ARROW = 0xC8
DOWN_ARROW = 0xD0
LEFT_MOUSE = 0x100
RIGHT_MOUSE = 0x101
MIDDLE_MOUSE = 0x102
MOUSE3 = 0x103
MOUSE4 = 0x104
MOUSE5 = 0x105
MOUSE6 = 0x106
MOUSE7 = 0x107
MOUSE_WHEEL_UP = 0x108
MOUSE_WHEEL_DOWN = 0x109

HOST = "irc.twitch.tv"
PORT = 6667
NICK = "greenden007"
OWNER = "greenden007"
CHANNEL = "greenden007"
PASS = "oauth:"
BOT = "TwitchBot"

s = socket.socket()
s.connect((HOST, PORT))
s.send(bytes("PASS " + PASS + "\r\n", "UTF-8"))
s.send(bytes("NICK " + NICK + "\r\n", "UTF-8"))
s.send(bytes("JOIN #" + CHANNEL + " \r\n", "UTF-8"))


def joinchat():

	loading = True
	while loading:
		read_inp = s.recv(1024)
		read_inp = read_inp.decode()
		for line in read_inp.split("\n")[0:-1]:
			print(line)
			loading = loadCmp(line)

def loadCmp(line):
	if("End of /NAMES list" in line):
		print("Bot has joined " + CHANNEL + "'s channel!")
		sendMsg(s, "Chat room joined")
		return False
	else:
		return True

def sendMsg(irc, msg):
	p_msg = "PRIVMSG #" + CHANNEL + " :" + msg
	irc.send((p_msg + "\n").encode())

def getUser(line):
	sep = line.split(":",2)
	user =sep[1].split("!", 1)[0]
	return user

def getMsg(line):
	try:
		msg = (line.split(":",2))[2]
	except:
		msg = ""

	return msg

def console(line):
	if "PRIVMSG" in line:
		return False
	else:
		return True


joinchat()

while True:
	try:
		read_ln = s.recv(1024).decode()
	except:
		read_ln = ""

	for line in read_ln.split("\r\n"):
		if line == "":
			continue
		elif "PING" in line and console(line):
			msgg = "PONG tmi.twitch.tv\r\n".encode()
			s.send(msgg)
			print(msgg)
			continue
		else:
			print(line)
			user = getUser(line)
			msg = getMsg(line)
			print(user + " : " + msg)
			if "stop" in msg.lower():
				exit()

			#For Pokemon - need to set hotkeys on emu tho
			elif msg.lower() == "x":
				PressKeyPynput(X)
				ReleaseKeyPynput(X)

			elif msg.lower() == "y":
				PressKeyPynput(Y)
				ReleaseKeyPynput(Y)

			elif msg.lower() == "a":
				PressKeyPynput(A)
				ReleaseKeyPynput(A)

			elif msg.lower() == "b":
				PressKeyPynput(B)
				ReleaseKeyPynput(B)

			elif msg.lower() == "up":
				PressKeyPynput(UP_ARROW)
				ReleaseKeyPynput(UP_ARROW)

			elif msg.lower() == "down":
				PressKeyPynput(DOWN_ARROW)
				ReleaseKeyPynput(DOWN_ARROW)

			elif msg.lower() == "right":
				PressKeyPynput(RIGHT_ARROW)
				ReleaseKeyPynput(RIGHT_ARROW)

			elif msg.lower() == "left":
				PressKeyPynput(LEFT_ARROW)
				ReleaseKeyPynput(LEFT_ARROW)