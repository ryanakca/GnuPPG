# GnuPPG - Create GnuPPG device
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

import subprocess

import gppg.configparser

def run_cryptsetup(command, device, *args):
    """ Will run 'cryptsetup args command device', passing args to cryptsetup.

    Can raise either a suprocess.CalledProcessError or an OSError.
    """

    cargs = ['crypsetup']
    for arg in args:
        cargs.append(arg)
    cargs += [command, device]

    s = subprocess.call(cargs)
    if retcode < 0:
        raise subprocess.CalledProcessError(s, ' '.join(cargs))


def run_format(fstype, device, *args):
    """ Will format device using '/sbin/mkfs.fstype *args device'.
    
    Can raise either a suprocess.CalledProcessError or an OSError.
    """

    cargs = ['mkfs.' + fstype]
    for arg in args:
        cargs.append(arg)
    cargs.append(device)

    s = subprocess.call(cargs)
    if retcode < 0:
        raise subprocess.CalledProcessError(s, ' '.join(cargs))

def create(device='', lvm=False, vgname='', lvname='', size='', fstype='',
        homedir='', cryptsetup_args=(), mkfs_args=())
    """ Will create the GnuPPG device.
    If not using LVM, device is a block device.
    If using LVM, lvm will be True. We require:
        vgname: name of the volume group
        lvname: name of the logical volume
        size: size of the logical volume
    In both cases, we require:
        fstype: filesystem type, there must be a mkfs.fstype
        homedir: path to the GnuPG homedir
    Optional arguments:
        cryptsetup_args: extra cryptsetup arguments
        mkfs_args: extra mkfs arguments
    """

