import random

# Lista de palabras para el juego
palabras = [
    "python", "ciberseguridad", "criptografia", "ingenieria",
    "programacion", "variable", "algoritmo", "bitacora"
]

# Selecciona aleatoriamente una palabra
palabra_secreta = random.choice(palabras).lower()
letras_adivinadas = []         # Letras que el jugador ha ingresado
vidas = 6                      # Número de intentos permitidos

print("🎮 ¡Bienvenido al juego del Ahorcado!")
print("🔐 Palabra secreta seleccionada... ¡Comienza a adivinar!\n")

# Bucle principal del juego
while True:
    # Mostrar estado actual de la palabra
    palabra_mostrada = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            palabra_mostrada += letra + " "
        else:
            palabra_mostrada += "_ "

    print(f"🔤 Palabra: {palabra_mostrada.strip()}")
    print(f"❤️ Vidas restantes: {vidas}")
    print(f"✍ Letras usadas: {', '.join(letras_adivinadas)}\n")

    # Verificar si se ganó el juego
    if all(letra in letras_adivinadas for letra in palabra_secreta):
        print("🎉 ¡Felicidades! Has adivinado la palabra completa:", palabra_secreta.upper())
        break

    # Verificar si se perdió el juego
    if vidas == 0:
        print("💀 Has perdido. La palabra era:", palabra_secreta.upper())
        break

    # Entrada del usuario
    intento = input("➡ Ingresa una letra: ").lower()

    # Validaciones básicas
    if not intento.isalpha() or len(intento) != 1:
        print("⚠️ Por favor ingresa solo una letra válida.\n")
        continue

    if intento in letras_adivinadas:
        print("🔁 Ya habías intentado con esa letra. Intenta otra.\n")
        continue

    # Agregar intento a las letras ingresadas
    letras_adivinadas.append(intento)

    # Verificar si la letra está en la palabra
    if intento not in palabra_secreta:
        vidas -= 1
        print(f"❌ La letra '{intento}' no está en la palabra. Pierdes una vida.\n")
    else:
        print(f"✅ ¡Bien! La letra '{intento}' está en la palabra.\n")
