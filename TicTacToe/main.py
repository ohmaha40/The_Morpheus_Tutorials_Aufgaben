##spielbereich
liste = ["1","2","3","4","5","6","7","8","9"]

class Spieler:
    def __init__(self, name, zeichen) -> None:
        self.name = name
        self.zeichen = zeichen 
def spielbereich():
    print("\n\n" + "TICTACTOE by Christian Keller")
    print("\n       " + liste[0] + "    " + liste[1] + "    " + liste[2] + " \n\n\n       " +liste[3] + "    " + liste[4] + "    " + liste[5] + " \n\n\n       " + liste[6] + "    " + liste[7] + "    " + liste[8]+ " \n\n\n")
def pruefen():
    if (liste[0] == "X" and liste[1] == "X" and liste[2] == "X") or (liste[0] == "O" and liste[1] == "O" and liste[2] == "O"):
        return True
    elif (liste[3] == "X" and liste[4] == "X" and liste[5] == "X") or (liste[3] == "O" and liste[4] == "O" and liste[5] == "O"):
        return True
    elif (liste[6] == "X" and liste[7] == "X" and liste[8] == "X") or (liste[6] == "O" and liste[7] == "O" and liste[8] == "O"):
        return True
    elif (liste[0] == "X" and liste[3] == "X" and liste[6] == "X") or (liste[0] == "O" and liste[3] == "O" and liste[6] == "O"):
        return True
    elif (liste[1] == "X" and liste[4] == "X" and liste[7] == "X") or (liste[1] == "O" and liste[4] == "O" and liste[7] == "O"):
        return True
    elif (liste[2] == "X" and liste[5] == "X" and liste[8] == "X") or (liste[2] == "O" and liste[5] == "O" and liste[8] == "O"):
        return True
    elif (liste[0] == "X" and liste[4] == "X" and liste[8] == "X") or (liste[0] == "O" and liste[4] == "O" and liste[8] == "O"):
        return True
    elif (liste[2] == "X" and liste[4] == "X" and liste[6] == "X") or (liste[2] == "O" and liste[4] == "O" and liste[6] == "O"):
        return True
    return False
def zug(spieler_a, spieler_b):
    ende = 0
    if ende == 0 or ende == 3:
        z = 1
        s = 1
        while z <= 9:
            if s == 1:
                spielbereich()
                korrekt = 0
                while korrekt == 0:
                    a = (int(input(spieler_a.name + " Dein Zug bitte: "))-1)
                    if liste[a] == str(a + 1):
                        liste[a] = "X"
                        korrekt = 1
                    else: 
                        print("Keine gültige Eingabe")
                if pruefen():
                    ende = 1
                    break
                else:
                    z = z + 1
                s = 2
            else:
                spielbereich()
                korrekt = 0
                while korrekt == 0:
                    a = (int(input(spieler_b.name + " Dein Zug bitte: "))-1)
                    if liste[a] == str(a + 1):
                        liste[a] = "O"
                        korrekt = 1
                    else: 
                        print("Keine gültige Eingabe")
                if pruefen():
                    ende = 2
                    break
                else:
                    z = z + 1
                s = 1
            if z == 9:
                ende = 3
    elif  ende == 3:
        return ende
    return ende    
def start():
    spieler_a = Spieler(input("Spieler A gib deinen Namen an: "), "X")
    spieler_b = Spieler(input("Spieler B gib deinen Namen an: "), "O")
    ergebnis = zug(spieler_a, spieler_b)
    spielbereich()
    if ergebnis == 1:
        print(spieler_a.name + " hat mit dem Zeichen " + spieler_a.zeichen + " das Spiel gewonnen")
    elif ergebnis == 2:
        print(spieler_b.name + " hat mit dem Zeichen " + spieler_b.zeichen + " das Spiel gewonnen")
    elif ergebnis == 3:
        print("Untentschieden")
    
if __name__ == "__main__":
    start()