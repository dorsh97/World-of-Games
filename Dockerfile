FROM python:alpine
WORKDIR /app
COPY main_score.py .
COPY Utilities/utils.py Utilities/utils.py
RUN pip install -r requirements.txt
EXPOSE 5000
ENV FLASK_APP=main_score.py
ENV FLASK_RUN_HOST=0.0.0.0
CMD ["flask", "run"]
