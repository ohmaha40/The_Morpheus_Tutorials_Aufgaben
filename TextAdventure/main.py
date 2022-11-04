class World:
    def __init__(self) -> None:
        pass
    def items(self):
        self.bread = "Brot"
        self.jelly_beans = "Jelly Beans"
        self.coke = "Cola"
        self.small_key = "Kleiner Schlüssel"
        self.big_key = "Großer Schlüssel"
        self.small_chest = "Kleine Truhe"
        self.big_chest = "Große Kiste"
class Raeume:
    def __init__(self) -> None:
        self.zimmer = [{
            "raumnummer": 1,
            "name": "Große Halle",
            "abzweige": 4,
            "angrenzende Räume": [2,3,4,5]
        },{
            "raumnummer": 2,
            "name": "Ausbildungsraum des Lichts",
            "abzweige": 1,
            "angrenzende Räume": [1]
        },{
            "raumnummer": 3,
            "name": "Ausbildsungsraum der Dunkelheit",
            "abzweige": 1,
            "angrenzende Räume": [1]
        },{
            "raumnummer": 4,
            "name": "Ausbildungsraum der Schwerkraft",
            "abzweige": 1,
            "angrenzende Räume": [1]
        },{
            "raumnummer": 5,
            "name": "Ausbildungsraum der Kraft",
            "abzweige": 1,
            "angrenzende Räume": [1]
        }]
    def raumwechsel(self, richtung, spieler):
        if richtung == "vor":
            spieler.aktuelle_raum = self.zimmer[self.zimmer.index(spieler.aktuelle_raum) + 1]
            spieler.aktuelle_pos = 1
        elif richtung == "zurück":
            if spieler.aktuelle_raum != self.zimmer[0]:
                spieler.aktuelle_raum = self.zimmer[self.zimmer.index(spieler.aktuelle_raum) - 1]
                spieler.aktuelle_pos = 1
            else: 
                return False
        

class Player():
    def __init__(self, name) -> None:
        self.name = name
        self.livepoint = 5
        self.magicpower = 10
        self.inventar = [
            [0.0],
            [0.0],
            [0.0],
            [0.0],
            [0.0]
        ]
        self.skills = {
            "Lumos": 0,
            "Nox": 0,
            "Lift": 0,
            "Power": 0
        }   ## Skill erlernt = 1 , anwenden mit Name
        self.aktuelle_pos = 1
        self.aktuelle_raum = raum.zimmer[0]
    def print_inventar(self):
        for item in self.inventar:
            for i in item:
                print(item)
    def eat(self):
        pass
        

    def move(self, spieler, raum):
        befehl = input("Wo hin soll es gehen?: ")
        if befehl == "vor":
            raum.raumwechsel(befehl, spieler)
        elif befehl == "zurück":
            raum.raumwechsel(befehl,spieler)
        elif befehl == exit:
            return False
    
if __name__ == "__main__":
    raum = Raeume()
    spieler = Player(input("Wie ist dein Name?: "))
    while True:
        print("Dein aktueller Raum ist " + spieler.aktuelle_raum["name"] + "\n")
        print("Du hast " + str(spieler.aktuelle_raum["abzweige"]) + " Wege wo du hin kannst")
        spieler.move(spieler, raum)
        