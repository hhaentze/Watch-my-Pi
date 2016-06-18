import psutil
import sys

Process_int = 0
Processes = []

pids = psutil.pids()
#print (pids)
#Processes.append(pids)
#print(Processes)

for pid in pids:
	Process_int = Process_int + 1
	print Process_int, " current", Processes
	p = psutil.Process(int(pid))
	status = p.is_running()
	if status == True:
		pid_name = p.name()
		cpu = p.cpu_percent(interval=1.0) 
		if cpu > 8:
			print pid, " ", cpu," " , pid_name
			Processes.append(pid)
		else:
			sys.stderr.write("\x1b[2J\x1b[H")
	else:
		sys.stderr.write("\x1b[2J\x1b[H")
print "total processes: ", Process_int
for process in Processes:
	try:
		p = psutil.Process(int(pid))
		pid_name = p.name()
		cpu = p.cpu_percent(interval=1.0)
		print pid, " ", cpu, " ", pid_name
	except:
		print "process was not found anymore"

