import psutil
import Pids
#config values
cpu_load_warning = 10 #70   #value for cpu warning message
cpu_interval = 3      #intval for cpu_percant_reequest




def cpu_load():
	count = psutil.cpu_count()
        condition_cpu_loop = True
        while (condition_cpu_loop):
            cpu_load = psutil.cpu_percent(interval=cpu_interval)
            print(cpu_load)
            if(cpu_load > cpu_load_warning):
                condition_cpu_loop = False
                print("Warning Warning")
                Pids.Pi(count)  
                #return(cpu_load)
                


print(cpu_load())
