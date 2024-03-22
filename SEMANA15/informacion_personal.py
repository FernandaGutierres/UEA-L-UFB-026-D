
#Creamos un diccionario

informacion_fernanda  = {

    'Nombre':  'Maria Fernanda Gutierres Arrobo',

    "Edad": 36,

    'Ciudad': 'Santo Domingo de los Tsachilas',

    'Profesion': 'Estudiante de la Universidad Estata Amazonica'
}


# Agregamos un clave valor y modificamos  la ciudad

informacion_fernanda['Ciudad'] = 'La Concordia'

# Tambien actualizamos la profesion

informacion_fernanda['Profesion'] = 'uea'

if 'Telefono' not in informacion_fernanda:
    informacion_fernanda['Telefono'] = '0987036924'

if 'Edad' in informacion_fernanda:
    del informacion_fernanda['Edad']

print(informacion_fernanda)