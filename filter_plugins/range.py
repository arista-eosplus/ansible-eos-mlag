# Copyright (c) 2017, Arista Networks, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#   Redistributions of source code must retain the above copyright notice,
#   this list of conditions and the following disclaimer.
#
#   Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
#
#   Neither the name of Arista Networks nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL ARISTA NETWORKS
# BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN
# IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

__metaclass__ = type
import re

def range_search(value, range_string):
    """ Returns true if value is found in the list of ranges specified.

    Args:
        value (int): an integer value to be searched for.
        range_list (str): a string representation of a list of ranges in
                          the format "2-5,7,9-11,20-22,44".

    Returns:
        True if the value is included in the range string, or
        False otherwise if it is not.
    """
    tpl = re.compile(r'^(\d+)\-(\d+)$')
    sgl = re.compile(r'^\d+$')

    range_list = range_string.split(',')
    ranges = []

    for item in range_list:
        this_tpl = tpl.match(item)
        if this_tpl:
            tup = (this_tpl.group(1), this_tpl.group(2))
            ranges.append(tup)
        else:
            this_sgl = sgl.match(item)
            if this_sgl:
                tup = (this_sgl.group(0), this_sgl.group(0))
                ranges.append(tup)
            else:
                raise ValueError("filter_plugin/range.py: improperly formatted "
                                 "range string passed in - %s" % range_string)

    for (lower, upper) in ranges:
        if (lower <= value <= upper):
            return True

    return False


class FilterModule(object):

    def filters(self):
        return {
            'range_search': range_search,
        }
