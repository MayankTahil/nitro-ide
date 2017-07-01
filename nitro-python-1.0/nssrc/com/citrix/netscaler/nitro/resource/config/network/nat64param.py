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

class nat64param(base_resource) :
	""" Configuration for NAT64 parameter resource. """
	def __init__(self) :
		self._td = None
		self._nat64ignoretos = None
		self._nat64zerochecksum = None
		self._nat64v6mtu = None
		self._nat64fragheader = None
		self.___count = 0

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
	def nat64ignoretos(self) :
		r"""Ignore TOS.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._nat64ignoretos
		except Exception as e:
			raise e

	@nat64ignoretos.setter
	def nat64ignoretos(self, nat64ignoretos) :
		r"""Ignore TOS.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._nat64ignoretos = nat64ignoretos
		except Exception as e:
			raise e

	@property
	def nat64zerochecksum(self) :
		r"""Calculate checksum for UDP packets with zero checksum.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._nat64zerochecksum
		except Exception as e:
			raise e

	@nat64zerochecksum.setter
	def nat64zerochecksum(self, nat64zerochecksum) :
		r"""Calculate checksum for UDP packets with zero checksum.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._nat64zerochecksum = nat64zerochecksum
		except Exception as e:
			raise e

	@property
	def nat64v6mtu(self) :
		r"""MTU setting for the IPv6 side. If the incoming IPv4 packet greater than this, either fragment or send icmp need fragmentation error.<br/>Default value: 1280<br/>Minimum length =  1280<br/>Maximum length =  9216.
		"""
		try :
			return self._nat64v6mtu
		except Exception as e:
			raise e

	@nat64v6mtu.setter
	def nat64v6mtu(self, nat64v6mtu) :
		r"""MTU setting for the IPv6 side. If the incoming IPv4 packet greater than this, either fragment or send icmp need fragmentation error.<br/>Default value: 1280<br/>Minimum length =  1280<br/>Maximum length =  9216
		"""
		try :
			self._nat64v6mtu = nat64v6mtu
		except Exception as e:
			raise e

	@property
	def nat64fragheader(self) :
		r"""When disabled, translator will not insert IPv6 fragmentation header for non fragmented IPv4 packets.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._nat64fragheader
		except Exception as e:
			raise e

	@nat64fragheader.setter
	def nat64fragheader(self, nat64fragheader) :
		r"""When disabled, translator will not insert IPv6 fragmentation header for non fragmented IPv4 packets.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._nat64fragheader = nat64fragheader
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nat64param_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nat64param
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.td is not None :
				return str(self.td)
			return None
		except Exception as e :
			raise e



	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update nat64param.
		"""
		try :
			if type(resource) is not list :
				updateresource = nat64param()
				updateresource.td = resource.td
				updateresource.nat64ignoretos = resource.nat64ignoretos
				updateresource.nat64zerochecksum = resource.nat64zerochecksum
				updateresource.nat64v6mtu = resource.nat64v6mtu
				updateresource.nat64fragheader = resource.nat64fragheader
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ nat64param() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].td = resource[i].td
						updateresources[i].nat64ignoretos = resource[i].nat64ignoretos
						updateresources[i].nat64zerochecksum = resource[i].nat64zerochecksum
						updateresources[i].nat64v6mtu = resource[i].nat64v6mtu
						updateresources[i].nat64fragheader = resource[i].nat64fragheader
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of nat64param resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = nat64param()
				if type(resource) !=  type(unsetresource):
					unsetresource.td = resource
				else :
					unsetresource.td = resource.td
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ nat64param() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].td = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ nat64param() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].td = resource[i].td
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the nat64param resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nat64param()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = nat64param()
					obj.td = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [nat64param() for _ in range(len(name))]
						obj = [nat64param() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = nat64param()
							obj[i].td = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of nat64param resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nat64param()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the nat64param resources configured on NetScaler.
		"""
		try :
			obj = nat64param()
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
		r""" Use this API to count filtered the set of nat64param resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nat64param()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Nat64fragheader:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Nat64zerochecksum:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Nat64ignoretos:
		YES = "YES"
		NO = "NO"

class nat64param_response(base_response) :
	def __init__(self, length=1) :
		self.nat64param = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nat64param = [nat64param() for _ in range(length)]

