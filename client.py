import socket
import cv2
import numpy as np
import imutils
import pickle
import struct

cap = cv2.VideoCapture(0)
c = socket.socket()
c.connect(('localhost', 6969))

while cap.isOpened():

    ret, frame = cap.read()

    frame = imutils.resize(frame, width=320)
    a = pickle.dumps(frame)
    message = struct.pack("Q", len(a)) + a
    c.sendall(message)


    # c.sendall(frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
c.close()
