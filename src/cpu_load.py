import psutil
import Pids
import Memory
import send_email
import os
from uuid import getnode as get_mac

mac = get_mac()
cpu_load_finish = 0
cpu_loadinglevel = False
while_loop = True

while(while_loop):

	cpu_load_warning = 70 #70   #value for cpu warning message
	cpu_interval = 6      #intval for cpu_percant_reequest
	
	def cpu_load():
		count = psutil.cpu_count()
		condition_cpu_loop = True
		mem = Memory.Free_Space()
		if mem < 200:
			print "Achtung, sehr wenig Speicher frei!"
					
		while (condition_cpu_loop == True):
			cpu_load = psutil.cpu_percent(interval=cpu_interval)
			print(cpu_load)
			cpu_load_finish = cpu_load
			if(cpu_load > cpu_load_warning):
				condition_cpu_loop = False
				print("Warning Warning")
				print Pids.Pi(count, cpu_load_finish)  
				return(cpu_load)
			

	print(cpu_load())
	#print("test1" + str(cpu_load_finish))
	if (cpu_load >= 80) & (cpu_loadinglevel == False):
		#print(cpu_load + " foo")		
		send_email.main("DANGER DANGER! Ihr Pi " +  (str(mac)) + " ist zu 80% ausgelastet - sofern sie es nicht willentlich tun, untersuchen sie ihn auf Schadsoftware.", "Danger!")
		#print("test2")
		cpu_loadinglevel = True
	if (cpu_load_finish >= 95) & (cpu_loadinglevel == True):
		#print(cpu_load + " foo")
		send_email.main("DANGER DANGER DANGER! Ihr Pi " +  (str(mac)) + "ist bereits zu 95% ausgelastet, er wird sich bald abschalten! Sichern sie ihre Daten, sonst koennte es 			zu Datenverlusten kommen!", "Danger! Danger!")
		print("test")
		cpu_loadinglevel = False
		while_loop = False
		break

Print("Programm wird beendet...")
	
