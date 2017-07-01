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

class inat(base_resource) :
	""" Configuration for inbound nat resource. """
	def __init__(self) :
		self._name = None
		self._publicip = None
		self._privateip = None
		self._mode = None
		self._tcpproxy = None
		self._ftp = None
		self._tftp = None
		self._usip = None
		self._usnip = None
		self._proxyip = None
		self._useproxyport = None
		self._td = None
		self._flags = None
		self.___count = 0

	@property
	def name(self) :
		r"""Name for the Inbound NAT (INAT) entry. Leading character must be a number or letter. Other characters allowed, after the first character, are @ _ - . (period) : (colon) # and space ( ).<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name for the Inbound NAT (INAT) entry. Leading character must be a number or letter. Other characters allowed, after the first character, are @ _ - . (period) : (colon) # and space ( ).<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def publicip(self) :
		r"""Public IP address of packets received on the NetScaler appliance. Can be aNetScaler-owned VIP or VIP6 address.<br/>Minimum length =  1.
		"""
		try :
			return self._publicip
		except Exception as e:
			raise e

	@publicip.setter
	def publicip(self, publicip) :
		r"""Public IP address of packets received on the NetScaler appliance. Can be aNetScaler-owned VIP or VIP6 address.<br/>Minimum length =  1
		"""
		try :
			self._publicip = publicip
		except Exception as e:
			raise e

	@property
	def privateip(self) :
		r"""IP address of the server to which the packet is sent by the NetScaler. Can be an IPv4 or IPv6 address.<br/>Minimum length =  1.
		"""
		try :
			return self._privateip
		except Exception as e:
			raise e

	@privateip.setter
	def privateip(self, privateip) :
		r"""IP address of the server to which the packet is sent by the NetScaler. Can be an IPv4 or IPv6 address.<br/>Minimum length =  1
		"""
		try :
			self._privateip = privateip
		except Exception as e:
			raise e

	@property
	def mode(self) :
		r"""Stateless translation.<br/>Possible values = STATELESS.
		"""
		try :
			return self._mode
		except Exception as e:
			raise e

	@mode.setter
	def mode(self, mode) :
		r"""Stateless translation.<br/>Possible values = STATELESS
		"""
		try :
			self._mode = mode
		except Exception as e:
			raise e

	@property
	def tcpproxy(self) :
		r"""Enable TCP proxy, which enables the NetScaler appliance to optimize the RNAT TCP traffic by using Layer 4 features.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._tcpproxy
		except Exception as e:
			raise e

	@tcpproxy.setter
	def tcpproxy(self, tcpproxy) :
		r"""Enable TCP proxy, which enables the NetScaler appliance to optimize the RNAT TCP traffic by using Layer 4 features.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._tcpproxy = tcpproxy
		except Exception as e:
			raise e

	@property
	def ftp(self) :
		r"""Enable the FTP protocol on the server for transferring files between the client and the server.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._ftp
		except Exception as e:
			raise e

	@ftp.setter
	def ftp(self, ftp) :
		r"""Enable the FTP protocol on the server for transferring files between the client and the server.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._ftp = ftp
		except Exception as e:
			raise e

	@property
	def tftp(self) :
		r"""To enable/disable TFTP (Default DISABLED).<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._tftp
		except Exception as e:
			raise e

	@tftp.setter
	def tftp(self, tftp) :
		r"""To enable/disable TFTP (Default DISABLED).<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._tftp = tftp
		except Exception as e:
			raise e

	@property
	def usip(self) :
		r"""Enable the NetScaler appliance to retain the source IP address of packets before sending the packets to the server.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._usip
		except Exception as e:
			raise e

	@usip.setter
	def usip(self, usip) :
		r"""Enable the NetScaler appliance to retain the source IP address of packets before sending the packets to the server.<br/>Possible values = ON, OFF
		"""
		try :
			self._usip = usip
		except Exception as e:
			raise e

	@property
	def usnip(self) :
		r"""Enable the NetScaler appliance to use a SNIP address as the source IP address of packets before sending the packets to the server.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._usnip
		except Exception as e:
			raise e

	@usnip.setter
	def usnip(self, usnip) :
		r"""Enable the NetScaler appliance to use a SNIP address as the source IP address of packets before sending the packets to the server.<br/>Possible values = ON, OFF
		"""
		try :
			self._usnip = usnip
		except Exception as e:
			raise e

	@property
	def proxyip(self) :
		r"""Unique IP address used as the source IP address in packets sent to the server. Must be a MIP or SNIP address.
		"""
		try :
			return self._proxyip
		except Exception as e:
			raise e

	@proxyip.setter
	def proxyip(self, proxyip) :
		r"""Unique IP address used as the source IP address in packets sent to the server. Must be a MIP or SNIP address.
		"""
		try :
			self._proxyip = proxyip
		except Exception as e:
			raise e

	@property
	def useproxyport(self) :
		r"""Enable the NetScaler appliance to proxy the source port of packets before sending the packets to the server.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._useproxyport
		except Exception as e:
			raise e

	@useproxyport.setter
	def useproxyport(self, useproxyport) :
		r"""Enable the NetScaler appliance to proxy the source port of packets before sending the packets to the server.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._useproxyport = useproxyport
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
	def flags(self) :
		r"""Flags for different modes.
		"""
		try :
			return self._flags
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(inat_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.inat
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
		r""" Use this API to add inat.
		"""
		try :
			if type(resource) is not list :
				addresource = inat()
				addresource.name = resource.name
				addresource.publicip = resource.publicip
				addresource.privateip = resource.privateip
				addresource.mode = resource.mode
				addresource.tcpproxy = resource.tcpproxy
				addresource.ftp = resource.ftp
				addresource.tftp = resource.tftp
				addresource.usip = resource.usip
				addresource.usnip = resource.usnip
				addresource.proxyip = resource.proxyip
				addresource.useproxyport = resource.useproxyport
				addresource.td = resource.td
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ inat() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].publicip = resource[i].publicip
						addresources[i].privateip = resource[i].privateip
						addresources[i].mode = resource[i].mode
						addresources[i].tcpproxy = resource[i].tcpproxy
						addresources[i].ftp = resource[i].ftp
						addresources[i].tftp = resource[i].tftp
						addresources[i].usip = resource[i].usip
						addresources[i].usnip = resource[i].usnip
						addresources[i].proxyip = resource[i].proxyip
						addresources[i].useproxyport = resource[i].useproxyport
						addresources[i].td = resource[i].td
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete inat.
		"""
		try :
			if type(resource) is not list :
				deleteresource = inat()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ inat() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ inat() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update inat.
		"""
		try :
			if type(resource) is not list :
				updateresource = inat()
				updateresource.name = resource.name
				updateresource.privateip = resource.privateip
				updateresource.tcpproxy = resource.tcpproxy
				updateresource.ftp = resource.ftp
				updateresource.tftp = resource.tftp
				updateresource.usip = resource.usip
				updateresource.usnip = resource.usnip
				updateresource.proxyip = resource.proxyip
				updateresource.useproxyport = resource.useproxyport
				updateresource.mode = resource.mode
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ inat() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].privateip = resource[i].privateip
						updateresources[i].tcpproxy = resource[i].tcpproxy
						updateresources[i].ftp = resource[i].ftp
						updateresources[i].tftp = resource[i].tftp
						updateresources[i].usip = resource[i].usip
						updateresources[i].usnip = resource[i].usnip
						updateresources[i].proxyip = resource[i].proxyip
						updateresources[i].useproxyport = resource[i].useproxyport
						updateresources[i].mode = resource[i].mode
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of inat resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = inat()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ inat() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ inat() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the inat resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = inat()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = inat()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [inat() for _ in range(len(name))]
						obj = [inat() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = inat()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of inat resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = inat()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the inat resources configured on NetScaler.
		"""
		try :
			obj = inat()
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
		r""" Use this API to count filtered the set of inat resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = inat()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Mode:
		STATELESS = "STATELESS"

	class Usnip:
		ON = "ON"
		OFF = "OFF"

	class Tftp:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Tcpproxy:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Useproxyport:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Usip:
		ON = "ON"
		OFF = "OFF"

	class Ftp:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class inat_response(base_response) :
	def __init__(self, length=1) :
		self.inat = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.inat = [inat() for _ in range(length)]

