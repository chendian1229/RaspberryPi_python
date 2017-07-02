#!/usr/bin/env python

import signal
import time

from pirc522 import RFID

run = True
rdr = RFID()
util = rdr.util()
util.debug = True

def end_read(signal,frame):
    global run
    print("\nCtrl+C captured, ending read.")
    run = False
    rdr.cleanup()

signal.signal(signal.SIGINT, end_read)

print("Starting")
while run:
    rdr.wait_for_tag()

    (error, data) = rdr.request()
    if not error:
        print("\nDetected: " + format(data, "02x"))

    (error, uid) = rdr.anticoll()
    if not error:
        print("Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]))

        print("Setting tag")
        s=[102, 201, 95, 92,186]
        util.set_tag(uid)
        print("\nAuthorizing")#0xFF,0xFF,0xFF,0xFF,0xFF,0xFF
        util.auth(rdr.auth_b, [0x74, 0x00, 0x52, 0x35, 0x00, 0xFF])
        print("\nWriting modified bytes")
        util.rewrite(0, [0x11, 0x22, 0x33, 0x00, 0x00])
        util.read_out(0)
        """
        print("\nWriting zero bytes")
        util.rewrite(2, [None, None, 0, 0, 0])
        util.read_out(2)
        print("\nDeauthorizing")
        util.deauth()
        """
        '''
        util.write_trailer(0,  (0xFF,0xFF,0xFF,0xFF,0xFF,0xFF),
                               (0xFF, 0x07, 0x80),
                           105,(0xFF,0xFF,0xFF,0xFF,0xFF,0xFF))
        '''
        util.write_trailer(0,  (0x12, 0x34, 0x56, 0x78, 0x96, 0x92),
                               (0xFF, 0x07, 0x80),
                           105,(0x74, 0x00, 0x52, 0x35, 0x00, 0xFF))
        
        util.deauth()

        time.sleep(1)
