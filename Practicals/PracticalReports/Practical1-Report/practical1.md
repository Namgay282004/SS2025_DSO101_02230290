# Practical Report: Docker Containerization

## Introduction

Docker is a containerization platform used to package applications along with their dependencies into containers. This ensures that applications run seamlessly across different environments, including development, testing, and production. Docker simplifies application deployment and execution by using container-based virtualization.

![](images/18.png)

## Containerization

Containerization is an OS-based virtualization technique that creates multiple isolated environments in the user space, known as containers. These containers share the same host kernel while maintaining isolation through private namespaces and OS-level resource control mechanisms. Unlike hypervisor-based virtualization, which requires significant hardware resources for virtualizing hardware and device drivers, container-based virtualization offers better efficiency and performance.

![](images/19.png)


## Steps Followed for Docker Containerization Exercise

### 1. Clone the Repository

Clone the repository from the following URL:

```sh
git clone https://github.com/douglasswmcst/reactjs-subdevice
```

### 2. Check Out the Development Branch

Navigate into the cloned repository and switch to the development branch:

```sh
cd reactjs-subdevice
git checkout development
```

### 3. Install Application Libraries

Install the necessary dependencies using npm:

```sh
npm install
```

### 4. Run the Application Locally

Start the application to verify that it works as expected:

```sh
npm start
```

If there are issues related to the Node.js version, switch to a version below 16 using:

```sh
nvm use 16
```

### 5. Create a Dockerfile for Testing

Create a Dockerfile.test in the root working directory.

![](images/20.png)

### 6. Build the Docker Image

Build the Docker image using the following command:

```sh
docker build -f Dockerfile.test -t <User_ID>/<Image_name> .
```
![](images/1.png)

### 7. Run the Docker Container

Run the Docker container with port forwarding and volume mounting:

```sh 
docker run -d -p 3000:3000 -v /app/node_modules -v $(pwd):/app <user_name>/<image_name>
```

Check running containers:

```sh
docker ps
```
![](images/3.png)


To stop the container:

```sh
docker stop <container_id>
```


### 8. Create a Docker Compose File

Create a docker-compose.yml file.

![alt text](images/6.png)

### 9. Start the Docker Container Using Docker Compose

Start the container using Docker Compose:

```sh
docker compose up -d --build
```
![](images/1.png)

### 10. Run Tests in a Separate Container

Check running containers:

```sh
docker ps
```
![](images/3.png)

Access the running container:
```sh
docker exec -it <web_container_id> sh
```
![](images/4.png)

Run the tests inside the container:
```sh
npm run test
```
![](images/5.png)

Exit the container shell:
```sh
exit
```
![](images/5.png)


### 11. Add Test Service in Docker Compose

Modify the docker-compose.yml file to include a test service, then save the file.

### 12. Stop the Container

```sh
docker compose stop
```
![](images/7.png)

### 13. Create a Multi-Stage Build Dockerfile

Create a new Dockerfile implementing a multi-stage build process using different base images.
![](images/8.png)


### 14. Rebuild and Start the Docker Container with the Test Service

Rebuild and start the container:

```sh
docker compose up -d --build
```
![](images/10.png)
![](images/9.png)


Check if the container is running:

```sh
docker ps
```
![](images/11.png)


Once both services are running, stop the containers:

```sh
docker compose stop
```
![](images/12.png)

### 15. Build the Multi-Phase Container Setup

Run the multi-phase container build process:

![](images/13.png)

```sh
docker build .
```
![](images/14.png)
![](images/15.png)



Ensure the image is successfully created by checking:

```sh
docker images
```
![](images/16.png)


### 16. Start the Multi-Phase Container and Expose Ports

Run the container with exposed ports:

```sh
docker run -d -p 8082:80 <image_ID>
```
![](images/17.png)

Here, 8082 is the local host port and 80 is the container port.

### 17. Verify Running Container

Access the application in the browser:
```sh
http://localhost:8082
```



