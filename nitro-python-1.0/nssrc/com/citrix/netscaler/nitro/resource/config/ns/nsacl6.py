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

class nsacl6(base_resource) :
	""" Configuration for ACL6 entry resource. """
	def __init__(self) :
		self._acl6name = None
		self._acl6action = None
		self._td = None
		self._srcipv6 = None
		self._srcipop = None
		self._srcipv6val = None
		self._srcport = None
		self._srcportop = None
		self._srcportval = None
		self._destipv6 = None
		self._destipop = None
		self._destipv6val = None
		self._destport = None
		self._destportop = None
		self._destportval = None
		self._ttl = None
		self._srcmac = None
		self._srcmacmask = None
		self._protocol = None
		self._protocolnumber = None
		self._vlan = None
		self._vxlan = None
		self._Interface = None
		self._established = None
		self._icmptype = None
		self._icmpcode = None
		self._priority = None
		self._state = None
		self._aclaction = None
		self._newname = None
		self._kernelstate = None
		self._hits = None
		self._aclassociate = []
		self.___count = 0

	@property
	def acl6name(self) :
		r"""Name for the ACL6 rule. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.<br/>Minimum length =  1.
		"""
		try :
			return self._acl6name
		except Exception as e:
			raise e

	@acl6name.setter
	def acl6name(self, acl6name) :
		r"""Name for the ACL6 rule. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.<br/>Minimum length =  1
		"""
		try :
			self._acl6name = acl6name
		except Exception as e:
			raise e

	@property
	def acl6action(self) :
		r"""Action to perform on the incoming IPv6 packets that match the ACL6 rule.
		Available settings function as follows:
		* ALLOW - The NetScaler appliance processes the packet.
		* BRIDGE - The NetScaler appliance bridges the packet to the destination without processing it.
		* DENY - The NetScaler appliance drops the packet.<br/>Possible values = BRIDGE, DENY, ALLOW.
		"""
		try :
			return self._acl6action
		except Exception as e:
			raise e

	@acl6action.setter
	def acl6action(self, acl6action) :
		r"""Action to perform on the incoming IPv6 packets that match the ACL6 rule.
		Available settings function as follows:
		* ALLOW - The NetScaler appliance processes the packet.
		* BRIDGE - The NetScaler appliance bridges the packet to the destination without processing it.
		* DENY - The NetScaler appliance drops the packet.<br/>Possible values = BRIDGE, DENY, ALLOW
		"""
		try :
			self._acl6action = acl6action
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
	def srcipv6(self) :
		r"""IP address or range of IP addresses to match against the source IP address of an incoming IPv6 packet. In the command line interface, separate the range with a hyphen.
		"""
		try :
			return self._srcipv6
		except Exception as e:
			raise e

	@srcipv6.setter
	def srcipv6(self, srcipv6) :
		r"""IP address or range of IP addresses to match against the source IP address of an incoming IPv6 packet. In the command line interface, separate the range with a hyphen.
		"""
		try :
			self._srcipv6 = srcipv6
		except Exception as e:
			raise e

	@property
	def srcipop(self) :
		r"""Either the equals (=) or does not equal (!=) logical operator.<br/>Possible values = =, !=, EQ, NEQ.
		"""
		try :
			return self._srcipop
		except Exception as e:
			raise e

	@srcipop.setter
	def srcipop(self, srcipop) :
		r"""Either the equals (=) or does not equal (!=) logical operator.<br/>Possible values = =, !=, EQ, NEQ
		"""
		try :
			self._srcipop = srcipop
		except Exception as e:
			raise e

	@property
	def srcipv6val(self) :
		r"""Source IPv6 address (range).
		"""
		try :
			return self._srcipv6val
		except Exception as e:
			raise e

	@srcipv6val.setter
	def srcipv6val(self, srcipv6val) :
		r"""Source IPv6 address (range).
		"""
		try :
			self._srcipv6val = srcipv6val
		except Exception as e:
			raise e

	@property
	def srcport(self) :
		r"""Port number or range of port numbers to match against the source port number of an incoming IPv6 packet. In the command line interface, separate the range with a hyphen. For example: 40-90.
		Note: The destination port can be specified only for TCP and UDP protocols.
		"""
		try :
			return self._srcport
		except Exception as e:
			raise e

	@srcport.setter
	def srcport(self, srcport) :
		r"""Port number or range of port numbers to match against the source port number of an incoming IPv6 packet. In the command line interface, separate the range with a hyphen. For example: 40-90.
		Note: The destination port can be specified only for TCP and UDP protocols.
		"""
		try :
			self._srcport = srcport
		except Exception as e:
			raise e

	@property
	def srcportop(self) :
		r"""Either the equals (=) or does not equal (!=) logical operator.<br/>Possible values = =, !=, EQ, NEQ.
		"""
		try :
			return self._srcportop
		except Exception as e:
			raise e

	@srcportop.setter
	def srcportop(self, srcportop) :
		r"""Either the equals (=) or does not equal (!=) logical operator.<br/>Possible values = =, !=, EQ, NEQ
		"""
		try :
			self._srcportop = srcportop
		except Exception as e:
			raise e

	@property
	def srcportval(self) :
		r"""Source port (range).<br/>Maximum length =  65535.
		"""
		try :
			return self._srcportval
		except Exception as e:
			raise e

	@srcportval.setter
	def srcportval(self, srcportval) :
		r"""Source port (range).<br/>Maximum length =  65535
		"""
		try :
			self._srcportval = srcportval
		except Exception as e:
			raise e

	@property
	def destipv6(self) :
		r"""IP address or range of IP addresses to match against the destination IP address of an incoming IPv6 packet.  In the command line interface, separate the range with a hyphen.
		"""
		try :
			return self._destipv6
		except Exception as e:
			raise e

	@destipv6.setter
	def destipv6(self, destipv6) :
		r"""IP address or range of IP addresses to match against the destination IP address of an incoming IPv6 packet.  In the command line interface, separate the range with a hyphen.
		"""
		try :
			self._destipv6 = destipv6
		except Exception as e:
			raise e

	@property
	def destipop(self) :
		r"""Either the equals (=) or does not equal (!=) logical operator.<br/>Possible values = =, !=, EQ, NEQ.
		"""
		try :
			return self._destipop
		except Exception as e:
			raise e

	@destipop.setter
	def destipop(self, destipop) :
		r"""Either the equals (=) or does not equal (!=) logical operator.<br/>Possible values = =, !=, EQ, NEQ
		"""
		try :
			self._destipop = destipop
		except Exception as e:
			raise e

	@property
	def destipv6val(self) :
		r"""Destination IPv6 address (range).
		"""
		try :
			return self._destipv6val
		except Exception as e:
			raise e

	@destipv6val.setter
	def destipv6val(self, destipv6val) :
		r"""Destination IPv6 address (range).
		"""
		try :
			self._destipv6val = destipv6val
		except Exception as e:
			raise e

	@property
	def destport(self) :
		r"""Port number or range of port numbers to match against the destination port number of an incoming IPv6 packet. In the command line interface, separate the range with a hyphen. For example: 40-90.
		Note: The destination port can be specified only for TCP and UDP protocols.
		"""
		try :
			return self._destport
		except Exception as e:
			raise e

	@destport.setter
	def destport(self, destport) :
		r"""Port number or range of port numbers to match against the destination port number of an incoming IPv6 packet. In the command line interface, separate the range with a hyphen. For example: 40-90.
		Note: The destination port can be specified only for TCP and UDP protocols.
		"""
		try :
			self._destport = destport
		except Exception as e:
			raise e

	@property
	def destportop(self) :
		r"""Either the equals (=) or does not equal (!=) logical operator.<br/>Possible values = =, !=, EQ, NEQ.
		"""
		try :
			return self._destportop
		except Exception as e:
			raise e

	@destportop.setter
	def destportop(self, destportop) :
		r"""Either the equals (=) or does not equal (!=) logical operator.<br/>Possible values = =, !=, EQ, NEQ
		"""
		try :
			self._destportop = destportop
		except Exception as e:
			raise e

	@property
	def destportval(self) :
		r"""Destination port (range).<br/>Maximum length =  65535.
		"""
		try :
			return self._destportval
		except Exception as e:
			raise e

	@destportval.setter
	def destportval(self, destportval) :
		r"""Destination port (range).<br/>Maximum length =  65535
		"""
		try :
			self._destportval = destportval
		except Exception as e:
			raise e

	@property
	def ttl(self) :
		r"""Time to expire this ACL6 (in seconds).<br/>Minimum length =  1<br/>Maximum length =  0x7FFFFFFF.
		"""
		try :
			return self._ttl
		except Exception as e:
			raise e

	@ttl.setter
	def ttl(self, ttl) :
		r"""Time to expire this ACL6 (in seconds).<br/>Minimum length =  1<br/>Maximum length =  0x7FFFFFFF
		"""
		try :
			self._ttl = ttl
		except Exception as e:
			raise e

	@property
	def srcmac(self) :
		r"""MAC address to match against the source MAC address of an incoming IPv6 packet.
		"""
		try :
			return self._srcmac
		except Exception as e:
			raise e

	@srcmac.setter
	def srcmac(self, srcmac) :
		r"""MAC address to match against the source MAC address of an incoming IPv6 packet.
		"""
		try :
			self._srcmac = srcmac
		except Exception as e:
			raise e

	@property
	def srcmacmask(self) :
		r""" Used to define range of Source MAC address. It takes string of 0 and 1, 0s are for exact match and 1s for wildcard. For matching first 3 bytes of MAC address, srcMacMask value "000000111111". .<br/>Default value: "000000000000".
		"""
		try :
			return self._srcmacmask
		except Exception as e:
			raise e

	@srcmacmask.setter
	def srcmacmask(self, srcmacmask) :
		r""" Used to define range of Source MAC address. It takes string of 0 and 1, 0s are for exact match and 1s for wildcard. For matching first 3 bytes of MAC address, srcMacMask value "000000111111". .<br/>Default value: "000000000000"
		"""
		try :
			self._srcmacmask = srcmacmask
		except Exception as e:
			raise e

	@property
	def protocol(self) :
		r"""Protocol, identified by protocol name, to match against the protocol of an incoming IPv6 packet.<br/>Possible values = ICMPV6, TCP, UDP.
		"""
		try :
			return self._protocol
		except Exception as e:
			raise e

	@protocol.setter
	def protocol(self, protocol) :
		r"""Protocol, identified by protocol name, to match against the protocol of an incoming IPv6 packet.<br/>Possible values = ICMPV6, TCP, UDP
		"""
		try :
			self._protocol = protocol
		except Exception as e:
			raise e

	@property
	def protocolnumber(self) :
		r"""Protocol, identified by protocol number, to match against the protocol of an incoming IPv6 packet.<br/>Minimum length =  1<br/>Maximum length =  255.
		"""
		try :
			return self._protocolnumber
		except Exception as e:
			raise e

	@protocolnumber.setter
	def protocolnumber(self, protocolnumber) :
		r"""Protocol, identified by protocol number, to match against the protocol of an incoming IPv6 packet.<br/>Minimum length =  1<br/>Maximum length =  255
		"""
		try :
			self._protocolnumber = protocolnumber
		except Exception as e:
			raise e

	@property
	def vlan(self) :
		r"""ID of the VLAN. The NetScaler appliance applies the ACL6 rule only to the incoming packets on the specified VLAN. If you do not specify a VLAN ID, the appliance applies the ACL6 rule to the incoming packets on all VLANs.<br/>Minimum length =  1<br/>Maximum length =  4094.
		"""
		try :
			return self._vlan
		except Exception as e:
			raise e

	@vlan.setter
	def vlan(self, vlan) :
		r"""ID of the VLAN. The NetScaler appliance applies the ACL6 rule only to the incoming packets on the specified VLAN. If you do not specify a VLAN ID, the appliance applies the ACL6 rule to the incoming packets on all VLANs.<br/>Minimum length =  1<br/>Maximum length =  4094
		"""
		try :
			self._vlan = vlan
		except Exception as e:
			raise e

	@property
	def vxlan(self) :
		r"""ID of the VXLAN. The NetScaler appliance applies the ACL6 rule only to the incoming packets on the specified VXLAN. If you do not specify a VXLAN ID, the appliance applies the ACL6 rule to the incoming packets on all VXLANs.<br/>Minimum length =  1<br/>Maximum length =  16777215.
		"""
		try :
			return self._vxlan
		except Exception as e:
			raise e

	@vxlan.setter
	def vxlan(self, vxlan) :
		r"""ID of the VXLAN. The NetScaler appliance applies the ACL6 rule only to the incoming packets on the specified VXLAN. If you do not specify a VXLAN ID, the appliance applies the ACL6 rule to the incoming packets on all VXLANs.<br/>Minimum length =  1<br/>Maximum length =  16777215
		"""
		try :
			self._vxlan = vxlan
		except Exception as e:
			raise e

	@property
	def Interface(self) :
		r"""ID of an interface. The NetScaler appliance applies the ACL6 rule only to the incoming packets from the specified interface. If you do not specify any value, the appliance applies the ACL6 rule to the incoming packets from all interfaces.
		"""
		try :
			return self._Interface
		except Exception as e:
			raise e

	@Interface.setter
	def Interface(self, Interface) :
		r"""ID of an interface. The NetScaler appliance applies the ACL6 rule only to the incoming packets from the specified interface. If you do not specify any value, the appliance applies the ACL6 rule to the incoming packets from all interfaces.
		"""
		try :
			self._Interface = Interface
		except Exception as e:
			raise e

	@property
	def established(self) :
		r"""Allow only incoming TCP packets that have the ACK or RST bit set if the action set for the ACL6 rule is ALLOW and these packets match the other conditions in the ACL6 rule.
		"""
		try :
			return self._established
		except Exception as e:
			raise e

	@established.setter
	def established(self, established) :
		r"""Allow only incoming TCP packets that have the ACK or RST bit set if the action set for the ACL6 rule is ALLOW and these packets match the other conditions in the ACL6 rule.
		"""
		try :
			self._established = established
		except Exception as e:
			raise e

	@property
	def icmptype(self) :
		r"""ICMP Message type to match against the message type of an incoming IPv6 ICMP packet. For example, to block DESTINATION UNREACHABLE messages, you must specify 3 as the ICMP type.
		Note: This parameter can be specified only for the ICMP protocol.<br/>Maximum length =  65536.
		"""
		try :
			return self._icmptype
		except Exception as e:
			raise e

	@icmptype.setter
	def icmptype(self, icmptype) :
		r"""ICMP Message type to match against the message type of an incoming IPv6 ICMP packet. For example, to block DESTINATION UNREACHABLE messages, you must specify 3 as the ICMP type.
		Note: This parameter can be specified only for the ICMP protocol.<br/>Maximum length =  65536
		"""
		try :
			self._icmptype = icmptype
		except Exception as e:
			raise e

	@property
	def icmpcode(self) :
		r"""Code of a particular ICMP message type to match against the ICMP code of an incoming IPv6 ICMP packet.  For example, to block DESTINATION HOST UNREACHABLE messages, specify 3 as the ICMP type and 1 as the ICMP code.
		If you set this parameter, you must set the ICMP Type parameter.<br/>Maximum length =  65536.
		"""
		try :
			return self._icmpcode
		except Exception as e:
			raise e

	@icmpcode.setter
	def icmpcode(self, icmpcode) :
		r"""Code of a particular ICMP message type to match against the ICMP code of an incoming IPv6 ICMP packet.  For example, to block DESTINATION HOST UNREACHABLE messages, specify 3 as the ICMP type and 1 as the ICMP code.
		If you set this parameter, you must set the ICMP Type parameter.<br/>Maximum length =  65536
		"""
		try :
			self._icmpcode = icmpcode
		except Exception as e:
			raise e

	@property
	def priority(self) :
		r"""Priority for the ACL6 rule, which determines the order in which it is evaluated relative to the other ACL6 rules. If you do not specify priorities while creating ACL6 rules, the ACL6 rules are evaluated in the order in which they are created.<br/>Minimum length =  1<br/>Maximum length =  81920.
		"""
		try :
			return self._priority
		except Exception as e:
			raise e

	@priority.setter
	def priority(self, priority) :
		r"""Priority for the ACL6 rule, which determines the order in which it is evaluated relative to the other ACL6 rules. If you do not specify priorities while creating ACL6 rules, the ACL6 rules are evaluated in the order in which they are created.<br/>Minimum length =  1<br/>Maximum length =  81920
		"""
		try :
			self._priority = priority
		except Exception as e:
			raise e

	@property
	def state(self) :
		r"""State of the ACL6.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@state.setter
	def state(self, state) :
		r"""State of the ACL6.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._state = state
		except Exception as e:
			raise e

	@property
	def aclaction(self) :
		r"""Action associated with the ACL6.<br/>Possible values = BRIDGE, DENY, ALLOW.
		"""
		try :
			return self._aclaction
		except Exception as e:
			raise e

	@aclaction.setter
	def aclaction(self, aclaction) :
		r"""Action associated with the ACL6.<br/>Possible values = BRIDGE, DENY, ALLOW
		"""
		try :
			self._aclaction = aclaction
		except Exception as e:
			raise e

	@property
	def newname(self) :
		r"""New name for the ACL6 rule. Must begin with an ASCII alphabetic or underscore \(_\) character, and must contain only ASCII alphanumeric, underscore, hash \(\#\), period \(.\), space, colon \(:\), at \(@\), equals \(=\), and hyphen \(-\) characters.<br/>Minimum length =  1.
		"""
		try :
			return self._newname
		except Exception as e:
			raise e

	@newname.setter
	def newname(self, newname) :
		r"""New name for the ACL6 rule. Must begin with an ASCII alphabetic or underscore \(_\) character, and must contain only ASCII alphanumeric, underscore, hash \(\#\), period \(.\), space, colon \(:\), at \(@\), equals \(=\), and hyphen \(-\) characters.<br/>Minimum length =  1
		"""
		try :
			self._newname = newname
		except Exception as e:
			raise e

	@property
	def kernelstate(self) :
		r"""Commit status of the ACL6.<br/>Default value: NOTAPPLIED<br/>Possible values = APPLIED, NOTAPPLIED, RE-APPLY, SFAPPLIED, SFNOTAPPLIED.
		"""
		try :
			return self._kernelstate
		except Exception as e:
			raise e

	@property
	def hits(self) :
		r"""Number of hits of this ACL6.
		"""
		try :
			return self._hits
		except Exception as e:
			raise e

	@property
	def aclassociate(self) :
		r"""ACL6 linked.<br/>Possible values = NAT, FORWARDINGSESSION, NAT64, LSN.
		"""
		try :
			return self._aclassociate
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nsacl6_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nsacl6
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.acl6name is not None :
				return str(self.acl6name)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add nsacl6.
		"""
		try :
			if type(resource) is not list :
				addresource = nsacl6()
				addresource.acl6name = resource.acl6name
				addresource.acl6action = resource.acl6action
				addresource.td = resource.td
				addresource.srcipv6 = resource.srcipv6
				addresource.srcipop = resource.srcipop
				addresource.srcipv6val = resource.srcipv6val
				addresource.srcport = resource.srcport
				addresource.srcportop = resource.srcportop
				addresource.srcportval = resource.srcportval
				addresource.destipv6 = resource.destipv6
				addresource.destipop = resource.destipop
				addresource.destipv6val = resource.destipv6val
				addresource.destport = resource.destport
				addresource.destportop = resource.destportop
				addresource.destportval = resource.destportval
				addresource.ttl = resource.ttl
				addresource.srcmac = resource.srcmac
				addresource.srcmacmask = resource.srcmacmask
				addresource.protocol = resource.protocol
				addresource.protocolnumber = resource.protocolnumber
				addresource.vlan = resource.vlan
				addresource.vxlan = resource.vxlan
				addresource.Interface = resource.Interface
				addresource.established = resource.established
				addresource.icmptype = resource.icmptype
				addresource.icmpcode = resource.icmpcode
				addresource.priority = resource.priority
				addresource.state = resource.state
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ nsacl6() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].acl6name = resource[i].acl6name
						addresources[i].acl6action = resource[i].acl6action
						addresources[i].td = resource[i].td
						addresources[i].srcipv6 = resource[i].srcipv6
						addresources[i].srcipop = resource[i].srcipop
						addresources[i].srcipv6val = resource[i].srcipv6val
						addresources[i].srcport = resource[i].srcport
						addresources[i].srcportop = resource[i].srcportop
						addresources[i].srcportval = resource[i].srcportval
						addresources[i].destipv6 = resource[i].destipv6
						addresources[i].destipop = resource[i].destipop
						addresources[i].destipv6val = resource[i].destipv6val
						addresources[i].destport = resource[i].destport
						addresources[i].destportop = resource[i].destportop
						addresources[i].destportval = resource[i].destportval
						addresources[i].ttl = resource[i].ttl
						addresources[i].srcmac = resource[i].srcmac
						addresources[i].srcmacmask = resource[i].srcmacmask
						addresources[i].protocol = resource[i].protocol
						addresources[i].protocolnumber = resource[i].protocolnumber
						addresources[i].vlan = resource[i].vlan
						addresources[i].vxlan = resource[i].vxlan
						addresources[i].Interface = resource[i].Interface
						addresources[i].established = resource[i].established
						addresources[i].icmptype = resource[i].icmptype
						addresources[i].icmpcode = resource[i].icmpcode
						addresources[i].priority = resource[i].priority
						addresources[i].state = resource[i].state
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete nsacl6.
		"""
		try :
			if type(resource) is not list :
				deleteresource = nsacl6()
				if type(resource) !=  type(deleteresource):
					deleteresource.acl6name = resource
				else :
					deleteresource.acl6name = resource.acl6name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ nsacl6() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].acl6name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ nsacl6() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].acl6name = resource[i].acl6name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update nsacl6.
		"""
		try :
			if type(resource) is not list :
				updateresource = nsacl6()
				updateresource.acl6name = resource.acl6name
				updateresource.aclaction = resource.aclaction
				updateresource.srcipv6 = resource.srcipv6
				updateresource.srcipop = resource.srcipop
				updateresource.srcipv6val = resource.srcipv6val
				updateresource.srcport = resource.srcport
				updateresource.srcportop = resource.srcportop
				updateresource.srcportval = resource.srcportval
				updateresource.destipv6 = resource.destipv6
				updateresource.destipop = resource.destipop
				updateresource.destipv6val = resource.destipv6val
				updateresource.destport = resource.destport
				updateresource.destportop = resource.destportop
				updateresource.destportval = resource.destportval
				updateresource.srcmac = resource.srcmac
				updateresource.srcmacmask = resource.srcmacmask
				updateresource.protocol = resource.protocol
				updateresource.protocolnumber = resource.protocolnumber
				updateresource.icmptype = resource.icmptype
				updateresource.icmpcode = resource.icmpcode
				updateresource.vlan = resource.vlan
				updateresource.vxlan = resource.vxlan
				updateresource.Interface = resource.Interface
				updateresource.priority = resource.priority
				updateresource.established = resource.established
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ nsacl6() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].acl6name = resource[i].acl6name
						updateresources[i].aclaction = resource[i].aclaction
						updateresources[i].srcipv6 = resource[i].srcipv6
						updateresources[i].srcipop = resource[i].srcipop
						updateresources[i].srcipv6val = resource[i].srcipv6val
						updateresources[i].srcport = resource[i].srcport
						updateresources[i].srcportop = resource[i].srcportop
						updateresources[i].srcportval = resource[i].srcportval
						updateresources[i].destipv6 = resource[i].destipv6
						updateresources[i].destipop = resource[i].destipop
						updateresources[i].destipv6val = resource[i].destipv6val
						updateresources[i].destport = resource[i].destport
						updateresources[i].destportop = resource[i].destportop
						updateresources[i].destportval = resource[i].destportval
						updateresources[i].srcmac = resource[i].srcmac
						updateresources[i].srcmacmask = resource[i].srcmacmask
						updateresources[i].protocol = resource[i].protocol
						updateresources[i].protocolnumber = resource[i].protocolnumber
						updateresources[i].icmptype = resource[i].icmptype
						updateresources[i].icmpcode = resource[i].icmpcode
						updateresources[i].vlan = resource[i].vlan
						updateresources[i].vxlan = resource[i].vxlan
						updateresources[i].Interface = resource[i].Interface
						updateresources[i].priority = resource[i].priority
						updateresources[i].established = resource[i].established
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of nsacl6 resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = nsacl6()
				if type(resource) !=  type(unsetresource):
					unsetresource.acl6name = resource
				else :
					unsetresource.acl6name = resource.acl6name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ nsacl6() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].acl6name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ nsacl6() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].acl6name = resource[i].acl6name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def enable(cls, client, resource) :
		r""" Use this API to enable nsacl6.
		"""
		try :
			if type(resource) is not list :
				enableresource = nsacl6()
				if type(resource) !=  type(enableresource):
					enableresource.acl6name = resource
				else :
					enableresource.acl6name = resource.acl6name
				return enableresource.perform_operation(client,"enable")
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						enableresources = [ nsacl6() for _ in range(len(resource))]
						for i in range(len(resource)) :
							enableresources[i].acl6name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						enableresources = [ nsacl6() for _ in range(len(resource))]
						for i in range(len(resource)) :
							enableresources[i].acl6name = resource[i].acl6name
				result = cls.perform_operation_bulk_request(client, enableresources,"enable")
			return result
		except Exception as e :
			raise e

	@classmethod
	def disable(cls, client, resource) :
		r""" Use this API to disable nsacl6.
		"""
		try :
			if type(resource) is not list :
				disableresource = nsacl6()
				if type(resource) !=  type(disableresource):
					disableresource.acl6name = resource
				else :
					disableresource.acl6name = resource.acl6name
				return disableresource.perform_operation(client,"disable")
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						disableresources = [ nsacl6() for _ in range(len(resource))]
						for i in range(len(resource)) :
							disableresources[i].acl6name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						disableresources = [ nsacl6() for _ in range(len(resource))]
						for i in range(len(resource)) :
							disableresources[i].acl6name = resource[i].acl6name
				result = cls.perform_operation_bulk_request(client, disableresources,"disable")
			return result
		except Exception as e :
			raise e

	@classmethod
	def rename(cls, client, resource, new_acl6name) :
		r""" Use this API to rename a nsacl6 resource.
		"""
		try :
			renameresource = nsacl6()
			if type(resource) == cls :
				renameresource.acl6name = resource.acl6name
			else :
				renameresource.acl6name = resource
			return renameresource.rename_resource(client,new_acl6name)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the nsacl6 resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nsacl6()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = nsacl6()
					obj.acl6name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [nsacl6() for _ in range(len(name))]
						obj = [nsacl6() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = nsacl6()
							obj[i].acl6name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of nsacl6 resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nsacl6()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the nsacl6 resources configured on NetScaler.
		"""
		try :
			obj = nsacl6()
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
		r""" Use this API to count filtered the set of nsacl6 resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nsacl6()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Protocol:
		ICMPV6 = "ICMPV6"
		TCP = "TCP"
		UDP = "UDP"

	class Srcipop:
		_EQ = "="
		_NEQ = "!="
		EQ = "EQ"
		NEQ = "NEQ"

	class Aclassociate:
		NAT = "NAT"
		FORWARDINGSESSION = "FORWARDINGSESSION"
		NAT64 = "NAT64"
		LSN = "LSN"

	class Destipop:
		_EQ = "="
		_NEQ = "!="
		EQ = "EQ"
		NEQ = "NEQ"

	class State:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Kernelstate:
		APPLIED = "APPLIED"
		NOTAPPLIED = "NOTAPPLIED"
		RE_APPLY = "RE-APPLY"
		SFAPPLIED = "SFAPPLIED"
		SFNOTAPPLIED = "SFNOTAPPLIED"

	class Acl6action:
		BRIDGE = "BRIDGE"
		DENY = "DENY"
		ALLOW = "ALLOW"

	class Destportop:
		_EQ = "="
		_NEQ = "!="
		EQ = "EQ"
		NEQ = "NEQ"

	class Aclaction:
		BRIDGE = "BRIDGE"
		DENY = "DENY"
		ALLOW = "ALLOW"

	class Srcportop:
		_EQ = "="
		_NEQ = "!="
		EQ = "EQ"
		NEQ = "NEQ"

class nsacl6_response(base_response) :
	def __init__(self, length=1) :
		self.nsacl6 = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nsacl6 = [nsacl6() for _ in range(length)]

