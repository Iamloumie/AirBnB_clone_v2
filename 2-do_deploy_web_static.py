#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that
distributes an archive to the web servers
"""

from os.path import exists
from fabric.api import put, run, env

env.hosts = ["100.25.201.126", "54.162.98.171"]


def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False

    try:
        file_name = archive_path.split("/")[-1]
        no_ext = file_name.split(".")[0]
        path = "/data/web_static/releases/"

        put(archive_path, "/tmp")
        run("mkdir -p {}{}/".format(path, no_ext))
        run("tar -xzf /tmp/{} -C {}{}/".format(file_name, path, no_ext))
        run("rm /tmp/{}".format(file_name))
        run("mv {0}{1}/web_static/* {0}{1}/".format(file_name, no_ext))
        run("rm -rf {}{}/web_static".format(path, no_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(path, no_ext))
        return True
    except:
        return False
