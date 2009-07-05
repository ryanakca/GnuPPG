# GnuPPG - Mounter script
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

import os.path

from gppg.configparser import GppgConfig, GppgHomedir
from gppg.utils import run_cryptsetup, run_mount

def cryptopen(GppgHdir):
    """ Decrypts a GppgHomedir. """
    run_cryptsetup('luksOpen', GppgHd.encrypted_device,
            GppgHd.decrypted_name)

# def mount_device():
#     """ Mounts a GppgHomedir. """
#     assert GppgHd.encrypted_device, "Please set the GppgHomedir's " +
#         "encrypted_device"
#     assert GppgHd.decrypted_name, "Please set the GppgHomedir's " +
#         "decrypted_name"
#     assert GppgHd.mount_point
#
#     if os.path.exists(GppgHd
#         raise ValueError
#     run_mount(GppgHomedir.
