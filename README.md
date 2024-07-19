# World of Games

Welcome to the World of Games project!
There are 3 main games to play - Currency Roullete Game, Guessing Game, and Memory Game.
The project includes functionality for displaying your score on a web page using Flask.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Docker](#docker)
- [Jenkins CI/CD Pipeline](#jenkins-cicd-pipeline)

## Installation

### Prerequisites
- Python 3.x
- Python-compatible IDE (optional)
- pip (Python package installer)
- Docker (optional, for containerization)
- Jenkins (optional, for CI/CD pipeline)

### Clone the Repository
```bash
git clone https://github.com/dorsh97/World-of-Games.git
cd World-of-Games
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage

### Starting the Game
```bash
python main.py
```

### Running the Scores Flask Application
```bash
python main.py
```
The application will start on http://localhost:5000

## Docker

You can also use Docker to run the Scores Flask Application.

### Build the Docker Image
```bash
docker-compose build
```

### Running the Docker Container
```bash
docker-compose up
```
The application will be available on http://localhost:5000

### Stopping and Removing the Docker Container
```bash
docker rm -vf wog-flask-container
```

### Removing the Docker Image
```bash
docker rmi dorsh97/wog-flask
```

## Jenkins CI/CD Pipeline

This project uses Jenkins for continuous integration and continuous deployment. The Jenkins pipeline is defined in the Jenkinsfile located in the root of the repository.

### Pipeline Stages
1. Checkout: Clones the repository.
2. Build: Builds the Docker image.
3. Run: Runs the Docker container.
4. Test: Executes end-to-end tests using Selenium.
5. Finalize: Pushes the Docker image to Docker Hub and cleans up resources.
6. Post Actions: Ensures cleanup of Docker containers and images, and workspace.


Have fun!
