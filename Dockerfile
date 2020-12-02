FROM python:3

# set a directory for the app
WORKDIR /usr/scr/app

# copy all the files to the container
COPY . .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# tell the port number the container should expose
EXPOSE 8080

# run the command
CMD ["python", "./Labatory.py"]
