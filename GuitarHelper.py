import random
import time

class GuitarHelper():
    
    strings = {
        1: "e",
        2: "B",
        3: "G",
        4: "D",
        5: "A",
        6: "E"
        }

    notes = {
        1: "A",
        2: "A#/Bb",
        3: "B",
        4: "C",
        5: "C#/Db",
        6: "D",
        7: "D#/Eb",
        8: "E",
        9: "F",
        10: "F#/Gb",
        11: "G",
        12: "G#/Ab"
        }

    section = {
        1: "Low",
        2: "High"
        }

    def __init__(self):

        pass

    def getSingleRandomNote(self):

        random_string = self.strings[random.randint(1,6)]
        random_note = self.notes[random.randint(1,12)]
        random_section = self.section[random.randint(1,2)]

        print(random_string + " string")
        print(random_section + " " + random_note)

    def getTimedRandomNotes(self, wait_time_seconds):
        try:
            while True:
                print("***********************")
                self.getSingleRandomNote()
                time.sleep(wait_time_seconds)
        except KeyboardInterrupt:
            pass
