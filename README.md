# RealTimeBWFilter

This Python code uses the OpenCV library for real-time video processing. It captures video from a specified source (default is the webcam) and continuously applies a black and white filter to each frame, displaying the processed frames in a window. The program exits when the 'q' key is pressed. The `apply_black_white_filter` function converts each frame to grayscale, applies a binary threshold, and converts it back to color before displaying it.
