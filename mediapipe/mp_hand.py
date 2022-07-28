import cv2
import mediapipe as mp
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

font = cv2.FONT_HERSHEY_SIMPLEX
text = ""

def distance(hand_landmarks, p1, p2):
    a1 = hand_landmarks.landmark[p1]
    a2 = hand_landmarks.landmark[p2]
    return np.sqrt((a1.x - a2.x)**2 + (a1.y - a2.y)**2)

with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    while True:
        ret, image = cap.read()

        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        text = ""
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                d1 = distance(hand_landmarks, 5, 0)
                d2 = distance(hand_landmarks, 8, 0)
                if (d2 > d1):
                    text = 'hand open' 
                if (d2 <= d1):
                    text = 'hand close'

                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style()
                )
        image = cv2.flip(image, 1)
        cv2.putText(image, text, (200, 100), font, 2, (0,140,255), 10)
        cv2.imshow('MediaPipe Hands', image)
        if cv2.waitKey(5) == 27:
            cv2.destroyAllWindows()
            break
