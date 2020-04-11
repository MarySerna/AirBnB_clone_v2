#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to your web servers,
using the function deploy
"""


import os.path
from fabric.api import local, put, run, env
import os
from datetime import datetime
from os.path import exists


env.hosts = ['34.74.131.201', '3.92.147.2']


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static
    """

    dtime = datetime.utcnow()
    archipath = "versions/web_static_{}{}{}{}{}{}.tgz".format(dtime.year,
                                                              dtime.month,
                                                              dtime.day,
                                                              dtime.hour,
                                                              dtime.minute,
                                                              dtime.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(archipath)).failed is True:
        return None
    return archipath


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers
    """

    filename = archive_path[9:-4]
    path = "/data/web_static/releases/{}".format(filename)

    if os.path.exists(archive_path):
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, '/tmp/')

        # Uncompress the archive to the folder
        run('mkdir -p {}'.format(path))
        run('tar -xzf /tmp/{}.tgz -C {}/'.format(filename, path))
        run('rm /tmp/{}.tgz'.format(filename))
        run('mv {}/web_static/* {}'.format(path, path))
        run('rm -rf {}/web_static'.format(path))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(path))
        print("New version deployed!")

        return True
    else:
        return False


def deploy():
    """creates and distributes an archive using the function deploy"""

    path_arch = do_pack()

    if path_arch is None:
        return False
    return do_deploy(path_arch)
