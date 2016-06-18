import psutil
import sys

Process_int = 0
Processes = []
Processes_D = {}
pids = psutil.pids()
draw = 0
PID = "PID"
CPU = "CPU"
PID_name = "PID_name"
bool warn = False

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
			sys.stderr.write("\x1b[2J\x1b[H")
	else:
		sys.stderr.write("\x1b[2J\x1b[H")
if (warn != True):
	print "total processes: ", Process_int
	for i in range(0,draw):
		try:
			print Processes_D["PID"+str(i)], " ", Processes_D["CPU"+str(i)], " ", Processes_D["PID_name"+str(i)]
		except:
			print "process was not found anymore"
else: 
	print "WARNING! WARNING! System will be repaired..."
	print PID, " " PID_name, "could be a problem for you, and may could damage your PC! Please keep that in mind."
	

