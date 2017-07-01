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

class mapbmr_binding(base_resource):
	""" Binding class showing the resources that can be bound to mapbmr_binding. 
	"""
	def __init__(self) :
		self._name = None
		self.mapbmr_bmrv4network_binding = []

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
	def mapbmr_bmrv4network_bindings(self) :
		r"""bmrv4network that can be bound to mapbmr.
		"""
		try :
			return self._mapbmr_bmrv4network_binding
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(mapbmr_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.mapbmr_binding
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
	def get(self, service, name="", option_="") :
		r""" Use this API to fetch mapbmr_binding resource.
		"""
		try :
			if not name :
				obj = mapbmr_binding()
				response = obj.get_resources(service, option_)
			elif type(name) is not list :
				obj = mapbmr_binding()
				obj.name = name
				response = obj.get_resource(service)
			else :
				if name and len(name) > 0 :
					obj = [mapbmr_binding() for _ in range(len(name))]
					for i in range(len(name)) :
						obj[i].name = name[i];
						response[i] = obj[i].get_resource(service)
			return response
		except Exception as e:
			raise e

class mapbmr_binding_response(base_response) :
	def __init__(self, length=1) :
		self.mapbmr_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.mapbmr_binding = [mapbmr_binding() for _ in range(length)]

