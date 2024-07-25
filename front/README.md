前端需要获取后端推理地址和端口，使用环境变量 INFERENCE_IP 和 INFERENCE_PORT 进行配置， 如果没有，默认后端推理地址使用 localhost:5000

docker build -t your-image .
docker run -d -p 8001:5001 -e INFERENCE_IP=10.64.1.148  -e INFERENCE_PORT=5000 your-image
docker run -d -p 8001:5001 -e INFERENCE_IP=10.64.1.148  -e INFERENCE_PORT=5000 front-infer
docker run -d -p 8001:5001 -e INFERENCE_IP=10.64.1.148  -e INFERENCE_PORT=5002 front-infer