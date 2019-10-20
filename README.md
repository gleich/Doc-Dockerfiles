# Auto-Doc-Dockerfiles

![GitHub release (latest by date)](https://img.shields.io/github/v/release/Matt-Gleich/Auto-Doc-Dockerfiles) ![GitHub repo size](https://img.shields.io/github/repo-size/Matt-Gleich/Auto-Doc-Dockerfiles) ![GitHub contributors](https://img.shields.io/github/contributors/Matt-Gleich/Auto-Doc-Dockerfiles) ![Docker Pulls](https://img.shields.io/docker/pulls/mattgleich/auto-doc-dockerfiles)

## Github Actions

| Action                                                                                                                                                                                      | Action Description                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------|
| [![Actions Status](https://github.com/Matt-Gleich/Auto-Doc-Dockerfiles/workflows/Python-Versions/badge.svg)](https://github.com/Matt-Gleich/Auto-Doc-Dockerfiles/actions) | Testing for Python 3.6, 3.7, and 3.7-dev |
| [![Actions Status](https://github.com/Matt-Gleich/Auto-Doc-Dockerfiles/workflows/Python-Cron/badge.svg)](https://github.com/Matt-Gleich/Auto-Doc-Dockerfiles/actions)     | Cron job for the Python-Versions action  |
| [![Actions Status](https://github.com/Matt-Gleich/Auto-Doc-Dockerfiles/workflows/Docker-Hub/badge.svg)](https://github.com/Matt-Gleich/Auto-Doc-Dockerfiles/actions)      | Pushing Image to Docker Hub              |

## Description

This application automatically created README.md files for Dockerfiles. This is mainly aimed toward a collection of Dockerfiles because it only work with the following file structure:

```
- folder
    - dockerID.txt
    - image name
        - Dockerfile
    - image name
        - Dockerfile
```

Once the README.md files are created automatically by the program, the file structure will look like:

```
- folder
    - dockerID.txt
    - image name
        - Dockerfile
        - README.md
    - image name
        - Dockerfile
        - README.md
```

Each README is based off the template show below. The items in {} are filled in by the program automatically. The program uses the Docker API to get the description from docker hub for the image.

```markdown
# {dockerID}/{imageName}

{DockerHubPulls}

{description}

## Registry

{registry}

## Running
Look inside the Dockerfile to find the commands needed to run the container
```

Here is a quick table explaining each var wrapped in {} that is filled in by the program:

| Variable         | Definition:                                                                                                                                                                                                                                                 |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| {dockerID}       | The id (username) for which the image is registered under on Docker Hub. The program knows this ID because it reads it in from the dockerID.txt file that is places in root of the project folder as seen in the diagram above.                             |
| {imageName}      | The name of the image. The program knows this name because is should be the name of the folder that the docker files is located in.                                                                                                                         |
| {DockerHubPulls} | The amount of pulls the image has on docker hub. If the image is not found on docker hub under the defined dockerID the it will not be displayed. An example would be: ![Docker Pulls](https://img.shields.io/docker/pulls/mattgleich/auto-doc-dockerfiles) |
| {registry}       | Url to the image on Docker Hub. If the image isn't found on Docker then it will just say `No description, look in Dockerfile`                                                                                                                               |

## Features

Below is a list of all the features of this program:

1. Create README.md files
2. If there is a README.md file already for the folder where the Dockerfile is the don't make a new one
3. Automatically find image meta data on Docker Hub

## Requirements

Below is a list of the requirements of this program:

1. Docker
2. Docker Compose

## Setup

1. Make sure that you have a file structure similar to the one show above in the Description section.
2. Inside of the folder where all the folders are, create a file called dockerID.txt and put you docker ID in there.
3. Make another file called docker-compose.yml and put the following in it (make sure you fill out the path to folder)

```yml
version: "3"

services:
  auto-doc:
    image: mattgleich/auto-doc-dockerfiles
    volumes: 
      - ~/Documents/Github/Dockerfiles:/src/repo
```

## Usage

To run the program run the following command:

```bash
docker-compose up
```

## Docker Images

| Image Tag                                                                                         | Image Description                                  |
|---------------------------------------------------------------------------------------------------|----------------------------------------------------|
| [latest](https://cloud.docker.com/u/mattgleich/repository/docker/mattgleich/auto-doc-dockerfiles/general) | Newest Docker Image created. |
