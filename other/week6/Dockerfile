FROM python:3.6-slim 
#this is an operating system (debian-slim)
#with python 3.6 installed on top!

WORKDIR /app
#mkdir /app inside the container

#ADD . /app 
COPY requirements.txt /app
# COPY bypasses rerunning docker-compose build every time
#just copy / add over all files into the container's app directory

RUN pip install --trusted-host pypi.python.org -r requirements.txt

# CMD ["bash"]

CMD ["python", "students.py"]
