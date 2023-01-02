# core-server
[![codecov](https://codecov.io/gh/the-deep-nlp/core-server/branch/main/graph/badge.svg?token=1RD8R54GKF)](https://codecov.io/gh/the-deep-nlp/core-server)
Core Project for maintaining database, jobs and tasks.


## Local setup with local DEEP instance
- Copy `.env.sample` as `.env` and set variables. More on some of the vars below.
- Note that, in addition to setting up database config for the core server, we
  need configurations for deep server as well.
- For DEEP db configs, use the config of your local deep database.
    - **NOTE**: you might need to expose ports for database service in your DEEP docker-compose.
- Set the cron job timings for indexing and deep data fetching. The default
  intervals are quite long. So you might want to make them a bit frequent by setting the following:
    ```
      CRON_DEEP_FETCH_MINUTE=*/2
      CRON_DEEP_FETCH_HOUR=*
      CRON_CREATE_INDICES_MINUTE=*/2
      CRON_CREATE_INDICES_HOUR=*
    ```
  This lets us pull deep data and create indices every 2 minutes.
- Then just do docker-compose up
- Create a super user:
    ```
    $ docker-compose exec server bash
    # ./manage.py createsuperuser
    ```
- Add some projects to fetch data and index leads:
    - Login to django admin panel: `http://localhost:9000/admin`.
    - On the side pane, click on `ToFetchProjects`.
    - Add a `ToFetchProject` instance with the `original project id` value as
      the project's id you want to pull data for.
    - Add other projects if needed.


## Setting up server
- Copy `.env.sample` as `.env` and set variables
- Note that, in addition to setting up database config for the core server, we
  need configurations for deep server as well.
    - There's a chance a proxy is being used to access the DEEP db server.
    - In that case, you need to set up a ssh tunnel to the proxy server as:
       `ssh -i ~/.ssh/ec2monitoring.pem -N -L 0.0.0.0:5432:<server_ip>:<server_port> ubuntu@<proxy_host>`.
    - This will listen to port 5432 on your host machine.
    - If you need to access this from inside container, set `DEEP_DB_HOST` env var to `host.docker.internal`.
    - Learn more about ssh tunneling [here](https://linuxhint.com/setup-ssh-tunneling-linux/).
- Then just do docker-compose up


## Modules

### Core
This consists of core entities like Leads, Entries, Analysis Frameworks, etc and the worker scripts used to populate them.

### Deduplication
This consists of entities like Index, Hashes, etc used for deduplication of DEEP leads and corresponding scripts.
