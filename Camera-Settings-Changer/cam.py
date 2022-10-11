import cv2

# Kamera wird ausgewählt
capture = cv2.VideoCapture(0)

# Einstellungen werden gesetzt
capture.set(cv2.CAP_PROP_BRIGHTNESS, 14)    # Helligkeit
capture.set(cv2.CAP_PROP_CONTRAST, 115)     # Kontrast
capture.set(cv2.CAP_PROP_HUE, 0)            # Hue
capture.set(cv2.CAP_PROP_SATURATION, 146)   # Sättigung