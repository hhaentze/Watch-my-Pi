import psutil
import sys
<<<<<<< Updated upstream
import os
<<<<<<< HEAD
from email import *
=======
>>>>>>> 1b4529c9460ffda1df54f78e6dd858dc43a895f4
=======
>>>>>>> Stashed changes

Process_int = 0
Processes = []
Processes_D = {}
pids = psutil.pids()
<<<<<<< Updated upstream
draw = 0
PID = "PID"
CPU = "CPU"
PID_name = "PID_name"
warn = False
=======
#print (pids)
#Processes.append(pids)
#print(Processes)
>>>>>>> Stashed changes

for pid in pids:
	Process_int = Process_int + 1
	print Process_int, " current", Processes
	p = psutil.Process(int(pid))
	status = p.is_running()
	if status == True:
		pid_name = p.name()
		cpu = p.cpu_percent(interval=1.0) 
		if cpu > 8:
<<<<<<< Updated upstream
	
			print pid, " ", cpu," " , pid_name
			Processes.append(pid)
			PID = "PID"+str(draw)
			CPU = "CPU"+str(draw)
			PID_name = "PID_name"+str(draw)
			PR1 = {PID:pid,CPU:cpu,PID_name:pid_name}
			Processes_D.update(PR1)
			draw = draw + 1
		elif cpu >= 85:
			print pid, " ", cpu," " , pid_name
			Processes.append(pid)
			PID = "PID"+str(draw)
			CPU = "CPU"+str(draw)
			PID_name = "PID_name"+str(draw)
			PR1 = {PID:pid,CPU:cpu,PID_name:pid_name}
			Processes_D.update(PR1)
			warn = True
			break
		else:
			os.system('clear')
	else:
		os.system('cls')
if (warn != True):
	print "total processes: ", Process_int
	for i in range(0,draw):
		try:
			print Processes_D["PID"+str(i)], " ", Processes_D["CPU"+str(i)], " ", Processes_D["PID_name"+str(i)]
		except:
			print "process was not found anymore"
else: 
	print "WARNING! WARNING! System will be repaired..."
	print PID, " ", PID_name, "could be a problem for you, and may could damage your PC! Please keep that in mind."
<<<<<<< HEAD
	
=======
>>>>>>> 1b4529c9460ffda1df54f78e6dd858dc43a895f4
	
=======
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
>>>>>>> Stashed changes

