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

class nsconnectiontable(base_resource) :
	""" Configuration for TCP/IP connection table resource. """
	def __init__(self) :
		self._filterexpression = None
		self._link = None
		self._filtername = None
		self._detail = []
		self._listen = None
		self._nodeid = None
		self._sourceip = None
		self._sourceport = None
		self._destip = None
		self._destport = None
		self._svctype = None
		self._idletime = None
		self._state = None
		self._linksourceip = None
		self._linksourceport = None
		self._linkdestip = None
		self._linkdestport = None
		self._linkservicetype = None
		self._linkidletime = None
		self._linkstate = None
		self._entityname = None
		self._linkentityname = None
		self._connid = None
		self._linkconnid = None
		self._connproperties = []
		self._optionflags = []
		self._nswsvalue = None
		self._peerwsvalue = None
		self._mss = None
		self._retxretrycnt = None
		self._rcvwnd = None
		self._advwnd = None
		self._sndcwnd = None
		self._iss = None
		self._irs = None
		self._rcvnxt = None
		self._maxack = None
		self._sndnxt = None
		self._sndunack = None
		self._httpendseq = None
		self._httpstate = None
		self._trcount = None
		self._priority = None
		self._httpreqver = None
		self._httprequest = None
		self._httprspcode = None
		self._rttsmoothed = None
		self._rttvariance = None
		self._outoforderpkts = None
		self._linkoptionflag = []
		self._linknswsvalue = None
		self._linkpeerwsvalue = None
		self._targetnodeidnnm = None
		self._sourcenodeidnnm = None
		self._channelidnnm = None
		self._msgversionnnm = None
		self._td = None
		self._maxrcvbuf = None
		self._linkmaxrcvbuf = None
		self._rxqsize = None
		self._linkrxqsize = None
		self._maxsndbuf = None
		self._linkmaxsndbuf = None
		self._txqsize = None
		self._linktxqsize = None
		self._flavor = None
		self._linkflavor = None
		self._bwestimate = None
		self._linkbwestimate = None
		self._rttmin = None
		self._linkrttmin = None
		self._name = None
		self._linkname = None
		self._tcpmode = None
		self._linktcpmode = None
		self._realtimertt = None
		self._linkrealtimertt = None
		self._sndbuf = None
		self._linksndbuf = None
		self._nsbtcpwaitq = None
		self._linknsbtcpwaitq = None
		self._nsbretxq = None
		self._linknsbretxq = None
		self._sackblocks = None
		self._linksackblocks = None
		self._congstate = None
		self._linkcongstate = None
		self._sndrecoverle = None
		self._linksndrecoverle = None
		self._creditsinbytes = None
		self._linkcredits = None
		self._rateinbytes = None
		self._linkrateinbytes = None
		self._rateschedulerqueue = None
		self._linkrateschedulerqueue = None
		self._burstratecontrol = None
		self._linkburstratecontrol = None
		self.___count = 0

	@property
	def filterexpression(self) :
		r"""The maximum length of filter expression is 255 and it can be of following format:
		<expression> [<relop> <expression>]
		<relop> = ( && | || )
		<expression> =:
		CONNECTION.<qualifier>.<qualifier-method>.(<qualifier-value>)
		<qualifier> = SRCIP
		<qualifier-method> = [ EQ | NE ]
		<qualifier-value>  = A valid IPv4 address
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
		<qualifier> = SVCNAME
		<qualifier-method> = [ EQ | NE | CONTAINS | STARTSWITH
		| ENDSWITH ]
		<qualifier-value>  = service name.
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
		<qualifier-value>  = A valid interface id in the form of
		x/y (n/x/y in case of cluster interface).
		examle = CONNECTION.INTF.EQ("0/1/1")
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
		<qualifier> = IDLETIME
		<qualifier-method> = [ EQ | NE | GT | GE | LT | LE
		| BETWEEN ]
		<qualifier-value>  = A positive integer indicating the
		idletime.
		example = CONNECTION.IDLETIME.LT(100)
		<qualifier> = TCPSTATE
		<qualifier-method> = [ EQ | NE ]
		<qualifier-value>  = ( CLOSE_WAIT | CLOSED | CLOSING |
		ESTABLISHED | FIN_WAIT_1 | FIN_WAIT_2 | LAST_ACK |
		LISTEN | SYN_RECEIVED | SYN_SENT | TIME_WAIT |
		NOT_APPLICABLE)
		example = CONNECTION.TCPSTATE.EQ(LISTEN)
		<qualifier> = SERVICE_TYPE
		<qualifier-method> = [ EQ | NE ]
		<qualifier-value>  = ( SVC_HTTP | FTP | TCP | UDP | SSL |
		SSL_BRIDGE | SSL_TCP | NNTP | RPCSVR | RPCSVRS |
		RPCCLNT | SVC_DNS | ADNS | SNMP | RTSP | DHCPRA | NAT | ANY |
		MONITOR | MONITOR_UDP | MONITOR_PING | SIP_UDP |
		SVC_MYSQL | SVC_MSSQL | SERVICE_UNKNOWN )
		example = CONNECTION.SERVICE_TYPE.EQ(ANY)
		<qualifier> = TRAFFIC_DOMAIN_ID
		<qualifier-method> = [ EQ | NE | GT | GE | LT | LE
		| BETWEEN ]
		<qualifier-value>  = A valid traffic domain ID.
		example = CONNECTION.TRAFFIC_DOMAIN_ID.EQ(0)
		common usecases:
		Filtering out loopback connections and view present
		connections through netsclaer
		show connectiontable "CONNECTION.IP.NEQ(127.0.0.1) &&
		CONNECTION.TCPSTATE.EQ(ESTABLISHED)" -detail full
		show connections from a particular sourceip and targeted
		to port 80
		show connectiontable "CONNECTION.SRCIP.EQ(10.102.1.91) &&
		CONNECTION.DSTPORT.EQ(80)"
		show connection particular to a service and its linked
		client connections
		show connectiontable "CONNECTION.SVCNAME.EQ("S1")"
		-detail link
		show connections for a particular servicetype(e.g.http)
		show connectiontable "CONNECTION.SERVICE_TYPE.EQ(TCP)"
		viewing connections that have been idle for a long time
		show connectiontable "CONNECTION.IDLETIME.GT(100)"
		show connections for a particular interface and vlan
		show connectiontable "CONNECTION.INTF.EQ("1/1") &&
		CONNECTION.VLANID.EQ(1)"
		.
		"""
		try :
			return self._filterexpression
		except Exception as e:
			raise e

	@filterexpression.setter
	def filterexpression(self, filterexpression) :
		r"""The maximum length of filter expression is 255 and it can be of following format:
		<expression> [<relop> <expression>]
		<relop> = ( && | || )
		<expression> =:
		CONNECTION.<qualifier>.<qualifier-method>.(<qualifier-value>)
		<qualifier> = SRCIP
		<qualifier-method> = [ EQ | NE ]
		<qualifier-value>  = A valid IPv4 address
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
		<qualifier> = SVCNAME
		<qualifier-method> = [ EQ | NE | CONTAINS | STARTSWITH
		| ENDSWITH ]
		<qualifier-value>  = service name.
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
		<qualifier-value>  = A valid interface id in the form of
		x/y (n/x/y in case of cluster interface).
		examle = CONNECTION.INTF.EQ("0/1/1")
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
		<qualifier> = IDLETIME
		<qualifier-method> = [ EQ | NE | GT | GE | LT | LE
		| BETWEEN ]
		<qualifier-value>  = A positive integer indicating the
		idletime.
		example = CONNECTION.IDLETIME.LT(100)
		<qualifier> = TCPSTATE
		<qualifier-method> = [ EQ | NE ]
		<qualifier-value>  = ( CLOSE_WAIT | CLOSED | CLOSING |
		ESTABLISHED | FIN_WAIT_1 | FIN_WAIT_2 | LAST_ACK |
		LISTEN | SYN_RECEIVED | SYN_SENT | TIME_WAIT |
		NOT_APPLICABLE)
		example = CONNECTION.TCPSTATE.EQ(LISTEN)
		<qualifier> = SERVICE_TYPE
		<qualifier-method> = [ EQ | NE ]
		<qualifier-value>  = ( SVC_HTTP | FTP | TCP | UDP | SSL |
		SSL_BRIDGE | SSL_TCP | NNTP | RPCSVR | RPCSVRS |
		RPCCLNT | SVC_DNS | ADNS | SNMP | RTSP | DHCPRA | NAT | ANY |
		MONITOR | MONITOR_UDP | MONITOR_PING | SIP_UDP |
		SVC_MYSQL | SVC_MSSQL | SERVICE_UNKNOWN )
		example = CONNECTION.SERVICE_TYPE.EQ(ANY)
		<qualifier> = TRAFFIC_DOMAIN_ID
		<qualifier-method> = [ EQ | NE | GT | GE | LT | LE
		| BETWEEN ]
		<qualifier-value>  = A valid traffic domain ID.
		example = CONNECTION.TRAFFIC_DOMAIN_ID.EQ(0)
		common usecases:
		Filtering out loopback connections and view present
		connections through netsclaer
		show connectiontable "CONNECTION.IP.NEQ(127.0.0.1) &&
		CONNECTION.TCPSTATE.EQ(ESTABLISHED)" -detail full
		show connections from a particular sourceip and targeted
		to port 80
		show connectiontable "CONNECTION.SRCIP.EQ(10.102.1.91) &&
		CONNECTION.DSTPORT.EQ(80)"
		show connection particular to a service and its linked
		client connections
		show connectiontable "CONNECTION.SVCNAME.EQ("S1")"
		-detail link
		show connections for a particular servicetype(e.g.http)
		show connectiontable "CONNECTION.SERVICE_TYPE.EQ(TCP)"
		viewing connections that have been idle for a long time
		show connectiontable "CONNECTION.IDLETIME.GT(100)"
		show connections for a particular interface and vlan
		show connectiontable "CONNECTION.INTF.EQ("1/1") &&
		CONNECTION.VLANID.EQ(1)"
		.
		"""
		try :
			self._filterexpression = filterexpression
		except Exception as e:
			raise e

	@property
	def link(self) :
		r"""Display link information if available.
		"""
		try :
			return self._link
		except Exception as e:
			raise e

	@link.setter
	def link(self, link) :
		r"""Display link information if available.
		"""
		try :
			self._link = link
		except Exception as e:
			raise e

	@property
	def filtername(self) :
		r"""Display name instead of IP for local entities.
		"""
		try :
			return self._filtername
		except Exception as e:
			raise e

	@filtername.setter
	def filtername(self, filtername) :
		r"""Display name instead of IP for local entities.
		"""
		try :
			self._filtername = filtername
		except Exception as e:
			raise e

	@property
	def detail(self) :
		r"""Specify display options for the connection table.
		* LINK - Displays the linked PCB (Protocol Control Block).
		* NAME - Displays along with the service name.
		* CONNFAILOVER - Displays PCB with connection failover.
		* FULL - Displays all available details.<br/>Possible values = LINK, NAME, CONNFAILOVER, FULL, NNM.
		"""
		try :
			return self._detail
		except Exception as e:
			raise e

	@detail.setter
	def detail(self, detail) :
		r"""Specify display options for the connection table.
		* LINK - Displays the linked PCB (Protocol Control Block).
		* NAME - Displays along with the service name.
		* CONNFAILOVER - Displays PCB with connection failover.
		* FULL - Displays all available details.<br/>Possible values = LINK, NAME, CONNFAILOVER, FULL, NNM
		"""
		try :
			self._detail = detail
		except Exception as e:
			raise e

	@property
	def listen(self) :
		r"""Display listening services only.
		"""
		try :
			return self._listen
		except Exception as e:
			raise e

	@listen.setter
	def listen(self, listen) :
		r"""Display listening services only.
		"""
		try :
			self._listen = listen
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
	def sourceip(self) :
		r"""Source IP of the connection.
		"""
		try :
			return self._sourceip
		except Exception as e:
			raise e

	@property
	def sourceport(self) :
		r"""Source port of the connection.<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API.
		"""
		try :
			return self._sourceport
		except Exception as e:
			raise e

	@property
	def destip(self) :
		r"""Destination IP of the connection.
		"""
		try :
			return self._destip
		except Exception as e:
			raise e

	@property
	def destport(self) :
		r"""Destination port of the connection.<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API.
		"""
		try :
			return self._destport
		except Exception as e:
			raise e

	@property
	def svctype(self) :
		r"""Protocol supported by the connection.<br/>Possible values = HTTP, FTP, TCP, UDP, SSL, SSL_BRIDGE, SSL_TCP, NNTP, RPCSVR, DNS, ADNS, SNMP, RTSP, DHCPRA, ANY, SIP_UDP, SIP_TCP, SIP_SSL, DNS_TCP, ADNS_TCP, HTTPSVR, HTTPCLIENT, NAT, HA, AAA, SINCTCP, VPN AFTP, MONITORS, SSLVPN UDP, SINCUDP, RIP, UDP CLNT, SASP, RPCCLNTS, ROUTE, AUDIT, STA HTTP, STA SSL, DNS RESOLVE, RDP, MYSQL, MSSQL, DIAMETER, SSL_DIAMETER, TFTP, ORACLE, ICA, RADIUS, RADIUSListener, SMPP, PPTP, GRE, SYSLOGTCP, SYSLOGUDP, FIX, SSL_FIX, TFTP_DATA, USER_TCP, USER_SSL_TCP.
		"""
		try :
			return self._svctype
		except Exception as e:
			raise e

	@property
	def idletime(self) :
		r"""Time since last activity was detected on the connection.
		"""
		try :
			return self._idletime
		except Exception as e:
			raise e

	@property
	def state(self) :
		r"""Current TCP/IP state of the connection.<br/>Possible values = CLOSED, LISTEN, SYN_SENT, SYN_RECEIVED, ESTABLISHED, CLOSE_WAIT, FIN_WAIT_1, CLOSING, LAST_ACK, FIN_WAIT_2, TIME_WAIT, NA.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@property
	def linksourceip(self) :
		r"""Source IP of the link connection.
		"""
		try :
			return self._linksourceip
		except Exception as e:
			raise e

	@property
	def linksourceport(self) :
		r"""Source port of the link connection.<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API.
		"""
		try :
			return self._linksourceport
		except Exception as e:
			raise e

	@property
	def linkdestip(self) :
		r"""Destination IP of the link connection.
		"""
		try :
			return self._linkdestip
		except Exception as e:
			raise e

	@property
	def linkdestport(self) :
		r"""Destination port of the link connection.<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API.
		"""
		try :
			return self._linkdestport
		except Exception as e:
			raise e

	@property
	def linkservicetype(self) :
		r"""Protocol supported by the link connection.<br/>Possible values = HTTP, FTP, TCP, UDP, SSL, SSL_BRIDGE, SSL_TCP, NNTP, RPCSVR, DNS, ADNS, SNMP, RTSP, DHCPRA, ANY, SIP_UDP, SIP_TCP, SIP_SSL, DNS_TCP, ADNS_TCP, HTTPSVR, HTTPCLIENT, NAT, HA, AAA, SINCTCP, VPN AFTP, MONITORS, SSLVPN UDP, SINCUDP, RIP, UDP CLNT, SASP, RPCCLNTS, ROUTE, AUDIT, STA HTTP, STA SSL, DNS RESOLVE, RDP, MYSQL, MSSQL, DIAMETER, SSL_DIAMETER, TFTP, ORACLE, ICA, RADIUS, RADIUSListener, SMPP, PPTP, GRE, SYSLOGTCP, SYSLOGUDP, FIX, SSL_FIX, TFTP_DATA, USER_TCP, USER_SSL_TCP.
		"""
		try :
			return self._linkservicetype
		except Exception as e:
			raise e

	@property
	def linkidletime(self) :
		r"""Time since last activity was detected on link connection.
		"""
		try :
			return self._linkidletime
		except Exception as e:
			raise e

	@property
	def linkstate(self) :
		r"""TCP/IP current state of link connection.<br/>Possible values = CLOSED, LISTEN, SYN_SENT, SYN_RECEIVED, ESTABLISHED, CLOSE_WAIT, FIN_WAIT_1, CLOSING, LAST_ACK, FIN_WAIT_2, TIME_WAIT, NA.
		"""
		try :
			return self._linkstate
		except Exception as e:
			raise e

	@property
	def entityname(self) :
		r"""NetScaler entity name for the connection.
		"""
		try :
			return self._entityname
		except Exception as e:
			raise e

	@property
	def linkentityname(self) :
		r"""NetScaler entity name for link connection.
		"""
		try :
			return self._linkentityname
		except Exception as e:
			raise e

	@property
	def connid(self) :
		r"""Unique transaction number for the connection.
		"""
		try :
			return self._connid
		except Exception as e:
			raise e

	@property
	def linkconnid(self) :
		r"""Unique transaction number for the peer connection.
		"""
		try :
			return self._linkconnid
		except Exception as e:
			raise e

	@property
	def connproperties(self) :
		r"""flags used to store connection properties like client, server etc.<br/>Possible values = LINK, HASLINK, CLIENT, SERVER, NNM, MPTCP, SUBFLOW.
		"""
		try :
			return self._connproperties
		except Exception as e:
			raise e

	@property
	def optionflags(self) :
		r"""flags used to store TCP options like Sack, WS.<br/>Possible values = sack, timstmp, ws.
		"""
		try :
			return self._optionflags
		except Exception as e:
			raise e

	@property
	def nswsvalue(self) :
		r"""netscaler window scaling value.
		"""
		try :
			return self._nswsvalue
		except Exception as e:
			raise e

	@property
	def peerwsvalue(self) :
		r"""peer window scaling value.
		"""
		try :
			return self._peerwsvalue
		except Exception as e:
			raise e

	@property
	def mss(self) :
		r"""Client side MSS for the connection - used in server SYN.
		"""
		try :
			return self._mss
		except Exception as e:
			raise e

	@property
	def retxretrycnt(self) :
		r"""Retransmission retry count for the connection.
		"""
		try :
			return self._retxretrycnt
		except Exception as e:
			raise e

	@property
	def rcvwnd(self) :
		r"""Received Advertised Window for the connection.
		"""
		try :
			return self._rcvwnd
		except Exception as e:
			raise e

	@property
	def advwnd(self) :
		r"""Sent advertised window for the connection.
		"""
		try :
			return self._advwnd
		except Exception as e:
			raise e

	@property
	def sndcwnd(self) :
		r"""sent congestion window for the connection.
		"""
		try :
			return self._sndcwnd
		except Exception as e:
			raise e

	@property
	def iss(self) :
		r"""Initial send sequence number for the connection.
		"""
		try :
			return self._iss
		except Exception as e:
			raise e

	@property
	def irs(self) :
		r"""Initial receive sequence number for the connection.
		"""
		try :
			return self._irs
		except Exception as e:
			raise e

	@property
	def rcvnxt(self) :
		r"""next expecting seq number for the connection.
		"""
		try :
			return self._rcvnxt
		except Exception as e:
			raise e

	@property
	def maxack(self) :
		r"""current running max ack sent for the connection.
		"""
		try :
			return self._maxack
		except Exception as e:
			raise e

	@property
	def sndnxt(self) :
		r"""next bytes seq number for the connection.
		"""
		try :
			return self._sndnxt
		except Exception as e:
			raise e

	@property
	def sndunack(self) :
		r"""Most recently received ACK for the connection.
		"""
		try :
			return self._sndunack
		except Exception as e:
			raise e

	@property
	def httpendseq(self) :
		r"""HTTP parsing tracking seq number for the connection.
		"""
		try :
			return self._httpendseq
		except Exception as e:
			raise e

	@property
	def httpstate(self) :
		r"""HTTP Protocol  state for the connection.<br/>Possible values = INITIALIZED, CONTENT_LENGTH, CHUNKED, WAIT_FINAL_ACK, UNKNOWN, DONE, WAIT_FIN.
		"""
		try :
			return self._httpstate
		except Exception as e:
			raise e

	@property
	def trcount(self) :
		r"""Max reuests allowed per connection.
		"""
		try :
			return self._trcount
		except Exception as e:
			raise e

	@property
	def priority(self) :
		r"""priority of the connection.<br/>Possible values = SC Priority, Priority queue1, priority queue2, priority queue3, DoS Priority, Surge Priority.
		"""
		try :
			return self._priority
		except Exception as e:
			raise e

	@property
	def httpreqver(self) :
		r"""current HTTP request version on the connection.<br/>Possible values = HTTP_1_0, HTTP_1_1, HTTP_0_9, RTSP_1_0, SIP_2_0, VPN_ICA_SOCKS, VPN_ICA_CGP, HTTP_2_0.
		"""
		try :
			return self._httpreqver
		except Exception as e:
			raise e

	@property
	def httprequest(self) :
		r"""current HTTP request type on the connection.<br/>Possible values = OPTIONS, GET, HEAD, POST, PUT, DELETE, TRACE, CONNECT, RPCCONNECT.
		"""
		try :
			return self._httprequest
		except Exception as e:
			raise e

	@property
	def httprspcode(self) :
		r"""current response type on the connection.
		"""
		try :
			return self._httprspcode
		except Exception as e:
			raise e

	@property
	def rttsmoothed(self) :
		r"""smoothed RTT value of the connection.
		"""
		try :
			return self._rttsmoothed
		except Exception as e:
			raise e

	@property
	def rttvariance(self) :
		r"""RTT variance for the connection.
		"""
		try :
			return self._rttvariance
		except Exception as e:
			raise e

	@property
	def outoforderpkts(self) :
		r"""held packets on the connection.
		"""
		try :
			return self._outoforderpkts
		except Exception as e:
			raise e

	@property
	def linkoptionflag(self) :
		r"""Link connection's TCP option flag for Sack and WS.<br/>Possible values = sack, timstmp, ws.
		"""
		try :
			return self._linkoptionflag
		except Exception as e:
			raise e

	@property
	def linknswsvalue(self) :
		r"""Link connection-s netscaler window scaling value.
		"""
		try :
			return self._linknswsvalue
		except Exception as e:
			raise e

	@property
	def linkpeerwsvalue(self) :
		r"""Link connection-s peer netscaler window scaling value.
		"""
		try :
			return self._linkpeerwsvalue
		except Exception as e:
			raise e

	@property
	def targetnodeidnnm(self) :
		r"""NNM connection target node ID.
		"""
		try :
			return self._targetnodeidnnm
		except Exception as e:
			raise e

	@property
	def sourcenodeidnnm(self) :
		r"""NNM connection source node ID.
		"""
		try :
			return self._sourcenodeidnnm
		except Exception as e:
			raise e

	@property
	def channelidnnm(self) :
		r"""NNM connection channel ID.
		"""
		try :
			return self._channelidnnm
		except Exception as e:
			raise e

	@property
	def msgversionnnm(self) :
		r"""nnm message version.
		"""
		try :
			return self._msgversionnnm
		except Exception as e:
			raise e

	@property
	def td(self) :
		r"""Traffic Domain Id.
		"""
		try :
			return self._td
		except Exception as e:
			raise e

	@property
	def maxrcvbuf(self) :
		r"""Maximum receive window that application advertizes to peer.
		"""
		try :
			return self._maxrcvbuf
		except Exception as e:
			raise e

	@property
	def linkmaxrcvbuf(self) :
		r"""Maximum receive window that application advertizes to peer in linked connection.
		"""
		try :
			return self._linkmaxrcvbuf
		except Exception as e:
			raise e

	@property
	def rxqsize(self) :
		r"""Total number of bytes in Netscaler receive buffer. This includes bytes being processed / policy related data / stored in application buffer.
		"""
		try :
			return self._rxqsize
		except Exception as e:
			raise e

	@property
	def linkrxqsize(self) :
		r"""Total number of bytes in Netscaler receive buffer for linked connection. This includes bytes being processed / policy related data / stored in application buffer.
		"""
		try :
			return self._linkrxqsize
		except Exception as e:
			raise e

	@property
	def maxsndbuf(self) :
		r"""Maximum send window that application can process and send.
		"""
		try :
			return self._maxsndbuf
		except Exception as e:
			raise e

	@property
	def linkmaxsndbuf(self) :
		r"""Maximum send window that application can process and send in linked connection.
		"""
		try :
			return self._linkmaxsndbuf
		except Exception as e:
			raise e

	@property
	def txqsize(self) :
		r"""Total number of bytes in Netscaler send buffer. This includes both inflight and queued bytes in netscaler.
		"""
		try :
			return self._txqsize
		except Exception as e:
			raise e

	@property
	def linktxqsize(self) :
		r"""Total number of bytes in Netscaler send buffer for linked connection. This includes both inflight and queued bytes in netscaler.
		"""
		try :
			return self._linktxqsize
		except Exception as e:
			raise e

	@property
	def flavor(self) :
		r"""TCP congestion control algorithm.<br/>Possible values = Default, Westwood, BIC, CUBIC, Nile.
		"""
		try :
			return self._flavor
		except Exception as e:
			raise e

	@property
	def linkflavor(self) :
		r"""TCP congestion control algorithm for a linked connection.<br/>Possible values = Default, Westwood, BIC, CUBIC, Nile.
		"""
		try :
			return self._linkflavor
		except Exception as e:
			raise e

	@property
	def bwestimate(self) :
		r"""TCP Bandwidth Estimate.
		"""
		try :
			return self._bwestimate
		except Exception as e:
			raise e

	@property
	def linkbwestimate(self) :
		r"""TCP Bandwidth Estimate for a linked connection.
		"""
		try :
			return self._linkbwestimate
		except Exception as e:
			raise e

	@property
	def rttmin(self) :
		r"""Minimum Round Trip Time for the connection.
		"""
		try :
			return self._rttmin
		except Exception as e:
			raise e

	@property
	def linkrttmin(self) :
		r"""Minimum Round Trip Time for linked connection.
		"""
		try :
			return self._linkrttmin
		except Exception as e:
			raise e

	@property
	def name(self) :
		r"""Name of TCP profile attached to the connection.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@property
	def linkname(self) :
		r"""Name of TCP profile attached to the connection.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._linkname
		except Exception as e:
			raise e

	@property
	def tcpmode(self) :
		r"""TCP Optimization modes TRANSPARENT / ENDPOINT.<br/>Possible values = TRANSPARENT, ENDPOINT.
		"""
		try :
			return self._tcpmode
		except Exception as e:
			raise e

	@property
	def linktcpmode(self) :
		r"""TCP Optimization modes TRANSPARENT / ENDPOINT for linked connection.<br/>Possible values = TRANSPARENT, ENDPOINT.
		"""
		try :
			return self._linktcpmode
		except Exception as e:
			raise e

	@property
	def realtimertt(self) :
		r"""Real Time / Instantaneous round trip time.
		"""
		try :
			return self._realtimertt
		except Exception as e:
			raise e

	@property
	def linkrealtimertt(self) :
		r"""Real Time / Instantaneous round trip time for linked connection.
		"""
		try :
			return self._linkrealtimertt
		except Exception as e:
			raise e

	@property
	def sndbuf(self) :
		r"""send buffer size.
		"""
		try :
			return self._sndbuf
		except Exception as e:
			raise e

	@property
	def linksndbuf(self) :
		r"""Send buffer size for linked connection.
		"""
		try :
			return self._linksndbuf
		except Exception as e:
			raise e

	@property
	def nsbtcpwaitq(self) :
		r"""Number of packets in TCP wait queue.
		"""
		try :
			return self._nsbtcpwaitq
		except Exception as e:
			raise e

	@property
	def linknsbtcpwaitq(self) :
		r"""Number of packets in wait queue for linked connection.
		"""
		try :
			return self._linknsbtcpwaitq
		except Exception as e:
			raise e

	@property
	def nsbretxq(self) :
		r"""Number of packets in retransmission queue.
		"""
		try :
			return self._nsbretxq
		except Exception as e:
			raise e

	@property
	def linknsbretxq(self) :
		r"""Number of packets in retransmission queue for linked connection.
		"""
		try :
			return self._linknsbretxq
		except Exception as e:
			raise e

	@property
	def sackblocks(self) :
		r"""Number of sack blocks attached to the connection.
		"""
		try :
			return self._sackblocks
		except Exception as e:
			raise e

	@property
	def linksackblocks(self) :
		r"""Number of sack blocks attached in linked connection.
		"""
		try :
			return self._linksackblocks
		except Exception as e:
			raise e

	@property
	def congstate(self) :
		r"""TCP congestion state.<br/>Possible values = open, recovery, loss, reneg, partial_ACK, retx_lost.
		"""
		try :
			return self._congstate
		except Exception as e:
			raise e

	@property
	def linkcongstate(self) :
		r"""TCP congestion state for a linked connection.<br/>Possible values = open, recovery, loss, reneg, partial_ACK, retx_lost.
		"""
		try :
			return self._linkcongstate
		except Exception as e:
			raise e

	@property
	def sndrecoverle(self) :
		r"""Sequence Number denoting end of fast recovery.
		"""
		try :
			return self._sndrecoverle
		except Exception as e:
			raise e

	@property
	def linksndrecoverle(self) :
		r"""Sequence Number denoting end of fast recovery for linked connection.
		"""
		try :
			return self._linksndrecoverle
		except Exception as e:
			raise e

	@property
	def creditsinbytes(self) :
		r"""Connections current credits in Bytes/ms.
		"""
		try :
			return self._creditsinbytes
		except Exception as e:
			raise e

	@property
	def linkcredits(self) :
		r"""Link connections current credits in Bytes/ms.
		"""
		try :
			return self._linkcredits
		except Exception as e:
			raise e

	@property
	def rateinbytes(self) :
		r"""Connections current rate in Bytes/ms.
		"""
		try :
			return self._rateinbytes
		except Exception as e:
			raise e

	@property
	def linkrateinbytes(self) :
		r"""Link connections current rate in Bytes/ms.
		"""
		try :
			return self._linkrateinbytes
		except Exception as e:
			raise e

	@property
	def rateschedulerqueue(self) :
		r"""Bytes that are queued in the rate scheduler for this connection.
		"""
		try :
			return self._rateschedulerqueue
		except Exception as e:
			raise e

	@property
	def linkrateschedulerqueue(self) :
		r"""Bytes that are queued in the rate scheduler for link connection.
		"""
		try :
			return self._linkrateschedulerqueue
		except Exception as e:
			raise e

	@property
	def burstratecontrol(self) :
		r"""TCP Burst Rate Control DISABLED/FIXED/DYNAMIC.<br/>Possible values = DISABLED, FIXED, DYNAMIC.
		"""
		try :
			return self._burstratecontrol
		except Exception as e:
			raise e

	@property
	def linkburstratecontrol(self) :
		r"""TCP Burst Rate Control DISABLED/FIXED/DYNAMIC.<br/>Possible values = DISABLED, FIXED, DYNAMIC.
		"""
		try :
			return self._linkburstratecontrol
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nsconnectiontable_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nsconnectiontable
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
		r""" Use this API to fetch all the nsconnectiontable resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nsconnectiontable()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		r""" Use this API to fetch all the nsconnectiontable resources that are configured on netscaler.
	# This uses nsconnectiontable_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = nsconnectiontable()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of nsconnectiontable resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nsconnectiontable()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the nsconnectiontable resources configured on NetScaler.
		"""
		try :
			obj = nsconnectiontable()
			option_ = options()
			option_.count = True
			response = obj.get_resources(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	@classmethod
	def count_filtered(cls, client, filter_) :
		r""" Use this API to count filtered the set of nsconnectiontable resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nsconnectiontable()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Priority:
		SC_Priority = "SC Priority"
		Priority_queue1 = "Priority queue1"
		priority_queue2 = "priority queue2"
		priority_queue3 = "priority queue3"
		DoS_Priority = "DoS Priority"
		Surge_Priority = "Surge Priority"

	class Linkoptionflag:
		sack = "sack"
		timstmp = "timstmp"
		ws = "ws"

	class State:
		CLOSED = "CLOSED"
		LISTEN = "LISTEN"
		SYN_SENT = "SYN_SENT"
		SYN_RECEIVED = "SYN_RECEIVED"
		ESTABLISHED = "ESTABLISHED"
		CLOSE_WAIT = "CLOSE_WAIT"
		FIN_WAIT_1 = "FIN_WAIT_1"
		CLOSING = "CLOSING"
		LAST_ACK = "LAST_ACK"
		FIN_WAIT_2 = "FIN_WAIT_2"
		TIME_WAIT = "TIME_WAIT"
		NA = "NA"

	class Flavor:
		Default = "Default"
		Westwood = "Westwood"
		BIC = "BIC"
		CUBIC = "CUBIC"
		Nile = "Nile"

	class Svctype:
		HTTP = "HTTP"
		FTP = "FTP"
		TCP = "TCP"
		UDP = "UDP"
		SSL = "SSL"
		SSL_BRIDGE = "SSL_BRIDGE"
		SSL_TCP = "SSL_TCP"
		NNTP = "NNTP"
		RPCSVR = "RPCSVR"
		DNS = "DNS"
		ADNS = "ADNS"
		SNMP = "SNMP"
		RTSP = "RTSP"
		DHCPRA = "DHCPRA"
		ANY = "ANY"
		SIP_UDP = "SIP_UDP"
		SIP_TCP = "SIP_TCP"
		SIP_SSL = "SIP_SSL"
		DNS_TCP = "DNS_TCP"
		ADNS_TCP = "ADNS_TCP"
		HTTPSVR = "HTTPSVR"
		HTTPCLIENT = "HTTPCLIENT"
		NAT = "NAT"
		HA = "HA"
		AAA = "AAA"
		SINCTCP = "SINCTCP"
		VPN_AFTP = "VPN AFTP"
		MONITORS = "MONITORS"
		SSLVPN_UDP = "SSLVPN UDP"
		SINCUDP = "SINCUDP"
		RIP = "RIP"
		UDP_CLNT = "UDP CLNT"
		SASP = "SASP"
		RPCCLNTS = "RPCCLNTS"
		ROUTE = "ROUTE"
		AUDIT = "AUDIT"
		STA_HTTP = "STA HTTP"
		STA_SSL = "STA SSL"
		DNS_RESOLVE = "DNS RESOLVE"
		RDP = "RDP"
		MYSQL = "MYSQL"
		MSSQL = "MSSQL"
		DIAMETER = "DIAMETER"
		SSL_DIAMETER = "SSL_DIAMETER"
		TFTP = "TFTP"
		ORACLE = "ORACLE"
		ICA = "ICA"
		RADIUS = "RADIUS"
		RADIUSListener = "RADIUSListener"
		SMPP = "SMPP"
		PPTP = "PPTP"
		GRE = "GRE"
		SYSLOGTCP = "SYSLOGTCP"
		SYSLOGUDP = "SYSLOGUDP"
		FIX = "FIX"
		SSL_FIX = "SSL_FIX"
		TFTP_DATA = "TFTP_DATA"
		USER_TCP = "USER_TCP"
		USER_SSL_TCP = "USER_SSL_TCP"

	class Tcpmode:
		TRANSPARENT = "TRANSPARENT"
		ENDPOINT = "ENDPOINT"

	class Connproperties:
		LINK = "LINK"
		HASLINK = "HASLINK"
		CLIENT = "CLIENT"
		SERVER = "SERVER"
		NNM = "NNM"
		MPTCP = "MPTCP"
		SUBFLOW = "SUBFLOW"

	class Httpreqver:
		HTTP_1_0 = "HTTP_1_0"
		HTTP_1_1 = "HTTP_1_1"
		HTTP_0_9 = "HTTP_0_9"
		RTSP_1_0 = "RTSP_1_0"
		SIP_2_0 = "SIP_2_0"
		VPN_ICA_SOCKS = "VPN_ICA_SOCKS"
		VPN_ICA_CGP = "VPN_ICA_CGP"
		HTTP_2_0 = "HTTP_2_0"

	class Httprequest:
		OPTIONS = "OPTIONS"
		GET = "GET"
		HEAD = "HEAD"
		POST = "POST"
		PUT = "PUT"
		DELETE = "DELETE"
		TRACE = "TRACE"
		CONNECT = "CONNECT"
		RPCCONNECT = "RPCCONNECT"

	class Httpstate:
		INITIALIZED = "INITIALIZED"
		CONTENT_LENGTH = "CONTENT_LENGTH"
		CHUNKED = "CHUNKED"
		WAIT_FINAL_ACK = "WAIT_FINAL_ACK"
		UNKNOWN = "UNKNOWN"
		DONE = "DONE"
		WAIT_FIN = "WAIT_FIN"

	class Congstate:
		open = "open"
		recovery = "recovery"
		loss = "loss"
		reneg = "reneg"
		partial_ACK = "partial_ACK"
		retx_lost = "retx_lost"

	class Linkstate:
		CLOSED = "CLOSED"
		LISTEN = "LISTEN"
		SYN_SENT = "SYN_SENT"
		SYN_RECEIVED = "SYN_RECEIVED"
		ESTABLISHED = "ESTABLISHED"
		CLOSE_WAIT = "CLOSE_WAIT"
		FIN_WAIT_1 = "FIN_WAIT_1"
		CLOSING = "CLOSING"
		LAST_ACK = "LAST_ACK"
		FIN_WAIT_2 = "FIN_WAIT_2"
		TIME_WAIT = "TIME_WAIT"
		NA = "NA"

	class Linkburstratecontrol:
		DISABLED = "DISABLED"
		FIXED = "FIXED"
		DYNAMIC = "DYNAMIC"

	class Optionflags:
		sack = "sack"
		timstmp = "timstmp"
		ws = "ws"

	class Burstratecontrol:
		DISABLED = "DISABLED"
		FIXED = "FIXED"
		DYNAMIC = "DYNAMIC"

	class Linktcpmode:
		TRANSPARENT = "TRANSPARENT"
		ENDPOINT = "ENDPOINT"

	class Linkflavor:
		Default = "Default"
		Westwood = "Westwood"
		BIC = "BIC"
		CUBIC = "CUBIC"
		Nile = "Nile"

	class Detail:
		LINK = "LINK"
		NAME = "NAME"
		CONNFAILOVER = "CONNFAILOVER"
		FULL = "FULL"
		NNM = "NNM"

	class Linkcongstate:
		open = "open"
		recovery = "recovery"
		loss = "loss"
		reneg = "reneg"
		partial_ACK = "partial_ACK"
		retx_lost = "retx_lost"

	class Linkservicetype:
		HTTP = "HTTP"
		FTP = "FTP"
		TCP = "TCP"
		UDP = "UDP"
		SSL = "SSL"
		SSL_BRIDGE = "SSL_BRIDGE"
		SSL_TCP = "SSL_TCP"
		NNTP = "NNTP"
		RPCSVR = "RPCSVR"
		DNS = "DNS"
		ADNS = "ADNS"
		SNMP = "SNMP"
		RTSP = "RTSP"
		DHCPRA = "DHCPRA"
		ANY = "ANY"
		SIP_UDP = "SIP_UDP"
		SIP_TCP = "SIP_TCP"
		SIP_SSL = "SIP_SSL"
		DNS_TCP = "DNS_TCP"
		ADNS_TCP = "ADNS_TCP"
		HTTPSVR = "HTTPSVR"
		HTTPCLIENT = "HTTPCLIENT"
		NAT = "NAT"
		HA = "HA"
		AAA = "AAA"
		SINCTCP = "SINCTCP"
		VPN_AFTP = "VPN AFTP"
		MONITORS = "MONITORS"
		SSLVPN_UDP = "SSLVPN UDP"
		SINCUDP = "SINCUDP"
		RIP = "RIP"
		UDP_CLNT = "UDP CLNT"
		SASP = "SASP"
		RPCCLNTS = "RPCCLNTS"
		ROUTE = "ROUTE"
		AUDIT = "AUDIT"
		STA_HTTP = "STA HTTP"
		STA_SSL = "STA SSL"
		DNS_RESOLVE = "DNS RESOLVE"
		RDP = "RDP"
		MYSQL = "MYSQL"
		MSSQL = "MSSQL"
		DIAMETER = "DIAMETER"
		SSL_DIAMETER = "SSL_DIAMETER"
		TFTP = "TFTP"
		ORACLE = "ORACLE"
		ICA = "ICA"
		RADIUS = "RADIUS"
		RADIUSListener = "RADIUSListener"
		SMPP = "SMPP"
		PPTP = "PPTP"
		GRE = "GRE"
		SYSLOGTCP = "SYSLOGTCP"
		SYSLOGUDP = "SYSLOGUDP"
		FIX = "FIX"
		SSL_FIX = "SSL_FIX"
		TFTP_DATA = "TFTP_DATA"
		USER_TCP = "USER_TCP"
		USER_SSL_TCP = "USER_SSL_TCP"

class nsconnectiontable_response(base_response) :
	def __init__(self, length=1) :
		self.nsconnectiontable = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nsconnectiontable = [nsconnectiontable() for _ in range(length)]

