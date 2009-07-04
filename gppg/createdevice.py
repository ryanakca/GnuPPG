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
import gppg.mounter

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

def create_lv(vgname, lvname, size, *args):
    # We may want to support extends down the road.
    SIZE_UNITS = 'kKmMgGtT'
    EXTENTS_UNITS = ['%VG', '%FREE']
    cargs = ['lvcreate', '-n %(lvname)' % {'lvname':lvname}]
    for arg in args:
        cargs.append(arg)
    if size[-1:] in SIZE_UNITS:
        cargs += ['-l %(size)' % {'size':size}]
        cargs += [vgname]
    elif (size[-3:] or size[-5:]) in EXTENTS_UNITS:
        cargs += ['-L %(size)' % {'size':size}]
        cargs += [vgname]
    else:
        raise ValueError("Invalid size %s, unit must be one of kKmMgGtT, %VG "
            "or %FREE." % size)


def create(device='', lvm=False, vgname='', lvname='', size='', fstype='',
        homedir='', config='', cryptsetup_args='', mkfs_args='')
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

    assert fstype, "Please provide a filesystem type"
    assert homedir, "Please provide a path to a GnuPG homedir"
    assert config, "Please provide a path to a GnuPPG configuration file"

    if (device && lvm) || ((len(device) == 0) && (lvm == False)):
        raise ValueError("Please provide either device or a True value to lvm")
    
    if device:
        run_cryptsetup(luksFormat, device, '-y' + cryptsetup_args)
        gppg.mounter.cryptopen(device)
        run_format(fstype, device, mkfs_args)
    else:
        create_lv(vgname, lvname, size, cryptsetup_args)
        lv =  '/dev/mapper/%(vgname)s-%(lvname)s' % {'vgname': vgname, 'lvname': lvname}
        run_cryptsetup('luksFormat', lv, cryptsetup_args)
        run_format(fstype, lv, mkfs_args)
