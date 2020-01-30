#Use python as base image
FROM python:3.5-slim

#Use working directory
WORKDIR /delhi-temperature-prediction

ADD . /delhi-temperature-prediction

#Installing required packages
RUN pip install --trusted-host pypi.python.org -r requirements.txt

#Open port 5000
EXPOSE 5000

#Set environment variable
ENV NAME delhi-temperature-prediction

#Run python program
CMD ["python","app.py"]