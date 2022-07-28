import sys
import cv2

class Streaming:
    def __init__(self):
        print('access-control-allow-origin: *')
        print('age: 0')
        print('cache-Control: no-cache, private')
        print('pragma: no-cache')
        print('content-type: multipart/x-mixed-replace; boundary=frame')
        print()
        sys.stdout.flush()

    def write(self, frame):
        try:
            data = cv2.imencode('.jpg', frame)[1].tobytes()
            print('--frame')
            print('content-type: image/jpeg')
            print('content-length: ', len(data))
            print()
            sys.stdout.flush()
            sys.stdout.buffer.write(data)
            sys.stdout.flush()
            print()
        except:
            sys.stderr.write('ERROR: write jpeg to browser fail.\n')
            quit()

