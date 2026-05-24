import cv2
from ultralytics import YOLO

def main():
    #import YOLO model

    try:
        model=YOLO("yolov8n.pt")
    except Exception as e:
        print("Error loading YOLO model: ",e)
        return

    webcam=cv2.VideoCapture(0)
    if not webcam.isOpened():
        print("Error:could not access the webcam: ")
        return
    print("Webcam Opened. Press 'esc' to quit.")

    while True:
        _,image=webcam.read()
        if not _:
            print("Failed to grab frame from webcam")
            break
        try:
            results=model(image)
            annotated_frame=results[0].plot()
        except Exception as e:
            print("Error during inference ",e)
            break
        cv2.imshow("YOLOv8 Webcam Detection",annotated_frame)

        key=cv2.waitKey(10)
        if key==27:
            break

    webcam.release()
    cv2.destroyAllWindows

if __name__== "__main__":
    main()