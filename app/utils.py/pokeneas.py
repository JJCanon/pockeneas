import random

POKENEAS = [
    {
        "id": 1,
        "nombre": "Juancho",
        "altura": 1.75,
        "habilidad": "Montañismo extremo",
        "imagen": "https://tu-bucket-s3.s3.amazonaws.com/juancho.jpg",
        "frase": "¡El que madruga, encuentra guayabo!"
    },
    {
        "id": 2,
        "nombre": "Doña Gloria",
        "altura": 1.60,
        "habilidad": "Regateo en el mercado",
        "imagen": "https://tu-bucket-s3.s3.amazonaws.com/donagloria.jpg",
        "frase": "¡No dé papaya, mijo!"
    },
    # Agrega 5-8 más
]

def get_random_pokenea():
    return random.choice(POKENEAS)