#!/Users/ckk/venv/cv/bin/python3
import cv2
import time

cap = cv2.VideoCapture(0)
time.sleep(1)
ret, image = cap.read()
cv2.imwrite('output.jpg', image)

print('content-type: text/html')
print()

print('''
<html>
<body>
<img src="../output.jpg" width="50%" height="50%">
</body>
</html>
''')

