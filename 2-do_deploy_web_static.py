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
    """Distributes an archive to your web servers,
    using the function do_deploy
    Args:
        archive_path: path to the archive
    Return:
        True if sucessfully and False otherwise.
    """

    """If archive_path does not exit"""
    if not os.path.exists(archive_path):
        return False

    try:
        archived_file = archive_path[9:]

        """Without the extension."""
        file_without_ext = archived_file[:-4]

        """Full path without the extension of the file"""
        file_dir = "/data/web_static/releases/{}/".format(
                file_without_ext)

        """Retrive the file name"""
        archived_file = "/tmp/" + archive_path[9:]

        """Upload to /tmp/ directory of the server"""
        put(archive_path, "/tmp/")

        """Create the directory & Uncompress the file"""
        run("mkdir -p {}".format(file_dir))

        run(
                "tar -xvf {} -C {}".format(
                    archived_file,
                    file_dir
                    )
                )

        """Remove thr archived file"""
        run("rm {}".format(archived_file))

        run("mv {}web_static/* {}".format(file_dir, file_dir))

        run("rm -rf {}web_static".format(file_dir))

        run("rm -rf {}".format("/data/web_static/current"))

        """Create a symbolic link"""
        run("ln -s {} /data/web_static/current".format(file_dir))

        print("New version deployed!")

        return True
    except Exception as e:
        return False
