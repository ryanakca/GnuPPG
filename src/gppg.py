#!/usr/bin/python
# GnuPPG - Main executable
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

import gppg.configparser

def main():
    usage = "Usage: %prog [command] [options]"
    description = \
    """
    [command] may be 'create', 'mount' or 'unmount' and defaults to 'mount'.
    GnuPPG  Copyright (C) 2009 Ryan Kavanagh <ryanakca@kubuntu.org>\n
    This program comes with ABSOLUTELY NO WARRANTY. This is free\n
    software, and you are welcome to redistribute it under certain\n
    conditions; type `%prog --copyright' for details.\n
    """

    parser = optparse.OptionParser(version="Pre-Alpha", usage=usage,
            description=description)
    parser.add_option("-c", "--config", help="Path to configuration file")
    parser.add_option("--copyright", help="Copyright and license information",
            action="callback", callback=print_copyright)
    create_group = optparse.OptionGroup(parser, "Create options",
    description="Options for creating a GnuPPG encrypted device.")
    create_group.add_option("-l", "--lvm", action="store_true", default=False,
            help="Create an LVM partition")
    create_group.add_option("-L", "--size", help="Size of the LVM partition. "+
            "[Default: %default]")
    create_group.add_option("-f", "--fstype", help="Filesystem type, must be " +
            "one of /bin/mkfs.* . [Default: %default]")
    create_group.add_option("-n", "--lvname", help="Name of the LVM logical " +
            "volume. [Default: %default]")
    create_group.add_option("-v", "--vgname", help="Name of the LVM volume " +
            "group. [Required with LVM]")
    parser.add_option_group(create_group)
    parser.set_defaults(size="32M", fstype="ext2", lvname="gppg-encrypted")
    (options, args) = parser.parse_args()

if __name__ == "__main__":
    main()
