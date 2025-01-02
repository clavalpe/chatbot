FROM python:3.13
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["uvicorn", "src.chatbot_routes:app", "--host", "0.0.0.0", "--port", "8000"]