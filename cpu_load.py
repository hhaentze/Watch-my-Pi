import psutil
import Pids
import Memory
#import email
#config values


cpu_load_warning = 10 #70   #value for cpu warning message
cpu_interval = 3      #intval for cpu_percant_reequest


def cpu_load():
	count = psutil.cpu_count()
        condition_cpu_loop = True
	mem = Memory.Free_Space()
	if mem < 200:
		print "Achtung! Dein Speicher ist kleiner als 200 MB! Bitte sorge dafuer, dass mehr Speicher zur Verfuegung steht."
        while (condition_cpu_loop):
		cpu_load = psutil.cpu_percent(interval=cpu_interval)
		print(cpu_load)
		if(cpu_load > cpu_load_warning):
		        condition_cpu_loop = False
		        print("Warning Warning")
		        print Pids.Pi(count)  
		        #return(cpu_load)
		
		


print(cpu_load())
