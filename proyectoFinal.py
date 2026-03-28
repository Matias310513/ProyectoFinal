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

#----------------------------------------------------------------FRAME----------------------------------------------------------------
mi_frame = tk.Frame()
mi_frame.pack()
mi_frame.config(width=1000, height=1000, bg='gray11', bd=11, relief='sunken')
imagen_inicial = tk.PhotoImage(file='temperatura-img.png').subsample(x=2, y=2)

#----------------------------------------------------------------LABELS----------------------------------------------------------------
mi_titulo = tk.Label(mi_frame, text=f'Temperatura hoy: {fecha_actual}', fg='black', font=('Comic Sans Ms', 20))
mi_titulo.grid(row=0, column=1, columnspan=2, pady=10)

mi_hora = tk.Label(mi_frame, text=f'Hora: {hora_actual}', fg='black', font=('Comic Sans Ms', 20))
mi_hora.grid(row=1, column=1, columnspan=2, pady=10)

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

def codigo_boton():
    miNombre.set('')
    miApellido.set('')
    miCorreo.set('')
    miContrasena.set('')
    GENERO.set(0)

#----------------------------------------------------------------BOTON----------------------------------------------------------------
enviar = tk.Button(mi_frame, text='Enviar', width=10, height=2, font=('Comic Sans Ms', 10), command=codigo_boton)
enviar.grid(row=8, column=0, padx=10, pady=10)

#----------------------------------------------------------------RADIOBUTTON----------------------------------------------------------------
genero1 = tk.Radiobutton(mi_frame, width=10, height=2, fg='gray', bg='gray15', font=('Comic Sans Ms', 10), text='Femenino', variable=GENERO, value=1)
genero1.grid(row=4, column=2, padx=10, pady=10)
genero2 = tk.Radiobutton(mi_frame, width=10, height=2, fg='gray', bg='gray15', font=('Comic Sans Ms', 10), text='Masculino', variable=GENERO, value=2)
genero2.grid(row=5, column=2, padx=10, pady=10)
genero3 = tk.Radiobutton(mi_frame, width=10, height=2, fg='gray', bg='gray15', font=('Comic Sans Ms', 10), text='Otro', variable=GENERO, value=3)
genero3.grid(row=6, column=2, padx=10, pady=10)

#----------------------------------------------------------------ACTUALIZAR VENTANA----------------------------------------------------------------
def actualizar():
    hora_actual = datetime.datetime.now().strftime('%H:%M:%S')
    mi_hora.config(text=f'Hora: {hora_actual}')
    fecha_actual = datetime.datetime.today().strftime('%A, %d-%B-%Y')
    mi_titulo.config = tk.Label(mi_frame, text=f'Temperatura hoy: {fecha_actual}', fg='black', font=('Comic Sans Ms', 20))
    raiz.after(500, actualizar)

actualizar()

raiz.mainloop()