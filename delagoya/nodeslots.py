# The MIT License (MIT)
# 
# Copyright (c) 2013 Angel Pizarro
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

'''
A StarCluster Plugin to set the number of slots for the execution nodes

    [plugin nodeslots]
    setup_class = delagoya.gridengine.NodeSlots
    num_slots = 1 # number of slots the exec nodes should have.

'''

class NodeSlots(ClusterSetup):
    def __init__(self,num_slots=None):
        self.num_slots = num_slots

    def run(self, nodes, master, user, user_shell, volumes):
        if self.num_slots:
            self._set_node_slots(master,nodes)
    def _set_node_slots(self,master,nodes):
        log.info("Setting the number of slots on nodes to {0}".format(self.num_slots))
        for node in nodes:
            master.ssh.execute("qconf -mattr queue slots '[%s=%s]' all.q" % (node.alias, self.num_slots), source_profile=True)
