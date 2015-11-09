MLAG Role for EOS
=================

The arista.eos-mlag role creates an abstraction for common MLAG configuration.
This means that you do not need to write any ansible tasks. Simply create
an object that matches the requirements below and this role will ingest that
object and perform the necessary configuration.

Requirements
------------

Requires the arista.eos role.  If you have not worked with the arista.eos role,
consider following the [Quickstart][http://ansible-eos.readthedocs.org/en/latest/quickstart.html] guide.

Role Variables
--------------

The tasks in this role are driven by the ``mlag`` object described below:

Sample host_vars file:

    mlag:
      mlag_domain_id: (string) The name of the MLAG Domain
      mlag_trunk_group: mlagpeer
      mlag_shutdown: false
      local_if_vlan: Vlan1024
      local_if_vlan_description: Peer MLAG Link
      local_if_ip_address: 10.0.0.1/30
      local_if_disable_spanning_tree: true
      peer_address: 10.0.0.2
      peer_link_if: Port-Channel10
      peer_link_mode: trunk
      peer_link_lacp_mode: active
      peer_link_enable: true
      peer_link_members:
        - Ethernet3
        - Ethernet4

    mlag:
      mlag_domain_id: mlag1
      mlag_trunk_group: mlagpeer
      mlag_shutdown: false
      local_if_vlan: Vlan1024
      local_if_vlan_description: Peer MLAG Link
      local_if_ip_address: 10.0.0.1/30
      local_if_disable_spanning_tree: true
      peer_address: 10.0.0.2
      peer_link_if: Port-Channel10
      peer_link_mode: trunk
      peer_link_lacp_mode: active
      peer_link_enable: true
      peer_link_members:
        - Ethernet3
        - Ethernet4


Dependencies
------------

The eos-mlag role utilizes modules distributed within the arista.eos role.

Example Playbook
----------------

Sample hosts file:

    [leafs]
    leaf1.example.com
    leaf2.example.com

Sample host_vars files:

    # host_vars/leaf1.example.com
    mlag:
      mlag_domain_id: mlag1
      mlag_trunk_group: mlagpeer
      mlag_shutdown: false
      local_if_vlan: Vlan1024
      local_if_vlan_description: Peer MLAG Link
      local_if_ip_address: 10.0.0.1/30
      local_if_disable_spanning_tree: true
      peer_address: 10.0.0.2
      peer_link_if: Port-Channel10
      peer_link_mode: trunk
      peer_link_lacp_mode: active
      peer_link_enable: true
      peer_link_members:
        - Ethernet3
        - Ethernet4

    # host_vars/leaf2.example.com
    mlag:
      mlag_domain_id: mlag1
      mlag_trunk_group: mlagpeer
      mlag_shutdown: false
      local_if_vlan: Vlan1024
      local_if_ip_address: 10.0.0.2/30
      local_if_disable_spanning_tree: true
      peer_address: 10.0.0.1
      peer_link_if: Port-Channel10
      peer_link_mode: trunk
      peer_link_lacp_mode: active
      peer_link_enable: true
      peer_link_members:
        - Ethernet3
        - Ethernet4



A simple playbook to enable MLAG on your leafs

    - hosts: leafs
      roles:
         - arista.eos-mlag

License
-------

Copyright (c) 2015, Arista Networks EOS+
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of ansible-eos-mlag nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Author Information
------------------

Please raise any issues using our GitHub repo or email us at ansible-dev@arista.com
