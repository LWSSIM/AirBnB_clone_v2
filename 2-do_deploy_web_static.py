#!/usr/bin/python3
""" Generates+deploys a .tgz archive from web_static/
Usage: fab -f 2-do_deploy_web_static.py do_deploy:archive_path=path
    -i ssh_pv_key -u user
"""


from fabric.decorators import task
from fabric.api import put, env, run
import os


env.hosts = ["54.237.2.143", "107.21.25.233"]


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
        with_ext = archive_path.split("/")[-1]

        without_ext = archive_path.split("/")[-1].split(".")[0]
        pth = "/data/web_static/releases/"
        put(archive_path, "/tmp/")
        run("mkdir -p " + pth + without_ext)
        run("tar -xzf /tmp/{} -C {}{}/".format(with_ext, pth, without_ext))
        run("rm /tmp/{}".format(with_ext))
        run("mv {1}{0}/web_static/* {1}{0}/".format(without_ext, pth))
        run("rm -rf {}{}/web_static".format(pth, without_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{} /data/web_static/current".format(pth, without_ext))
        return True
    except Exception:
        return False
