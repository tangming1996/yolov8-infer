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