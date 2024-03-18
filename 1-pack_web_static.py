#!/usr/bin/python3
"""
This module provides a function to create a .tgz archive from web_static folder
"""

from datetime import datetime
from fabric.api import local

def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    # Obtain the current date and time
    now = datetime.now().strftime("%Y%m%d%H%M%S")

    # Construct path where archive will be saved
    archive_path = "versions/web_static_{}.tgz".format(now)

    # Use fabric's local function to create directory if dosen't exist
    local("mkdir -p versions")

    # Create a compressed archive of the web_static
    archived = local("tar -cvzf {} web_static".format(archive_path))

    # Check archive creation was successful
    if archived.return_code != 0:
        return None
    else:
        return archive_path
