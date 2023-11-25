#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

# write 'hello world' to the console
print('hello world')

import random

def obtener_opcion_oponente():
    opciones = ["rock", "paper", "scissors"]
    return random.choice(opciones)

def determinar_ganador(jugador, oponente):
    if jugador == oponente:
        return "Empate"
    elif (
        (jugador == "rock" and oponente == "scissors") or
        (jugador == "scissors" and oponente == "paper") or
        (jugador == "paper" and oponente == "rock")
    ):
        return "Ganaste"
    else:
        return "Perdiste"

def jugar():
    puntuacion = 0

    while True:
        print("\n--- Piedra, Papel o Tijeras ---")
        print("Opciones: rock, paper, scissors")
        
        # Obtener la elección del jugador
        jugador = input("Elige tu opción: ").lower()

        # Validar la entrada del jugador
        if jugador not in ["rock", "paper", "scissors"]:
            print("Opción no válida. Por favor, elige entre rock, paper o scissors.")
            continue

        # Obtener la elección del oponente
        oponente = obtener_opcion_oponente()

        print(f"El oponente eligió: {oponente}")

        # Determinar el ganador de la ronda
        resultado = determinar_ganador(jugador, oponente)
        print(f"Resultado: {resultado}")

        # Actualizar la puntuación
        if resultado == "Ganaste":
            puntuacion += 1

        # Preguntar al jugador si quiere jugar de nuevo
        jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ").lower()
        if jugar_de_nuevo != "s":
            break

    print(f"\nPuntuación final: {puntuacion}")

# Iniciar el juego
jugar()

