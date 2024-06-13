FROM python:3.12.3

COPY requirements.txt /usr/app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD ["python", "api/app.py"]

# Change directory to the client folder
WORKDIR /app/client

# Install frontend dependencies
RUN npm install

RUN npm start

