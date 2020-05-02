import time
import RPi.GPIO as GPIO
import lib.rfid.MFRC522
import db_actions as dba
import signal

buttonRed = 5
buttonGreen = 7

def insert_into_datalog(userId,time):
    s = "-"
    time_in=int(time)
    dba.display_message(s.join(userId),time)

 # Function as specified in uploaded examples on e - portal
def initialize_reader():
    MIFAREReader = MFRC522.MFRC522()
    print("----card reader working -----")
    print("Press red button or green one or key S to stop")

    try:
        while GPIO.input(buttonRed) and GPIO.input(buttonGreen):
            (status, TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
            if status == MIFAREReader.MI_OK:
                (status,userId) = MIFAREReader.MFRC522_Anticoll()
                if status == MIFAREReader.MI_OK:
                    insert_into_datalog(userId,time)
        print("RFID disabled")
        time.sleep(0.5)
    except KeyboardInterrupt:
        GPIO.cleanup()

