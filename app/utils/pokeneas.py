import random

POKENEAS = [
    {
        "id": 1,
        "nombre": "Juancho",
        "altura": 1.75,
        "habilidad": "Montañismo extremo",
        "imagen": "https://pokenea-imagenes.s3.us-east-1.amazonaws.com/juancho.png",
        "frase": "¡El que madruga, encuentra guayabo!"
    },
    {
        "id": 2,
        "nombre": "Doña Gloria",
        "altura": 1.60,
        "habilidad": "Regateo en el mercado",
        "imagen": "https://pokenea-imagenes.s3.us-east-1.amazonaws.com/donagloria.png",
        "frase": "¡No dé papaya, mijo!"
    },
    {
        "id": 3,
        "nombre": "El Brayan",
        "altura": 1.68,
        "habilidad": "Reparar motos con alambre y fe",
        "imagen": "https://pokenea-imagenes.s3.us-east-1.amazonaws.com/brayan.png",
        "frase": "¡Eso se arregla con un cable y dos babillas!"
    },
    {
        "id": 4,
        "nombre": "Yeison 'El Gato'",
        "altura": 1.72,
        "habilidad": "Escaparse de los tombos en segundos",
        "imagen": "https://pokenea-imagenes.s3.us-east-1.amazonaws.com/yeison.png",
        "frase": "¡Ni que tuvieran turbo, parce!"
    },
    {
        "id": 5,
        "nombre": "La Karen",
        "altura": 1.65,
        "habilidad": "Chismosear mientras vende minutos",
        "imagen": "https://pokenea-imagenes.s3.us-east-1.amazonaws.com/karen.png",
        "frase": "¡Uy, ¿y esa novia que no le cocina?!"
    },
    {
        "id": 6,
        "nombre": "Don Jacinto",
        "altura": 1.70,
        "habilidad": "Predecir el clima con el dolor de huesos",
        "imagen": "https://pokenea-imagenes.s3.us-east-1.amazonaws.com/jacinto.png",
        "frase": "¡Cuando me duele la cadera, llueve más que en Arca de Noé!"
    },
    {
        "id": 7,
        "nombre": "Marlon 'El Chicle'",
        "altura": 1.80,
        "habilidad": "Vender dulces en los buses sin que lo pillen",
        "imagen": "https://pokenea-imagenes.s3.us-east-1.amazonaws.com/marlon.png",
        "frase": "¡A 500 las mentas, ¡y no me regatee!"
    },
    {
        "id": 8,
        "nombre": "La Fresa",
        "altura": 1.63,
        "habilidad": "Bailar reguetón en tacones en cualquier andén",
        "imagen": "https://pokenea-imagenes.s3.us-east-1.amazonaws.com/fresa.png",
        "frase": "¡Si no tiembla, no es fiesta!"
    },
    {
        "id": 9,
        "nombre": "Camilo 'El Chorro'",
        "altura": 1.75,
        "habilidad": "Saber dónde hay fiesta gratis solo con un mensaje de WhatsApp",
        "imagen": "https://pokenea-imagenes.s3.us-east-1.amazonaws.com/camilo.png",
        "frase": "¡El que paga entrada es porque no tiene barrio!"
    },
    {
        "id": 10,
        "nombre": "Doña Tere",
        "altura": 1.58,
        "habilidad": "Hacer sancocho con lo que haya en la nevera",
        "imagen": "https://pokenea-imagenes.s3.us-east-1.amazonaws.com/tere.png",
        "frase": "¡Hasta un hueso de aguacate sirve para dar sabor!"
    },
]

def get_random_pokenea():
    return random.choice(POKENEAS)