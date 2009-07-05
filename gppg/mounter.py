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

from gppg.configparser import GppgConfig, GppgHomedir
from gppg.utils import run_cryptsetup

def cryptopen(GppgHomedir):
    """ Decrypts a GppgHomedir. """
    run_cryptsetup('luksOpen', GppgHomedir.encrypted_device,
            GppgHomedir.decrypted_device)

def mount(GppgHomedir):
    """ Mounts a GppgHomedir. """
    pass
