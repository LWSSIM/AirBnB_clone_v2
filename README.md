# [Air BnB Project](https://github.com/LWSSIM/AirBnB_clone/blob/master/README.md)

# Web flask + MySQL


# Fabric Deployment README

![image](https://github.com/LWSSIM/AirBnB_clone_v2/assets/127129101/2e8996d6-ce8c-4249-a7a7-6051fd5cf077)


## Introduction
This README provides a comprehensive guide on using Fabric for deploying code to a server, managing Nginx configuration, and executing commands both locally and remotely. Fabric is a Python library and command-line tool designed to simplify the process of remote administration and deployment tasks.

## What is Fabric?
Fabric is a Python library and command-line tool that simplifies the process of executing commands remotely over SSH. It provides a simple and Pythonic interface for automating tasks such as deployment, system administration, and configuration management.

## How to Deploy Code to a Server Easily
To deploy code to a server using Fabric, follow these steps:

1. Install Fabric using pip: `pip install fabric`.
2. Write a Fabric script (usually named `fabfile.py`) defining deployment tasks.
3. Define tasks for tasks like pulling code from a version control system, copying files to the server, restarting services, etc.
4. Execute the Fabric commands to run the deployment tasks defined in the fabfile.

Example of a simple `fabfile.py`:

```python
from fabric import task

@task
def deploy(c):
    c.run("git pull origin main")
    c.run("docker-compose down")
    c.run("docker-compose up -d")
```

To execute the deployment task locally, run:
```
fab deploy
```

## What is a tgz Archive?
A tgz archive, also known as a tarball, is a compressed archive format commonly used in Unix-based systems. It combines multiple files into a single archive while compressing them using gzip compression. It's often used for packaging and distributing files or directories.

## How to Execute Fabric Command Locally
To execute a Fabric command locally, you can use the `local` context manager provided by Fabric. Here's an example:

```python
from fabric import task

@task
def local_command(c):
    with c.local.cwd('/path/to/local/directory'):
        c.local('ls -la')
```

To run this command locally, execute:
```
fab local_command
```

## How to Execute Fabric Command Remotely
To execute a Fabric command remotely, you can use the `run` function provided by Fabric within your task. Here's an example:

```python
from fabric import task

@task
def remote_command(c):
    c.run('ls -la')
```

To run this command remotely, execute:
```
fab -H username@hostname remote_command
```

## How to Transfer Files with Fabric
Fabric provides a `put` function to transfer files from the local system to a remote system and a `get` function to transfer files from the remote system to the local system. Here's an example:

```python
from fabric import task

@task
def transfer_files(c):
    c.put('local_file.txt', '/remote/path/')
    c.get('/remote/path/remote_file.txt', 'local_destination/')
```

## How to Manage Nginx Configuration
Nginx configuration management involves modifying configuration files typically found in `/etc/nginx/conf.d/` or `/etc/nginx/sites-available/`. You can use Fabric to automate tasks related to Nginx configuration such as editing configuration files, reloading Nginx, etc.

Example task to reload Nginx:

```python
from fabric import task

@task
def reload_nginx(c):
    c.sudo('systemctl reload nginx')
```

## Difference Between Root and Alias in Nginx Configuration
In Nginx configuration, `root` and `alias` directives are used to define the document root for requests matching a location block. 

- `root`: Sets the root directory that will be used to search for a file to serve a request. It appends the request URI to the path specified.
- `alias`: Similar to `root`, but it replaces the part of the request URI that matches the location path with the specified path.

Example configuration:

```nginx
server {
    listen 80;
    server_name example.com;

    location /files/ {
        root /var/www/;
    }

    location /images/ {
        alias /var/images/;
    }
}
```

In this example, requests to `http://example.com/files/` will be served from `/var/www/files/`, while requests to `http://example.com/images/` will be served from `/var/images/`.
