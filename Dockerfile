FROM python:alpine
WORKDIR /app
COPY main_score.py .
COPY Utilities/utils.py Utilities/utils.py
RUN pip install Flask
EXPOSE 5000
CMD python main_score.py
