import random
from time import sleep
import sys


print("Eine kleine Würfelgeschichte\n\n\n"
      "Du erwachst auf einer Waldlichtung.\n"
      "Von hier führen vier Wege weg.\n"
      "In der Mitte sitzt eine Kreatur.\n"
      "Es ist eine Fee.\n"
      "Die Fee fordert dich zu einem Würfelspiel heraus.\n"
      "Die Zahl, die du wirfst entspricht einem der Wege,\n"
      "die offensichtlich verzaubert sind.\n"
      "Dorthin wirst du dann teleportiert.\n")

antwort = input("Nimmst du die Würfel? > ").lower()

if "ja" in antwort:
    pass
else:
    print("Ein magischer Strahl trifft dich\n"
          "und teleportiert dich weg aus dieser Realität.")
    sys.exit()

ergebnis = random.randint(1, 4)
print("Du hast die Zahl", ergebnis, "gewürfelt.\n\n\n")
sleep(4)

if ergebnis == 1:
    print("Du hast offensichtlich den Ausgang gefunden!\n"
          "Du erwachst und erinnerst dich nur an einen Traum, oder?")
elif ergebnis == 2:
    print("Du wirst an ein Moor teleportiert und läufst rein.\n")
elif ergebnis == 3:
    print("Du kommst in das Schlaraffenland.\n"
          "Hier bekommst du alles was du dir wünschst.\n"
          "Du darfst dich auch nach Hause wünschen.\n"
          "Aber nach drei Tagen kehrst du wieder zurück.")
elif ergebnis == 4:
    print("Du fällst in einen endlos tiefen Brunnen.")
