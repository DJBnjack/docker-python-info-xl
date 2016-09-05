docker kill dpi
docker rm dpi
docker build -t dpi . 
timeout 2
docker run -d -p 5000:5000 -v /var/run/docker.sock:/var/run/docker.sock --name dpi dpi