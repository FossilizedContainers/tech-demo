# Fossilized Containers Tech Demo

Description goes here

## Demonstration 1

## Demonstration 2

### Creating a Container with the CLI

Challenges addressed: Installing the CLI, user prompts for CLI, containerization, and documentation

1. Download the file titled "presto-0.0.1-py3-none-any.whl" from presto/dist. You can use the following command on linux to download it
~~~bash
wget https://github.com/FossilizedContainers/tech-demo/raw/master/presto/dist/presto-0.0.1-py3-none-any.whl
~~~
2. `cd` into the folder containing the wheel distribution file
3. Run the following command to install the presto package
~~~bash
$ pip install presto-0.0.1-py3-none-any.whl
~~~

#### Creating the container
1. Run the following command
~~~bash
$ presto create
~~~
2. Enter the OS you would like your container to use
3. Enter the message you would like to display
4. View the dockerfile created
   1. Example of a dockerfile:
   ~~~bash
   FROM alpine
   CMD ["echo", "Hello World!"]
    ~~~
5. Download the demonstration Dockerfile from our github.
   ~~~bash
   wget https://raw.githubusercontent.com/FossilizedContainers/tech-demo/master/C4/Dockerfile
   ~~~
6. Run the following command
   ~~~bash
   presto run
   ~~~

7. You should have seen your container running
   1. Example output:
   ~~~bash
   Building image from Dockerfile...

   Finished building image...

   Running the container...

   Hello World!
   ~~~

8. Now run the following command to clean up the container to free up resources
  ~~~bash
  presto clean
  ~~~
## Demonstration 3
