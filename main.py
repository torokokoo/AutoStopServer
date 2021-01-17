import keyboard
from datetime import datetime
import time

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    time.sleep(15)
    
    if str(current_time) == "02:45":
        keyboard.write('say "El servidor se apagara en 15 minutos, devuelvete a tu casa si no quieres morir"')
        keyboard.press_and_release('enter')
        print(str(current_time) + ': Alerta de 15 minutos enviada')
    
    if str(current_time) == "03:00":
        keyboard.write('say "Gracias por estar en el servidor! Nos vemos mañana al mediodia"')
        keyboard.press_and_release('enter')
        print(str(current_time) + ': Alerta de apagado enviado')
        
        keyboard.write("save")
        keyboard.press_and_release('enter')
        
        print('Started saving')
        time.sleep(75)
        
        keyboard.write("quit")
        keyboard.press_and_release('enter')
        
        print('Started Quitting')
        time.sleep(75)
        
        keyboard.send('alt+F4')
        print(str(current_time) + ': Consola cerrada')

        

