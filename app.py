import cv2
import numpy as np
from src.hand_tracking import HandDetector
from src.ui_manager import UIManager

def main():
    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)
    
    detector = HandDetector()
    ui = UIManager()
    xp, yp = 0, 0
    current_color = 0

    while True:
        success, frame = cap.read()
        if not success: break
        frame = cv2.flip(frame, 1)

        # 1. Detect Hand
        frame = detector.find_hands(frame)
        lm_list = detector.get_position(frame)

        if len(lm_list) != 0:
            x1, y1 = lm_list[8][1:]  # Index tip
            x2, y2 = lm_list[12][1:] # Middle tip
            fingers = detector.fingers_up(lm_list)

            # 2. Selection Mode (2 fingers)
            if fingers[0] and fingers[1]:
                xp, yp = 0, 0
                if y1 < 100:
                    selected = ui.get_color(x1)
                    if selected is not None: current_color = selected
                    elif 970 < x1 < 1250: ui.clear_canvas()
                cv2.rectangle(frame, (x1, y1-25), (x2, y2+25), ui.colors[current_color], cv2.FILLED)

            # 3. Drawing Mode (1 finger)
            elif fingers[0] and not fingers[1]:
                cv2.circle(frame, (x1, y1), 15, ui.colors[current_color], cv2.FILLED)
                if xp == 0 and yp == 0: xp, yp = x1, y1
                cv2.line(ui.canvas, (xp, yp), (x1, y1), ui.colors[current_color], 15)
                xp, yp = x1, y1
            else:
                xp, yp = 0, 0

        # 4. Final Processing
        ui.draw_header(frame)
        img_gray = cv2.cvtColor(ui.canvas, cv2.COLOR_BGR2GRAY)
        _, img_inv = cv2.threshold(img_gray, 50, 255, cv2.THRESH_BINARY_INV)
        frame = cv2.bitwise_and(frame, cv2.cvtColor(img_inv, cv2.COLOR_GRAY2BGR))
        frame = cv2.bitwise_or(frame, ui.canvas)

        cv2.imshow("AirCanvas BYOP", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
