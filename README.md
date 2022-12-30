# core-server
[![codecov](https://codecov.io/gh/the-deep-nlp/core-server/branch/main/graph/badge.svg?token=1RD8R54GKF)](https://codecov.io/gh/the-deep-nlp/core-server)
Core Project for maintaining database, jobs and tasks.


## Setting up
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
