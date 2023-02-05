import mediapipe as mp
import cv2
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

#This class is responsible for returning the positions and visibilities of the different anchor points in the pose
class MediapipePose:
  def __init__(self):
    self.pose = mp_pose.Pose(
      min_detection_confidence=0.5,
      min_tracking_confidence=0.5)

  def getPoseParams(self,image):
    image.flags.writeable = False
    results = self.pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    if results.pose_landmarks != None:
      for point in results.pose_landmarks.landmark:
        #TODO HERE I HAVE TO SAVE EACH VALUE OF X Y AND VIS, CURRENTLY I'M JUST PASSING THE LAST VALUE, I'LL FIX TOMORROW
        x = int(point.x*image.shape[1])
        y = int(point.y*image.shape[0])
        vis = point.visibility
        cv2.circle(image, (x, y), radius=5, color=(225, 0, 100), thickness=-1)
      return x,y,vis,image
    else:
      return [],[],[],image

  def getOriginalPoseParams(self,originalImage):
    #TODO: modify this function to save the params and in the future it'll search the saved params instead of reprocessing the Original image again
    xOrg,yOrg,visOrg,image =  self.getPoseParams(originalImage)

    if xOrg != []:
      return xOrg,yOrg,visOrg,image
    else:
      print("We couldn't find any pose in the original image.")

def drawPoses(image,xOrg,yOrg,visOrg,xCurrent,yCurrent,visCurrent):
  for i in xOrg.len:
    #Draw original points
    cv2.circle(image, (xOrg[i], yOrg[i]), radius=5, color=(0, 255, 0), thickness=1)
    #draw current points
    cv2.circle(image, (xCurrent[i], yCurrent[i]), radius=3, color=(255, 0, 0), thickness=1)

  return image


def main():
  #Initialize the mediapipe local class
  mediapipePose = MediapipePose()

  #Get params from the original image
  originalImage = cv2.imread("OriginalImage.jpg")
  xOrg,yOrg,visOrg,image = mediapipePose.getOriginalPoseParams(originalImage)

  #Initializes the camera
  cap = cv2.VideoCapture(0)
  success = False
  while not success:
    success, image = cap.read()

  #Loops through the different sequential frames
  while cap.isOpened():
    success, imageCurrent = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      continue

    xCurrent,yCurrent,visCurrent,annotatedImage = mediapipePose.getPoseParams(imageCurrent)

    resultImage = drawPoses(imageCurrent,xOrg,yOrg,visOrg,xCurrent,yCurrent,visCurrent)

    # Draw the pose annotation on the image.
    #image.flags.writeable = True
    #image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    #mp_drawing.draw_landmarks(
    #    image,
    #    results.pose_landmarks,
    #    mp_pose.POSE_CONNECTIONS,
    #    landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Pose', cv2.flip(resultImage, 1))
    if cv2.waitKey(1) & 0xFF == 27:
      break
  cap.release()

if __name__ == "__main__":
  main()