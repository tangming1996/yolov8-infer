### 基本说明

容器内默认暴露端口为 5000，访问路径在 /infer

访问URL：http://localhost:5000/infer

后端需要获取推理服务地址，使用环境变量 **INFER_SERVICE** 进行配置

### docker 编译及部署

```shell
docker build -t your-image .
docker run -d -p 5002:5000 -e INFER_SERVICE={推理服务IP} your-image
# 例如
# docker run -d -p 5002:5000 -e INFER_SERVICE=http://localhost:8000/yolov8-infer backend:v1
```



