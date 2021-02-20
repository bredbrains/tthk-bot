FROM python
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
RUN python3 -m pytest tests.py
RUN python3 main.py