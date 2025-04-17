import numpy as np
import cv2

def basic_thresholding(gray_frame, threshold_value):
    """Applies basic thresholding to a grayscale frame."""
    ret, thresh_basic = cv2.threshold(gray_frame, threshold_value, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow("Basic Binary Frame", thresh_basic)

def adaptive_thresholding(gray_frame, threshold_value):
    """Applies adaptive thresholding to a grayscale frame."""
    adaptive_thresh = cv2.adaptiveThreshold(gray_frame, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                                            cv2.THRESH_BINARY_INV, threshold_value, 2)
    cv2.imshow("Adaptive Threshold Frame", adaptive_thresh)

def main():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Open webcam

    if not cap.isOpened():
        print("Error: Could not open webcam")
        return

    threshold_value = 115  # Adjustable threshold

    while True:
        ret, frame = cap.read()
        if not ret:
            break  # Exit if no frame is captured

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to grayscale

        basic_thresholding(gray_frame, threshold_value)
        # adaptive_thresholding(gray_frame, threshold_value)  # Uncomment if needed

        cv2.imshow("Original Frame", frame)  # Show original frame

        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
