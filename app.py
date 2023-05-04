# Importeer de random module zodat we kunnen werken met willekeur
import random

# Herhaal de code oneindig
while True:
    # Doormiddel van input stellen we een vraag aan de gebruiker
    # De input van de functie is de tekst die verschijnt als vraag
    # Het resultaat slaan we op in een variabele genaamd question
    question = input('Uw vraag: ')

    # Controleer of de gebruiker wilt stoppen
    if question.lower() == 'stop':
        # Stop de herhaling en laat het programma eindigen
        break

    # Maak een reeks met alle mogelijke antwoorden
    answers = [
        'Ja!', 
        'Nee!', 
        'Ik denk het niet', 
        'Zeker niet!', 
        'Echt wel!', 
        'Natuurlijk!', 
        'Waarschijnlijk niet', 
        'Misschien'
    ]

    # Het resultaat van question printen we vervolgens naar de console
    print(random.choice(answers))