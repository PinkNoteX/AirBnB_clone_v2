#!/usr/bin/python3
# generate a .tgz archive from web_static
from fabric.api import *
import os
from datetime import datetime
import tarfile


def do_pack():
    """ do_pack func """
    try:
        p = "web_static_" + datetime.now().strftime("%Y%m%d%H%M%S")
        local('mkdir -p versions')
        local("tar -cvzf versions/{}.tgz {}".format(p, "web_static/"))
        s = os.path.getsize("./versions/{}.tgz".format(p))
        print("web_static packed: versions/{}.tgz -> {}Bytes".format(p, s))
    except Exception:
        return None
