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

class mapdmr(base_resource) :
	""" Configuration for MAP-T Default Mapping rule resource. """
	def __init__(self) :
		self._name = None
		self._bripv6prefix = None
		self.___count = 0

	@property
	def name(self) :
		r"""Name for the Default Mapping Rule. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the MAP Default Mapping Rule is created. The following requirement applies only to the NetScaler CLI: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "add network MapDmr map1 -BRIpv6Prefix 2003::/96").
		Default Mapping Rule (DMR) is defined in terms of the IPv6 prefix advertised by one or more BRs, which provide external connectivity.  A typical MAP-T CE will install an IPv4 default route using this rule.  A BR will use this rule when translating all outside IPv4 source addresses to the IPv6 MAP domain.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name for the Default Mapping Rule. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the MAP Default Mapping Rule is created. The following requirement applies only to the NetScaler CLI: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "add network MapDmr map1 -BRIpv6Prefix 2003::/96").
		Default Mapping Rule (DMR) is defined in terms of the IPv6 prefix advertised by one or more BRs, which provide external connectivity.  A typical MAP-T CE will install an IPv4 default route using this rule.  A BR will use this rule when translating all outside IPv4 source addresses to the IPv6 MAP domain.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def bripv6prefix(self) :
		r"""IPv6 prefix of Border Relay (Netscaler) device.MAP-T CE will send ipv6 packets to this ipv6 prefix.The DMR IPv6 prefix length SHOULD be 64 bits long by default and in any case MUST NOT exceed 96 bits.
		"""
		try :
			return self._bripv6prefix
		except Exception as e:
			raise e

	@bripv6prefix.setter
	def bripv6prefix(self, bripv6prefix) :
		r"""IPv6 prefix of Border Relay (Netscaler) device.MAP-T CE will send ipv6 packets to this ipv6 prefix.The DMR IPv6 prefix length SHOULD be 64 bits long by default and in any case MUST NOT exceed 96 bits.
		"""
		try :
			self._bripv6prefix = bripv6prefix
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(mapdmr_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.mapdmr
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
		r""" Use this API to add mapdmr.
		"""
		try :
			if type(resource) is not list :
				addresource = mapdmr()
				addresource.name = resource.name
				addresource.bripv6prefix = resource.bripv6prefix
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ mapdmr() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].bripv6prefix = resource[i].bripv6prefix
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete mapdmr.
		"""
		try :
			if type(resource) is not list :
				deleteresource = mapdmr()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ mapdmr() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ mapdmr() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the mapdmr resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = mapdmr()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = mapdmr()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [mapdmr() for _ in range(len(name))]
						obj = [mapdmr() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = mapdmr()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of mapdmr resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = mapdmr()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the mapdmr resources configured on NetScaler.
		"""
		try :
			obj = mapdmr()
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
		r""" Use this API to count filtered the set of mapdmr resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = mapdmr()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


class mapdmr_response(base_response) :
	def __init__(self, length=1) :
		self.mapdmr = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.mapdmr = [mapdmr() for _ in range(length)]

