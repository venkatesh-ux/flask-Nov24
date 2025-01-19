FROM python:3.11.9-bookworm
WORKDIR /flask-docker

RUN python3 -m pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENV FLASK_APP=loan_app.py

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]

