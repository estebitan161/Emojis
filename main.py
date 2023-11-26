import re
from tkinter import *

#libreria para expresiones regulares
emojis = {
    ":)": "😀",
    ":(": "😞",
    ":D": "😁",
     ";)": "😉",
     ":P": "😛",
     "xD" : "😆",
     ":-)" : "😀",
     ":-(" :   "😞",
     "(y)" : "👍",
     "(n)" : "👎",
     "<3" : "❤️",
     "\\m/" : "🤘",
     ":-O" : "😲",
     ":O" : "😲",
     ":-|" : "😐",  #keys se le denomina a los emojis hechos con caracteres
     ":|" : "😐",
     ":*" : "😘",
     ">:(" : "😠",
     "^^": "😊",
     ":-]": "😊",
}

def analizador_lexicografico(palabra_del_metodo):
   nueva_palabra = palabra_del_metodo
   palabra_sin_emojis = palabra_del_metodo
   numero_emojis = 0

   for emoji in emojis.keys():
       patron = re.compile(re.escape(emoji)) #compila y anula caracter especial
       similitudes = re.findall(patron, nueva_palabra)
       numero_emojis += len(similitudes)
       nueva_palabra = re.sub(patron, emojis[emoji], nueva_palabra) #convierte de una palabra a emoji

   for emoji in emojis.keys():
       patron = re.compile(re.escape(emoji)) #compila y anula caracter especial
       palabra_sin_emojis = re.sub(patron, " ", palabra_sin_emojis) #convierte de una palabra a espacio en blanco

   titulo_resultados.config(text="Resultados")

   label_palabra_nueva.config(text=f"La nueva palabra es: {nueva_palabra}")

   label_num_emojis.config(text=f"La cantidad de emojis encontrados es: {numero_emojis}")

   label_num_palabras.config(text=f"La cantidad de palabras encontradas es: {len(palabra_sin_emojis.split())}")

def presionar_boton():
    analizador_lexicografico(entrada.get().strip()) #ejecucion de boton

if __name__ == '__main__':
    interfaz = Tk() #ventana que emerge
    interfaz.title("Proyecto final") #titulo de la ventana
    interfaz.geometry("1000x800")
    interfaz.resizable(width=False, height=False)

    titulo = Label(interfaz, text="Ingresa una frase", font=("Arial", 20))
    titulo.pack(pady=20)

    entrada = Entry(interfaz, font=("Arial", 16))
    entrada.pack(pady=20)

    boton = Button(interfaz, text="Analizar", font=("Arial", 16), command=presionar_boton)
    boton.pack(pady=10)

    titulo_resultados = Label(interfaz, text="", font=("Arial", 20))
    titulo_resultados.pack(pady=20)

    label_palabra_nueva = Label(interfaz, text="", font=("Arial", 18))
    label_palabra_nueva.pack(pady=20)

    label_num_emojis = Label(interfaz, text="", font=("Arial", 18))
    label_num_emojis.pack(pady=20)

    label_num_palabras = Label(interfaz, text="", font=("Arial", 18))
    label_num_palabras.pack(pady=20)

    interfaz.mainloop() #corre