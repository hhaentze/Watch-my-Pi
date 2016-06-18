import psutil

Processes = []

pids = psutil.pids()
print (pids)
#Processes.append(pids)
#print(Processes)

for pid in pids:
	p = psutil.Process(int(pid))
	pid_name = p.name()
	cpu = p.cpu_percent(interval=1.0)
	print pid, " ", cpu," " , pid_name
