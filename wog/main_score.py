import os
from flask import Flask
from utils import SCORES_FILE_NAME
from utils import BAD_RETURN_CODE


def score_server():
    app = Flask(__name__)
    if os.path.exists(SCORES_FILE_NAME):
        with open(SCORES_FILE_NAME, 'r') as file:
            score = file.read()
        if score.isdigit():
            @app.route("/")
            def flask():
                return f"""
                <html>
                    <head>
                        <title>Scores Game</title>
                    </head>
                    <body>
                        <h1>The Score is:</h1>             
                        <div id="score">{score}</div>
                    </body>
                </html>
        """
        else:
            score = BAD_RETURN_CODE
    if not os.path.exists(SCORES_FILE_NAME) or score == BAD_RETURN_CODE:
        @app.route("/")
        def flask():
            return f"""
            <html>
                <head>
                    <title>Scores Game</title>
                </head>
                <body>
                    <h1>ERROR:</h1>             
                    <div id="score" style="color:red">{BAD_RETURN_CODE}</div>
                </body>
            </html>
    """
    return app.run("0.0.0.0")
