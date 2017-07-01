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

class mapbmr(base_resource) :
	""" Configuration for MAP-T Basic Mapping rule resource. """
	def __init__(self) :
		self._name = None
		self._ruleipv6prefix = None
		self._psidoffset = None
		self._eabitlength = None
		self._psidlength = None
		self.___count = 0

	@property
	def name(self) :
		r"""Name for the Basic Mapping Rule. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the  MAP Basic Mapping Rule is created. The following requirement applies only to the NetScaler CLI: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "add network MapBmr bmr1 -natprefix 2005::/64 -EAbitLength 16 -psidoffset 6 -portsharingratio 8" ).
		The Basic Mapping Rule information allows a MAP BR to determine source IPv4 address from the IPv6 packet sent from MAP CE device.
		Also it allows to determine destination IPv6 address of MAP CE before sending packets to MAP CE.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name for the Basic Mapping Rule. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the  MAP Basic Mapping Rule is created. The following requirement applies only to the NetScaler CLI: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "add network MapBmr bmr1 -natprefix 2005::/64 -EAbitLength 16 -psidoffset 6 -portsharingratio 8" ).
		The Basic Mapping Rule information allows a MAP BR to determine source IPv4 address from the IPv6 packet sent from MAP CE device.
		Also it allows to determine destination IPv6 address of MAP CE before sending packets to MAP CE.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def ruleipv6prefix(self) :
		r"""IPv6 prefix of Customer Edge(CE) device.MAP-T CE will send ipv6 packets with this ipv6 prefix as source ipv6 address prefix.
		"""
		try :
			return self._ruleipv6prefix
		except Exception as e:
			raise e

	@ruleipv6prefix.setter
	def ruleipv6prefix(self, ruleipv6prefix) :
		r"""IPv6 prefix of Customer Edge(CE) device.MAP-T CE will send ipv6 packets with this ipv6 prefix as source ipv6 address prefix.
		"""
		try :
			self._ruleipv6prefix = ruleipv6prefix
		except Exception as e:
			raise e

	@property
	def psidoffset(self) :
		r"""Start bit position  of Port Set Identifier(PSID) value in Embedded Address (EA) bits.<br/>Default value: 6<br/>Minimum length =  1<br/>Maximum length =  15.
		"""
		try :
			return self._psidoffset
		except Exception as e:
			raise e

	@psidoffset.setter
	def psidoffset(self, psidoffset) :
		r"""Start bit position  of Port Set Identifier(PSID) value in Embedded Address (EA) bits.<br/>Default value: 6<br/>Minimum length =  1<br/>Maximum length =  15
		"""
		try :
			self._psidoffset = psidoffset
		except Exception as e:
			raise e

	@property
	def eabitlength(self) :
		r"""The Embedded Address (EA) bit field encodes the CE-specific IPv4 address and port information.  The EA bit field, which is unique for a 
		given Rule IPv6 prefix.<br/>Default value: 16<br/>Minimum length =  2<br/>Maximum length =  47.
		"""
		try :
			return self._eabitlength
		except Exception as e:
			raise e

	@eabitlength.setter
	def eabitlength(self, eabitlength) :
		r"""The Embedded Address (EA) bit field encodes the CE-specific IPv4 address and port information.  The EA bit field, which is unique for a 
		given Rule IPv6 prefix.<br/>Default value: 16<br/>Minimum length =  2<br/>Maximum length =  47
		"""
		try :
			self._eabitlength = eabitlength
		except Exception as e:
			raise e

	@property
	def psidlength(self) :
		r"""Length of Port Set IdentifierPort Set Identifier(PSID) in Embedded Address (EA) bits.<br/>Default value: 8<br/>Minimum length =  1<br/>Maximum length =  16.
		"""
		try :
			return self._psidlength
		except Exception as e:
			raise e

	@psidlength.setter
	def psidlength(self, psidlength) :
		r"""Length of Port Set IdentifierPort Set Identifier(PSID) in Embedded Address (EA) bits.<br/>Default value: 8<br/>Minimum length =  1<br/>Maximum length =  16
		"""
		try :
			self._psidlength = psidlength
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(mapbmr_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.mapbmr
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
		r""" Use this API to add mapbmr.
		"""
		try :
			if type(resource) is not list :
				addresource = mapbmr()
				addresource.name = resource.name
				addresource.ruleipv6prefix = resource.ruleipv6prefix
				addresource.psidoffset = resource.psidoffset
				addresource.eabitlength = resource.eabitlength
				addresource.psidlength = resource.psidlength
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ mapbmr() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].ruleipv6prefix = resource[i].ruleipv6prefix
						addresources[i].psidoffset = resource[i].psidoffset
						addresources[i].eabitlength = resource[i].eabitlength
						addresources[i].psidlength = resource[i].psidlength
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete mapbmr.
		"""
		try :
			if type(resource) is not list :
				deleteresource = mapbmr()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ mapbmr() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ mapbmr() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the mapbmr resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = mapbmr()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = mapbmr()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [mapbmr() for _ in range(len(name))]
						obj = [mapbmr() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = mapbmr()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of mapbmr resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = mapbmr()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the mapbmr resources configured on NetScaler.
		"""
		try :
			obj = mapbmr()
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
		r""" Use this API to count filtered the set of mapbmr resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = mapbmr()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


class mapbmr_response(base_response) :
	def __init__(self, length=1) :
		self.mapbmr = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.mapbmr = [mapbmr() for _ in range(length)]

