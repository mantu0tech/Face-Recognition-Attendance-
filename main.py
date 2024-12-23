# Import the OpenCV library
import cv2

# Define a video capture object, which connects to your camera (camera index 0)
vid = cv2.VideoCapture(0)

# Flag to indicate whether to capture an image
capture_image = False

# Start an infinite loop to continuously capture frames
while True:
    # Capture a video frame from the camera
    ret, frame = vid.read()

    # Display the captured frame in a window labeled 'frame'
    cv2.imshow('frame', frame)

    # Check if the spacebar (' ') key is pressed
    if cv2.waitKey(1) & 0xFF == ord(' '):
        # If the spacebar is pressed, save the frame as an image named 'captured_image.jpg'
        cv2.imwrite('captured_image.jpg', frame)
        print("Image captured!")
        # Reset the flag to indicate that the image has been captured
        capture_image = False

    # Check if the 'q' key is pressed to quit the program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object to free up camera resources
vid.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
