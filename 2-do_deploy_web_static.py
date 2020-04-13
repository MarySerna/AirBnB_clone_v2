#!/usr/bin/python3
"""
Fabric script that distributes an archive to the web servers,
using the function do_deploy
"""


from fabric.api import local, put, run, env
import os
from datetime import datetime
from os.path import exists

env.hosts = ['34.74.131.201', '3.92.147.2']


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static
    """
    time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    file_name = "versions/web_static_{}.tgz".format(time)
    try:
        local("mkdir -p ./versions")
        local("tar --create --verbose -z --file={} ./web_static"
              .format(file_name))
        return file_name
    except:
        return None


def do_deploy(archive_path):
    """
        using fabric to distribute archive
    """
    b_path = archive_path[9:-4]
    path = "/data/web_static/releases/{}".format(b_path)

    if os.path.exists(archive_path):
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, '/tmp/')

        # Uncompress the archive to the folder
        run('sudo mkdir -p {}'.format(path))
        run('tar -xzf /tmp/{}.tgz -C {}/'.format(b_path, path))
        run('rm /tmp/{}.tgz'.format(b_path))
        run('mv {}/web_static/* {}'.format(path, path))
        run('rm -rf {}/web_static'.format(path))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(path))
        print("New version deployed!")

        return True
    else:
        return False
