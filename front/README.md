### 前端部署基本说明

前端需要获取后端推理地址和端口，使用环境变量 **INFERENCE_IP** 和 **INFERENCE_PORT** 进行配置， 如果没有，默认后端推理地址使用 localhost:5000

前端容器部署端口为 5001，url 路径为 /infer ---->  localhost:5001/infer

docker 编译及部署

```shell
docker build -t your-image .
docker run -d -p 8001:5001 -e INFERENCE_IP={后端服务IP}  -e INFERENCE_PORT=5000 your-image
# 例如
docker run -d -p 8001:5001 -e INFERENCE_IP=127.0.0.1 -e INFERENCE_PORT=5000 front-ui:v1
```



