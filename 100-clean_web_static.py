#!/usr/bin/python3
""" Generates+deploys a .tgz archive from web_static/
Usage: fab -f 2-do_deploy_web_static.py do_deploy:archive_path=path
    -i ssh_pv_key -u user
"""


from datetime import datetime
from fabric.decorators import runs_once, task
from fabric.api import put, env, run, local
import os


env.hosts = ["54.237.2.143", "107.21.25.233"]


@task
def do_clean(number=0):
    """formats input and cleans remote"""
    x = 1
    if int(number) != 0:
        x = int(number)
    path = "/data/web_static/releases/*"
    local("ls -dt ./versions/* | head -n -{} | xargs rm -fr".format(x))
    run("ls -dt {} | head -n -{} | xargs rm -fr".format(path, x))


@task
def deploy():
    """parse and deploy"""
    file_path = do_pack()

    if file_path is None:
        return False
    return do_deploy(file_path)


@task
def do_deploy(archive_path):
    """gen+deploys .tgz

    Return:
        str: /path
        null: fail
    """
    try:
        if not os.path.exists(archive_path):
            return False
        ext = archive_path.split("/")[-1]

        no_ext = archive_path.split("/")[-1].split(".")[0]
        pth = "/data/web_static/releases/"
        put(archive_path, "/tmp/")
        run("mkdir -p " + pth + no_ext)
        run("tar --verbose -xvzf /tmp/{} -C {}{}/".format(ext, pth, no_ext))
        run("rm /tmp/{}".format(ext))
        run("mv {1}{0}/web_static/* {1}{0}/".format(no_ext, pth))
        run("rm -rf {}{}/web_static".format(pth, no_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{} /data/web_static/current".format(pth, no_ext))
        return True
    except Exception:
        return False


@runs_once
def do_pack():
    """gen .tgz

    Return:
        str: /path
        null: fail
    """

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive = "web_static_{}.tgz".format(timestamp)
    path = "versions/{}".format(archive)

    local("mkdir -p versions")
    result = local("tar --verbose -czf {} web_static/".format(path))

    if result is None:
        return None
    else:
        return path
