import tkinter as tk
import requests 
import datetime

def obtener_temperatura(ciudad):
    API_KEY = "b659ac379534e31a9554ad46824f94d2"
    URL = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric"

    respuesta = requests.get(URL)
    datos = respuesta.json()

    print(datos)

    if respuesta.status_code == 200: 
        temperatura_celsius = datos["main"]["temp"]
        temperatura_kelvin = temperatura_celsius + 273.15
        temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32

        return temperatura_celsius, temperatura_kelvin, temperatura_fahrenheit
    else:
        return None

#----------------------------------------------------------------RAIZ----------------------------------------------------------------
raiz = tk.Tk()

raiz.title('Temperatura Ciudad')
raiz.config(bg='gray20', bd=20, relief='solid')

#----------------------------------------------------------------VARIABLES----------------------------------------------------------------
fecha_actual = datetime.datetime.today().strftime('%A, %d-%B-%Y')
hora_actual = datetime.datetime.now().time().strftime('%H:%M:%S')
miNombre = tk.StringVar()
miCorreo = tk.StringVar()
miContrasena = tk.StringVar()
miApellido = tk.StringVar()
miCiudad = tk.StringVar()
GENERO = tk.IntVar()
celsius = tk.IntVar()
kelvin = tk.IntVar() 
fahrenheit = tk.IntVar()
temp_c = None
temp_k = None
temp_f = None

#----------------------------------------------------------------FRAME----------------------------------------------------------------
mi_frame = tk.Frame()
mi_frame.pack()
mi_frame.config(width=1000, height=1000, bg='gray11', bd=11, relief='sunken')
imagen_inicial = tk.PhotoImage(file='temperatura-img.png').subsample(x=3, y=3)
imagen_frio = tk.PhotoImage(file='invierno-img.png').subsample(x=3, y=3)
imagen_templado = tk.PhotoImage(file='templado-img.png').subsample(x=3, y=3)
imagen_calor = tk.PhotoImage(file='verano-img.png').subsample(x=3, y=3)

#----------------------------------------------------------------LABELS----------------------------------------------------------------
mi_titulo = tk.Label(mi_frame, text=f'Temperatura hoy: {fecha_actual}', fg='black', font=('Comic Sans Ms', 15))
mi_titulo.grid(row=0, column=0, columnspan=4, pady=10)

mi_hora = tk.Label(mi_frame, text=f'Hora: {hora_actual}', fg='black', font=('Comic Sans Ms', 15))
mi_hora.grid(row=1, column=0, columnspan=4, pady=10)

mi_imagen_label = tk.Label(mi_frame, image=imagen_inicial)
mi_imagen_label.grid(row=2, column=0, columnspan=3, pady=10)

mi_nombre = tk.Label(mi_frame, text='Nombre: ', fg='white', bg='gray11', font=('Comic Sans Ms', 10))
mi_nombre.grid(row=3, column=0, padx=10, pady=10)

mi_apellido = tk.Label(mi_frame, text='Apellido: ', fg='white', bg='gray11', font=('Comic Sans Ms', 10))
mi_apellido.grid(row=4, column=0, padx=10, pady=10)

mi_correo = tk.Label(mi_frame, text='Correo: ', fg='white', bg='gray11', font=('Comic Sans Ms', 10))
mi_correo.grid(row=5, column=0, padx=10, pady=10)

mi_contrasena = tk.Label(mi_frame, text='Contrasena: ', fg='white', bg='gray11', font=('Comic Sans Ms', 10))
mi_contrasena.grid(row=6, column=0, padx=10, pady=10)

mi_ciudad = tk.Label(mi_frame, text='Ingrese una ciudad: ', fg='white', bg='gray11', font=('Comic Sans Ms', 10))
mi_ciudad.grid(row=7, column=0, padx=10, pady=10)

mi_genero = tk.Label(mi_frame, text='Seleccione su genero: ', fg='white', bg='gray11', font=('Comic Sans Ms', 10))
mi_genero.grid(row=3, column=2, padx=10, pady=10)

resultado_temperatura = tk.Label(mi_frame, text='', fg='orange', bg='gray11', font=('Comic Sans Ms', 10))
resultado_temperatura.grid(row=9, column=0, padx=10, pady=10)

temperatura = tk.Label(mi_frame, text='', fg='orange', bg='gray11', font=('Comic Sans Ms', 10))
temperatura.grid(row=7, column=3, padx=10, pady=10)

#----------------------------------------------------------------ENTRY----------------------------------------------------------------
mi_nombre_entry = tk.Entry(mi_frame, width=10, fg='gray', bg='gray15', justify='center', font=('Comic Sans Ms', 20), textvariable=miNombre)
mi_nombre_entry.grid(row=3, column=1, padx=10, pady=10)

mi_apellido_entry = tk.Entry(mi_frame, width=10, fg='gray', bg='gray15', justify='center', font=('Comic Sans Ms', 20), textvariable=miApellido)
mi_apellido_entry.grid(row=4, column=1, padx=10, pady=10)

