# Importamos el módulo a utilizar
import pyttsx3

# Solicitamos al usuario el texto a convertir en voz
texto = input("Introduzca texto a convertir: ")

# Separamos el texto completo en palabras
texto_linea = texto.split()

# Inicializamos el motor
engine = pyttsx3.init()

# Reproducimos el texto
# Recorremos palabra por palabra del texto
for linea in texto_linea:
    # Reproducimos dicha palabra
    engine.say(linea)
    # Mantiene el programa reproduciendo hasta el final del texto
    engine.runAndWait()