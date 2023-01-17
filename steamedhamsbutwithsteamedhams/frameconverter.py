import cv2

# Open the video file
video = cv2.VideoCapture('SteamedHams.mp4')

# Get the frames per second (fps) of the video
fps = int(video.get(cv2.CAP_PROP_FPS))

# Get the total number of frames in the video
total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

# Create a variable to keep track of the current frame
current_frame = 0

while True:
    # Read the current frame
    ret, frame = video.read()

    # Break the loop if we've reached the end of the video
    if not ret:
        break

    # Save the current frame as an image
    cv2.imwrite('Frames/frame{}.jpg'.format(current_frame), frame)

    # Update the current frame
    current_frame += 1

    # Show the current frame (optional)
    cv2.imshow('frame', frame)
    if cv2.waitKey(int(1000/fps)) & 0xFF == ord('q'):
        break

# Release the video capture object
video.release()

# Close all OpenCV windows (optional)
cv2.destroyAllWindows()
