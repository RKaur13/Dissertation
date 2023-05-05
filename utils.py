#Defining number of pixels
margin = 10
row_size = 10
#Defining text properties
font_size = 1
font_thickness = 1
txt_colour = (0, 0, 255)  # colour RGB = red

# Creating a function called 'speech' to read allowed class names using gtts library
def speech(a):
    tts = gTTS(text=a, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")

def Counting_Freq(list):
    frequency = {}
    for items in list:
        freq[items] = list.count(items)
        a=str(frequency)
    speech(x)
    print(x)

#Initialising parameters for bounding boxes of inferences of detections
def visualise(
    image: np.ndarray,
    result: processor.DetectionResult,
) -> np.ndarray:

  Args:
    image: The input RGB image.
    result: The list of all "Detection" objects ready to be visualised.

  Returns:
    image with bounding boxes.

  list = []
  
  for detection in result.detections:
    # Draw bounding box's
    bbox = detection.bounding_box
    start_point = bbox.origin_x, bbox.origin_y
    end_point = bbox.origin_x + bbox.width, bbox.origin_y + bbox.height
    cv2.rectangle(image, start_point, end_point, txt_colour, 3)

    # Showing labels of object classes and confidence levels
    category = detection.categories[0]
    category_name = category.category_name
    list.append(category_name)
    probability = round(category.score, 2)
    result_text = category_name + ' (' + str(probability) + ')'

    text_location = (margin + bbox.origin_x, margin + row_size + bbox.origin_y)

    cv2.putText(image, result_text, text_location, cv2.FONT_HERSHEY_PLAIN, font_size, text_colour, font_thickness)

  Counting_Freq(list)
  return image
