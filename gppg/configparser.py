# GPPG - Config parser
# Copyright (C) 2009  Ryan Kavanagh <ryanakca@kubuntu.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import ConfigParser
import os

class GppgHomedir:
    """ This class represents a LUKS encrypted device used by GPPG. It provides access to
    the device path, the mount point, the unmount time, etc.
    """

    def __init__(self, section="Default", 
            config_file=os.path.expanduser("~/.gppgrc")):
        config = ConfigParser.SafeConfigParser()
        config.read(config_file)
        if config.has_option(section, "unmount_time"):
            self.unmount_time = config.get(section, "unmount_time")
        else:
            self.unmount_time = config.get("Global", "unmount_time")
        self.encrypted_device = config.get(section, "encrypted_device")
        self.decrypted_device = config.get(section, "decrypted_device")
        self.mount_point = config.get(section, "mount_point")
