from flask import Flask, request, jsonify
from ultralytics import YOLO
import os
import base64
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 允许所有来源的跨域请求


@app.route('/infer', methods=['POST'])
def infer():
    try:
        file = request.files['file']
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)) + '/res', 'uploaded.jpg')
        print(file_path)
        file.save(file_path)

        # Run inference on the server
        infer_service = os.getenv('INFER_SERVICE', 'http://localhost:8000/yolov8-infer')
        model = YOLO(infer_service, task="detect")
        results = model(file_path)

        # Process results list
        for result in results:
            result.save(filename = os.path.dirname(os.path.abspath(__file__)) + "/res/result.jpg")

        # Read the result image and encode it as base64
        with open(os.path.dirname(os.path.abspath(__file__)) + "/res/result.jpg", "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

        return jsonify({'result': encoded_string})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
