#
# Copyright (c) 2008-2016 Citrix Systems, Inc.
#
#   Licensed under the Apache License, Version 2.0 (the "License")
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

from nssrc.com.citrix.netscaler.nitro.resource.base.base_resource import base_resource
from nssrc.com.citrix.netscaler.nitro.resource.base.base_resource import base_response
from nssrc.com.citrix.netscaler.nitro.service.options import options
from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception

from nssrc.com.citrix.netscaler.nitro.util.nitro_util import nitro_util

class nstrace(base_resource) :
	""" Configuration for nstrace operations resource. """
	def __init__(self) :
		self._nf = None
		self._time = None
		self._size = None
		self._mode = []
		self._pernic = None
		self._filename = None
		self._fileid = None
		self._filter = None
		self._link = None
		self._nodes = []
		self._filesize = None
		self._traceformat = None
		self._merge = None
		self._doruntimecleanup = None
		self._tracebuffers = None
		self._skiprpc = None
		self._skiplocalssh = None
		self._capsslkeys = None
		self._capdroppkt = None
		self._inmemorytrace = None
		self._nodeid = None
		self._state = None
		self._scope = None
		self._tracelocation = None

	@property
	def nf(self) :
		r"""Number of files to be generated in cycle.<br/>Default value: 24<br/>Minimum length =  1<br/>Maximum length =  100.
		"""
		try :
			return self._nf
		except Exception as e:
			raise e

	@nf.setter
	def nf(self, nf) :
		r"""Number of files to be generated in cycle.<br/>Default value: 24<br/>Minimum length =  1<br/>Maximum length =  100
		"""
		try :
			self._nf = nf
		except Exception as e:
			raise e

	@property
	def time(self) :
		r"""Time per file (sec).<br/>Default value: 3600<br/>Minimum length =  1.
		"""
		try :
			return self._time
		except Exception as e:
			raise e

	@time.setter
	def time(self, time) :
		r"""Time per file (sec).<br/>Default value: 3600<br/>Minimum length =  1
		"""
		try :
			self._time = time
		except Exception as e:
			raise e

	@property
	def size(self) :
		r"""Size of the captured data. Set 0 for full packet trace.<br/>Default value: 164<br/>Maximum length =  1514.
		"""
		try :
			return self._size
		except Exception as e:
			raise e

	@size.setter
	def size(self, size) :
		r"""Size of the captured data. Set 0 for full packet trace.<br/>Default value: 164<br/>Maximum length =  1514
		"""
		try :
			self._size = size
		except Exception as e:
			raise e

	@property
	def mode(self) :
		r"""Capturing mode for trace. Mode can be any of the following values or combination of these values:
		RX          Received packets before NIC pipelining (Filter does not work when RX capturing mode is ON)
		NEW_RX      Received packets after NIC pipelining
		TX          Transmitted packets
		TXB         Packets buffered for transmission
		IPV6        Translated IPv6 packets
		C2C         Capture C2C message
		NS_FR_TX    TX/TXB packets are not captured in flow receiver.
		MPTCP       MPTCP master flow
		Default mode: NEW_RX TXB .<br/>Default value: DEFAULT_MODE<br/>Possible values = TX, TXB, RX, IPV6, NEW_RX, C2C, NS_FR_TX, APPFW, MPTCP.
		"""
		try :
			return self._mode
		except Exception as e:
			raise e

	@mode.setter
	def mode(self, mode) :
		r"""Capturing mode for trace. Mode can be any of the following values or combination of these values:
		RX          Received packets before NIC pipelining (Filter does not work when RX capturing mode is ON)
		NEW_RX      Received packets after NIC pipelining
		TX          Transmitted packets
		TXB         Packets buffered for transmission
		IPV6        Translated IPv6 packets
		C2C         Capture C2C message
		NS_FR_TX    TX/TXB packets are not captured in flow receiver.
		MPTCP       MPTCP master flow
		Default mode: NEW_RX TXB .<br/>Default value: DEFAULT_MODE<br/>Possible values = TX, TXB, RX, IPV6, NEW_RX, C2C, NS_FR_TX, APPFW, MPTCP
		"""
		try :
			self._mode = mode
		except Exception as e:
			raise e

	@property
	def pernic(self) :
		r"""Use separate trace files for each interface. Works only with cap format.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._pernic
		except Exception as e:
			raise e

	@pernic.setter
	def pernic(self, pernic) :
		r"""Use separate trace files for each interface. Works only with cap format.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._pernic = pernic
		except Exception as e:
			raise e

	@property
	def filename(self) :
		r"""Name of the trace file.
		"""
		try :
			return self._filename
		except Exception as e:
			raise e

	@filename.setter
	def filename(self, filename) :
		r"""Name of the trace file.
		"""
		try :
			self._filename = filename
		except Exception as e:
			raise e

	@property
	def fileid(self) :
		r"""ID for the trace file name for uniqueness. Should be used only with -name option.
		"""
		try :
			return self._fileid
		except Exception as e:
			raise e

	@fileid.setter
	def fileid(self, fileid) :
		r"""ID for the trace file name for uniqueness. Should be used only with -name option.
		"""
		try :
			self._fileid = fileid
		except Exception as e:
			raise e

	@property
	def filter(self) :
		r"""Filter expression for nstrace. Maximum length of filter is 255 and it can be of following format:
		<expression> [<relop> <expression>]
		<relop> = ( && | || )
		<expression> =:
		CONNECTION.<qualifier>.<qualifier-method>.(<qualifier-value>)
		<qualifier> = SRCIP
		<qualifier-method> = [ EQ | NE ]
		<qualifier-value>  = A valid IPv4 address.
		example = CONNECTION.SRCIP.EQ(127.0.0.1)
		<qualifier> = DSTIP
		<qualifier-method> = [ EQ | NE ]
		<qualifier-value>  = A valid IPv4 address.
		example = CONNECTION.DSTIP.EQ(127.0.0.1)
		<qualifier> = IP
		<qualifier-method> = [ EQ | NE ]
		<qualifier-value>  = A valid IPv4 address.
		example = CONNECTION.IP.EQ(127.0.0.1)
		<qualifier> = SRCIPv6
		<qualifier-method> = [ EQ | NE ]
		<qualifier-value>  = A valid IPv6 address.
		example = CONNECTION.SRCIPv6.EQ(2001:db8:0:0:1::1)
		<qualifier> = DSTIPv6
		<qualifier-method> = [ EQ | NE ]
		<qualifier-value>  = A valid IPv6 address.
		example = CONNECTION.DSTIPv6.EQ(2001:db8:0:0:1::1)
		<qualifier> = IPv6
		<qualifier-method> = [ EQ | NE ]
		<qualifier-value>  = A valid IPv6 address.
		example = CONNECTION.IPv6.EQ(2001:db8:0:0:1::1)
		<qualifier> = SRCPORT
		<qualifier-method> = [ EQ | NE | GT | GE | LT | LE
		| BETWEEN ]
		<qualifier-value>  = A valid port number.
		example = CONNECTION.SRCPORT.EQ(80)
		<qualifier> = DSTPORT
		<qualifier-method> = [ EQ | NE | GT | GE | LT | LE
		| BETWEEN ]
		<qualifier-value>  = A valid port number.
		example = CONNECTION.DSTPORT.EQ(80)
		<qualifier> = PORT
		<qualifier-method> = [ EQ | NE | GT | GE | LT | LE
		| BETWEEN ]
		<qualifier-value>  = A valid port number.
		example = CONNECTION.PORT.EQ(80)
		<qualifier> = VLANID
		<qualifier-method> = [ EQ | NE | GT | GE | LT | LE
		| BETWEEN ]
		<qualifier-value>  = A valid VLAN ID.
		example = CONNECTION.VLANID.EQ(0)
		<qualifier> = CONNID
		<qualifier-method> = [ EQ | NE | GT | GE | LT | LE
		| BETWEEN ]
		<qualifier-value>  = A valid PCB dev number.
		example = CONNECTION.CONNID.EQ(0)
		<qualifier> = PPEID
		<qualifier-method> = [ EQ | NE | GT | GE | LT | LE
		| BETWEEN ]
		<qualifier-value>  = A valid core ID.
		example = CONNECTION.PPEID.EQ(0)    
		<qualifier> = SVCNAME
		<qualifier-method> = [ EQ | NE | CONTAINS | STARTSWITH 
		| ENDSWITH ] 
		<qualifier-value>  = A valid text string.
		example = CONNECTION.SVCNAME.EQ("name")
		<qualifier> = LB_VSERVER.NAME
		<qualifier-method> = [ EQ | NE | CONTAINS | STARTSWITH
		| ENDSWITH ]
		<qualifier-value>  = LB vserver name.
		example = CONNECTION.LB_VSERVER.NAME.EQ("name")
		<qualifier> = CS_VSERVER.NAME
		<qualifier-method> = [ EQ | NE | CONTAINS | STARTSWITH
		| ENDSWITH ]
		<qualifier-value>  = CS vserver name.
		example = CONNECTION.CS_VSERVER.NAME.EQ("name")
		<qualifier> = INTF
		<qualifier-method> = [ EQ | NE ]
		<qualifier-value>  =  A valid interface id in the
		form of x/y.
		example = CONNECTION.INTF.EQ("x/y")
		<qualifier> = SERVICE_TYPE
		<qualifier-method> = [ EQ | NE ]
		<qualifier-value>  = ( SVC_HTTP | FTP | TCP | UDP | SSL |
		SSL_BRIDGE | SSL_TCP | NNTP | RPCSVR | RPCSVRS |
		RPCCLNT | SVC_DNS | ADNS | SNMP | RTSP | DHCPRA | ANY|
		MONITOR | MONITOR_UDP | MONITOR_PING | SIP_UDP |
		SVC_MYSQL | SVC_MSSQL | FIX | SSL_FIX | SERVICE_UNKNOWN )
		example = CONNECTION.SERVICE_TYPE.EQ(ANY)
		<qualifier> = TRAFFIC_DOMAIN_ID
		<qualifier-method> = [ EQ | NE | GT | GE | LT | LE
		| BETWEEN ]
		<qualifier-value>  = A valid traffic domain ID.
		example = CONNECTION.TRAFFIC_DOMAIN_ID.EQ(0)
		eg: start nstrace -filter "CONNECTION.SRCIP.EQ(127.0.0.1) || (CONNECTION.SVCNAME.NE("s1") && CONNECTION.SRCPORT.EQ(80))"
		The filter expression should be given in double quotes. 
		common use cases:
		Trace capturing full sized traffic from/to ip 10.102.44.111, excluding loopback traffic
		start nstrace -size 0 -filter "CONNECTION.IP.NE(127.0.0.1) && CONNECTION.IP.EQ(10.102.44.111)"
		Trace capturing all traffic to (terminating at) port 80 or 443 
		start nstrace -size 0 -filter "CONNECTION.DSTPORT.EQ(443) || CONNECTION.DSTPORT.EQ(80)"
		Trace capturing all backend traffic specific to service service1 along with corresponding client side traffic
		start nstrace -size 0 -filter "CONNECTION.SVCNAME.EQ("service1")" -link ENABLED
		Trace capturing all traffic through NS interface 1/1
		start nstrace -filter "CONNECTION.INTF.EQ("1/1")"
		Trace capturing all traffic specific through vlan 2
		start nstrace -filter "CONNECTION.VLANID.EQ(2)"
		Trace capturing all frontend (client side) traffic specific to lb vserver vserver1 along with corresponding server side traffic
		start nstrace -size 0 -filter "CONNECTION.LB_VSERVER.NAME.EQ("vserver1")" -link ENABLED .
		"""
		try :
			return self._filter
		except Exception as e:
			raise e

	@filter.setter
	def filter(self, filter) :
		r"""Filter expression for nstrace. Maximum length of filter is 255 and it can be of following format:
		<expression> [<relop> <expression>]
		<relop> = ( && | || )
		<expression> =:
		CONNECTION.<qualifier>.<qualifier-method>.(<qualifier-value>)
		<qualifier> = SRCIP
		<qualifier-method> = [ EQ | NE ]
		<qualifier-value>  = A valid IPv4 address.
		example = CONNECTION.SRCIP.EQ(127.0.0.1)
		<qualifier> = DSTIP
		<qualifier-method> = [ EQ | NE ]
		<qualifier-value>  = A valid IPv4 address.
		example = CONNECTION.DSTIP.EQ(127.0.0.1)
		<qualifier> = IP
		<qualifier-method> = [ EQ | NE ]
		<qualifier-value>  = A valid IPv4 address.
		example = CONNECTION.IP.EQ(127.0.0.1)
		<qualifier> = SRCIPv6
		<qualifier-method> = [ EQ | NE ]
		<qualifier-value>  = A valid IPv6 address.
		example = CONNECTION.SRCIPv6.EQ(2001:db8:0:0:1::1)
		<qualifier> = DSTIPv6
		<qualifier-method> = [ EQ | NE ]
		<qualifier-value>  = A valid IPv6 address.
		example = CONNECTION.DSTIPv6.EQ(2001:db8:0:0:1::1)
		<qualifier> = IPv6
		<qualifier-method> = [ EQ | NE ]
		<qualifier-value>  = A valid IPv6 address.
		example = CONNECTION.IPv6.EQ(2001:db8:0:0:1::1)
		<qualifier> = SRCPORT
		<qualifier-method> = [ EQ | NE | GT | GE | LT | LE
		| BETWEEN ]
		<qualifier-value>  = A valid port number.
		example = CONNECTION.SRCPORT.EQ(80)
		<qualifier> = DSTPORT
		<qualifier-method> = [ EQ | NE | GT | GE | LT | LE
		| BETWEEN ]
		<qualifier-value>  = A valid port number.
		example = CONNECTION.DSTPORT.EQ(80)
		<qualifier> = PORT
		<qualifier-method> = [ EQ | NE | GT | GE | LT | LE
		| BETWEEN ]
		<qualifier-value>  = A valid port number.
		example = CONNECTION.PORT.EQ(80)
		<qualifier> = VLANID
		<qualifier-method> = [ EQ | NE | GT | GE | LT | LE
		| BETWEEN ]
		<qualifier-value>  = A valid VLAN ID.
		example = CONNECTION.VLANID.EQ(0)
		<qualifier> = CONNID
		<qualifier-method> = [ EQ | NE | GT | GE | LT | LE
		| BETWEEN ]
		<qualifier-value>  = A valid PCB dev number.
		example = CONNECTION.CONNID.EQ(0)
		<qualifier> = PPEID
		<qualifier-method> = [ EQ | NE | GT | GE | LT | LE
		| BETWEEN ]
		<qualifier-value>  = A valid core ID.
		example = CONNECTION.PPEID.EQ(0)    
		<qualifier> = SVCNAME
		<qualifier-method> = [ EQ | NE | CONTAINS | STARTSWITH 
		| ENDSWITH ] 
		<qualifier-value>  = A valid text string.
		example = CONNECTION.SVCNAME.EQ("name")
		<qualifier> = LB_VSERVER.NAME
		<qualifier-method> = [ EQ | NE | CONTAINS | STARTSWITH
		| ENDSWITH ]
		<qualifier-value>  = LB vserver name.
		example = CONNECTION.LB_VSERVER.NAME.EQ("name")
		<qualifier> = CS_VSERVER.NAME
		<qualifier-method> = [ EQ | NE | CONTAINS | STARTSWITH
		| ENDSWITH ]
		<qualifier-value>  = CS vserver name.
		example = CONNECTION.CS_VSERVER.NAME.EQ("name")
		<qualifier> = INTF
		<qualifier-method> = [ EQ | NE ]
		<qualifier-value>  =  A valid interface id in the
		form of x/y.
		example = CONNECTION.INTF.EQ("x/y")
		<qualifier> = SERVICE_TYPE
		<qualifier-method> = [ EQ | NE ]
		<qualifier-value>  = ( SVC_HTTP | FTP | TCP | UDP | SSL |
		SSL_BRIDGE | SSL_TCP | NNTP | RPCSVR | RPCSVRS |
		RPCCLNT | SVC_DNS | ADNS | SNMP | RTSP | DHCPRA | ANY|
		MONITOR | MONITOR_UDP | MONITOR_PING | SIP_UDP |
		SVC_MYSQL | SVC_MSSQL | FIX | SSL_FIX | SERVICE_UNKNOWN )
		example = CONNECTION.SERVICE_TYPE.EQ(ANY)
		<qualifier> = TRAFFIC_DOMAIN_ID
		<qualifier-method> = [ EQ | NE | GT | GE | LT | LE
		| BETWEEN ]
		<qualifier-value>  = A valid traffic domain ID.
		example = CONNECTION.TRAFFIC_DOMAIN_ID.EQ(0)
		eg: start nstrace -filter "CONNECTION.SRCIP.EQ(127.0.0.1) || (CONNECTION.SVCNAME.NE("s1") && CONNECTION.SRCPORT.EQ(80))"
		The filter expression should be given in double quotes. 
		common use cases:
		Trace capturing full sized traffic from/to ip 10.102.44.111, excluding loopback traffic
		start nstrace -size 0 -filter "CONNECTION.IP.NE(127.0.0.1) && CONNECTION.IP.EQ(10.102.44.111)"
		Trace capturing all traffic to (terminating at) port 80 or 443 
		start nstrace -size 0 -filter "CONNECTION.DSTPORT.EQ(443) || CONNECTION.DSTPORT.EQ(80)"
		Trace capturing all backend traffic specific to service service1 along with corresponding client side traffic
		start nstrace -size 0 -filter "CONNECTION.SVCNAME.EQ("service1")" -link ENABLED
		Trace capturing all traffic through NS interface 1/1
		start nstrace -filter "CONNECTION.INTF.EQ("1/1")"
		Trace capturing all traffic specific through vlan 2
		start nstrace -filter "CONNECTION.VLANID.EQ(2)"
		Trace capturing all frontend (client side) traffic specific to lb vserver vserver1 along with corresponding server side traffic
		start nstrace -size 0 -filter "CONNECTION.LB_VSERVER.NAME.EQ("vserver1")" -link ENABLED .
		"""
		try :
			self._filter = filter
		except Exception as e:
			raise e

	@property
	def link(self) :
		r"""Includes filtered connection's peer traffic.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._link
		except Exception as e:
			raise e

	@link.setter
	def link(self, link) :
		r"""Includes filtered connection's peer traffic.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._link = link
		except Exception as e:
			raise e

	@property
	def nodes(self) :
		r"""Nodes on which tracing is started.
		<br/>Maximum length =  32.
		"""
		try :
			return self._nodes
		except Exception as e:
			raise e

	@nodes.setter
	def nodes(self, nodes) :
		r"""Nodes on which tracing is started.
		<br/>Maximum length =  32
		"""
		try :
			self._nodes = nodes
		except Exception as e:
			raise e

	@property
	def filesize(self) :
		r"""File size, in MB, treshold for rollover. If free disk space is less than 2GB at the time of rollover, trace will stop
		.<br/>Default value: 1024<br/>Maximum length =  10240.
		"""
		try :
			return self._filesize
		except Exception as e:
			raise e

	@filesize.setter
	def filesize(self, filesize) :
		r"""File size, in MB, treshold for rollover. If free disk space is less than 2GB at the time of rollover, trace will stop
		.<br/>Default value: 1024<br/>Maximum length =  10240
		"""
		try :
			self._filesize = filesize
		except Exception as e:
			raise e

	@property
	def traceformat(self) :
		r"""Format in which trace will be generated
		.<br/>Default value: 0<br/>Possible values = NSCAP, PCAP.
		"""
		try :
			return self._traceformat
		except Exception as e:
			raise e

	@traceformat.setter
	def traceformat(self, traceformat) :
		r"""Format in which trace will be generated
		.<br/>Default value: 0<br/>Possible values = NSCAP, PCAP
		"""
		try :
			self._traceformat = traceformat
		except Exception as e:
			raise e

	@property
	def merge(self) :
		r"""Specify how traces across PE's are merged
		.<br/>Default value: 0<br/>Possible values = ONSTOP, ONTHEFLY, NOMERGE.
		"""
		try :
			return self._merge
		except Exception as e:
			raise e

	@merge.setter
	def merge(self, merge) :
		r"""Specify how traces across PE's are merged
		.<br/>Default value: 0<br/>Possible values = ONSTOP, ONTHEFLY, NOMERGE
		"""
		try :
			self._merge = merge
		except Exception as e:
			raise e

	@property
	def doruntimecleanup(self) :
		r"""Enable or disable runtime temp file cleanup.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._doruntimecleanup
		except Exception as e:
			raise e

	@doruntimecleanup.setter
	def doruntimecleanup(self, doruntimecleanup) :
		r"""Enable or disable runtime temp file cleanup.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._doruntimecleanup = doruntimecleanup
		except Exception as e:
			raise e

	@property
	def tracebuffers(self) :
		r"""Number of 16KB trace buffers.<br/>Default value: 5000<br/>Minimum length =  1000.
		"""
		try :
			return self._tracebuffers
		except Exception as e:
			raise e

	@tracebuffers.setter
	def tracebuffers(self, tracebuffers) :
		r"""Number of 16KB trace buffers.<br/>Default value: 5000<br/>Minimum length =  1000
		"""
		try :
			self._tracebuffers = tracebuffers
		except Exception as e:
			raise e

	@property
	def skiprpc(self) :
		r"""skip RPC packets.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._skiprpc
		except Exception as e:
			raise e

	@skiprpc.setter
	def skiprpc(self, skiprpc) :
		r"""skip RPC packets.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._skiprpc = skiprpc
		except Exception as e:
			raise e

	@property
	def skiplocalssh(self) :
		r"""skip local SSH packets.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._skiplocalssh
		except Exception as e:
			raise e

	@skiplocalssh.setter
	def skiplocalssh(self, skiplocalssh) :
		r"""skip local SSH packets.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._skiplocalssh = skiplocalssh
		except Exception as e:
			raise e

	@property
	def capsslkeys(self) :
		r"""Capture SSL Master keys. Master keys will not be captured on FIPS machine.
		Warning: The captured keys can be used to decrypt information that may be confidential. The captured key files have to be stored in a secure environment.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._capsslkeys
		except Exception as e:
			raise e

	@capsslkeys.setter
	def capsslkeys(self, capsslkeys) :
		r"""Capture SSL Master keys. Master keys will not be captured on FIPS machine.
		Warning: The captured keys can be used to decrypt information that may be confidential. The captured key files have to be stored in a secure environment.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._capsslkeys = capsslkeys
		except Exception as e:
			raise e

	@property
	def capdroppkt(self) :
		r"""Captures Dropped Packets if set to ENABLED.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._capdroppkt
		except Exception as e:
			raise e

	@capdroppkt.setter
	def capdroppkt(self, capdroppkt) :
		r"""Captures Dropped Packets if set to ENABLED.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._capdroppkt = capdroppkt
		except Exception as e:
			raise e

	@property
	def inmemorytrace(self) :
		r"""Logs packets in appliance's memory and dumps the trace file on stopping the nstrace operation.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._inmemorytrace
		except Exception as e:
			raise e

	@inmemorytrace.setter
	def inmemorytrace(self, inmemorytrace) :
		r"""Logs packets in appliance's memory and dumps the trace file on stopping the nstrace operation.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._inmemorytrace = inmemorytrace
		except Exception as e:
			raise e

	@property
	def nodeid(self) :
		r"""Unique number that identifies the cluster node.<br/>Maximum length =  31.
		"""
		try :
			return self._nodeid
		except Exception as e:
			raise e

	@nodeid.setter
	def nodeid(self, nodeid) :
		r"""Unique number that identifies the cluster node.<br/>Maximum length =  31
		"""
		try :
			self._nodeid = nodeid
		except Exception as e:
			raise e

	@property
	def state(self) :
		r"""Current running state of trace.<br/>Default value: 0<br/>Possible values = RUNNING, STOPPED.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@property
	def scope(self) :
		r"""Scope of started trace, local or cluster level.<br/>Default value: 0<br/>Possible values = CLUSTER, LOCAL.
		"""
		try :
			return self._scope
		except Exception as e:
			raise e

	@property
	def tracelocation(self) :
		r"""Directory where current trace files are saved.
		"""
		try :
			return self._tracelocation
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nstrace_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nstrace
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			return 0
		except Exception as e :
			raise e



	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the nstrace resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nstrace()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		r""" Use this API to fetch all the nstrace resources that are configured on netscaler.
	# This uses nstrace_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = nstrace()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Pernic:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Skiprpc:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Mode:
		TX = "TX"
		TXB = "TXB"
		RX = "RX"
		IPV6 = "IPV6"
		NEW_RX = "NEW_RX"
		C2C = "C2C"
		NS_FR_TX = "NS_FR_TX"
		APPFW = "APPFW"
		MPTCP = "MPTCP"

	class State:
		RUNNING = "RUNNING"
		STOPPED = "STOPPED"

	class Traceformat:
		NSCAP = "NSCAP"
		PCAP = "PCAP"

	class Merge:
		ONSTOP = "ONSTOP"
		ONTHEFLY = "ONTHEFLY"
		NOMERGE = "NOMERGE"

	class Skiplocalssh:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Scope:
		CLUSTER = "CLUSTER"
		LOCAL = "LOCAL"

	class Link:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Capdroppkt:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Capsslkeys:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Inmemorytrace:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Doruntimecleanup:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class nstrace_response(base_response) :
	def __init__(self, length=1) :
		self.nstrace = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nstrace = [nstrace() for _ in range(length)]

