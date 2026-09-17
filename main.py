import cv2
from ultralytics import YOLO

def run_detection(input_path="sample_traffic.jpg", output_path="annotated_traffic.jpg"):
    """
    Loads an input image, runs YOLO object detection, and saves the annotated result.
    """
    # 1. Load a pre-trained YOLO model (downloads automatically on first run)
    model = YOLO("yolov8n.pt")

    # 2. Run object detection on the input image
    print(f"Processing image: {input_path}...")
    results = model(input_path)

    # 3. Extract the annotated frame with bounding boxes and labels
    annotated_frame = results[0].plot()

    # 4. Save the processed image to disk
    cv2.imwrite(output_path, annotated_frame)
    print(f"Success! Detection output saved to: {output_path}")

if __name__ == "__main__":
    run_detection()
