容器内默认暴露端口为 5000
访问路径在 /infer   http://localhost:5000

docker build -t your-image .
docker run -d backend-infer

docker run -d -p 5002:5000 backend-infer