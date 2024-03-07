#!/usr/bin/env python3
""" Generates a .tgz archive from web_static/
Usage: fab -f <file.py> function
"""


from fabric.api import local
from datetime import datetime


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
