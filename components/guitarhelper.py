import random
import time

from components.constants import *

class GuitarHelper():

    def __init__(self):

        pass

    def getSingleRandomNote(self):

        random_note = TWELVE_TONE_EQUAL_TEMPERAMENT_NOTES[random.randint(0, 11)]
        random_string = SIX_STRING_GUITAR_STRINGS[random.randint(0,5)]
        random_section = SIX_STRING_GUITAR_NECK_SECTION[random.randint(0,1)]

        print("***********************")
        print(random_string + " string")
        print(random_section + " " + random_note)

    def getTimedRandomNotes(self, wait_time_seconds):
        try:
            while True:
                self.getSingleRandomNote()
                time.sleep(wait_time_seconds)
        except KeyboardInterrupt:
            pass
