docker stop itnun
docker rm itnun
docker build -t itnun:latest .
docker run -d -p 0.0.0.0:5000:5000/tcp --name itnun itnun:latest