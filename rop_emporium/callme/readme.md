As usual use pwngdb and overflow the buffer to find the size of trash to reach Return Address (40).
Find the address of the 3 function to call with Rizin.
Then you need to call them with the parameter specified on the site. On 64bit the parameter are passed in order with RSI, RDI, RDX registers so you need to find a ROP gadget chain to POP stack value into those registers. 
