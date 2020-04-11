#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of
the web_static
"""

import os.path
from fabric.api import local
from datetime import datetime


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
