# Fossilized Containers Tech Demo

Read me to walk through the tech demo and better explain what is going on

## Demonstration 1

1. Downloading the LMR Turbo model

  a. $ sudo wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
  b. $ sudo chmod +x Miniconda3-latest-*.sh && ./Miniconda3-latest-*.sh

  c. export PATH="~/miniconda3/bin:$PATH"
     . ~/miniconda3/etc/profile.d/conda.sh

  d. $ source ~/.bashrc
  e. $ which conda

  f. $ conda create -n LMRt python=3.8
  g. $ If HTTP error, $ conda update conda

  h. $ conda activate LMRt
  i. $ conda install -c conda-forge cartopy pyspharm jupyterlab
  j. $ pip install LMRt
  k. $ sudo apt-get update && sudo apt-get upgrade

  l. https://drive.google.com/drive/folders/1UGn-LNd_tGSjPUKa52E6ffEM-ms2VD-N
  m. Extract into Downloads directory
  n. $ mkdir testcases
  o. $ mv Downloads/PAGES2k_CCSM4_GISTEMP testcases/PAGES2k_CCSM4_GISTEMP

  q. $ jupyter notebook
  r. Run file, then exit Jupyter Notebook

  s. $ conda deactivate


2. Download Ubuntu image from Dockerhub

  a. $ sudo apt-get update
  b. $ sudo apt-get install ca-certificates curl gnupg lsb-release

  c. $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
  d. $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

  e.* For Linux Mint
      $  echo \
          "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
          xenial \ stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    * For Ubuntu Impish 21.10, Ubuntu Hirsute 21.04, Ubuntu Focal 20.04 (LTS),
      Ubuntu Bionic 18.04 (LTS)
      $  echo \
          "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
          $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
  f. $ sudo apt-get update

  g. $ apt-cache policy docker-ce

  h. $ sudo apt-get install docker-ce docker-ce-cli containerd.io

  i. $ sudo groupadd docker
  j. $ sudo usermod -aG docker mumbi
  k. $ newgrp docker
  l. $ docker run hello-world

  m. docker pull ubuntu


3. Create Dockerfile for LMR Turbo model

  a. $ nano Dockerfile
        FROM ubuntu

        COPY

4. Create the image of LMR Turbo

  a. docker pull mumbimamb/fossilizedcontainers:latest
  # takes a bit of time

5. From the image, run the LMR Turbo model in a container

  a. docker run -i -t mumbimamb/fossilizedcontainers bash

6. Check that the container is running properly (Docker containers command)

  b. docker run -p 8888:8888 <ID>

7. View the model

  a. $ jupyter notebook --allow-root
  b. Run all

8. Exit the model

  a. Exit jupyter notebook
  b. $ conda deactivate
     $ conda deactivate


9. Stop and delete the container

  a. exit
  b. docker container ls -a
  c. docker rm <CONTAINER ID>

10. Recreate the container from the already created image

  a. docker build -t osboxes/lmrt .

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

1. Go into the folder for Demonstration 3:
```
cd demo3/
```

2. Start the Python server. This is what will receive the LiPD files and send back the NetCDF files.

```
python3 ./server.py
```

1. Start the Python client. This is what will send the LiPD files / Climate Model Parameters and receive the resulting NetCDF file.

```
python3 ./client.py
```

4. Verify the files have been properly sent and received.
