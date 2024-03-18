#!/usr/bin/python3
"""
This fabfile distributes an archive to my web servers
"""

import os
from fabric.api import *
from datetime import datetime

# The host IP addresses for web-01 and web-02
env.hosts = ['18.234.105.167', '100.25.222.179']
env.user = "ubuntu"


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(now)
    local("mkdir -p versions")
    archived = local("tar -cvzf {} web_static".format(archive_path))

    # Archive creation status
    if archived.return_code != 0:
        return None
    else:
        return archive_path


def do_deploy(archive_path):
    '''use os module to check for valid file path'''
    # Check the provided archive_path exists
    if os.path.exists(archive_path):
        archive = archive_path.split('/')[1]
        archive_name = archive.split('.')[0]
        tmp_archive_path = "/tmp/{}".format(archive)
        deploy_path = "/data/web_static/releases/{}/".format(archive_name)

        # Archive to the temporary directory
        put(archive_path, tmp_archive_path)
        run("mkdir -p {}".format(deploy_path))
        run("tar -xzf {} -C {}".format(tmp_archive_path, deploy_path))
        run("rm {}".format(tmp_archive_path))
        run("mv -f {}web_static/* {}".format(deploy_path, deploy_path))
        run("rm -rf {}web_static".format(deploy_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(deploy_path))

        return True
    return False
