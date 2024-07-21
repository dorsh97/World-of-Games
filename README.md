# World of Games

Welcome to the World of Games project!

There are 3 main games to play:

1. Currency Roulette Game
2. Guessing Game
3. Memory Game

The project includes functionality for displaying your score on a web page using Flask.

Additionally, the project uses a Jenkins pipeline for CI/CD, Docker for containerization, and includes Selenium testing for the Flask app.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Docker](#docker)
- [Jenkins CI/CD Pipeline](#jenkins-cicd-pipeline)
- [Manual Testing](#manual-testing)

## Installation

### Requirements
- Python 3.x
- Python-compatible IDE (optional)
- pip (Python package installer)
- Docker (optional, for containerization)
- Jenkins (optional, for CI/CD pipeline)

### Clone the Repository
```bash
git clone https://github.com/dorsh97/World-of-Games.git
```
```bash
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
You can also open the entire project using any Python-compatible IDE.

### Running the Scores Flask Application
```bash
python main_score.py
```
The application will start on http://localhost:5000

### Starting Over
In order to start over, you need to clear the contents of Scores.txt
```bash
echo "" > Scores.txt
```

## Docker

You can also use Docker to run the Scores Flask application. 

### Building and running the Docker Container
```bash
docker-compose up -d
```

### Starting the game inside the Container
```bash
docker exec -it wog-container python main.py
```
The application will be available on http://localhost:5000

### Stopping and Removing the Docker Container
```bash
docker rm -vf wog-container
```

### Removing the Docker Image
```bash
docker rmi dorsh97/wog
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

## Manual Testing

You can also perform end-to-end testing of the Flask app manually from the `Utilities` folder.

```bash
cd Utilities
```
```bash
python e2e.py
```

##

Have fun!
