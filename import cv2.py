import cv2

# create a video capture object
cap = cv2.VideoCapture(0)

# check if the video capture object was successfully created
if not cap.isOpened():
    print("Error opening video capture")

# loop over frames from the video capture object
while True:
    # capture a frame
    ret, frame = cap.read()

    # display the captured frame
    cv2.imshow("Image", frame)

    # save the captured frame to disk as a PNG file
    cv2.imwrite("captured_image.png", frame)

    # wait for a key press and then release the video capture object and close all windows
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'): # press 'q' to quit the loop
        break

# release the video capture object and close all windows
#cap.release()
#cv2.destroyAllWindows()
