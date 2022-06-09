#!/usr/bin/env python

# topology mininet 2 host dan 2 switch

from mininet.topo import Topo
from mininet.log import setLogLevel, info

class MyTopo( Topo ):

    def addSwitch(self, name, **opts ):
        kwargs = { 'protocols' : 'OpenFlow13'}
        kwargs.update( opts )
        return super(MyTopo, self).addSwitch( name, **kwargs )

    def __init__( self ):
        "Create MyTopo topology..."
        
        # Inisialisasi Topology
        Topo.__init__( self )

        # Tambahkan node, switch, dan host
        info( '*** Add switches\n')
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')

        info( '*** Add hosts\n')
        h1 = self.addHost('h1', ip='10.1.0.1/24')
        h2 = self.addHost('h2', ip='10.1.0.2/24')
        
     
        info( '*** Add links\n')
        self.addLink(s1, h1, 1, 1)
        self.addLink(s2, h2, 1, 1)
        self.addLink(s1, s2, 2, 2)

topos = { 'mytopo': ( lambda: MyTopo() ) }