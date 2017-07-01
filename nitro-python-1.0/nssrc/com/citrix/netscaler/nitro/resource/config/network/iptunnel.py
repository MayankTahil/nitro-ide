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

class iptunnel(base_resource) :
	""" Configuration for ip Tunnel resource. """
	def __init__(self) :
		self._name = None
		self._remote = None
		self._remotesubnetmask = None
		self._local = None
		self._protocol = None
		self._grepayload = None
		self._ipsecprofilename = None
		self._vlan = None
		self._ownergroup = None
		self._sysname = None
		self._type = None
		self._encapip = None
		self._channel = None
		self._tunneltype = []
		self._ipsectunnelstatus = None
		self._refcnt = None
		self.___count = 0

	@property
	def name(self) :
		r"""Name for the IP tunnel. Leading character must be a number or letter. Other characters allowed, after the first character, are @ _ - . (period) : (colon) # and space ( ).<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name for the IP tunnel. Leading character must be a number or letter. Other characters allowed, after the first character, are @ _ - . (period) : (colon) # and space ( ).<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def remote(self) :
		r"""Public IPv4 address, of the remote device, used to set up the tunnel. For this parameter, you can alternatively specify a network address.<br/>Minimum length =  1.
		"""
		try :
			return self._remote
		except Exception as e:
			raise e

	@remote.setter
	def remote(self, remote) :
		r"""Public IPv4 address, of the remote device, used to set up the tunnel. For this parameter, you can alternatively specify a network address.<br/>Minimum length =  1
		"""
		try :
			self._remote = remote
		except Exception as e:
			raise e

	@property
	def remotesubnetmask(self) :
		r"""Subnet mask of the remote IP address of the tunnel.
		"""
		try :
			return self._remotesubnetmask
		except Exception as e:
			raise e

	@remotesubnetmask.setter
	def remotesubnetmask(self, remotesubnetmask) :
		r"""Subnet mask of the remote IP address of the tunnel.
		"""
		try :
			self._remotesubnetmask = remotesubnetmask
		except Exception as e:
			raise e

	@property
	def local(self) :
		r"""Type ofNetScaler owned public IPv4 address, configured on the local NetScaler appliance and used to set up the tunnel.
		"""
		try :
			return self._local
		except Exception as e:
			raise e

	@local.setter
	def local(self, local) :
		r"""Type ofNetScaler owned public IPv4 address, configured on the local NetScaler appliance and used to set up the tunnel.
		"""
		try :
			self._local = local
		except Exception as e:
			raise e

	@property
	def protocol(self) :
		r"""Name of the protocol to be used on this tunnel.<br/>Default value: IPIP<br/>Possible values = IPIP, GRE, IPSEC.
		"""
		try :
			return self._protocol
		except Exception as e:
			raise e

	@protocol.setter
	def protocol(self, protocol) :
		r"""Name of the protocol to be used on this tunnel.<br/>Default value: IPIP<br/>Possible values = IPIP, GRE, IPSEC
		"""
		try :
			self._protocol = protocol
		except Exception as e:
			raise e

	@property
	def grepayload(self) :
		r"""The payload GRE will carry.<br/>Default value: ETHERNETwithDOT1Q<br/>Possible values = ETHERNETwithDOT1Q, ETHERNET, IP.
		"""
		try :
			return self._grepayload
		except Exception as e:
			raise e

	@grepayload.setter
	def grepayload(self, grepayload) :
		r"""The payload GRE will carry.<br/>Default value: ETHERNETwithDOT1Q<br/>Possible values = ETHERNETwithDOT1Q, ETHERNET, IP
		"""
		try :
			self._grepayload = grepayload
		except Exception as e:
			raise e

	@property
	def ipsecprofilename(self) :
		r"""Name of IPSec profile to be associated.<br/>Default value: "ns_ipsec_default_profile".
		"""
		try :
			return self._ipsecprofilename
		except Exception as e:
			raise e

	@ipsecprofilename.setter
	def ipsecprofilename(self, ipsecprofilename) :
		r"""Name of IPSec profile to be associated.<br/>Default value: "ns_ipsec_default_profile"
		"""
		try :
			self._ipsecprofilename = ipsecprofilename
		except Exception as e:
			raise e

	@property
	def vlan(self) :
		r"""The vlan for mulicast packets.<br/>Minimum length =  1<br/>Maximum length =  4094.
		"""
		try :
			return self._vlan
		except Exception as e:
			raise e

	@vlan.setter
	def vlan(self, vlan) :
		r"""The vlan for mulicast packets.<br/>Minimum length =  1<br/>Maximum length =  4094
		"""
		try :
			self._vlan = vlan
		except Exception as e:
			raise e

	@property
	def ownergroup(self) :
		r"""The owner node group in a Cluster for the iptunnel.<br/>Default value: DEFAULT_NG<br/>Minimum length =  1.
		"""
		try :
			return self._ownergroup
		except Exception as e:
			raise e

	@ownergroup.setter
	def ownergroup(self, ownergroup) :
		r"""The owner node group in a Cluster for the iptunnel.<br/>Default value: DEFAULT_NG<br/>Minimum length =  1
		"""
		try :
			self._ownergroup = ownergroup
		except Exception as e:
			raise e

	@property
	def sysname(self) :
		r"""The name of the ip tunnel.
		"""
		try :
			return self._sysname
		except Exception as e:
			raise e

	@property
	def type(self) :
		r"""The type of this tunnel.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@property
	def encapip(self) :
		r"""The effective local IP address of the tunnel. Used as the source of the encapsulated packets.
		"""
		try :
			return self._encapip
		except Exception as e:
			raise e

	@property
	def channel(self) :
		r"""The tunnel that is bound to a netbridge.
		"""
		try :
			return self._channel
		except Exception as e:
			raise e

	@property
	def tunneltype(self) :
		r"""Indicates that a tunnel is User-Configured, Internal or DELETE-IN-PROGRESS.<br/>Possible values = Configured, Delete-In-Progress.
		"""
		try :
			return self._tunneltype
		except Exception as e:
			raise e

	@property
	def ipsectunnelstatus(self) :
		r"""Whether the ipsec on this tunnel is up or down.<br/>Possible values = DOWN, UP, PARTIAL-UP, UNKNOWN.
		"""
		try :
			return self._ipsectunnelstatus
		except Exception as e:
			raise e

	@property
	def refcnt(self) :
		r"""Number of PBRs to bound to this iptunnel.
		"""
		try :
			return self._refcnt
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(iptunnel_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.iptunnel
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
		r""" Use this API to add iptunnel.
		"""
		try :
			if type(resource) is not list :
				addresource = iptunnel()
				addresource.name = resource.name
				addresource.remote = resource.remote
				addresource.remotesubnetmask = resource.remotesubnetmask
				addresource.local = resource.local
				addresource.protocol = resource.protocol
				addresource.grepayload = resource.grepayload
				addresource.ipsecprofilename = resource.ipsecprofilename
				addresource.vlan = resource.vlan
				addresource.ownergroup = resource.ownergroup
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ iptunnel() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].remote = resource[i].remote
						addresources[i].remotesubnetmask = resource[i].remotesubnetmask
						addresources[i].local = resource[i].local
						addresources[i].protocol = resource[i].protocol
						addresources[i].grepayload = resource[i].grepayload
						addresources[i].ipsecprofilename = resource[i].ipsecprofilename
						addresources[i].vlan = resource[i].vlan
						addresources[i].ownergroup = resource[i].ownergroup
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete iptunnel.
		"""
		try :
			if type(resource) is not list :
				deleteresource = iptunnel()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ iptunnel() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ iptunnel() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the iptunnel resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = iptunnel()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = iptunnel()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [iptunnel() for _ in range(len(name))]
						obj = [iptunnel() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = iptunnel()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		r""" Use this API to fetch all the iptunnel resources that are configured on netscaler.
	# This uses iptunnel_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = iptunnel()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of iptunnel resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = iptunnel()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the iptunnel resources configured on NetScaler.
		"""
		try :
			obj = iptunnel()
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
		r""" Use this API to count filtered the set of iptunnel resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = iptunnel()
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
		IPIP = "IPIP"
		GRE = "GRE"
		IPSEC = "IPSEC"

	class Tunneltype:
		Configured = "Configured"
		Delete_In_Progress = "Delete-In-Progress"

	class Ipsectunnelstatus:
		DOWN = "DOWN"
		UP = "UP"
		PARTIAL_UP = "PARTIAL-UP"
		UNKNOWN = "UNKNOWN"

	class Grepayload:
		ETHERNETwithDOT1Q = "ETHERNETwithDOT1Q"
		ETHERNET = "ETHERNET"
		IP = "IP"

class iptunnel_response(base_response) :
	def __init__(self, length=1) :
		self.iptunnel = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.iptunnel = [iptunnel() for _ in range(length)]

