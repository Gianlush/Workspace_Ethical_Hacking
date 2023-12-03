#!/usr/bin/python3

# run with 'gdb -q -x morph.py'

import gdb

FLAG_LEN = 23

def callgdb(cmd):
	return gdb.execute(cmd, to_string=True).splitlines()
	
def getEntrypoint(arg):
	callgdb("run " + arg)
	info = callgdb("info file")[3]
	entrypoint = info.split(": ")[1]
	return int(entrypoint, 16)
	
def getCorrectChar():
	current_instruction = callgdb("x/i $pc")[0].split("\t")[1]
	correctChar = current_instruction.split(" ")[4].split(",")[1]
	return chr(int(correctChar, 16))
	
def getCharPosition():
	cmd = callgdb("x/s $rdi")[0].split(" ")
	print(cmd)
	length = 0
	if(len(cmd)>=2):
		length = int(cmd[2])
	else:
		cmd = cmd[0].split("\t")
		if(length == 1):
			length = len(cmd[0])
		else:
			length = len(cmd[1])-2
	return FLAG_LEN - length
	
def get_1_flag_char(flag):
	callgdb("si")
	callgdb("si")
	callgdb("ni")
	callgdb("ni")
	c = getCorrectChar()
	p = getCharPosition()
	flag[p] = c
	callgdb("set $al=" + hex(ord(c)))
	
callgdb("file ./morph")
arg = 'a' * FLAG_LEN	# stringa in input (della stessa len della flag) al programma
entrypoint = getEntrypoint(arg)

offset1 = 0x3F5
b_callrax1 = entrypoint+offset1

offset2 = 0x31
b_callrax2 = b_callrax1+offset2


callgdb("break *" + hex(b_callrax1))
callgdb("break *" + hex(b_callrax2))
callgdb("run")

flag = ['' for i in range(23)]
for i in range(FLAG_LEN-1):
	get_1_flag_char(flag)
	callgdb("continue")
get_1_flag_char(flag)


print("".join(flag))
callgdb("q")


