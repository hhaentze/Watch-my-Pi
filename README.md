####	Watch-my-Pi	

![alt tag](https://github.com/harti768/Watch-my-Pi/blob/master/RaspberryPie.png)

###__Was ist Watch-my-Pi?__


 Watch My Pi! ist eine Überwachungs-Software für deinen Raspberry Pi welche in der Lage ist CPU und RAM zu scannen.
 Damit kann es  fehlerhafte sowie schädliche Programme entdecken, welche den Raspberry behindern und so keine volle
 Auslastung erlauben. Das Ziel ist dabei nicht Viren oder Trojaner zu entdecken, sondern eine Überlastung des Paspberry
 zu verhindern. Ab einem festgelegten Grenzwert bei CPU oder RAM reagiert Watch My Pi!, protokolliert die fehlerhaften
 Programme und sendet eine E-Mail mit Informationen bezüglich des aufgetretenden Problems an den Besitzer.

 Watch My Pi! soll sich auch durch seine Simpelheit auszeichen, welche jedem Verbraucher, ob Amateur, Profi, jung
 oder alt erlaubt ohne Probleme damit umzugehen. Eine einmalige Installation und Watch My Pi! muss nie wieder angerührt werden.  

 ~
 ~

 Watch My Pi! is a monitoring programm for your Raspberry Pi which is able to scan the RAM and CPU to discover erroneous
 and dangerous programms which prevent your Raspberry from working like it is supposed to. The purpose is not finding viruses
 or trojans but to prevent it from overloading. After reaching a specific limit Watch My Pi! starts to log the erroneous
 programms and sends an e-mail with information about the problem to the owner.

 Our Intention was to create a security programm for the Raspberry everyone, even without extended programming knowledge, can use.
 One unique installation and Watch My Pi! will be your third eye, supervising your Raspberry even when you are not able to.


###__Installation-Ubuntu/Debian__
(works fine with python 2.7.9+)



```

$ sudo apt-get install python-pip

$ pip install psutil

$ pip install email

```

git repository clonen oder herunterladen

TestEmailData.txt unter /opt/watch-my-py/Data.txt speichern

cpu_load.py starten und los gehts!