mi_correo_entry = tk.Entry(mi_frame, width=10, fg='gray', bg='gray15', justify='center', font=('Comic Sans Ms', 20), textvariable=miCorreo)
mi_correo_entry.grid(row=5, column=1, padx=10, pady=10)

mi_contrasena_entry = tk.Entry(mi_frame, width=10, fg='gray', bg='gray15', justify='center', font=('Comic Sans Ms', 20), textvariable=miContrasena)
mi_contrasena_entry.grid(row=6, column=1, padx=10, pady=10)
mi_contrasena_entry.config(show='*')

mi_ciudad_entry = tk.Entry(mi_frame, width=10, fg='gray', bg='gray15', justify='center', font=('Comic Sans Ms', 20), textvariable=miCiudad)
mi_ciudad_entry.grid(row=7, column=1, padx=10, pady=10)

def codigo_temperatura():
    global temp_c, temp_k, temp_f
    ciudad = miCiudad.get()

    resultado = obtener_temperatura(ciudad)

    if resultado:
        temp_c, temp_k, temp_f = resultado
        resultado_temperatura.config(text=f'{temp_c}°C | {temp_k}°K | {temp_f}°F')
    else:
        resultado_temperatura.config(text='Error la obtener la temperatura')
        temp_c = None
        temp_k = None
        temp_f = None

    if temp_c < 10:
        mi_imagen_label.config(image=imagen_frio)
    elif temp_c > 10 and temp_c < 25:
        mi_imagen_label.config(image=imagen_templado)
    elif temp_c > 25:
        mi_imagen_label.config(image=imagen_calor)

def codigo_boton():
    miNombre.set('')
    miApellido.set('')
    miCorreo.set('')
    miContrasena.set('')
    GENERO.set(0)

#----------------------------------------------------------------BOTON----------------------------------------------------------------
temperatura_boton = tk.Button(mi_frame, text='Obtener Temperatura', width=18, height=1, font=('Comic Sans Ms', 10), command=codigo_temperatura)
temperatura_boton.grid(row=8, column=0, padx=10, pady=10)

enviar = tk.Button(mi_frame, text='Enviar', width=18, height=1, font=('Comic Sans Ms', 10), command=codigo_boton)
enviar.grid(row=10, column=0, columnspan=4, pady=10)
#----------------------------------------------------------------RADIOBUTTON----------------------------------------------------------------
genero1 = tk.Radiobutton(mi_frame, width=10, height=2, fg='gray', bg='gray15', font=('Comic Sans Ms', 10), text='Femenino', variable=GENERO, value=1)
genero1.grid(row=4, column=2, padx=10, pady=10)
genero2 = tk.Radiobutton(mi_frame, width=10, height=2, fg='gray', bg='gray15', font=('Comic Sans Ms', 10), text='Masculino', variable=GENERO, value=2)
genero2.grid(row=5, column=2, padx=10, pady=10)
genero3 = tk.Radiobutton(mi_frame, width=10, height=2, fg='gray', bg='gray15', font=('Comic Sans Ms', 10), text='Otro', variable=GENERO, value=3)
genero3.grid(row=6, column=2, padx=10, pady=10)

#----------------------------------------------------------------ACTUALIZAR LABEL CHECKBUTTON----------------------------------------------------------------
def actualizarLabelCheckbutton():
    texto = ''

    if temp_c is None:
        temperatura.config(text='Primero obten la temperatura')
        return
    if celsius.get() == 1:
        texto += f'{temp_c}°C | '
    if kelvin.get() == 1:
        texto += f'{temp_k}°K | '
    if fahrenheit.get() == 1:
        texto += f'{temp_f}°F'

    temperatura.config(text=texto)

#----------------------------------------------------------------CHECKBUTTON----------------------------------------------------------------
temp = tk.Label(mi_frame, text='Temperatura en:', fg='green2', bg='gray11', font=('Comic Sans Ms', 10))
temp.grid(row=2, column=3, padx=10, rowspan=3)
tk.Checkbutton(mi_frame, text='°C', fg='black', bg='red', font=('Comic Sans Ms', 10), variable=celsius, command=actualizarLabelCheckbutton).grid(row=3, column=3, padx=10, pady=10)
tk.Checkbutton(mi_frame, text='°K', fg='black', bg='blue', font=('Comic Sans Ms', 10), variable=kelvin, command=actualizarLabelCheckbutton).grid(row=4, column=3, padx=10, pady=10)
tk.Checkbutton(mi_frame, text='°F', fg='black', bg='yellow', font=('Comic Sans Ms', 10), variable=fahrenheit, command=actualizarLabelCheckbutton).grid(row=5, column=3, padx=10, pady=10)

#----------------------------------------------------------------ACTUALIZAR VENTANA----------------------------------------------------------------
def actualizar():
    hora_actual = datetime.datetime.now().strftime('%H:%M:%S')
    mi_hora.config(text=f'Hora: {hora_actual}')
    fecha_actual = datetime.datetime.today().strftime('%A, %d-%B-%Y')
    mi_titulo.config(text=f'Temperatura hoy: {fecha_actual}')
    raiz.after(500, actualizar)

actualizar()

raiz.mainloop()