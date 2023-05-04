# Magic Eight Ball in Python

In deze repo gaan we doormiddel van Python een simpele Magic Eight Ball applicatie maken.
De applicatie draait in de console tot dat we zeggen dat deze moet stoppen.
In dit voorbeeld gaan ik niet in op het installeren van Python.

[Voor het installeren van Python, kun je naar deze instructie kijken.](https://www.informaticastudent.net/1304512_python-installeren-op-windows)

## De Vraag

De eerste stap is de gebruiker een vraag laten stellen aan onze applicatie.
In Python hebben we hier een handige functie voor, namelijk ```input()```.
De input functie heeft één parameter: een prompt.
Door deze parameter een string te geven, wordt deze tekst getoond aan de gebruiker.
De vraag moeten we vervolgens opslaan in een variabele.
Om te testen of dit werkt, kunnen we de input direct in de console plaatsen met ```print()```

```python
# Doormiddel van input stellen we een vraag aan de gebruiker
# De input van de functie is de tekst die verschijnt als vraag
# Het resultaat slaan we op in een variabele genaamd question.
question = input('Uw vraag: ')

# Het resultaat van question printen we vervolgens naar de console.
print(question)
```

## Een Antwoord

De vraag is binnen, tijd om antwoord te geven.
Het idee achter de Magic Eight Ball is er een willekeurig antwoord wordt gegeven op een ja/nee vraag.
Dit willekeurige antwoord komt uit een verzameling van 8 antwoorden.
Laten we eerste beginnen met het programmeren van een enkel antwoord,
hiervoor hoeven we alleen de print functie aan te passen.

```python
# Het resultaat van question printen we vervolgens naar de console.
print('Ja!')
```

## Reeksen

Nu wordt iedere keer het antwoord ```Ja!``` gegeven.
Om meerdere antwoorden mogelijk te maken kunnen we gebruik maken van reeksen (arrays).
Een reeks maken we in Python met [ en ], daartussen zet je alle waarden.
Tussen de ```input()``` en de ```print()``` opdracht zetten we onze nieuwe reeks neer.
Het is ook mogelijk om de reeks op een enkele regel te zetten,
dit vind ik persoonlijk beter leesbaar.

```python
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
```

Om iets uit een reeks te halen, maken we gebruik van een wijzer (index).
In Python, en veel (maar niet alle) andere talen, begint dit bij 0.
Het eerste item in onze reeks (```Ja!```), heeft wijzer 0.
Het tweede item heeft wijzer 1, enzovoorts.
Doormiddel van blokhaakjes kunnen we een item uit de reeks halen met de wijzer.
Dit proberen we weer in de ```print()``` functie.

```python
# Het resultaat van question printen we vervolgens naar de console.
print(answers[3])
```

## Willekeurig Antwoord

Een Magic Eight Ball dat continue hetzelfde antwoord geeft is niet heel interessant.
Tijd om een beetje willekeur aan het programma toe te voegen.
Python biedt hier ondersteuning door middel van de ```random``` module.
Deze moeten we importeren bovenin onze code.

```python
# Importeer de random module zodat we kunnen werken met willekeur
import random
```

Nu kunnen we de ```random``` module gebruiken om willekeur toe te voegen aan ons applicatie.
De random module biedt hiervoor een functie genaamd ```randint()```.
Deze functie geeft een willekeurig getal terug tussen twee gegeven getallen.
De functie is inclusief, de twee gegeven getallen zelf tellen mee.
Door een random getal te maken en op te slaan, kunnen we het antwoord willekeurig maken.
Het volledige bestand ziet er nu als volgt uit.

```python
# Importeer de random module zodat we kunnen werken met willekeur
import random

# Doormiddel van input stellen we een vraag aan de gebruiker
# De input van de functie is de tekst die verschijnt als vraag
# Het resultaat slaan we op in een variabele genaamd question.
question = input('Uw vraag: ')

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

# Genereer een willekeurig antwoord voor alle index
# Om een functie uit een bibliotheek te gebruiken, gebruik je een punt.
# Je leest: uit de random bibliotheek gebruik je de randint functie met 0 en 7 als inputs.
# 0, 1, 2, 3, 4, 5, 6 en 7
chosen_answer = random.randint(0, 7)

# Het resultaat van question printen we vervolgens naar de console.
print(answers[chosen_answer])
```

Het kan echter korter, de ```random``` bibliotheek heeft hier een speciale functie voor.
Dit is de ```choice``` functie. Dit kiest een willekeurig item uit een reeks.

```python
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
```

# Herhalen

De code die we nu hebben geschreven stelt de gebruiker een vraag en geeft antwoord.
De volgende stap dit zich laten herhalen totdat de gebruiker zegt te willen stoppen.
Dit kunnen we doen door een herhaling toe te voegen.
Een herhaling laat de code herhalen zolang er aan een bepaalde voorwaarde wordt voldaan.
Wij kunnen onze code herhalen door alle code, behalve de import, in een while loop te zetten.

```python
# Importeer de random module zodat we kunnen werken met willekeur
import random

# Herhaal de code oneindig
while True:
    # Doormiddel van input stellen we een vraag aan de gebruiker
    # De input van de functie is de tekst die verschijnt als vraag
    # Het resultaat slaan we op in een variabele genaamd question.
    question = input('Uw vraag: ')

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
```

De gebruiker moet wel een manier hebben om de applicatie te stoppen.
Hiervoor maken we gebruik van een voorwaarde.
Op het moment dat er aan een bepaalde voorwaarde wordt voldaan, doen we iets.
In code gebeurd dit met ```if```.
Laten we voor ons programma zeggen dat de gebruiker stop moet invullen om te stoppen.
Nadat de gebruik zijn vraag heeft gesteld, kunnen we hierop controleren.
Een controle is altijd met ```==```.

```python
# Importeer de random module zodat we kunnen werken met willekeur
import random

# Herhaal de code oneindig
while True:
    # Doormiddel van input stellen we een vraag aan de gebruiker
    # De input van de functie is de tekst die verschijnt als vraag
    # Het resultaat slaan we op in een variabele genaamd question.
    question = input('Uw vraag: ')

    # Controleer of de gebruiker wilt stoppen
    if question == 'stop':
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
```

Er is een enkel puntje dat nog niet helemaal werkt zoals gewenst.
De gebruiker moet nu stop invullen met kleine letter, hoofdletters werken niet.
Laten we ervoor zorgen dat dit niet uitmaakt.
Hiervoor kunnen we de ```lower()``` functie gebruiken op de gebruikers input tijdens het controleren.

```python
# Controleer of de gebruiker wilt stoppen
if question.lower() == 'stop':
    # Stop de herhaling en laat het programma eindigen
    break
```

## Uitdaging

Pas de code zo aan dat er gecontroleerd wordt of er daadwerkelijk een vraag wordt gesteld.
Je zou hiervoor kunnen controleren of de input langer is dan 5 tekens en eindigt met een vraagteken.
Succes met coderen!
