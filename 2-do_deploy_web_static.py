#!/usr/bin/python3
""" Generates+deploys a .tgz archive from web_static/
Usage: fab -f 2-do_deploy_web_static.py do_deploy:archive_path=path
    -i ssh_pv_key -u user
"""


from fabric.decorators import task
from fabric.api import local, put, get, env, run
from os.path import exists
from datetime import datetime


env.hosts = ["54.237.2.143", "107.21.25.233"]


@task
def do_deploy(archive_path):
    """gen+deploys .tgz

    Return:
        str: /path
        null: fail
    """
    if not exists(archive_path):
        return False

    try:
        arch_name = archive_path.split("/")[-1].split(".")[0]
        data_pth = "/data/web_static/releases"

        put(archive_path, "/tmp/")

        run("mkdir -p {}/{}".format(data_pth, arch_name))

        run(
            "tar -xzf /tmp/{}.tgz -C {}/{}/"
        .format(arch_name, data_pth, arch_name))

        run("rm -fr /tmp/{}.tgz".format(arch_name))

        run(
            "mv {}/{}/web_static/* {}/{}"
        .format(data_pth, arch_name, data_pth, arch_name))

        run("rm -fr {}/{}/web_static".format(data_pth, arch_name))

        run("rm -fr /data/web_static/current")

        run("ln -s {}/{} /data/web_static/current".format(data_pth, arch_name))

        return True
    except Exception:
        return False



@task
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
    result = local("tar -czf {} web_static/".format(path))

    if result is None:
        return None
    else:
        return path
