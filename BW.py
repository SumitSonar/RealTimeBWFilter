import cv2

# Function to apply black and white filter to frame
def apply_black_white_filter(frame):
    # Convert frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Convert grayscale frame to black and white
    _, bw_frame = cv2.threshold(gray_frame, 127, 255, cv2.THRESH_BINARY)
    
    # Convert black and white frame back to BGR color space
    bw_frame_bgr = cv2.cvtColor(bw_frame, cv2.COLOR_GRAY2BGR)
    
    return bw_frame_bgr

# Initialize video capture object
cap = cv2.VideoCapture(0)  # Use 0 for default webcam, change if using other video sources

# Check if the video capture object is opened successfully
if not cap.isOpened():
    print("Error: Unable to open video capture.")
    exit()

# Main loop for real-time video processing
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # Check if frame is captured successfully
    if ret:
        # Apply black and white filter to frame
        processed_frame = apply_black_white_filter(frame)
        
        # Display the processed frame
        cv2.imshow('Processed Frame', processed_frame)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()