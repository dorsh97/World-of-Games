FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN if [ ! -f Scores.txt ]; then touch Scores.txt; fi
COPY Scores.txt /Scores.txt
RUN pip install -r requirements.txt
EXPOSE 5000
ENV FLASK_APP=main_score.py
ENV FLASK_RUN_HOST=0.0.0.0
CMD ["flask", "run"]
