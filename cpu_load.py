import psutil
import Pids
import Memory
import send_email
#import email
#config values
while_loop = True
while(True):

	cpu_load_warning = 10 #70   #value for cpu warning message
	cpu_interval = 3      #intval for cpu_percant_reequest
	cpu_loadinglevel = False
	cpu_load_finish = 0
	def cpu_load():
		count = psutil.cpu_count()
		condition_cpu_loop = True
		mem = Memory.Free_Space()
		if mem < 200:
			print "Achtung! Dein Speicher ist kleiner als 200 MB! Bitte sorge dafuer, dass mehr Speicher zur Verfuegung steht."
		while (condition_cpu_loop):
			cpu_load = psutil.cpu_percent(interval=cpu_interval)
			print(cpu_load)
			cpu_load_finish = cpu_load
			if(cpu_load > cpu_load_warning):
				condition_cpu_loop = False
				print("Warning Warning")
				print Pids.Pi(count)  
				return(cpu_load)
			
			
			
		
		


	print(cpu_load())
	if (cpu_load_finish >= 80) & (cpu_loadinglevel == False):
		#print(cpu_load + " foo")		
		send_email.main("DANGER DANGER! Ihr Pi ist zu 85% ausgelastet - sofern sie es nicht willentlich tun, untersuchen sie ihn auf Schadsoftware.")
		cpu_loadinglevel = True
	if (cpu_load_finish >= 95) & (cpu_loadinglevel == True):
		#print(cpu_load + " foo")
		send_email.main("DANGER DANGER DANGER! Ihr Pi ist bereits zu 95% ausgelastet, er wird sich bald abschalten! Sichern sie ihre Daten, sonst koennte es 			zu Datenverlusten kommen!") 
		cpu_loadinglevel = False
		while_loop = False
		break

Print("Programm wird beendet...")
	
