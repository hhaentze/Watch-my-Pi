import psutil

Processes = []

pids = psutil.pids()
print (pids)
#Processes.append(pids)
#print(Processes)

for pid in pids:
	p = psutil.Process(int(pid))
	pid_name = p.name()
	print pid, " ", pid_name

