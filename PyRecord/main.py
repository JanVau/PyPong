import cv2, numpy, pyautogui, keyboard

filename = "recording"
screen_size = (1920,1080)
codec = cv2.VideoWriter_fourcc(*'mp4v')
vid = cv2.VideoWriter(filename+'.mp4', codec,60.0,(screen_size))

print('starte Aufname')
while True:
    img =pyautogui.screenshot()
    numpy_frame = numpy.array(img)
    frame = cv2.cvtColor(numpy_frame, cv2.COLOR_BGR2RxGB)
    vid.write(frame)
    if keyboard.is_pressed('x'):
        print('stoppe Aufname')
        break

cv2.destroyAllWindows()
vid.release()