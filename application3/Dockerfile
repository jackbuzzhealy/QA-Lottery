FROM python:3.7
  
#Working Directory for image 
WORKDIR /QA-Lottery-service3

#Copying requirments.txt to working directory 
COPY requirements.txt .

#Installs all requirements/prerequisites 
RUN pip3 install -r requirements.txt

#Copy everything in application1 to working directory 
COPY . .

#Command that runs app
ENTRYPOINT ["/usr/local/bin/python3", "app.py"]  
