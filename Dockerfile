#build like
#docker build -t my_image .

#run like 
#$docker run -i my_image .

FROM python:3.9


WORKDIR /app

COPY requirements.txt .

RUN python3 -m venv venv

# THIS command executes when the image is being built
RUN venv/bin/python3 -m pip install -r requirements.txt


RUN python3 -m pip install -r requirements.txt


# THIS is just metadata on the image - what command will execute to start each container
CMD ["venv/bin/python3", "cryptotrading.py"]
# you can override the CMD with a second argument to docker run
# usually we use this more awkward syntax for CMD

COPY . .