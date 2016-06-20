 # coding=utf-8


def main():
    #Eingabe von Informationen
    print("Willkomen bei der Installation von Watch My Pi! \nZum Nutzen der Software benötigt Watch My Pi! ihre E-Mail Adresse und Anmelde Daten \nDiese werden nur lokal gespeichert und kommen an keiner Stellle online. \nACHTUNG: Die Anmelde Daten inbegriffen dem Passwort sind zurzeit lokal zugreifbar, wir empfehlen daher eine eigene E-Mail nur fuer Watch My Pi! zu verwenden.")
    emailData = raw_input("\n E_Mail: \n ") +"|"
    emailData += raw_input("\n SMTP Adresse (Form: smtp.domain.com): \n ") +"|"
    emailData += raw_input("\n Passwort: \n ")

    rightKey = False;
    #TODO: Random key generation
    key = "7T23C"

    #Speichern der Daten als .txt Datei
    path = "/opt/Watch-my-Pi/src/Data.txt"
    file = open(path, "w")
    file.write(emailData)
    file.close()

    import send_email
	
	
	
    #Senden einer Email und bestaetigen des Keys
    send_email.main("Bitte uebertragen sie diesen Schluessel in die Konsole:\n\n", key)
    print("\nIhn wurde ein Schluessel per E-Mail gesendet. Bitte bestaetigen sie die Richtigkeit der angegebenen Daten indem sie den Schluessel in die Konsole schreiben.")
    while(rightKey):
        if(input("Schluessel: ")==key):
            rightKey = True
        else:
            print("Der Schluessel war leider falsch")
            
    print("Sie haben Watch My Pi erfolgreich instaliert. Viel Spass damit!")
    
    return True
