#!/usr/bin/python3
"""
This fabfile distributes an archive to my web servers
"""

import os
from fabric.api import *
from datetime import datetime


# Set the host IP addresses for web-01 && web-02
env.hosts = ['100.25.223.70', '100.26.11.97']
env.user = "ubuntu"


def do_deploy(archive_path):
    '''Deploy the web_static content to the web servers'''
    if not os.path.exists(archive_path):
        print("Archive does not exist.")
        return False

    try:
        # Extract archive filename and folder name
        archive_filename = os.path.basename(archive_path)
        folder_name = archive_filename.split('.')[0]

        # Remote paths
        remote_tmp_path = "/tmp/"
        remote_release_path = "/data/web_static/releases/{}/".format(folder_name)
        remote_current_path = "/data/web_static/current"

        # Upload archive to the server
        put(archive_path, remote_tmp_path)

        # Create necessary directories
        run("mkdir -p {}".format(remote_release_path))

        # Extract archive
        run("tar -xzf {} -C {}".format(remote_tmp_path + archive_filename, remote_release_path))

        # Delete archive from server
        run("rm -f {}".format(remote_tmp_path + archive_filename))

        # Move contents to proper location
        run("mv -u {}/web_static/* {}".format(remote_release_path, remote_release_path))

        # Remove symbolic link if exists
        run("rm -rf {}".format(remote_current_path))

        # Create new symbolic link
        run("ln -s {} {}".format(remote_release_path, remote_current_path))

        print("New version deployed!")
        return True

    except Exception as e:
        print("Deployment failed:", str(e))
        return False
