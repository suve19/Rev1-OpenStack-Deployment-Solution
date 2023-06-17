Rev1 OpenStack Deployment Solution

This repository contains Python scripts to deploy and operate the Rev1 service within an OpenStack environment. The solution consists of the following files:

- `install.py`: This Python script installs all the required packages and dependencies for the project.
- `operate.py`: This script deploys and operates the service within the OpenStack environment by creating the required network(s), router(s), nodes, and other required items.
- `cleanup.py`: This script releases and removes all allocated cloud resources once the operation and monitoring of the system are complete.
- `requirements.txt`: This file lists all the required Python packages and libraries required for the project.

## Installation

1. Clone the repository to your local machine.

```bash
git clone https://github.com/suve19/Rev1-OpenStack-Deployment.git
```

2. Navigate to the repository directory.

```bash
cd Rev1-OpenStack-Deployment
```

3. Run the installation script.

```bash
python3 install.py
```

This will install all the required packages and dependencies for the project.

4. Update the `openrc` file with your OpenStack authentication details.

## Operate

To deploy the solution, run the following command:

```bash
python3 operate.py
```

This will create the required network(s), router(s), nodes, and other required items to deploy the Rev1 service within the OpenStack environment.


## Cleanup

Once the operation and monitoring of the system are complete, release and remove all allocated cloud resources by running the following command:

```bash
python3 cleanup.py
```

This will remove all allocated cloud resources, including nodes, security groups, router, subnet, network, floating IPs, and keypair.
