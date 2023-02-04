import mediapipe as mp
import cv2
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

def getPoseParams(image):
  with mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as pose:

    image.flags.writeable = False
    results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    if results.pose_landmarks != None:
      for point in results.pose_landmarks.landmark:
        x = int(point.x*shape[1])
        y = int(point.y*shape[0])
        vis = point.visibility
        cv2.circle(image, (x, y), radius=5, color=(225, 0, 100), thickness=-1)
      return x,y,vis,image
    else:
      return [],[],[],image


cap = cv2.VideoCapture(0)
success = False
while not success:
  success, image = cap.read()
  shape = image.shape


while cap.isOpened():
  success, image = cap.read()
  if not success:
    print("Ignoring empty camera frame.")
    continue

  #0image.flags.writeable = False
  x,y,vis,annotatedImage = getPoseParams(image)

  #cv2.circle(image, (x, y), radius=5, color=(225, 0, 100), thickness=-1)

  # Draw the pose annotation on the image.
  #image.flags.writeable = True
  #image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
  #mp_drawing.draw_landmarks(
  #    image,
  #    results.pose_landmarks,
  #    mp_pose.POSE_CONNECTIONS,
  #    landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
  # Flip the image horizontally for a selfie-view display.
  cv2.imshow('MediaPipe Pose', cv2.flip(annotatedImage, 1))
  if cv2.waitKey(1) & 0xFF == 27:
    #SALVAR DADOS AQUI
    break
cap.release()