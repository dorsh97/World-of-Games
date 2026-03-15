# World of Games

Welcome to the World of Games project!

There are 3 main games to play:

1. Currency Roulette Game
2. Guessing Game
3. Memory Game

All three games and the scoreboard are unified into a single Flask web application — no terminal required, just run the app and play in your browser.

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
- pip (Python package installer)
- Python-compatible IDE (optional)
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

### Starting the App
```bash
python app.py
```
* The application will be available on http://localhost:5000

You can also open the entire project using any Python-compatible IDE.

### Starting Over
You can reset your score directly from the scoreboard page in the app, or manually:
```bash
echo "" > Scores.txt
```

## Docker

You can also use Docker to run the unified Flask application.

### Building and running the Docker Container
```bash
docker-compose up -d
```
* The application will be available on http://localhost:5000

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
python e2e.py 5000
```

The script will return a system exit code: 0 indicates that all tests passed successfully, while 1 indicates that the testing has failed.

(note that `5000` is the port number)

##

Have fun!
