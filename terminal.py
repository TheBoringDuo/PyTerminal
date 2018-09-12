import time
from subprocess import call
import os

## here you need to add your new commands
commands = ['#anatomic', 'test']

call("clear")


## here you can change your input sign
sign = "<!> "

## here you need to add a elif for your function (use the examples)
def execute(uin):
	z = 0
	while z<len(commands):
		if uin=="#anatomic":
			def anatomic():
				try:
					print("#anatomic")
					time.sleep(0.3)
					anatomic()
				except KeyboardInterrupt:
					print("Stopped!")
					main()
			anatomic()
		elif uin=="test":
			def anatomic():
				try:
					print("#anatomic")
					time.sleep(0.3)
					anatomic()
				except KeyboardInterrupt:
					print("Stopped!")
					main()
			anatomic()
		else:
			z = z + 1
	main()

## Dont touch anything under that line!!!
## Dont touch anything under that line!!!
## Dont touch anything under that line!!!



def main():
	
	i = 0
	
	uin = input(sign)

	
	while i<len(commands):
		if uin == commands[i]:
			execute(uin)
		i = i + 1
		
	if uin.startswith("cd"):
		try:
			cdcommand = []
			cdcommand = uin.split()
			dir = cdcommand[1]
			os.chdir(dir)
			print("You are now in {} (dir)".format(dir))
			main()
		except:
			uin=" "
					
			print("There is something strange!")
			main()
	else:	
		try:
			call(uin)	
			main()
		except:
					
			print("Wrong command!")
			main()
				
		
			
main()