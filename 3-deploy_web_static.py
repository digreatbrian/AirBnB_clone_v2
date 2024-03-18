#!/usr/bin/python3
"""
This script handles deployment of an archive to web servers.
"""

import os
from fabric.api import *
from datetime import datetime

# The host IP addresses and user for web servers
env.hosts = ['18.234.105.167', '100.25.222.179']
env.user = "ubuntu"


def create_archive():
    """Create a tar gzipped archive of the web_static directory."""
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(now)
    local("mkdir -p versions")
    result = local("tar -cvzf {} web_static".format(archive_path))
    if result.return_code != 0:
        return None
    else:
        return archive_path


def deploy_archive(archive_path):
    '''Use os module to check for valid file path'''
    if os.path.exists(archive_path):
        archive = os.path.basename(archive_path)
        archive_name = os.path.splitext(archive)[0]
        tmp_archive_path = "/tmp/{}".format(archive)
        deployment_path = "/data/web_static/releases/{}/".format(archive_name)

        put(archive_path, tmp_archive_path)
        run("mkdir -p {}".format(deployment_path))
        run("tar -xzf {} -C {}".format(tmp_archive_path, deployment_path))
        run("rm {}".format(tmp_archive_path))
        run("mv -f {}web_static/* {}".deployment_path))
        run("rm -rf {}web_static".format(deployment_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(deployment_path))
        return True
    return False


def deploy():
    """ Create and deploy the archive """
    archive_path = create_archive()
    if archive_path:
        return deploy_archive(archive_path)
    else:
        return False
