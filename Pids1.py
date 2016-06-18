import psutil

Processes = []

pids = psutil.pids()
print (pids)
#Processes.append(pids)
#print(Processes)

for pid in pids:
	p = psutil.Process(pid)
	pid_name = p.name()
	cpu = p.cpu_percent(interval=0.1)
	cpu = cpu / psutil.cpu_count()
        if(cpu > 10):
            print pid, "", cpu ,"", pid_name 
