
import cv2
import numpy as np

def analyze_otolith(img_path):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    _, thresh = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    try:
        largest = max(contours, key=cv2.contourArea)
        cv2.drawContours(img, [largest], -1, (255,255,255), 3)
        print('Otolith outline detected.')
    except Exception:
        print('No otolith found.')

if __name__ == "__main__":
    analyze_otolith("otolith_sample.jpg")
