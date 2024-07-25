### Triton 推理服务基本说明

- 启动命令: docker run -d --rm -v ./tmp/triton_repo:/models -p 8000:8000 nvcr.io/nvidia/tritonserver:23.09-py3 tritonserver --model-repository=/models
- 当前 config.pbtxt 文件中为空，如果需要往里面添加内容，可以参考以下模版

```yaml
name: "yolo"  # 这个名称需要与模型目录名称一致
platform: "onnxruntime_onnx"
input [
  {
    name: "images",
    data_type: TYPE_FP32,
    dims: [ 1,3,640,640 ]
  }
]
output[
  {
    name: "output0",
    data_type: TYPE_FP32
    dims: [ 1,84,8400 ]
  }
]
```
以部署 yolov8 模型为例，需要将 .pt 格式的模型文件装换成 .onnx 格式的模型文件，并且将名称改为 model.onnx, 放置在 ./tmp/triton_repo/yolo/1/model.onnx 目录下

本项目提供了 transfer_to_onnx.py 脚本进行模型转换