# DockerAssignment



Everything is done already to access this application on docker desktop yo have two ways one of them is:
### **1.Docker by creating images and running on container:**
### **2.Docker compose:**
### **Using Docker pull commands:**
If we go ahead with general way then we have to keep this docker file in your directory or you can just run these commands you just need to have Docker Desktop in your Machine the Commands are:
```sh
docker pull syedsofiyan/guessing-game:lastest
docker run -p 5000:5000 syedsofiyan/guessing-game
```
This will pull the image from Docker Hub and then it will run the program on the port 5000 on your machine.
### **Using Docker compose:**
You just need to have the Docker-compose file from this Repository in your machine and just run this command:
```sh
docker-compose up
      (or)
docker-compose up --build
```
it will run automatically
if you want to shut it down use command:
```sh
docker-compose down
```




### **End of Assignment**
