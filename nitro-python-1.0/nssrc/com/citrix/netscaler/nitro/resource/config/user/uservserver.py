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

class uservserver(base_resource) :
	""" Configuration for virtual server resource. """
	def __init__(self) :
		self._name = None
		self._userprotocol = None
		self._ipaddress = None
		self._port = None
		self._defaultlb = None
		self._Params = None
		self._comment = None
		self._state = None
		self._value = None
		self._statechangetimesec = None
		self._statechangetimemsec = None
		self._tickssincelaststatechange = None
		self.___count = 0

	@property
	def name(self) :
		r"""Name for the virtual server. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen (-) characters.
		CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my vserver" or 'my vserver'). .<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name for the virtual server. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen (-) characters.
		CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my vserver" or 'my vserver'). .<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def userprotocol(self) :
		r"""User protocol uesd by the service.
		"""
		try :
			return self._userprotocol
		except Exception as e:
			raise e

	@userprotocol.setter
	def userprotocol(self, userprotocol) :
		r"""User protocol uesd by the service.
		"""
		try :
			self._userprotocol = userprotocol
		except Exception as e:
			raise e

	@property
	def ipaddress(self) :
		r"""IPv4 or IPv6 address to assign to the virtual server.
		"""
		try :
			return self._ipaddress
		except Exception as e:
			raise e

	@ipaddress.setter
	def ipaddress(self, ipaddress) :
		r"""IPv4 or IPv6 address to assign to the virtual server.
		"""
		try :
			self._ipaddress = ipaddress
		except Exception as e:
			raise e

	@property
	def port(self) :
		r"""Port number for the virtual server.<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API.
		"""
		try :
			return self._port
		except Exception as e:
			raise e

	@port.setter
	def port(self, port) :
		r"""Port number for the virtual server.<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API
		"""
		try :
			self._port = port
		except Exception as e:
			raise e

	@property
	def defaultlb(self) :
		r"""Name of the default Load Balancing virtual server used for load balancing of services. The protocol type of default Load Balancing virtual server should be a user type.
		"""
		try :
			return self._defaultlb
		except Exception as e:
			raise e

	@defaultlb.setter
	def defaultlb(self, defaultlb) :
		r"""Name of the default Load Balancing virtual server used for load balancing of services. The protocol type of default Load Balancing virtual server should be a user type.
		"""
		try :
			self._defaultlb = defaultlb
		except Exception as e:
			raise e

	@property
	def Params(self) :
		r"""Any comments associated with the protocol.
		"""
		try :
			return self._Params
		except Exception as e:
			raise e

	@Params.setter
	def Params(self, Params) :
		r"""Any comments associated with the protocol.
		"""
		try :
			self._Params = Params
		except Exception as e:
			raise e

	@property
	def comment(self) :
		r"""Any comments that you might want to associate with the virtual server.
		"""
		try :
			return self._comment
		except Exception as e:
			raise e

	@comment.setter
	def comment(self, comment) :
		r"""Any comments that you might want to associate with the virtual server.
		"""
		try :
			self._comment = comment
		except Exception as e:
			raise e

	@property
	def state(self) :
		r"""Current user vserver state.<br/>Possible values = UP, DOWN, UNKNOWN, BUSY, OUT OF SERVICE, GOING OUT OF SERVICE, DOWN WHEN GOING OUT OF SERVICE, NS_EMPTY_STR, Unknown, DISABLED.
		"""
		try :
			return self._state
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

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(uservserver_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.uservserver
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
		r""" Use this API to add uservserver.
		"""
		try :
			if type(resource) is not list :
				addresource = uservserver()
				addresource.name = resource.name
				addresource.userprotocol = resource.userprotocol
				addresource.ipaddress = resource.ipaddress
				addresource.port = resource.port
				addresource.defaultlb = resource.defaultlb
				addresource.Params = resource.Params
				addresource.comment = resource.comment
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ uservserver() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].userprotocol = resource[i].userprotocol
						addresources[i].ipaddress = resource[i].ipaddress
						addresources[i].port = resource[i].port
						addresources[i].defaultlb = resource[i].defaultlb
						addresources[i].Params = resource[i].Params
						addresources[i].comment = resource[i].comment
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete uservserver.
		"""
		try :
			if type(resource) is not list :
				deleteresource = uservserver()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ uservserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ uservserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update uservserver.
		"""
		try :
			if type(resource) is not list :
				updateresource = uservserver()
				updateresource.name = resource.name
				updateresource.ipaddress = resource.ipaddress
				updateresource.defaultlb = resource.defaultlb
				updateresource.Params = resource.Params
				updateresource.comment = resource.comment
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ uservserver() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].ipaddress = resource[i].ipaddress
						updateresources[i].defaultlb = resource[i].defaultlb
						updateresources[i].Params = resource[i].Params
						updateresources[i].comment = resource[i].comment
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of uservserver resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = uservserver()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ uservserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ uservserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the uservserver resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = uservserver()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = uservserver()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [uservserver() for _ in range(len(name))]
						obj = [uservserver() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = uservserver()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of uservserver resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = uservserver()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the uservserver resources configured on NetScaler.
		"""
		try :
			obj = uservserver()
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
		r""" Use this API to count filtered the set of uservserver resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = uservserver()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class State:
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

class uservserver_response(base_response) :
	def __init__(self, length=1) :
		self.uservserver = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.uservserver = [uservserver() for _ in range(length)]

