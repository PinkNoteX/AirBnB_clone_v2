#!/usr/bin/python3
# distribute an archive to web servers
from fabric.api import *
import os
from datetime import datetime
import tarfile


env.hosts = ['34.204.101.190', '100.25.197.195']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_pack():
    """ do_pack func """
    try:
        p = "web_static_" + datetime.now().strftime("%Y%m%d%H%M%S")
        local('mkdir -p versions')
        local("tar -cvzf versions/{}.tgz {}".format(p, "web_static/"))
        s = os.path.getsize("./versions/{}.tgz".format(p))
        print("web_static packed: versions/{}.tgz -> {}Bytes".format(p, s))
        return ("./versions/{}.tgz".format(p))
    except Exception:
        return None


def do_deploy(archive_path):
    """ do_deploy func """
    f = archive_path.split('/')[1]
    try:
        put(archive_path, '/tmp/{}'.format(f))
        run('mkdir -p /data/web_static/releases/{}'.format(f))
        run('rm -fr /data/web_static/releases/{}/*'.format(f))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}'.format(f, f))
        run('rm /tmp/{}'.format(f))
        run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".format(f, f))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(f))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/\
                /data/web_static/current'.format(f))
        print("New version deployed!")
        return True
    except Exception:
        print("New version not deployed...")
        return False


def deploy():
    """ pack then deploy """
    try:
        path = do_pack()
        return do_deploy(path)
    except Exception:
        return False
