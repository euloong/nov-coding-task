# Nov Coding task

Write a small docker-compose system that has two http services.

One has an endpoint `/send` which accepts a request with a message parameter. It then HTTP POSTs that message parameter to the other http service, which then logs it to standout.

You will then be able to visit the first service via a browser or curl command on `/send` and issue a message that will be displayed in the stdout of the docker-compose network while it's running.

## Prerequisites

[Install Docker Compose instructions](https://docs.docker.com/compose/install/)

## Running locally

I created a sender service that will accept a message parameter in the browser or with a curl command. It then posts the message to the receiver service which in turn displays the message in the stdout of the running docker-compose network.

1. To build the services, run:

    ```text
    docker-compose build --no-cache
    ```

2. Then run:

    ```text
    docker-compose up
    ```

3. Check that the services are running by hitting the ping endpoints:

    ```text
    http://localhost:8001/ping # Sender service
    http://localhost:8002/ping # Receiver service
    ```

4. Send a message to the sender `/send` endpoint:

    ```text
    http://localhost:8001/send?message=Hello%2C%20World!
    # or
    curl "http://localhost:8001/send?message=Hello%2C%20World!"
    ```

5. Check that you get a successful response back.
