# HoneyPy Copyright (C) 2013-2017 foospidy
# https://github.com/foospidy/HoneyPy
# See LICENSE for details

from twisted.internet.protocol import DatagramProtocol
from twisted.python import log
import uuid

### START CUSTOM IMPORTS ###

############################

class pluginMain(DatagramProtocol):

	def datagramReceived(self, data, (host, port)):
		rcvd_data = self.rx(host, port, data)

		### START CUSTOM CODE ####################################################################
		if 'stats' in rcvd_data:
			data = 'STAT pid 1360\
			\r\nSTAT uptime 604532\
			\r\nSTAT time 1520561946\
			\r\nSTAT version 1.2.6\
			\r\nSTAT pointer_size 32\
			\r\nSTAT curr_items 1\
			\r\nSTAT total_items 437\
			\r\nSTAT bytes 1000049\
			\r\nSTAT curr_connections 5\
			\r\nSTAT total_connections 17820\
			\r\nSTAT connection_structures 94\
			\r\nSTAT cmd_get 1576846\
			\r\nSTAT cmd_set 437\
			\r\nSTAT get_hits 116375\
			\r\nSTAT get_misses 1460471\
			\r\nSTAT evictions 0\
			\r\nSTAT bytes_read 477480515\
			\r\nSTAT bytes_written 121922313904\
			\r\nSTAT limit_maxbytes 0\
			\r\nSTAT threads 1\
			\r\nEND\
			\r\n'
		else:
			data = 'ERROR'
		self.tx(host, port, data)

		##########################################################################################

	### START CUSTOM FUNCTIONS ###################################################################

	##############################################################################################

	def tx(self, host, port, data):
		log.msg('%s UDP TX %s %s %s %s %s %s %s' % (self.session, self.host, self.port, self.name, host, port, data.encode("hex"), data))
		self.transport.write(data, (host, port))

	def rx(self, host, port, data):
		self.session = uuid.uuid1()
		log.msg('%s UDP RX %s %s %s %s %s %s %s' % (self.session, self.host, self.port, self.name, host, port, data.encode("hex"), data))
		return data

	def __init__(self, name=None, host=None, port=None):
		self.name    = name or 'HoneyPy'
		self.host    = host or '???'
		self.port    = port or '???'
		self.session = None
