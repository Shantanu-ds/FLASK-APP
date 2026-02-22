######################### DOCKERFILE #########################
FROM python:3.9-slim

WORKDIR /FLASK-APP

RUN python -m pip install --upgrade pip

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "loan_app1.py"]