#!/usr/bin/env python
# -*- coding: utf8 -*-
from sh import echo
import subprocess
def rr_dd():		
	for c in a:
		d=subprocess.call("arping -c 1 "+str(c),shell=True)
		if d==0:
			b.write("\n---IP---"+str(c)+"\t---ONLINE---\n")
		else:
			b.write("\n---IP---"+str(c)+"\t---OFFLINE---\n")
	b.close()
	a.close()
def ff_dd():
	k=" "
	k=input("Vvedite skaniruemie IP adresa : ")
	a.write(str(k))
	if k==0:
		rr_dd()
b=open("/root/MyScripts/ip_r.txt", "w")
try:
	a=open("/root/MyScripts/ip.txt", "r")
except (IOError, NameError):
	k="\n\t------ Net faila s IP adresami v papke s ispolnyemim failom ------\n\n\t------\
	Sozdaite tekstoviy dokument i napihite skaniruemae hosti ------\n"
	print (k)
	b.write(k)
	a=open("/root/MyScripts/ip.txt", "w+")
	k=1
	while k==1:
		k=" "
		k=input("Vvedite skaniruemie IP adresa : ")
		a.write(str(k))
		if k==0:
			rr_dd()
a=open("/root/MyScripts/ip.txt", "r")	
rr_dd()


