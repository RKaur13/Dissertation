import sys
import argparse
import cv2
from tflite_support.task import core
import time
from tflite_support.task import processor
from tflite_support.task import vision
import utils

# Initialises the camera to take continuous inferences
def run(model: str, camera_id: int, width: int, height: int, num_threads: int,
        enable_edgetpu: bool) -> None:

# Defining input variables for later use
  Args:
    model: Name of the TFLite object detection model.
    camera_no: The camera id to be passed to OpenCV.
    width: The width of the frame captured from the camera.
    height: The height of the frame captured from the camera.
    num_threads: The number of CPU threads to run the model.
    enable_edgetpu: True/False whether the model is a EdgeTPU model.


  # Initialising variables to calculate the frames per second of camera
  counter, fps = 0, 0
  # Use time function to start the timer
  start_time = time.time()

  # Use camera to capture the video
  capture = cv2.VideoCapture(camera_no)
  capture.set(cv2.CAP_PROP_FRAME_WIDTH, width)
  capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

  # Initialising variables to show visuals of captured inferences
  #Define image size
  row_size = 20
  left_margin = 24
  #Define text characteristics
  text_color = (0, 0, 255)
  font_size = 1
  font_thickness = 1
  fps_avg_frame_count = 10

  # Initialising the model
  base_options = core.BaseOptions(
      file_name=model, use_coral=enable_edgetpu, num_threads=num_threads)
  detection_options = processor.DetectionOptions(
      max_results=3, score_threshold=0.3)
  options = vision.ObjectDetectorOptions(
      base_options=base_options, detection_options=detection_options)
  detector = vision.ObjectDetector.create_from_options(options)

  # Using continuous loop to capture images and allow model to make inferences
  while capture.isOpened():
    success, image = capture.read()
    if not success:
      sys.exit(
          'ERROR: Please troubleshoot the connected camera'
      )

    # Counting the number of objects present per class in a continuous counter
    counter += 1
    image = cv2.flip(image, 1)

    # Converting image to RGB for TFLite model
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    input_tensor = vision.TensorImage.create_from_array(rgb_image)

    # Using model to run object detection predictions
    detection_result = detector.detect(input_tensor)

    # Draw key areas on image to visualise detections - following utils.py
    image = utils.visualize(image, detection_result)

    # Calculating the frames per second
    if counter % fps_avg_frame_count == 0:
      end_time = time.time() #Stop the timer
      duration = fps_avg_frame_count / (end_time - start_time)
      start_time = time.time()

    # Displaying the FPS on the real-time viddeo capture
    fps_text = 'FPS = {:.1f}'.format(fps)
    text_location = (left_margin, row_size) #Positioning of the text
    cv2.putText(image, fps_text, text_location, cv2.FONT_HERSHEY_PLAIN,
                font_size, text_color, font_thickness)

    # Interruption for user to stop running program if esc is pressed
    if cv2.waitKey(1) == 27:
      break
    cv2.imshow('object_detector', image)

  cap.release()
  cv2.destroyAllWindows()


def main():
  parser = argparse.ArgumentParser(
      formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument(
      '--model',
      help='Path/location of the object detection model.',
      required=False,
      default='efficientdet_lite0.tflite')
  parser.add_argument(
      '--camerano', help='Number of camera.', required=False, type=int, default=0)
  parser.add_argument(
      '--frameWidth',
      help='Width of the frame capture from camera.',
      required=False,
      type=int,
      default=640)
  parser.add_argument(
      '--frameHeight',
      help='Height of frame capture from camera.',
      required=False,
      type=int,
      default=480)
  parser.add_argument(
      '--numThreads',
      help='Number of CPU threads to run model.',
      required=False,
      type=int,
      default=4)
  parser.add_argument(
      '--enableEdgeTPU',
      help='EdgeTPU required?',
      action='store_true',
      required=False,
      default=False)
  args = parser.parse_args()

  run(args.model, int(args.camerano), args.frameWidth, args.frameHeight,
      int(args.numThreads), bool(args.enableEdgeTPU))


if __name__ == '__main__':
  main()
