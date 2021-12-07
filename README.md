# Fossilized Containers Tech Demo

Description goes here

##Demonstration 1

##Demonstration 2

###Creating a Container with the CLI

Challenges addressed: Installing the CLI, user prompts for CLI, containerization, and documentation

1. Download the file titled "presto-0.0.1-py3-none-any.whl" from above
2. `cd` into the folder containing the wheel distribution file
3. Run the following command to install the presto package
~~~bash
$ pip install presto-0.0.1-py3-none-any.whl
~~~

####Creating the container
1. Run the following command
~~~bash 
$ presto create
~~~
2. Enter the image you would like your container to use when prompted
3. Enter a message for the container to display
4. View the dockerfile created 
   1. Example of a dockerfile:
   ~~~bash 
   FROM python:latest

   RUN pip install flask
   RUN pip install LiPD

   COPY server.py /
   COPY static/ /
   
   EXPOSE 80
   CMD python /server.py
    ~~~
I believe you would start here Emily

##Demonstration 3