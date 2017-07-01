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

class nsip6(base_resource) :
	""" Configuration for ip6 resource. """
	def __init__(self) :
		self._ipv6address = None
		self._scope = None
		self._type = None
		self._vlan = None
		self._nd = None
		self._icmp = None
		self._vserver = None
		self._telnet = None
		self._ftp = None
		self._gui = None
		self._ssh = None
		self._snmp = None
		self._mgmtaccess = None
		self._restrictaccess = None
		self._dynamicrouting = None
		self._hostroute = None
		self._networkroute = None
		self._tag = None
		self._ip6hostrtgw = None
		self._metric = None
		self._vserverrhilevel = None
		self._ospf6lsatype = None
		self._ospfarea = None
		self._state = None
		self._map = None
		self._vrid6 = None
		self._ownernode = None
		self._ownerdownresponse = None
		self._td = None
		self._iptype = []
		self._curstate = None
		self._viprtadv2bsd = None
		self._vipvsercount = None
		self._vipvserdowncount = None
		self._systemtype = None
		self.___count = 0

	@property
	def ipv6address(self) :
		r"""IPv6 address to create on the NetScaler appliance.<br/>Minimum length =  1.
		"""
		try :
			return self._ipv6address
		except Exception as e:
			raise e

	@ipv6address.setter
	def ipv6address(self, ipv6address) :
		r"""IPv6 address to create on the NetScaler appliance.<br/>Minimum length =  1
		"""
		try :
			self._ipv6address = ipv6address
		except Exception as e:
			raise e

	@property
	def scope(self) :
		r"""Scope of the IPv6 address to be created. Cannot be changed after the IP address is created.<br/>Default value: global<br/>Possible values = global, link-local.
		"""
		try :
			return self._scope
		except Exception as e:
			raise e

	@scope.setter
	def scope(self, scope) :
		r"""Scope of the IPv6 address to be created. Cannot be changed after the IP address is created.<br/>Default value: global<br/>Possible values = global, link-local
		"""
		try :
			self._scope = scope
		except Exception as e:
			raise e

	@property
	def type(self) :
		r"""Type of IP address to be created on the NetScaler appliance. Cannot be changed after the IP address is created.<br/>Default value: SNIP<br/>Possible values = NSIP, VIP, SNIP, GSLBsiteIP, ADNSsvcIP, RADIUSListenersvcIP, CLIP.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@type.setter
	def type(self, type) :
		r"""Type of IP address to be created on the NetScaler appliance. Cannot be changed after the IP address is created.<br/>Default value: SNIP<br/>Possible values = NSIP, VIP, SNIP, GSLBsiteIP, ADNSsvcIP, RADIUSListenersvcIP, CLIP
		"""
		try :
			self._type = type
		except Exception as e:
			raise e

	@property
	def vlan(self) :
		r"""The VLAN number.<br/>Default value: 0<br/>Maximum length =  4094.
		"""
		try :
			return self._vlan
		except Exception as e:
			raise e

	@vlan.setter
	def vlan(self, vlan) :
		r"""The VLAN number.<br/>Default value: 0<br/>Maximum length =  4094
		"""
		try :
			self._vlan = vlan
		except Exception as e:
			raise e

	@property
	def nd(self) :
		r"""Respond to Neighbor Discovery (ND) requests for this IP address.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._nd
		except Exception as e:
			raise e

	@nd.setter
	def nd(self, nd) :
		r"""Respond to Neighbor Discovery (ND) requests for this IP address.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._nd = nd
		except Exception as e:
			raise e

	@property
	def icmp(self) :
		r"""Respond to ICMP requests for this IP address.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._icmp
		except Exception as e:
			raise e

	@icmp.setter
	def icmp(self, icmp) :
		r"""Respond to ICMP requests for this IP address.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._icmp = icmp
		except Exception as e:
			raise e

	@property
	def vserver(self) :
		r"""Enable or disable the state of all the virtual servers associated with this VIP6 address.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._vserver
		except Exception as e:
			raise e

	@vserver.setter
	def vserver(self, vserver) :
		r"""Enable or disable the state of all the virtual servers associated with this VIP6 address.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._vserver = vserver
		except Exception as e:
			raise e

	@property
	def telnet(self) :
		r"""Allow Telnet access to this IP address.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._telnet
		except Exception as e:
			raise e

	@telnet.setter
	def telnet(self, telnet) :
		r"""Allow Telnet access to this IP address.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._telnet = telnet
		except Exception as e:
			raise e

	@property
	def ftp(self) :
		r"""Allow File Transfer Protocol (FTP) access to this IP address.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._ftp
		except Exception as e:
			raise e

	@ftp.setter
	def ftp(self, ftp) :
		r"""Allow File Transfer Protocol (FTP) access to this IP address.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._ftp = ftp
		except Exception as e:
			raise e

	@property
	def gui(self) :
		r"""Allow graphical user interface (GUI) access to this IP address.<br/>Default value: ENABLED<br/>Possible values = ENABLED, SECUREONLY, DISABLED.
		"""
		try :
			return self._gui
		except Exception as e:
			raise e

	@gui.setter
	def gui(self, gui) :
		r"""Allow graphical user interface (GUI) access to this IP address.<br/>Default value: ENABLED<br/>Possible values = ENABLED, SECUREONLY, DISABLED
		"""
		try :
			self._gui = gui
		except Exception as e:
			raise e

	@property
	def ssh(self) :
		r"""Allow secure Shell (SSH) access to this IP address.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._ssh
		except Exception as e:
			raise e

	@ssh.setter
	def ssh(self, ssh) :
		r"""Allow secure Shell (SSH) access to this IP address.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._ssh = ssh
		except Exception as e:
			raise e

	@property
	def snmp(self) :
		r"""Allow Simple Network Management Protocol (SNMP) access to this IP address.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._snmp
		except Exception as e:
			raise e

	@snmp.setter
	def snmp(self, snmp) :
		r"""Allow Simple Network Management Protocol (SNMP) access to this IP address.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._snmp = snmp
		except Exception as e:
			raise e

	@property
	def mgmtaccess(self) :
		r"""Allow access to management applications on this IP address.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._mgmtaccess
		except Exception as e:
			raise e

	@mgmtaccess.setter
	def mgmtaccess(self, mgmtaccess) :
		r"""Allow access to management applications on this IP address.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._mgmtaccess = mgmtaccess
		except Exception as e:
			raise e

	@property
	def restrictaccess(self) :
		r"""Block access to nonmanagement applications on this IP address. This option is applicable forMIP6s, SNIP6s, and NSIP6s, and is disabled by default. Nonmanagement applications can run on the underlying NetScaler Free BSD operating system.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._restrictaccess
		except Exception as e:
			raise e

	@restrictaccess.setter
	def restrictaccess(self, restrictaccess) :
		r"""Block access to nonmanagement applications on this IP address. This option is applicable forMIP6s, SNIP6s, and NSIP6s, and is disabled by default. Nonmanagement applications can run on the underlying NetScaler Free BSD operating system.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._restrictaccess = restrictaccess
		except Exception as e:
			raise e

	@property
	def dynamicrouting(self) :
		r"""Allow dynamic routing on this IP address. Specific to Subnet IPv6 (SNIP6) address.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._dynamicrouting
		except Exception as e:
			raise e

	@dynamicrouting.setter
	def dynamicrouting(self, dynamicrouting) :
		r"""Allow dynamic routing on this IP address. Specific to Subnet IPv6 (SNIP6) address.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._dynamicrouting = dynamicrouting
		except Exception as e:
			raise e

	@property
	def hostroute(self) :
		r"""Option to push the VIP6 to ZebOS routing table for Kernel route redistribution through dynamic routing protocols.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._hostroute
		except Exception as e:
			raise e

	@hostroute.setter
	def hostroute(self, hostroute) :
		r"""Option to push the VIP6 to ZebOS routing table for Kernel route redistribution through dynamic routing protocols.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._hostroute = hostroute
		except Exception as e:
			raise e

	@property
	def networkroute(self) :
		r"""Option to push the SNIP6 subnet to ZebOS routing table for Kernel route redistribution through dynamic routing protocol.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._networkroute
		except Exception as e:
			raise e

	@networkroute.setter
	def networkroute(self, networkroute) :
		r"""Option to push the SNIP6 subnet to ZebOS routing table for Kernel route redistribution through dynamic routing protocol.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._networkroute = networkroute
		except Exception as e:
			raise e

	@property
	def tag(self) :
		r"""Tag value for the network/host route associated with this IP.<br/>Default value: 0.
		"""
		try :
			return self._tag
		except Exception as e:
			raise e

	@tag.setter
	def tag(self, tag) :
		r"""Tag value for the network/host route associated with this IP.<br/>Default value: 0
		"""
		try :
			self._tag = tag
		except Exception as e:
			raise e

	@property
	def ip6hostrtgw(self) :
		r"""IPv6 address of the gateway for the route. If Gateway is not set, VIP uses :: as the gateway.<br/>Default value: 0.
		"""
		try :
			return self._ip6hostrtgw
		except Exception as e:
			raise e

	@ip6hostrtgw.setter
	def ip6hostrtgw(self, ip6hostrtgw) :
		r"""IPv6 address of the gateway for the route. If Gateway is not set, VIP uses :: as the gateway.<br/>Default value: 0
		"""
		try :
			self._ip6hostrtgw = ip6hostrtgw
		except Exception as e:
			raise e

	@property
	def metric(self) :
		r"""Integer value to add to or subtract from the cost of the route advertised for the VIP6 address.<br/>Minimum length =  -16777215.
		"""
		try :
			return self._metric
		except Exception as e:
			raise e

	@metric.setter
	def metric(self, metric) :
		r"""Integer value to add to or subtract from the cost of the route advertised for the VIP6 address.<br/>Minimum length =  -16777215
		"""
		try :
			self._metric = metric
		except Exception as e:
			raise e

	@property
	def vserverrhilevel(self) :
		r"""Advertise or do not advertise the route for the Virtual IP (VIP6) address on the basis of the state of the virtual servers associated with that VIP6.
		* NONE - Advertise the route for the VIP6 address, irrespective of the state of the virtual servers associated with the address.
		* ONE VSERVER - Advertise the route for the VIP6 address if at least one of the associated virtual servers is in UP state.
		* ALL VSERVER - Advertise the route for the VIP6 address if all of the associated virtual servers are in UP state.
		* VSVR_CNTRLD.   Advertise the route for the VIP address according to the  RHIstate (RHI STATE) parameter setting on all the associated virtual servers of the VIP address along with their states.
		When Vserver RHI Level (RHI) parameter is set to VSVR_CNTRLD, the following are different RHI behaviors for the VIP address on the basis of RHIstate (RHI STATE) settings on the virtual servers associated with the VIP address:
		* If you set RHI STATE to PASSIVE on all virtual servers, the NetScaler ADC always advertises the route for the VIP address.
		* If you set RHI STATE to ACTIVE on all virtual servers, the NetScaler ADC advertises the route for the VIP address if at least one of the associated virtual servers is in UP state.
		*If you set RHI STATE to ACTIVE on some and PASSIVE on others, the NetScaler ADC advertises the route for the VIP address if at least one of the associated virtual servers, whose RHI STATE set to ACTIVE, is in UP state.<br/>Default value: ONE_VSERVER<br/>Possible values = ONE_VSERVER, ALL_VSERVERS, NONE, VSVR_CNTRLD.
		"""
		try :
			return self._vserverrhilevel
		except Exception as e:
			raise e

	@vserverrhilevel.setter
	def vserverrhilevel(self, vserverrhilevel) :
		r"""Advertise or do not advertise the route for the Virtual IP (VIP6) address on the basis of the state of the virtual servers associated with that VIP6.
		* NONE - Advertise the route for the VIP6 address, irrespective of the state of the virtual servers associated with the address.
		* ONE VSERVER - Advertise the route for the VIP6 address if at least one of the associated virtual servers is in UP state.
		* ALL VSERVER - Advertise the route for the VIP6 address if all of the associated virtual servers are in UP state.
		* VSVR_CNTRLD.   Advertise the route for the VIP address according to the  RHIstate (RHI STATE) parameter setting on all the associated virtual servers of the VIP address along with their states.
		When Vserver RHI Level (RHI) parameter is set to VSVR_CNTRLD, the following are different RHI behaviors for the VIP address on the basis of RHIstate (RHI STATE) settings on the virtual servers associated with the VIP address:
		* If you set RHI STATE to PASSIVE on all virtual servers, the NetScaler ADC always advertises the route for the VIP address.
		* If you set RHI STATE to ACTIVE on all virtual servers, the NetScaler ADC advertises the route for the VIP address if at least one of the associated virtual servers is in UP state.
		*If you set RHI STATE to ACTIVE on some and PASSIVE on others, the NetScaler ADC advertises the route for the VIP address if at least one of the associated virtual servers, whose RHI STATE set to ACTIVE, is in UP state.<br/>Default value: ONE_VSERVER<br/>Possible values = ONE_VSERVER, ALL_VSERVERS, NONE, VSVR_CNTRLD
		"""
		try :
			self._vserverrhilevel = vserverrhilevel
		except Exception as e:
			raise e

	@property
	def ospf6lsatype(self) :
		r"""Type of LSAs to be used by the IPv6 OSPF protocol, running on the NetScaler appliance, for advertising the route for the VIP6 address.<br/>Default value: EXTERNAL<br/>Possible values = INTRA_AREA, EXTERNAL.
		"""
		try :
			return self._ospf6lsatype
		except Exception as e:
			raise e

	@ospf6lsatype.setter
	def ospf6lsatype(self, ospf6lsatype) :
		r"""Type of LSAs to be used by the IPv6 OSPF protocol, running on the NetScaler appliance, for advertising the route for the VIP6 address.<br/>Default value: EXTERNAL<br/>Possible values = INTRA_AREA, EXTERNAL
		"""
		try :
			self._ospf6lsatype = ospf6lsatype
		except Exception as e:
			raise e

	@property
	def ospfarea(self) :
		r"""ID of the area in which the Intra-Area-Prefix LSAs are to be advertised for the VIP6 address by the IPv6 OSPF protocol running on the NetScaler appliance. When ospfArea is not set, VIP6 is advertised on all areas.<br/>Default value: -1<br/>Maximum length =  4294967294LU.
		"""
		try :
			return self._ospfarea
		except Exception as e:
			raise e

	@ospfarea.setter
	def ospfarea(self, ospfarea) :
		r"""ID of the area in which the Intra-Area-Prefix LSAs are to be advertised for the VIP6 address by the IPv6 OSPF protocol running on the NetScaler appliance. When ospfArea is not set, VIP6 is advertised on all areas.<br/>Default value: -1<br/>Maximum length =  4294967294LU
		"""
		try :
			self._ospfarea = ospfarea
		except Exception as e:
			raise e

	@property
	def state(self) :
		r"""Enable or disable the IP address.<br/>Default value: ENABLED<br/>Possible values = DISABLED, ENABLED.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@state.setter
	def state(self, state) :
		r"""Enable or disable the IP address.<br/>Default value: ENABLED<br/>Possible values = DISABLED, ENABLED
		"""
		try :
			self._state = state
		except Exception as e:
			raise e

	@property
	def map(self) :
		r"""Mapped IPV4 address for the IPV6 address.
		"""
		try :
			return self._map
		except Exception as e:
			raise e

	@map.setter
	def map(self, map) :
		r"""Mapped IPV4 address for the IPV6 address.
		"""
		try :
			self._map = map
		except Exception as e:
			raise e

	@property
	def vrid6(self) :
		r"""A positive integer that uniquely identifies a VMAC address for binding to this VIP address. This binding is used to set up NetScaler appliances in an active-active configuration using VRRP.<br/>Minimum length =  1<br/>Maximum length =  255.
		"""
		try :
			return self._vrid6
		except Exception as e:
			raise e

	@vrid6.setter
	def vrid6(self, vrid6) :
		r"""A positive integer that uniquely identifies a VMAC address for binding to this VIP address. This binding is used to set up NetScaler appliances in an active-active configuration using VRRP.<br/>Minimum length =  1<br/>Maximum length =  255
		"""
		try :
			self._vrid6 = vrid6
		except Exception as e:
			raise e

	@property
	def ownernode(self) :
		r"""ID of the cluster node for which you are adding the IP address. Must be used if you want the IP address to be active only on the specific node. Can be configured only through the cluster IP address. Cannot be changed after the IP address is created.<br/>Default value: 255.
		"""
		try :
			return self._ownernode
		except Exception as e:
			raise e

	@ownernode.setter
	def ownernode(self, ownernode) :
		r"""ID of the cluster node for which you are adding the IP address. Must be used if you want the IP address to be active only on the specific node. Can be configured only through the cluster IP address. Cannot be changed after the IP address is created.<br/>Default value: 255
		"""
		try :
			self._ownernode = ownernode
		except Exception as e:
			raise e

	@property
	def ownerdownresponse(self) :
		r"""in cluster system, if the owner node is down, whether should it respond to icmp/arp.<br/>Default value: YES<br/>Possible values = YES, NO.
		"""
		try :
			return self._ownerdownresponse
		except Exception as e:
			raise e

	@ownerdownresponse.setter
	def ownerdownresponse(self, ownerdownresponse) :
		r"""in cluster system, if the owner node is down, whether should it respond to icmp/arp.<br/>Default value: YES<br/>Possible values = YES, NO
		"""
		try :
			self._ownerdownresponse = ownerdownresponse
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
	def iptype(self) :
		r"""The type of the IPv6 address.<br/>Possible values = NSIP, VIP, SNIP, GSLBsiteIP, ADNSsvcIP, RADIUSListenersvcIP, CLIP.
		"""
		try :
			return self._iptype
		except Exception as e:
			raise e

	@property
	def curstate(self) :
		r"""Current state of this IP.<br/>Default value: ENABLED<br/>Possible values = DISABLED, ENABLED.
		"""
		try :
			return self._curstate
		except Exception as e:
			raise e

	@property
	def viprtadv2bsd(self) :
		r"""Whether this route is advertised to FreeBSD.
		"""
		try :
			return self._viprtadv2bsd
		except Exception as e:
			raise e

	@property
	def vipvsercount(self) :
		r"""Number	of vservers	bound to this VIP.
		"""
		try :
			return self._vipvsercount
		except Exception as e:
			raise e

	@property
	def vipvserdowncount(self) :
		r"""Number	of vservers	bound to this VIP, which are down.
		"""
		try :
			return self._vipvserdowncount
		except Exception as e:
			raise e

	@property
	def systemtype(self) :
		r"""The type of the System. Possible Values: Standalone, HA, Cluster. Used for display purpose.<br/>Possible values = Stand-alone, HA, Cluster.
		"""
		try :
			return self._systemtype
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nsip6_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nsip6
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.ipv6address is not None :
				return str(self.ipv6address)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add nsip6.
		"""
		try :
			if type(resource) is not list :
				addresource = nsip6()
				addresource.ipv6address = resource.ipv6address
				addresource.scope = resource.scope
				addresource.type = resource.type
				addresource.vlan = resource.vlan
				addresource.nd = resource.nd
				addresource.icmp = resource.icmp
				addresource.vserver = resource.vserver
				addresource.telnet = resource.telnet
				addresource.ftp = resource.ftp
				addresource.gui = resource.gui
				addresource.ssh = resource.ssh
				addresource.snmp = resource.snmp
				addresource.mgmtaccess = resource.mgmtaccess
				addresource.restrictaccess = resource.restrictaccess
				addresource.dynamicrouting = resource.dynamicrouting
				addresource.hostroute = resource.hostroute
				addresource.networkroute = resource.networkroute
				addresource.tag = resource.tag
				addresource.ip6hostrtgw = resource.ip6hostrtgw
				addresource.metric = resource.metric
				addresource.vserverrhilevel = resource.vserverrhilevel
				addresource.ospf6lsatype = resource.ospf6lsatype
				addresource.ospfarea = resource.ospfarea
				addresource.state = resource.state
				addresource.map = resource.map
				addresource.vrid6 = resource.vrid6
				addresource.ownernode = resource.ownernode
				addresource.ownerdownresponse = resource.ownerdownresponse
				addresource.td = resource.td
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ nsip6() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].ipv6address = resource[i].ipv6address
						addresources[i].scope = resource[i].scope
						addresources[i].type = resource[i].type
						addresources[i].vlan = resource[i].vlan
						addresources[i].nd = resource[i].nd
						addresources[i].icmp = resource[i].icmp
						addresources[i].vserver = resource[i].vserver
						addresources[i].telnet = resource[i].telnet
						addresources[i].ftp = resource[i].ftp
						addresources[i].gui = resource[i].gui
						addresources[i].ssh = resource[i].ssh
						addresources[i].snmp = resource[i].snmp
						addresources[i].mgmtaccess = resource[i].mgmtaccess
						addresources[i].restrictaccess = resource[i].restrictaccess
						addresources[i].dynamicrouting = resource[i].dynamicrouting
						addresources[i].hostroute = resource[i].hostroute
						addresources[i].networkroute = resource[i].networkroute
						addresources[i].tag = resource[i].tag
						addresources[i].ip6hostrtgw = resource[i].ip6hostrtgw
						addresources[i].metric = resource[i].metric
						addresources[i].vserverrhilevel = resource[i].vserverrhilevel
						addresources[i].ospf6lsatype = resource[i].ospf6lsatype
						addresources[i].ospfarea = resource[i].ospfarea
						addresources[i].state = resource[i].state
						addresources[i].map = resource[i].map
						addresources[i].vrid6 = resource[i].vrid6
						addresources[i].ownernode = resource[i].ownernode
						addresources[i].ownerdownresponse = resource[i].ownerdownresponse
						addresources[i].td = resource[i].td
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete nsip6.
		"""
		try :
			if type(resource) is not list :
				deleteresource = nsip6()
				if type(resource) !=  type(deleteresource):
					deleteresource.ipv6address = resource
				else :
					deleteresource.ipv6address = resource.ipv6address
					deleteresource.td = resource.td
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ nsip6() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].ipv6address = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ nsip6() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].ipv6address = resource[i].ipv6address
							deleteresources[i].td = resource[i].td
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update nsip6.
		"""
		try :
			if type(resource) is not list :
				updateresource = nsip6()
				updateresource.ipv6address = resource.ipv6address
				updateresource.td = resource.td
				updateresource.nd = resource.nd
				updateresource.icmp = resource.icmp
				updateresource.vserver = resource.vserver
				updateresource.telnet = resource.telnet
				updateresource.ftp = resource.ftp
				updateresource.gui = resource.gui
				updateresource.ssh = resource.ssh
				updateresource.snmp = resource.snmp
				updateresource.mgmtaccess = resource.mgmtaccess
				updateresource.ownerdownresponse = resource.ownerdownresponse
				updateresource.restrictaccess = resource.restrictaccess
				updateresource.state = resource.state
				updateresource.map = resource.map
				updateresource.dynamicrouting = resource.dynamicrouting
				updateresource.hostroute = resource.hostroute
				updateresource.networkroute = resource.networkroute
				updateresource.ip6hostrtgw = resource.ip6hostrtgw
				updateresource.metric = resource.metric
				updateresource.vserverrhilevel = resource.vserverrhilevel
				updateresource.ospf6lsatype = resource.ospf6lsatype
				updateresource.ospfarea = resource.ospfarea
				updateresource.tag = resource.tag
				updateresource.vrid6 = resource.vrid6
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ nsip6() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].ipv6address = resource[i].ipv6address
						updateresources[i].td = resource[i].td
						updateresources[i].nd = resource[i].nd
						updateresources[i].icmp = resource[i].icmp
						updateresources[i].vserver = resource[i].vserver
						updateresources[i].telnet = resource[i].telnet
						updateresources[i].ftp = resource[i].ftp
						updateresources[i].gui = resource[i].gui
						updateresources[i].ssh = resource[i].ssh
						updateresources[i].snmp = resource[i].snmp
						updateresources[i].mgmtaccess = resource[i].mgmtaccess
						updateresources[i].ownerdownresponse = resource[i].ownerdownresponse
						updateresources[i].restrictaccess = resource[i].restrictaccess
						updateresources[i].state = resource[i].state
						updateresources[i].map = resource[i].map
						updateresources[i].dynamicrouting = resource[i].dynamicrouting
						updateresources[i].hostroute = resource[i].hostroute
						updateresources[i].networkroute = resource[i].networkroute
						updateresources[i].ip6hostrtgw = resource[i].ip6hostrtgw
						updateresources[i].metric = resource[i].metric
						updateresources[i].vserverrhilevel = resource[i].vserverrhilevel
						updateresources[i].ospf6lsatype = resource[i].ospf6lsatype
						updateresources[i].ospfarea = resource[i].ospfarea
						updateresources[i].tag = resource[i].tag
						updateresources[i].vrid6 = resource[i].vrid6
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of nsip6 resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = nsip6()
				if type(resource) !=  type(unsetresource):
					unsetresource.ipv6address = resource
				else :
					unsetresource.ipv6address = resource.ipv6address
					unsetresource.td = resource.td
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ nsip6() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].ipv6address = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ nsip6() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].ipv6address = resource[i].ipv6address
							unsetresources[i].td = resource[i].td
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the nsip6 resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nsip6()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) != cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					option_ = options()
					option_.args = nitro_util.object_to_string_withoutquotes(name)
					response = name.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) != cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [nsip6() for _ in range(len(name))]
						for i in range(len(name)) :
							option_ = options()
							option_.args = nitro_util.object_to_string_withoutquotes(name[i])
							response[i] = name[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of nsip6 resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nsip6()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the nsip6 resources configured on NetScaler.
		"""
		try :
			obj = nsip6()
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
		r""" Use this API to count filtered the set of nsip6 resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nsip6()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Iptype:
		NSIP = "NSIP"
		VIP = "VIP"
		SNIP = "SNIP"
		GSLBsiteIP = "GSLBsiteIP"
		ADNSsvcIP = "ADNSsvcIP"
		RADIUSListenersvcIP = "RADIUSListenersvcIP"
		CLIP = "CLIP"

	class Networkroute:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Ssh:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class State:
		DISABLED = "DISABLED"
		ENABLED = "ENABLED"

	class Ospf6lsatype:
		INTRA_AREA = "INTRA_AREA"
		EXTERNAL = "EXTERNAL"

	class Scope:
		GLOBAL = "global"
		link_local = "link-local"

	class Nd:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Systemtype:
		Stand_alone = "Stand-alone"
		HA = "HA"
		Cluster = "Cluster"

	class Gui:
		ENABLED = "ENABLED"
		SECUREONLY = "SECUREONLY"
		DISABLED = "DISABLED"

	class Dynamicrouting:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Type:
		NSIP = "NSIP"
		VIP = "VIP"
		SNIP = "SNIP"
		GSLBsiteIP = "GSLBsiteIP"
		ADNSsvcIP = "ADNSsvcIP"
		RADIUSListenersvcIP = "RADIUSListenersvcIP"
		CLIP = "CLIP"

	class Mgmtaccess:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Hostroute:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Ftp:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Ownerdownresponse:
		YES = "YES"
		NO = "NO"

	class Vserverrhilevel:
		ONE_VSERVER = "ONE_VSERVER"
		ALL_VSERVERS = "ALL_VSERVERS"
		NONE = "NONE"
		VSVR_CNTRLD = "VSVR_CNTRLD"

	class Icmp:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Vserver:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Snmp:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Curstate:
		DISABLED = "DISABLED"
		ENABLED = "ENABLED"

	class Restrictaccess:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Telnet:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class nsip6_response(base_response) :
	def __init__(self, length=1) :
		self.nsip6 = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nsip6 = [nsip6() for _ in range(length)]

