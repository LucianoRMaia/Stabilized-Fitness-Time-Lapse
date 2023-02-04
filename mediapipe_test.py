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
  return x,y,vis


cap = cv2.VideoCapture(0)
success = False
while not success:
  success, image = cap.read()
  shape = image.shape

with mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as pose:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      continue

    image.flags.writeable = False
    #image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    if results.pose_landmarks != None:
      for ponto in results.pose_landmarks.landmark:
        x = int(ponto.x*shape[1])
        y = int(ponto.y*shape[0])
        vis = ponto.visibility

        #x_relativo = int(x*shape[1])
        #y_relativo = int(y*shape[0])
        cv2.circle(image, (x, y), radius=5, color=(225, 0, 100), thickness=-1)

    # Draw the pose annotation on the image.
    #image.flags.writeable = True
    #image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    #mp_drawing.draw_landmarks(
    #    image,
    #    results.pose_landmarks,
    #    mp_pose.POSE_CONNECTIONS,
    #    landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Pose', cv2.flip(image, 1))
    if cv2.waitKey(5) & 0xFF == 27:
      #SALVAR DADOS AQUI
      break
cap.release()