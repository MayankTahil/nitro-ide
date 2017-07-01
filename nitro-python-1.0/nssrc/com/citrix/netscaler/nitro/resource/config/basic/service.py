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

class service(base_resource) :
	""" Configuration for service resource. """
	def __init__(self) :
		self._name = None
		self._ip = None
		self._servername = None
		self._servicetype = None
		self._port = None
		self._cleartextport = None
		self._cachetype = None
		self._maxclient = None
		self._healthmonitor = None
		self._maxreq = None
		self._cacheable = None
		self._cip = None
		self._cipheader = None
		self._usip = None
		self._pathmonitor = None
		self._pathmonitorindv = None
		self._useproxyport = None
		self._sc = None
		self._sp = None
		self._rtspsessionidremap = None
		self._clttimeout = None
		self._svrtimeout = None
		self._customserverid = None
		self._serverid = None
		self._cka = None
		self._tcpb = None
		self._cmp = None
		self._maxbandwidth = None
		self._accessdown = None
		self._monthreshold = None
		self._state = None
		self._downstateflush = None
		self._tcpprofilename = None
		self._httpprofilename = None
		self._hashid = None
		self._comment = None
		self._appflowlog = None
		self._netprofile = None
		self._td = None
		self._processlocal = None
		self._dnsprofilename = None
		self._monconnectionclose = None
		self._ipaddress = None
		self._weight = None
		self._monitor_name_svc = None
		self._riseapbrstatsmsgcode = None
		self._delay = None
		self._graceful = None
		self._all = None
		self._Internal = None
		self._newname = None
		self._numofconnections = None
		self._policyname = None
		self._serviceconftype = None
		self._serviceconftype2 = None
		self._value = None
		self._gslb = None
		self._dup_state = None
		self._publicip = None
		self._publicport = None
		self._svrstate = None
		self._monitor_state = None
		self._monstatcode = None
		self._lastresponse = None
		self._responsetime = None
		self._riseapbrstatsmsgcode2 = None
		self._monstatparam1 = None
		self._monstatparam2 = None
		self._monstatparam3 = None
		self._statechangetimesec = None
		self._statechangetimemsec = None
		self._tickssincelaststatechange = None
		self._stateupdatereason = None
		self._clmonowner = None
		self._clmonview = None
		self._serviceipstr = None
		self._oracleserverversion = None
		self.___count = 0

	@property
	def name(self) :
		r"""Name for the service. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the service has been created.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name for the service. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the service has been created.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def ip(self) :
		r"""IP to assign to the service.<br/>Minimum length =  1.
		"""
		try :
			return self._ip
		except Exception as e:
			raise e

	@ip.setter
	def ip(self, ip) :
		r"""IP to assign to the service.<br/>Minimum length =  1
		"""
		try :
			self._ip = ip
		except Exception as e:
			raise e

	@property
	def servername(self) :
		r"""Name of the server that hosts the service.<br/>Minimum length =  1.
		"""
		try :
			return self._servername
		except Exception as e:
			raise e

	@servername.setter
	def servername(self, servername) :
		r"""Name of the server that hosts the service.<br/>Minimum length =  1
		"""
		try :
			self._servername = servername
		except Exception as e:
			raise e

	@property
	def servicetype(self) :
		r"""Protocol in which data is exchanged with the service.<br/>Possible values = HTTP, FTP, TCP, UDP, SSL, SSL_BRIDGE, SSL_TCP, DTLS, NNTP, RPCSVR, DNS, ADNS, SNMP, RTSP, DHCPRA, ANY, SIP_UDP, SIP_TCP, SIP_SSL, DNS_TCP, ADNS_TCP, MYSQL, MSSQL, ORACLE, RADIUS, RADIUSListener, RDP, DIAMETER, SSL_DIAMETER, TFTP, SMPP, PPTP, GRE, SYSLOGTCP, SYSLOGUDP, FIX, SSL_FIX, USER_TCP, USER_SSL_TCP.
		"""
		try :
			return self._servicetype
		except Exception as e:
			raise e

	@servicetype.setter
	def servicetype(self, servicetype) :
		r"""Protocol in which data is exchanged with the service.<br/>Possible values = HTTP, FTP, TCP, UDP, SSL, SSL_BRIDGE, SSL_TCP, DTLS, NNTP, RPCSVR, DNS, ADNS, SNMP, RTSP, DHCPRA, ANY, SIP_UDP, SIP_TCP, SIP_SSL, DNS_TCP, ADNS_TCP, MYSQL, MSSQL, ORACLE, RADIUS, RADIUSListener, RDP, DIAMETER, SSL_DIAMETER, TFTP, SMPP, PPTP, GRE, SYSLOGTCP, SYSLOGUDP, FIX, SSL_FIX, USER_TCP, USER_SSL_TCP
		"""
		try :
			self._servicetype = servicetype
		except Exception as e:
			raise e

	@property
	def port(self) :
		r"""Port number of the service.<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API.
		"""
		try :
			return self._port
		except Exception as e:
			raise e

	@port.setter
	def port(self, port) :
		r"""Port number of the service.<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API
		"""
		try :
			self._port = port
		except Exception as e:
			raise e

	@property
	def cleartextport(self) :
		r"""Port to which clear text data must be sent after the appliance decrypts incoming SSL traffic. Applicable to transparent SSL services.<br/>Minimum length =  1.
		"""
		try :
			return self._cleartextport
		except Exception as e:
			raise e

	@cleartextport.setter
	def cleartextport(self, cleartextport) :
		r"""Port to which clear text data must be sent after the appliance decrypts incoming SSL traffic. Applicable to transparent SSL services.<br/>Minimum length =  1
		"""
		try :
			self._cleartextport = cleartextport
		except Exception as e:
			raise e

	@property
	def cachetype(self) :
		r"""Cache type supported by the cache server.<br/>Possible values = TRANSPARENT, REVERSE, FORWARD.
		"""
		try :
			return self._cachetype
		except Exception as e:
			raise e

	@cachetype.setter
	def cachetype(self, cachetype) :
		r"""Cache type supported by the cache server.<br/>Possible values = TRANSPARENT, REVERSE, FORWARD
		"""
		try :
			self._cachetype = cachetype
		except Exception as e:
			raise e

	@property
	def maxclient(self) :
		r"""Maximum number of simultaneous open connections to the service.<br/>Maximum length =  4294967294.
		"""
		try :
			return self._maxclient
		except Exception as e:
			raise e

	@maxclient.setter
	def maxclient(self, maxclient) :
		r"""Maximum number of simultaneous open connections to the service.<br/>Maximum length =  4294967294
		"""
		try :
			self._maxclient = maxclient
		except Exception as e:
			raise e

	@property
	def healthmonitor(self) :
		r"""Monitor the health of this service. Available settings function as follows:
		YES - Send probes to check the health of the service.
		NO - Do not send probes to check the health of the service. With the NO option, the appliance shows the service as UP at all times.<br/>Default value: YES<br/>Possible values = YES, NO.
		"""
		try :
			return self._healthmonitor
		except Exception as e:
			raise e

	@healthmonitor.setter
	def healthmonitor(self, healthmonitor) :
		r"""Monitor the health of this service. Available settings function as follows:
		YES - Send probes to check the health of the service.
		NO - Do not send probes to check the health of the service. With the NO option, the appliance shows the service as UP at all times.<br/>Default value: YES<br/>Possible values = YES, NO
		"""
		try :
			self._healthmonitor = healthmonitor
		except Exception as e:
			raise e

	@property
	def maxreq(self) :
		r"""Maximum number of requests that can be sent on a persistent connection to the service. 
		Note: Connection requests beyond this value are rejected.<br/>Maximum length =  65535.
		"""
		try :
			return self._maxreq
		except Exception as e:
			raise e

	@maxreq.setter
	def maxreq(self, maxreq) :
		r"""Maximum number of requests that can be sent on a persistent connection to the service. 
		Note: Connection requests beyond this value are rejected.<br/>Maximum length =  65535
		"""
		try :
			self._maxreq = maxreq
		except Exception as e:
			raise e

	@property
	def cacheable(self) :
		r"""Use the transparent cache redirection virtual server to forward requests to the cache server.
		Note: Do not specify this parameter if you set the Cache Type parameter.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._cacheable
		except Exception as e:
			raise e

	@cacheable.setter
	def cacheable(self, cacheable) :
		r"""Use the transparent cache redirection virtual server to forward requests to the cache server.
		Note: Do not specify this parameter if you set the Cache Type parameter.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._cacheable = cacheable
		except Exception as e:
			raise e

	@property
	def cip(self) :
		r"""Before forwarding a request to the service, insert an HTTP header with the client's IPv4 or IPv6 address as its value. Used if the server needs the client's IP address for security, accounting, or other purposes, and setting the Use Source IP parameter is not a viable option.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._cip
		except Exception as e:
			raise e

	@cip.setter
	def cip(self, cip) :
		r"""Before forwarding a request to the service, insert an HTTP header with the client's IPv4 or IPv6 address as its value. Used if the server needs the client's IP address for security, accounting, or other purposes, and setting the Use Source IP parameter is not a viable option.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._cip = cip
		except Exception as e:
			raise e

	@property
	def cipheader(self) :
		r"""Name for the HTTP header whose value must be set to the IP address of the client. Used with the Client IP parameter. If you set the Client IP parameter, and you do not specify a name for the header, the appliance uses the header name specified for the global Client IP Header parameter (the cipHeader parameter in the set ns param CLI command or the Client IP Header parameter in the Configure HTTP Parameters dialog box at System > Settings > Change HTTP parameters). If the global Client IP Header parameter is not specified, the appliance inserts a header with the name "client-ip.".<br/>Minimum length =  1.
		"""
		try :
			return self._cipheader
		except Exception as e:
			raise e

	@cipheader.setter
	def cipheader(self, cipheader) :
		r"""Name for the HTTP header whose value must be set to the IP address of the client. Used with the Client IP parameter. If you set the Client IP parameter, and you do not specify a name for the header, the appliance uses the header name specified for the global Client IP Header parameter (the cipHeader parameter in the set ns param CLI command or the Client IP Header parameter in the Configure HTTP Parameters dialog box at System > Settings > Change HTTP parameters). If the global Client IP Header parameter is not specified, the appliance inserts a header with the name "client-ip.".<br/>Minimum length =  1
		"""
		try :
			self._cipheader = cipheader
		except Exception as e:
			raise e

	@property
	def usip(self) :
		r"""Use the client's IP address as the source IP address when initiating a connection to the server. When creating a service, if you do not set this parameter, the service inherits the global Use Source IP setting (available in the enable ns mode and disable ns mode CLI commands, or in the System > Settings > Configure modes > Configure Modes dialog box). However, you can override this setting after you create the service.<br/>Possible values = YES, NO.
		"""
		try :
			return self._usip
		except Exception as e:
			raise e

	@usip.setter
	def usip(self, usip) :
		r"""Use the client's IP address as the source IP address when initiating a connection to the server. When creating a service, if you do not set this parameter, the service inherits the global Use Source IP setting (available in the enable ns mode and disable ns mode CLI commands, or in the System > Settings > Configure modes > Configure Modes dialog box). However, you can override this setting after you create the service.<br/>Possible values = YES, NO
		"""
		try :
			self._usip = usip
		except Exception as e:
			raise e

	@property
	def pathmonitor(self) :
		r"""Path monitoring for clustering.<br/>Possible values = YES, NO.
		"""
		try :
			return self._pathmonitor
		except Exception as e:
			raise e

	@pathmonitor.setter
	def pathmonitor(self, pathmonitor) :
		r"""Path monitoring for clustering.<br/>Possible values = YES, NO
		"""
		try :
			self._pathmonitor = pathmonitor
		except Exception as e:
			raise e

	@property
	def pathmonitorindv(self) :
		r"""Individual Path monitoring decisions.<br/>Possible values = YES, NO.
		"""
		try :
			return self._pathmonitorindv
		except Exception as e:
			raise e

	@pathmonitorindv.setter
	def pathmonitorindv(self, pathmonitorindv) :
		r"""Individual Path monitoring decisions.<br/>Possible values = YES, NO
		"""
		try :
			self._pathmonitorindv = pathmonitorindv
		except Exception as e:
			raise e

	@property
	def useproxyport(self) :
		r"""Use the proxy port as the source port when initiating connections with the server. With the NO setting, the client-side connection port is used as the source port for the server-side connection. 
		Note: This parameter is available only when the Use Source IP (USIP) parameter is set to YES.<br/>Possible values = YES, NO.
		"""
		try :
			return self._useproxyport
		except Exception as e:
			raise e

	@useproxyport.setter
	def useproxyport(self, useproxyport) :
		r"""Use the proxy port as the source port when initiating connections with the server. With the NO setting, the client-side connection port is used as the source port for the server-side connection. 
		Note: This parameter is available only when the Use Source IP (USIP) parameter is set to YES.<br/>Possible values = YES, NO
		"""
		try :
			self._useproxyport = useproxyport
		except Exception as e:
			raise e

	@property
	def sc(self) :
		r"""State of SureConnect for the service.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._sc
		except Exception as e:
			raise e

	@sc.setter
	def sc(self, sc) :
		r"""State of SureConnect for the service.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._sc = sc
		except Exception as e:
			raise e

	@property
	def sp(self) :
		r"""Enable surge protection for the service.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._sp
		except Exception as e:
			raise e

	@sp.setter
	def sp(self, sp) :
		r"""Enable surge protection for the service.<br/>Possible values = ON, OFF
		"""
		try :
			self._sp = sp
		except Exception as e:
			raise e

	@property
	def rtspsessionidremap(self) :
		r"""Enable RTSP session ID mapping for the service.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._rtspsessionidremap
		except Exception as e:
			raise e

	@rtspsessionidremap.setter
	def rtspsessionidremap(self, rtspsessionidremap) :
		r"""Enable RTSP session ID mapping for the service.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._rtspsessionidremap = rtspsessionidremap
		except Exception as e:
			raise e

	@property
	def clttimeout(self) :
		r"""Time, in seconds, after which to terminate an idle client connection.<br/>Maximum length =  31536000.
		"""
		try :
			return self._clttimeout
		except Exception as e:
			raise e

	@clttimeout.setter
	def clttimeout(self, clttimeout) :
		r"""Time, in seconds, after which to terminate an idle client connection.<br/>Maximum length =  31536000
		"""
		try :
			self._clttimeout = clttimeout
		except Exception as e:
			raise e

	@property
	def svrtimeout(self) :
		r"""Time, in seconds, after which to terminate an idle server connection.<br/>Maximum length =  31536000.
		"""
		try :
			return self._svrtimeout
		except Exception as e:
			raise e

	@svrtimeout.setter
	def svrtimeout(self, svrtimeout) :
		r"""Time, in seconds, after which to terminate an idle server connection.<br/>Maximum length =  31536000
		"""
		try :
			self._svrtimeout = svrtimeout
		except Exception as e:
			raise e

	@property
	def customserverid(self) :
		r"""Unique identifier for the service. Used when the persistency type for the virtual server is set to Custom Server ID.<br/>Default value: "None".
		"""
		try :
			return self._customserverid
		except Exception as e:
			raise e

	@customserverid.setter
	def customserverid(self, customserverid) :
		r"""Unique identifier for the service. Used when the persistency type for the virtual server is set to Custom Server ID.<br/>Default value: "None"
		"""
		try :
			self._customserverid = customserverid
		except Exception as e:
			raise e

	@property
	def serverid(self) :
		r"""The  identifier for the service. This is used when the persistency type is set to Custom Server ID.
		"""
		try :
			return self._serverid
		except Exception as e:
			raise e

	@serverid.setter
	def serverid(self, serverid) :
		r"""The  identifier for the service. This is used when the persistency type is set to Custom Server ID.
		"""
		try :
			self._serverid = serverid
		except Exception as e:
			raise e

	@property
	def cka(self) :
		r"""Enable client keep-alive for the service.<br/>Possible values = YES, NO.
		"""
		try :
			return self._cka
		except Exception as e:
			raise e

	@cka.setter
	def cka(self, cka) :
		r"""Enable client keep-alive for the service.<br/>Possible values = YES, NO
		"""
		try :
			self._cka = cka
		except Exception as e:
			raise e

	@property
	def tcpb(self) :
		r"""Enable TCP buffering for the service.<br/>Possible values = YES, NO.
		"""
		try :
			return self._tcpb
		except Exception as e:
			raise e

	@tcpb.setter
	def tcpb(self, tcpb) :
		r"""Enable TCP buffering for the service.<br/>Possible values = YES, NO
		"""
		try :
			self._tcpb = tcpb
		except Exception as e:
			raise e

	@property
	def cmp(self) :
		r"""Enable compression for the service.<br/>Possible values = YES, NO.
		"""
		try :
			return self._cmp
		except Exception as e:
			raise e

	@cmp.setter
	def cmp(self, cmp) :
		r"""Enable compression for the service.<br/>Possible values = YES, NO
		"""
		try :
			self._cmp = cmp
		except Exception as e:
			raise e

	@property
	def maxbandwidth(self) :
		r"""Maximum bandwidth, in Kbps, allocated to the service.<br/>Maximum length =  4294967287.
		"""
		try :
			return self._maxbandwidth
		except Exception as e:
			raise e

	@maxbandwidth.setter
	def maxbandwidth(self, maxbandwidth) :
		r"""Maximum bandwidth, in Kbps, allocated to the service.<br/>Maximum length =  4294967287
		"""
		try :
			self._maxbandwidth = maxbandwidth
		except Exception as e:
			raise e

	@property
	def accessdown(self) :
		r"""Use Layer 2 mode to bridge the packets sent to this service if it is marked as DOWN. If the service is DOWN, and this parameter is disabled, the packets are dropped.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._accessdown
		except Exception as e:
			raise e

	@accessdown.setter
	def accessdown(self, accessdown) :
		r"""Use Layer 2 mode to bridge the packets sent to this service if it is marked as DOWN. If the service is DOWN, and this parameter is disabled, the packets are dropped.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._accessdown = accessdown
		except Exception as e:
			raise e

	@property
	def monthreshold(self) :
		r"""Minimum sum of weights of the monitors that are bound to this service. Used to determine whether to mark a service as UP or DOWN.<br/>Maximum length =  65535.
		"""
		try :
			return self._monthreshold
		except Exception as e:
			raise e

	@monthreshold.setter
	def monthreshold(self, monthreshold) :
		r"""Minimum sum of weights of the monitors that are bound to this service. Used to determine whether to mark a service as UP or DOWN.<br/>Maximum length =  65535
		"""
		try :
			self._monthreshold = monthreshold
		except Exception as e:
			raise e

	@property
	def state(self) :
		r"""Initial state of the service.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@state.setter
	def state(self, state) :
		r"""Initial state of the service.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._state = state
		except Exception as e:
			raise e

	@property
	def downstateflush(self) :
		r"""Flush all active transactions associated with a service whose state transitions from UP to DOWN. Do not enable this option for applications that must complete their transactions.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._downstateflush
		except Exception as e:
			raise e

	@downstateflush.setter
	def downstateflush(self, downstateflush) :
		r"""Flush all active transactions associated with a service whose state transitions from UP to DOWN. Do not enable this option for applications that must complete their transactions.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._downstateflush = downstateflush
		except Exception as e:
			raise e

	@property
	def tcpprofilename(self) :
		r"""Name of the TCP profile that contains TCP configuration settings for the service.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._tcpprofilename
		except Exception as e:
			raise e

	@tcpprofilename.setter
	def tcpprofilename(self, tcpprofilename) :
		r"""Name of the TCP profile that contains TCP configuration settings for the service.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._tcpprofilename = tcpprofilename
		except Exception as e:
			raise e

	@property
	def httpprofilename(self) :
		r"""Name of the HTTP profile that contains HTTP configuration settings for the service.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._httpprofilename
		except Exception as e:
			raise e

	@httpprofilename.setter
	def httpprofilename(self, httpprofilename) :
		r"""Name of the HTTP profile that contains HTTP configuration settings for the service.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._httpprofilename = httpprofilename
		except Exception as e:
			raise e

	@property
	def hashid(self) :
		r"""A numerical identifier that can be used by hash based load balancing methods. Must be unique for each service.<br/>Minimum length =  1.
		"""
		try :
			return self._hashid
		except Exception as e:
			raise e

	@hashid.setter
	def hashid(self, hashid) :
		r"""A numerical identifier that can be used by hash based load balancing methods. Must be unique for each service.<br/>Minimum length =  1
		"""
		try :
			self._hashid = hashid
		except Exception as e:
			raise e

	@property
	def comment(self) :
		r"""Any information about the service.
		"""
		try :
			return self._comment
		except Exception as e:
			raise e

	@comment.setter
	def comment(self, comment) :
		r"""Any information about the service.
		"""
		try :
			self._comment = comment
		except Exception as e:
			raise e

	@property
	def appflowlog(self) :
		r"""Enable logging of AppFlow information.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._appflowlog
		except Exception as e:
			raise e

	@appflowlog.setter
	def appflowlog(self, appflowlog) :
		r"""Enable logging of AppFlow information.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._appflowlog = appflowlog
		except Exception as e:
			raise e

	@property
	def netprofile(self) :
		r"""Network profile to use for the service.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._netprofile
		except Exception as e:
			raise e

	@netprofile.setter
	def netprofile(self, netprofile) :
		r"""Network profile to use for the service.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._netprofile = netprofile
		except Exception as e:
			raise e

	@property
	def td(self) :
		r"""Integer value that uniquely identifies the traffic domain in which you want to configure the entity. If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of 0.<br/>Maximum length =  4094.
		"""
		try :
			return self._td
		except Exception as e:
			raise e

	@td.setter
	def td(self, td) :
		r"""Integer value that uniquely identifies the traffic domain in which you want to configure the entity. If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of 0.<br/>Maximum length =  4094
		"""
		try :
			self._td = td
		except Exception as e:
			raise e

	@property
	def processlocal(self) :
		r"""By turning on this option packets destined to a service in a cluster will not under go any steering. Turn this option for single packet request response mode or when the upstream device is performing a proper RSS for connection based distribution.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._processlocal
		except Exception as e:
			raise e

	@processlocal.setter
	def processlocal(self, processlocal) :
		r"""By turning on this option packets destined to a service in a cluster will not under go any steering. Turn this option for single packet request response mode or when the upstream device is performing a proper RSS for connection based distribution.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._processlocal = processlocal
		except Exception as e:
			raise e

	@property
	def dnsprofilename(self) :
		r"""Name of the DNS profile to be associated with the service. DNS profile properties will applied to the transactions processed by a service. This parameter is valid only for ADNS and ADNS-TCP services.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._dnsprofilename
		except Exception as e:
			raise e

	@dnsprofilename.setter
	def dnsprofilename(self, dnsprofilename) :
		r"""Name of the DNS profile to be associated with the service. DNS profile properties will applied to the transactions processed by a service. This parameter is valid only for ADNS and ADNS-TCP services.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._dnsprofilename = dnsprofilename
		except Exception as e:
			raise e

	@property
	def monconnectionclose(self) :
		r"""Close monitoring connections by sending the service a connection termination message with the specified bit set.<br/>Default value: NONE<br/>Possible values = RESET, FIN.
		"""
		try :
			return self._monconnectionclose
		except Exception as e:
			raise e

	@monconnectionclose.setter
	def monconnectionclose(self, monconnectionclose) :
		r"""Close monitoring connections by sending the service a connection termination message with the specified bit set.<br/>Default value: NONE<br/>Possible values = RESET, FIN
		"""
		try :
			self._monconnectionclose = monconnectionclose
		except Exception as e:
			raise e

	@property
	def ipaddress(self) :
		r"""The new IP address of the service.
		"""
		try :
			return self._ipaddress
		except Exception as e:
			raise e

	@ipaddress.setter
	def ipaddress(self, ipaddress) :
		r"""The new IP address of the service.
		"""
		try :
			self._ipaddress = ipaddress
		except Exception as e:
			raise e

	@property
	def weight(self) :
		r"""Weight to assign to the monitor-service binding. When a monitor is UP, the weight assigned to its binding with the service determines how much the monitor contributes toward keeping the health of the service above the value configured for the Monitor Threshold parameter.<br/>Minimum length =  1<br/>Maximum length =  100.
		"""
		try :
			return self._weight
		except Exception as e:
			raise e

	@weight.setter
	def weight(self, weight) :
		r"""Weight to assign to the monitor-service binding. When a monitor is UP, the weight assigned to its binding with the service determines how much the monitor contributes toward keeping the health of the service above the value configured for the Monitor Threshold parameter.<br/>Minimum length =  1<br/>Maximum length =  100
		"""
		try :
			self._weight = weight
		except Exception as e:
			raise e

	@property
	def monitor_name_svc(self) :
		r"""Name of the monitor bound to the specified service.<br/>Minimum length =  1.
		"""
		try :
			return self._monitor_name_svc
		except Exception as e:
			raise e

	@monitor_name_svc.setter
	def monitor_name_svc(self, monitor_name_svc) :
		r"""Name of the monitor bound to the specified service.<br/>Minimum length =  1
		"""
		try :
			self._monitor_name_svc = monitor_name_svc
		except Exception as e:
			raise e

	@property
	def riseapbrstatsmsgcode(self) :
		r"""The code indicating the rise apbr status.
		"""
		try :
			return self._riseapbrstatsmsgcode
		except Exception as e:
			raise e

	@riseapbrstatsmsgcode.setter
	def riseapbrstatsmsgcode(self, riseapbrstatsmsgcode) :
		r"""The code indicating the rise apbr status.
		"""
		try :
			self._riseapbrstatsmsgcode = riseapbrstatsmsgcode
		except Exception as e:
			raise e

	@property
	def delay(self) :
		r"""Time, in seconds, allocated to the NetScaler appliance for a graceful shutdown of the service. During this period, new requests are sent to the service only for clients who already have persistent sessions on the appliance. Requests from new clients are load balanced among other available services. After the delay time expires, no requests are sent to the service, and the service is marked as unavailable (OUT OF SERVICE).
		"""
		try :
			return self._delay
		except Exception as e:
			raise e

	@delay.setter
	def delay(self, delay) :
		r"""Time, in seconds, allocated to the NetScaler appliance for a graceful shutdown of the service. During this period, new requests are sent to the service only for clients who already have persistent sessions on the appliance. Requests from new clients are load balanced among other available services. After the delay time expires, no requests are sent to the service, and the service is marked as unavailable (OUT OF SERVICE).
		"""
		try :
			self._delay = delay
		except Exception as e:
			raise e

	@property
	def graceful(self) :
		r"""Shut down gracefully, not accepting any new connections, and disabling the service when all of its connections are closed.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._graceful
		except Exception as e:
			raise e

	@graceful.setter
	def graceful(self, graceful) :
		r"""Shut down gracefully, not accepting any new connections, and disabling the service when all of its connections are closed.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._graceful = graceful
		except Exception as e:
			raise e

	@property
	def all(self) :
		r"""Display both user-configured and dynamically learned services.
		"""
		try :
			return self._all
		except Exception as e:
			raise e

	@all.setter
	def all(self, all) :
		r"""Display both user-configured and dynamically learned services.
		"""
		try :
			self._all = all
		except Exception as e:
			raise e

	@property
	def Internal(self) :
		r"""Display only dynamically learned services.
		"""
		try :
			return self._Internal
		except Exception as e:
			raise e

	@Internal.setter
	def Internal(self, Internal) :
		r"""Display only dynamically learned services.
		"""
		try :
			self._Internal = Internal
		except Exception as e:
			raise e

	@property
	def newname(self) :
		r"""New name for the service. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.<br/>Minimum length =  1.
		"""
		try :
			return self._newname
		except Exception as e:
			raise e

	@newname.setter
	def newname(self, newname) :
		r"""New name for the service. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.<br/>Minimum length =  1
		"""
		try :
			self._newname = newname
		except Exception as e:
			raise e

	@property
	def numofconnections(self) :
		r"""This will tell the number of client side connections are still open.
		"""
		try :
			return self._numofconnections
		except Exception as e:
			raise e

	@property
	def policyname(self) :
		r"""The name of the policyname for which this service is bound.
		"""
		try :
			return self._policyname
		except Exception as e:
			raise e

	@property
	def serviceconftype(self) :
		r"""The configuration type of the service.
		"""
		try :
			return self._serviceconftype
		except Exception as e:
			raise e

	@property
	def serviceconftype2(self) :
		r"""The configuration type of the service (Internal/Dynamic/Configured).<br/>Possible values = Configured, Dynamic, Internal.
		"""
		try :
			return self._serviceconftype2
		except Exception as e:
			raise e

	@property
	def value(self) :
		r"""SSL status.<br/>Possible values = Certkey not bound, SSL feature disabled.
		"""
		try :
			return self._value
		except Exception as e:
			raise e

	@property
	def gslb(self) :
		r"""The GSLB option for the corresponding virtual server.<br/>Possible values = REMOTE, LOCAL.
		"""
		try :
			return self._gslb
		except Exception as e:
			raise e

	@property
	def dup_state(self) :
		r"""Added this field for getting state value from table.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._dup_state
		except Exception as e:
			raise e

	@property
	def publicip(self) :
		r"""public ip.
		"""
		try :
			return self._publicip
		except Exception as e:
			raise e

	@property
	def publicport(self) :
		r"""public port.<br/>Minimum value =  1<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API.
		"""
		try :
			return self._publicport
		except Exception as e:
			raise e

	@property
	def svrstate(self) :
		r"""The state of the service.<br/>Possible values = UP, DOWN, UNKNOWN, BUSY, OUT OF SERVICE, GOING OUT OF SERVICE, DOWN WHEN GOING OUT OF SERVICE, NS_EMPTY_STR, Unknown, DISABLED.
		"""
		try :
			return self._svrstate
		except Exception as e:
			raise e

	@property
	def monitor_state(self) :
		r"""The running state of the monitor on this service.<br/>Possible values = UP, DOWN, UNKNOWN, BUSY, OUT OF SERVICE, GOING OUT OF SERVICE, DOWN WHEN GOING OUT OF SERVICE, NS_EMPTY_STR, Unknown, DISABLED.
		"""
		try :
			return self._monitor_state
		except Exception as e:
			raise e

	@property
	def monstatcode(self) :
		r"""The code indicating the monitor response.
		"""
		try :
			return self._monstatcode
		except Exception as e:
			raise e

	@property
	def lastresponse(self) :
		r"""The string form of monstatcode.
		"""
		try :
			return self._lastresponse
		except Exception as e:
			raise e

	@property
	def responsetime(self) :
		r"""Response time of this monitor.
		"""
		try :
			return self._responsetime
		except Exception as e:
			raise e

	@property
	def riseapbrstatsmsgcode2(self) :
		r"""The code indicating other rise stats.
		"""
		try :
			return self._riseapbrstatsmsgcode2
		except Exception as e:
			raise e

	@property
	def monstatparam1(self) :
		r"""First parameter for use with message code.
		"""
		try :
			return self._monstatparam1
		except Exception as e:
			raise e

	@property
	def monstatparam2(self) :
		r"""Second parameter for use with message code.
		"""
		try :
			return self._monstatparam2
		except Exception as e:
			raise e

	@property
	def monstatparam3(self) :
		r"""Third parameter for use with message code.
		"""
		try :
			return self._monstatparam3
		except Exception as e:
			raise e

	@property
	def statechangetimesec(self) :
		r"""Time when last state change happened. Seconds part.
		"""
		try :
			return self._statechangetimesec
		except Exception as e:
			raise e

	@property
	def statechangetimemsec(self) :
		r"""Time at which last state change happened. Milliseconds part.
		"""
		try :
			return self._statechangetimemsec
		except Exception as e:
			raise e

	@property
	def tickssincelaststatechange(self) :
		r"""Time in 10 millisecond ticks since the last state change.
		"""
		try :
			return self._tickssincelaststatechange
		except Exception as e:
			raise e

	@property
	def stateupdatereason(self) :
		r"""Checks state update reason on the secondary node.
		"""
		try :
			return self._stateupdatereason
		except Exception as e:
			raise e

	@property
	def clmonowner(self) :
		r"""Tells the mon owner of the service.<br/>Minimum value =  0<br/>Maximum value =  32.
		"""
		try :
			return self._clmonowner
		except Exception as e:
			raise e

	@property
	def clmonview(self) :
		r"""Tells the view id of the monitoring owner.
		"""
		try :
			return self._clmonview
		except Exception as e:
			raise e

	@property
	def serviceipstr(self) :
		r"""This field has been intorduced to show the dbs services ip.
		"""
		try :
			return self._serviceipstr
		except Exception as e:
			raise e

	@property
	def oracleserverversion(self) :
		r"""Oracle server version.<br/>Default value: 10G<br/>Possible values = 10G, 11G.
		"""
		try :
			return self._oracleserverversion
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(service_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.service
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.name is not None :
				return str(self.name)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add service.
		"""
		try :
			if type(resource) is not list :
				addresource = service()
				addresource.name = resource.name
				addresource.ip = resource.ip
				addresource.servername = resource.servername
				addresource.servicetype = resource.servicetype
				addresource.port = resource.port
				addresource.cleartextport = resource.cleartextport
				addresource.cachetype = resource.cachetype
				addresource.maxclient = resource.maxclient
				addresource.healthmonitor = resource.healthmonitor
				addresource.maxreq = resource.maxreq
				addresource.cacheable = resource.cacheable
				addresource.cip = resource.cip
				addresource.cipheader = resource.cipheader
				addresource.usip = resource.usip
				addresource.pathmonitor = resource.pathmonitor
				addresource.pathmonitorindv = resource.pathmonitorindv
				addresource.useproxyport = resource.useproxyport
				addresource.sc = resource.sc
				addresource.sp = resource.sp
				addresource.rtspsessionidremap = resource.rtspsessionidremap
				addresource.clttimeout = resource.clttimeout
				addresource.svrtimeout = resource.svrtimeout
				addresource.customserverid = resource.customserverid
				addresource.serverid = resource.serverid
				addresource.cka = resource.cka
				addresource.tcpb = resource.tcpb
				addresource.cmp = resource.cmp
				addresource.maxbandwidth = resource.maxbandwidth
				addresource.accessdown = resource.accessdown
				addresource.monthreshold = resource.monthreshold
				addresource.state = resource.state
				addresource.downstateflush = resource.downstateflush
				addresource.tcpprofilename = resource.tcpprofilename
				addresource.httpprofilename = resource.httpprofilename
				addresource.hashid = resource.hashid
				addresource.comment = resource.comment
				addresource.appflowlog = resource.appflowlog
				addresource.netprofile = resource.netprofile
				addresource.td = resource.td
				addresource.processlocal = resource.processlocal
				addresource.dnsprofilename = resource.dnsprofilename
				addresource.monconnectionclose = resource.monconnectionclose
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ service() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].ip = resource[i].ip
						addresources[i].servername = resource[i].servername
						addresources[i].servicetype = resource[i].servicetype
						addresources[i].port = resource[i].port
						addresources[i].cleartextport = resource[i].cleartextport
						addresources[i].cachetype = resource[i].cachetype
						addresources[i].maxclient = resource[i].maxclient
						addresources[i].healthmonitor = resource[i].healthmonitor
						addresources[i].maxreq = resource[i].maxreq
						addresources[i].cacheable = resource[i].cacheable
						addresources[i].cip = resource[i].cip
						addresources[i].cipheader = resource[i].cipheader
						addresources[i].usip = resource[i].usip
						addresources[i].pathmonitor = resource[i].pathmonitor
						addresources[i].pathmonitorindv = resource[i].pathmonitorindv
						addresources[i].useproxyport = resource[i].useproxyport
						addresources[i].sc = resource[i].sc
						addresources[i].sp = resource[i].sp
						addresources[i].rtspsessionidremap = resource[i].rtspsessionidremap
						addresources[i].clttimeout = resource[i].clttimeout
						addresources[i].svrtimeout = resource[i].svrtimeout
						addresources[i].customserverid = resource[i].customserverid
						addresources[i].serverid = resource[i].serverid
						addresources[i].cka = resource[i].cka
						addresources[i].tcpb = resource[i].tcpb
						addresources[i].cmp = resource[i].cmp
						addresources[i].maxbandwidth = resource[i].maxbandwidth
						addresources[i].accessdown = resource[i].accessdown
						addresources[i].monthreshold = resource[i].monthreshold
						addresources[i].state = resource[i].state
						addresources[i].downstateflush = resource[i].downstateflush
						addresources[i].tcpprofilename = resource[i].tcpprofilename
						addresources[i].httpprofilename = resource[i].httpprofilename
						addresources[i].hashid = resource[i].hashid
						addresources[i].comment = resource[i].comment
						addresources[i].appflowlog = resource[i].appflowlog
						addresources[i].netprofile = resource[i].netprofile
						addresources[i].td = resource[i].td
						addresources[i].processlocal = resource[i].processlocal
						addresources[i].dnsprofilename = resource[i].dnsprofilename
						addresources[i].monconnectionclose = resource[i].monconnectionclose
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete service.
		"""
		try :
			if type(resource) is not list :
				deleteresource = service()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ service() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ service() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update service.
		"""
		try :
			if type(resource) is not list :
				updateresource = service()
				updateresource.name = resource.name
				updateresource.ipaddress = resource.ipaddress
				updateresource.maxclient = resource.maxclient
				updateresource.maxreq = resource.maxreq
				updateresource.cacheable = resource.cacheable
				updateresource.cip = resource.cip
				updateresource.cipheader = resource.cipheader
				updateresource.usip = resource.usip
				updateresource.pathmonitor = resource.pathmonitor
				updateresource.pathmonitorindv = resource.pathmonitorindv
				updateresource.useproxyport = resource.useproxyport
				updateresource.sc = resource.sc
				updateresource.sp = resource.sp
				updateresource.rtspsessionidremap = resource.rtspsessionidremap
				updateresource.healthmonitor = resource.healthmonitor
				updateresource.clttimeout = resource.clttimeout
				updateresource.svrtimeout = resource.svrtimeout
				updateresource.customserverid = resource.customserverid
				updateresource.serverid = resource.serverid
				updateresource.cka = resource.cka
				updateresource.tcpb = resource.tcpb
				updateresource.cmp = resource.cmp
				updateresource.maxbandwidth = resource.maxbandwidth
				updateresource.accessdown = resource.accessdown
				updateresource.monthreshold = resource.monthreshold
				updateresource.weight = resource.weight
				updateresource.monitor_name_svc = resource.monitor_name_svc
				updateresource.downstateflush = resource.downstateflush
				updateresource.tcpprofilename = resource.tcpprofilename
				updateresource.httpprofilename = resource.httpprofilename
				updateresource.hashid = resource.hashid
				updateresource.comment = resource.comment
				updateresource.appflowlog = resource.appflowlog
				updateresource.netprofile = resource.netprofile
				updateresource.processlocal = resource.processlocal
				updateresource.dnsprofilename = resource.dnsprofilename
				updateresource.monconnectionclose = resource.monconnectionclose
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ service() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].ipaddress = resource[i].ipaddress
						updateresources[i].maxclient = resource[i].maxclient
						updateresources[i].maxreq = resource[i].maxreq
						updateresources[i].cacheable = resource[i].cacheable
						updateresources[i].cip = resource[i].cip
						updateresources[i].cipheader = resource[i].cipheader
						updateresources[i].usip = resource[i].usip
						updateresources[i].pathmonitor = resource[i].pathmonitor
						updateresources[i].pathmonitorindv = resource[i].pathmonitorindv
						updateresources[i].useproxyport = resource[i].useproxyport
						updateresources[i].sc = resource[i].sc
						updateresources[i].sp = resource[i].sp
						updateresources[i].rtspsessionidremap = resource[i].rtspsessionidremap
						updateresources[i].healthmonitor = resource[i].healthmonitor
						updateresources[i].clttimeout = resource[i].clttimeout
						updateresources[i].svrtimeout = resource[i].svrtimeout
						updateresources[i].customserverid = resource[i].customserverid
						updateresources[i].serverid = resource[i].serverid
						updateresources[i].cka = resource[i].cka
						updateresources[i].tcpb = resource[i].tcpb
						updateresources[i].cmp = resource[i].cmp
						updateresources[i].maxbandwidth = resource[i].maxbandwidth
						updateresources[i].accessdown = resource[i].accessdown
						updateresources[i].monthreshold = resource[i].monthreshold
						updateresources[i].weight = resource[i].weight
						updateresources[i].monitor_name_svc = resource[i].monitor_name_svc
						updateresources[i].downstateflush = resource[i].downstateflush
						updateresources[i].tcpprofilename = resource[i].tcpprofilename
						updateresources[i].httpprofilename = resource[i].httpprofilename
						updateresources[i].hashid = resource[i].hashid
						updateresources[i].comment = resource[i].comment
						updateresources[i].appflowlog = resource[i].appflowlog
						updateresources[i].netprofile = resource[i].netprofile
						updateresources[i].processlocal = resource[i].processlocal
						updateresources[i].dnsprofilename = resource[i].dnsprofilename
						updateresources[i].monconnectionclose = resource[i].monconnectionclose
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of service resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = service()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ service() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ service() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def enable(cls, client, resource) :
		r""" Use this API to enable service.
		"""
		try :
			if type(resource) is not list :
				enableresource = service()
				if type(resource) !=  type(enableresource):
					enableresource.name = resource
				else :
					enableresource.name = resource.name
				return enableresource.perform_operation(client,"enable")
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						enableresources = [ service() for _ in range(len(resource))]
						for i in range(len(resource)) :
							enableresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						enableresources = [ service() for _ in range(len(resource))]
						for i in range(len(resource)) :
							enableresources[i].name = resource[i].name
				result = cls.perform_operation_bulk_request(client, enableresources,"enable")
			return result
		except Exception as e :
			raise e

	@classmethod
	def disable(cls, client, resource) :
		r""" Use this API to disable service.
		"""
		try :
			if type(resource) is not list :
				disableresource = service()
				if type(resource) !=  type(disableresource):
					disableresource.name = resource
				else :
					disableresource.name = resource.name
					disableresource.delay = resource.delay
					disableresource.graceful = resource.graceful
				return disableresource.perform_operation(client,"disable")
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						disableresources = [ service() for _ in range(len(resource))]
						for i in range(len(resource)) :
							disableresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						disableresources = [ service() for _ in range(len(resource))]
						for i in range(len(resource)) :
							disableresources[i].name = resource[i].name
							disableresources[i].delay = resource[i].delay
							disableresources[i].graceful = resource[i].graceful
				result = cls.perform_operation_bulk_request(client, disableresources,"disable")
			return result
		except Exception as e :
			raise e

	@classmethod
	def rename(cls, client, resource, new_name) :
		r""" Use this API to rename a service resource.
		"""
		try :
			renameresource = service()
			if type(resource) == cls :
				renameresource.name = resource.name
			else :
				renameresource.name = resource
			return renameresource.rename_resource(client,new_name)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the service resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = service()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = service()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [service() for _ in range(len(name))]
						obj = [service() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = service()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		r""" Use this API to fetch all the service resources that are configured on netscaler.
	# This uses service_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = service()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of service resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = service()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the service resources configured on NetScaler.
		"""
		try :
			obj = service()
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
		r""" Use this API to count filtered the set of service resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = service()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Sp:
		ON = "ON"
		OFF = "OFF"

	class Oracleserverversion:
		_10G = "10G"
		_11G = "11G"

	class Sc:
		ON = "ON"
		OFF = "OFF"

	class State:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Cachetype:
		TRANSPARENT = "TRANSPARENT"
		REVERSE = "REVERSE"
		FORWARD = "FORWARD"

	class Downstateflush:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Servicetype:
		HTTP = "HTTP"
		FTP = "FTP"
		TCP = "TCP"
		UDP = "UDP"
		SSL = "SSL"
		SSL_BRIDGE = "SSL_BRIDGE"
		SSL_TCP = "SSL_TCP"
		DTLS = "DTLS"
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
		MYSQL = "MYSQL"
		MSSQL = "MSSQL"
		ORACLE = "ORACLE"
		RADIUS = "RADIUS"
		RADIUSListener = "RADIUSListener"
		RDP = "RDP"
		DIAMETER = "DIAMETER"
		SSL_DIAMETER = "SSL_DIAMETER"
		TFTP = "TFTP"
		SMPP = "SMPP"
		PPTP = "PPTP"
		GRE = "GRE"
		SYSLOGTCP = "SYSLOGTCP"
		SYSLOGUDP = "SYSLOGUDP"
		FIX = "FIX"
		SSL_FIX = "SSL_FIX"
		USER_TCP = "USER_TCP"
		USER_SSL_TCP = "USER_SSL_TCP"

	class Svrstate:
		UP = "UP"
		DOWN = "DOWN"
		UNKNOWN = "UNKNOWN"
		BUSY = "BUSY"
		OUT_OF_SERVICE = "OUT OF SERVICE"
		GOING_OUT_OF_SERVICE = "GOING OUT OF SERVICE"
		DOWN_WHEN_GOING_OUT_OF_SERVICE = "DOWN WHEN GOING OUT OF SERVICE"
		NS_EMPTY_STR = "NS_EMPTY_STR"
		Unknown = "Unknown"
		DISABLED = "DISABLED"

	class Monitor_state:
		UP = "UP"
		DOWN = "DOWN"
		UNKNOWN = "UNKNOWN"
		BUSY = "BUSY"
		OUT_OF_SERVICE = "OUT OF SERVICE"
		GOING_OUT_OF_SERVICE = "GOING OUT OF SERVICE"
		DOWN_WHEN_GOING_OUT_OF_SERVICE = "DOWN WHEN GOING OUT OF SERVICE"
		NS_EMPTY_STR = "NS_EMPTY_STR"
		Unknown = "Unknown"
		DISABLED = "DISABLED"

	class Value:
		Certkey_not_bound = "Certkey not bound"
		SSL_feature_disabled = "SSL feature disabled"

	class Useproxyport:
		YES = "YES"
		NO = "NO"

	class Gslb:
		REMOTE = "REMOTE"
		LOCAL = "LOCAL"

	class Usip:
		YES = "YES"
		NO = "NO"

	class Cacheable:
		YES = "YES"
		NO = "NO"

	class Monconnectionclose:
		RESET = "RESET"
		FIN = "FIN"

	class Serviceconftype2:
		Configured = "Configured"
		Dynamic = "Dynamic"
		Internal = "Internal"

	class Processlocal:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Pathmonitor:
		YES = "YES"
		NO = "NO"

	class Tcpb:
		YES = "YES"
		NO = "NO"

	class Cip:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Pathmonitorindv:
		YES = "YES"
		NO = "NO"

	class Healthmonitor:
		YES = "YES"
		NO = "NO"

	class Cka:
		YES = "YES"
		NO = "NO"

	class Appflowlog:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Dup_state:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Accessdown:
		YES = "YES"
		NO = "NO"

	class Cmp:
		YES = "YES"
		NO = "NO"

	class Rtspsessionidremap:
		ON = "ON"
		OFF = "OFF"

	class Graceful:
		YES = "YES"
		NO = "NO"

class service_response(base_response) :
	def __init__(self, length=1) :
		self.service = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.service = [service() for _ in range(length)]

