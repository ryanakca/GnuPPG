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

class GppgConfig(object):
    """ This class represents the global config options used by GPPG. It
    provides access to paths, etc. """

    def __init__(self,
            config_file=os.path.expanduser('~/.gppgrc')):
        defaults = {'gpg_path':'/usr/bin/gpg', 'at_path':'/usr/bin/at',
                'mount_path':'/bin/mount', 'unmount_time':15,
                'decrypted_name':'gpg-decrypted', 'mount_point':'/media/gppg'}
        self.config_file = config_file
        self.config = ConfigParser.RawConfigParser(defaults)
        self.config.read(config_file)
        self.gpg_path = self.config.get('Global', 'gpg_path')
        self.at_path = self.config.get('Global', 'at_path')
        self.mount_path = self.config.get('Global', 'mount_path')
        self.unmount_time = self.config.get('Global', 'unmount_time')


class GppgHomedir(GppgConfig):
    """ This class represents a LUKS encrypted device used by GPPG. It provides access to
    the device path, the mount point, the unmount time, etc.
    """

    def __init__(self, section='Default', 
            config_file=os.path.expanduser('~/.gppgrc')):
        super(GppgHomedir, self).__init__(config_file=config_file)
        self.section = section

    def read(self):
        # If the self.unmount_time lines are unclear, what we're doing is checking
        # if "unmount_time" was defined in 'section', if not, we'll check if it
        # was defined in "Global", if not, we'll set it to our default.
        if self.config.has_option(section, 'unmount_time'):
            self.unmount_time = self.config.get(section, 'unmount_time')
        self.encrypted_device = self.config.get(section, 'encrypted_device')
        self.decrypted_name = self.config.get(section, 'decrypted_name')
        self.mount_point = self.config.get(section, 'mount_point')

    def save(self):
        # config_file: user supplied, config: temporary object, self.config: our
        # config object.
        self.config.write(open(self.config_file, 'wb'))

