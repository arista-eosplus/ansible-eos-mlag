MLAG Role for EOS
=================

The arista.eos-mlag role creates an abstraction for common MLAG configuration.
This means that you do not need to write any ansible tasks. Simply create
an object that matches the requirements below and this role will ingest that
object and perform the necessary configuration.

Requirements
------------

Requires an SSH connection for connectivity to your Arista device. You can use
any of the built-in eos connection variables, or the convenience ``provider``
dictionary.

Role Variables
--------------

The ``mlag`` dictionary includes the following keys described below:

|                            Key | Type                                | Notes                                                                                                                                                               |
|-------------------------------:|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                 mlag_domain_id | string                              | The name of the MLAG Domain                                                                                                                                         |
|               mlag_trunk_group | string                              | Trunk group assigned to Vlan                                                                                                                                        |
|                  mlag_shutdown | boolean:true, false*                | Enable or disable the MLAG configuration                                                                                                                            |
|                  local_if_vlan | string                              | The Vlan for the peer link, eg Vlan1024                                                                                                                             |
|      local_if_vlan_description | string                              | Description for local_if_vlan                                                                                                                                       |
|            local_if_ip_address | string                              | IP Address for the local_if_vlan                                                                                                                                    |
| local_if_disable_spanning_tree | boolean:true*, false                | Enable or disable STP on the peer Vlan                                                                                                                              |
|                   peer_address | string                              | IP Address for the MLAG Peer                                                                                                                                        |
|                   peer_link_if | string                              | The Port-Channel used for the peer link                                                                                                                             |
|                 peer_link_mode | choices: trunk*, access             | The switchport mode for the peer link                                                                                                                               |
|            peer_link_lacp_mode | choices: active*, passive, disabled | The LACP mode for each Port-Channel member.                                                                                                                         |
|               peer_link_enable | boolean:true*, false                | Enable or disable the peer link member interfaces                                                                                                                   |
|              peer_link_members | (List)                              | List of interfaces that make up the peer link.                                                                                                                      |
|                          state | boolean:present*, absent            | Whether to add or remove all mlag-related configuration.  When set to absent, all configuration will be removed and the mlag configuration block will be defaulted. |

```
Note: Asterisk (*) denotes the default value if none specified
```


Dependencies
------------

The eos-bridging role is built on modules included in the core Ansible code.
These modules were added in ansible version 2.1

- Ansible 2.1.0

Example Playbook
----------------

The following example will use the arista.eos-mlag role to completely setup MLAG
on two leaf switches without writing any tasks. We'll create a ``hosts`` file
with our two leaf switches, then a corresponding ``host_vars`` file for each
leaf and then a simple playbook which only references the mlag role. By including
the role we automatically get access to all of the tasks to configure MLAG. What's
nice about this is that if you have a host without MLAG configuration, the
tasks will be skipped without any issue.


Sample hosts file:

    [leafs]
    leaf1.example.com
    leaf2.example.com

Sample host_vars/leaf1.example.com

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

Sample host_vars/leaf2.example.com

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

A simple playbook to enable MLAG on your leafs, leaf.yml

    - hosts: leafs
      roles:
         - arista.eos-mlag

Then run with:

    ansible-playbook -i hosts leaf.yml

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

[quickstart]: http://ansible-eos.readthedocs.org/en/latest/quickstart.html
