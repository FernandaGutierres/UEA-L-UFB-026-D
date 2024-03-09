#  función temperatura_promedio_ciudad calcula el
#  promedio de temperatura semanal para una ciudad específica
def Temperatura_Promedio_Ciudad(ciudad_datos):
    promedios_semanales = []

    # Iteramos sobre cada semana en los datos de la ciudad
    for semana in ciudad_datos:
        # Sumamos las temperaturas de cada día en la semana
        suma_temperaturas = sum(dia["Temperatura"] for dia in semana)
        # Calculamos el promedio de temperatura de la semana y
        # lo agregamos a la lista de promedios
        promedio_semanal = suma_temperaturas / len(semana)
        promedios_semanales.append(promedio_semanal)

    # Calculamos el Promedio General de la Ciudad
    promedio_general = sum(promedios_semanales) / len(promedios_semanales)
    return promedio_general


#  Creamos una funcion calcular_temperatura_promedio
#  toma los datos específicos de cada ciudad y calcula el promedio de temperatura
def Calcular_Temperatura_Promedio(Datos_Ciudades):
    for Ciudad_Datos in Datos_Ciudades:
        for Ciudad_Nombre, Datos_Ciudad in Ciudad_Datos.items():
            # calcula el promedio de temperatura
            Promedio_Ciudad = Temperatura_Promedio_Ciudad(Datos_Ciudad)
            print(" \n ======================================================>")
            print(f"El promedio de temperatura en {Ciudad_Nombre} es: {Promedio_Ciudad:.2f}°Celsius")


# Ejemplo de uso

# Ejemplo de uso
datos_ciudades = [
    {"Santo Domingo": [
        # Datos de Concordia...
        [  # SEMANA 1
            {"Dia": "Lunes", "Temperatura": 30},
            {"Dia": "Martes", "Temperatura": 31},
            {"Dia": "Miercoles", "Temperatura": 26},
            {"Dia": "Jueves", "Temperatura": 32},
            {"Dia": "Viernes", "Temperatura": 33},
            {"Dia": "Sabado", "Temperatura": 34},
            {"Dia": "Domingo", "Temperatura": 35}
        ],
        [  # SEMANA 2
            {"Dia": "Lunes", "Temperatura": 20},
            {"Dia": "Martes", "Temperatura": 21},
            {"Dia": "Miercoles", "Temperatura": 22},
            {"Dia": "Jueves", "Temperatura": 23},
            {"Dia": "Viernes", "Temperatura": 24},
            {"Dia": "Sabado", "Temperatura": 25},
            {"Dia": "Domingo", "Temperatura": 26}
        ],
        [  # SEMANA 3
            {"Dia": "Lunes", "Temperatura": 16},
            {"Dia": "Martes", "Temperatura": 17},
            {"Dia": "Miercoles", "Temperatura": 18},
            {"Dia": "Jueves", "Temperatura": 19},
            {"Dia": "Viernes", "Temperatura": 20},
            {"Dia": "Sabado", "Temperatura": 21},
            {"Dia": "Domingo", "Temperatura": 22}
        ],
        [  # SEMANA 4
            {"Dia": "Lunes", "Temperatura": 22},
            {"Dia": "Martes", "Temperatura": 23},
            {"Dia": "Miercoles", "Temperatura": 24},
            {"Dia": "Jueves", "Temperatura": 25},
            {"Dia": "Viernes", "Temperatura": 26},
            {"Dia": "Sabado", "Temperatura": 27},
            {"Dia": "Domingo", "Temperatura": 28}
        ],
    ]},

    {"Concordia": [
        # Datos de Archidona
        [  # SEMANA 1
            {"Dia": "Lunes", "Temperatura": 10},
            {"Dia": "Martes", "Temperatura": 11},
            {"Dia": "Miercoles", "Temperatura": 12},
            {"Dia": "Jueves", "Temperatura": 13},
            {"Dia": "Viernes", "Temperatura": 14},
            {"Dia": "Sabado", "Temperatura": 15},
            {"Dia": "Domingo", "Temperatura": 16}
        ],
        [  # SEMANA 2
            {"Dia": "Lunes", "Temperatura": 17},
            {"Dia": "Martes", "Temperatura": 18},
            {"Dia": "Miercoles", "Temperatura": 19},
            {"Dia": "Jueves", "Temperatura": 20},
            {"Dia": "Viernes", "Temperatura": 21},
            {"Dia": "Sabado", "Temperatura": 22},
            {"Dia": "Domingo", "Temperatura": 23}
        ],
        [  # SEMANA 3
            {"Dia": "Lunes", "Temperatura": 15},
            {"Dia": "Martes", "Temperatura": 16},
            {"Dia": "Miercoles", "Temperatura": 17},
            {"Dia": "Jueves", "Temperatura": 18},
            {"Dia": "Viernes", "Temperatura": 19},
            {"Dia": "Sabado", "Temperatura": 20},
            {"Dia": "Domingo", "Temperatura": 21}
        ],
        [  # SEMANA 4
            {"Dia": "Lunes", "Temperatura": 10},
            {"Dia": "Martes", "Temperatura": 12},
            {"Dia": "Miercoles", "Temperatura": 13},
            {"Dia": "Jueves", "Temperatura": 14},
            {"Dia": "Viernes", "Temperatura": 15},
            {"Dia": "Sabado", "Temperatura": 16},
            {"Dia": "Domingo", "Temperatura": 17}
        ],

    ]},

    {"Santo Domingo": [
        [  # SEMANA 1
            {"Dia": "Lunes", "Temperatura": 20},
            {"Dia": "Martes", "Temperatura": 26},
            {"Dia": "Miercoles", "Temperatura": 23},
            {"Dia": "Jueves", "Temperatura": 24},
            {"Dia": "Viernes", "Temperatura": 15},
            {"Dia": "Sabado", "Temperatura": 22},
            {"Dia": "Domingo", "Temperatura": 26}
        ],

        [  # SEMANA 2
            {"Dia": "Lunes", "Temperatura": 30},
            {"Dia": "Martes", "Temperatura": 31},
            {"Dia": "Miercoles", "Temperatura": 31},
            {"Dia": "Jueves", "Temperatura": 32},
            {"Dia": "Viernes", "Temperatura": 34},
            {"Dia": "Sabado", "Temperatura": 35},
            {"Dia": "Domingo", "Temperatura": 36}
        ],
        [  # SEMANA 3
            {"Dia": "Lunes", "Temperatura": 25},
            {"Dia": "Martes", "Temperatura": 26},
            {"Dia": "Miercoles", "Temperatura": 27},
            {"Dia": "Jueves", "Temperatura": 28},
            {"Dia": "Viernes", "Temperatura": 29},
            {"Dia": "Sabado", "Temperatura": 30},
            {"Dia": "Domingo", "Temperatura": 24}
        ],
        [  # SEMANA 4
            {"Dia": "Lunes", "Temperatura": 15},
            {"Dia": "Martes", "Temperatura": 16},
            {"Dia": "Miercoles", "Temperatura": 16},
            {"Dia": "Jueves", "Temperatura": 22},
            {"Dia": "Viernes", "Temperatura": 22},
            {"Dia": "Sabado", "Temperatura": 24},
            {"Dia": "Domingo", "Temperatura": 34}
        ]
    ]}
]

Calcular_Temperatura_Promedio(datos_ciudades)
