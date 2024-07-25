import cv2
import numpy as np
from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO("yolov8n.pt")

# Open the video file
# video_path = 1
video_path = "rtsp://your-video-stream-address"
cap = cv2.VideoCapture(video_path)

# 画面尺寸
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 分成4x4的区域
num_regions_x = 3
num_regions_y = 3
region_width = width // num_regions_x
region_height = height // num_regions_y

# 初始化计数矩阵
region_counts = np.zeros((num_regions_y, num_regions_x), dtype=int)

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 inference on the frame
        results = model(frame)

        # 目标检测结果
        detections = results[0].boxes.data.cpu().numpy()

        # 计算每个检测框的中心点
        centers = np.column_stack(
            ((detections[:, 0] + detections[:, 2]) / 2, (detections[:, 1] + detections[:, 3]) / 2))

        # 重置计数矩阵
        region_counts.fill(0)

        # 遍历每个检测框
        for i, (cx, cy) in enumerate(centers):
            # 检查是否是人
            if detections[i, 5] == 0:  # 类别为0是人
                # 计算中心点在哪个区域
                region_x = int(cx // region_width)
                region_y = int(cy // region_height)

                # 增加相应区域的人数计数
                if 0 <= region_x < num_regions_x and 0 <= region_y < num_regions_y:
                    region_counts[region_y, region_x] += 1

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # 绘制分割线
        for i in range(1, num_regions_x):
            cv2.line(annotated_frame, (i * region_width, 0), (i * region_width, height), (0, 255, 0), 2)
        for i in range(1, num_regions_y):
            cv2.line(annotated_frame, (0, i * region_height), (width, i * region_height), (0, 255, 0), 2)

        # Display the annotated frame with region counts
        for y in range(num_regions_y):
            for x in range(num_regions_x):
                text = f'({x},{y}): {region_counts[y, x]}'
                cv2.putText(annotated_frame, text, (x * region_width + 10, y * region_height + 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

        cv2.imshow("YOLOv8 Inference", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()