import cv2

# Open the default camera (camera index 0)
capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not capture.isOpened():
    print("Error: Could not open camera.")
    exit()

print("Camera opened successfully. Press 'Q' to quit.")

while True:
    # Capture frame-by-frame
    ret, frame = capture.read()

    if not ret:
        print("Error: Could not read frame from camera.")
        break

    # Display the frame in a window
    cv2.imshow('Camera Feed', frame)

    # Break the loop if 'Q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the window
capture.release()
cv2.destroyAllWindows()
