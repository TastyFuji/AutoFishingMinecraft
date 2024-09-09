import cv2
import pytesseract
import pyautogui
import numpy as np
import time
import os

print("ระบบกำลังจะเริ่มทำงานในอีก 5 วินาที กรุณาสลับไปที่หน้าต่างเกมแบบเต็มจอ")
time.sleep(5.0)

pyautogui.click(button="right")

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

os.system('cls' if os.name == 'nt' else 'clear')
print(f"[Auto Fishing 1.0] Starting auto-fishing [TastyFuji] {time.asctime()}")

detectPhrase = "Fishing Bobber"
screenRegion = (2350, 1200, 2560, 1440)
catchCount = 0

try:
    while True:
        phraseFound = False

        # แคปจอ ในพื้นที่ที่ระบุ
        screenCapture = pyautogui.screenshot(region=screenRegion)
        scImage = cv2.cvtColor(np.array(screenCapture), cv2.COLOR_RGB2BGR)

        # ใช้ Tesseract แปลง scImage จากรูปภาพเป็นข้อความ
        scText = pytesseract.image_to_string(scImage)

        if detectPhrase.lower() in scText.lower():
            phraseFound = True
            catchCount += 1
            print(f"[TastyFuji] Attempting catch number: {catchCount}", end="\r")
            pyautogui.moveTo(screenRegion[0], screenRegion[1])
            pyautogui.click(button="right")
        
        if phraseFound:
            time.sleep(4.0)
            pyautogui.click(button="right")
    
        time.sleep(0.2)

except KeyboardInterrupt:
    print("\n[Auto Fishing] Stopping auto-fishing [TastyFuji]")
