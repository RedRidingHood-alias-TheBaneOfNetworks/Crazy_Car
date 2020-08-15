# coding: utf-8

import time
import os
interface = raw_input("choose device to test (vcan0, can0, etc...) >>> ")

enum = open("wordlist.lst")
option = raw_input("choose option (bruteforce/findIDs) >>> ")
for id in enum:
	if option == "bruteforce":
		def oFunction1(interface,id):
			print("cansend " + interface +" "+ id.rstrip() + "#000000FF")
		def oFunction2(interface,id):
			os.system("cansend " + interface +" "+ id.rstrip() +"#000000FF")
		def TheBestFunction(interface,id):
			oFunction1(interface,id)
			oFunction2(interface,id)
		TheBestFunction(interface,id)


	if option == "findIDs":
		def oFunction1(interface,id):
			time.sleep(0.1)
                	print("cansend " + interface +" "+ id.rstrip() +"#000000FF")
        	def oFunction2(interface,id):
			time.sleep(0.1)
                	os.system("cansend " + interface +" "+ id.rstrip() +"#000000FF")
          	def TheBestFunction(interface,id):
                	oFunction1(interface,id)
                	oFunction2(interface,id)
                TheBestFunction(interface,id)
