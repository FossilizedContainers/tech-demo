import click
import docker

# creating a group of commands that can be run
@click.group()
def cli():
    pass


# Requires: Initialized docker client
# TO DO:    Check if docker client is initialized, if not then pass an error
# adding the pull image command to the group and taking the name an image to pull
@cli.command()
@click.argument('image')
def pull_image(image):
    print(f"Pulling {image} image...")

    # Pull the specified image from dockerhub
    # Equivalent to: docker pull <image>
    image = client.images.pull(image)
    print(image.id + '\n')

# Requires: Initialized docker client,
#           Alpine image pulled and/or available
# TO DO:    Check if docker client is initialized, if not then pass an error
# TO DO:    Check if the image is available, if not then pass an error
# adding the hello-world command to the group
@cli.command()
def hello_world():
    example = click.prompt("Please specify what OS you would like to use", type=str)
    message = "echo "
    message += click.prompt("Please enter a message for the container to display", type=str)
    print("\nCreating new container...")

    client.attrs.image(example)
    client.attrs.exec_run(message)
    # Run the hello world container
    # Equivalent to: docker run alpine echo hello world
    print(client.attrs.start)


@cli.command()
def run():
    # Build the image
    print("Building image from Dockerfile...\n")
    client.images.build(path=".", tag="tech-demo")
    print("Finished building image...\n")

    # Run the container
    print("Running the container...\n")
    cont = client.containers.run("tech-demo", detach=True)
    print(cont.logs().decode("utf-8"))


# Requires: Initialized docker client,
#           Alpine image pulled and/or available
# TO DO:    Check if docker client is initialized, if not then pass an error
# TO DO:    Check if the image is available, if not then pass an error
# adding the detached-hello command to the group
@cli.command()
def detached_hello():
    print("\nStarting new detached container...")
    # Run the hello world container, but this time we detach it and get the logs after
    # Equivalent to: docker run -d alpine echo hello world
    alpine_cont = client.containers.run("alpine", "echo hello world",
                                        detach=True)
    print("\nContainer Logs:")

    # print of the logs of the container
    # Equivalent to: docker logs <container_id>
    print(alpine_cont.logs().decode("utf-8"))

@cli.command()
def displayContainers():
    client.containers.list()

# command mostly for testing
# will stop all containers and prune them
@cli.command()
def clean():
    print("Stopping all containers...\n")
    for container in client.containers.list():
        container.stop()

    print("Deleting all containers...\n")
    client.containers.prune()

# main to initiate variables and group
def main():
    global client
    client = docker.from_env()
    cli()


if __name__ == '__main__':
    main()
