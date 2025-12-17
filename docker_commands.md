# Docker Commands

Fill in the Docker commands you used to complete the test.

## Volume

### Create the volume

```bash
docker volume create my-app
```

### Seed the volume (via Docker Desktop)

```bash

```

## Server 1

### Build the image

```bash
docker build -t week9:1.0 .
```

### Run the container

```bash
docker run -d --name server1 -p 8000:8000 --mount source=my-app,target=/app/db week9:1.0
```
## Server 2

### Build the image

```bash
docker build -t week9-2:1.0 .
```


### Run the container

```bash
docker run -d --name server2 -p 8001:8000 --mount source=my-app,target=/app/db week9-2:1.0
```
