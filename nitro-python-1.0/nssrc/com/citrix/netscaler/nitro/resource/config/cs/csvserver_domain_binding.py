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

class csvserver_domain_binding(base_resource) :
	""" Binding class showing the domain that can be bound to csvserver.
	"""
	def __init__(self) :
		self._domainname = None
		self._ttl = None
		self._backupip = None
		self._cookiedomain = None
		self._cookietimeout = None
		self._sitedomainttl = None
		self._appflowlog = None
		self._name = None
		self.___count = 0

	@property
	def backupip(self) :
		r""".<br/>Minimum length =  1.
		"""
		try :
			return self._backupip
		except Exception as e:
			raise e

	@backupip.setter
	def backupip(self, backupip) :
		r""".<br/>Minimum length =  1
		"""
		try :
			self._backupip = backupip
		except Exception as e:
			raise e

	@property
	def ttl(self) :
		r""".<br/>Minimum value =  1.
		"""
		try :
			return self._ttl
		except Exception as e:
			raise e

	@ttl.setter
	def ttl(self, ttl) :
		r""".<br/>Minimum value =  1
		"""
		try :
			self._ttl = ttl
		except Exception as e:
			raise e

	@property
	def name(self) :
		r"""Name of the content switching virtual server to which the content switching policy applies.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name of the content switching virtual server to which the content switching policy applies.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def domainname(self) :
		r"""Domain name for which to change the time to live (TTL) and/or backup service IP address.<br/>Minimum length =  1.
		"""
		try :
			return self._domainname
		except Exception as e:
			raise e

	@domainname.setter
	def domainname(self, domainname) :
		r"""Domain name for which to change the time to live (TTL) and/or backup service IP address.<br/>Minimum length =  1
		"""
		try :
			self._domainname = domainname
		except Exception as e:
			raise e

	@property
	def sitedomainttl(self) :
		r""".<br/>Minimum value =  1.
		"""
		try :
			return self._sitedomainttl
		except Exception as e:
			raise e

	@sitedomainttl.setter
	def sitedomainttl(self, sitedomainttl) :
		r""".<br/>Minimum value =  1
		"""
		try :
			self._sitedomainttl = sitedomainttl
		except Exception as e:
			raise e

	@property
	def cookiedomain(self) :
		r""".<br/>Minimum length =  1.
		"""
		try :
			return self._cookiedomain
		except Exception as e:
			raise e

	@cookiedomain.setter
	def cookiedomain(self, cookiedomain) :
		r""".<br/>Minimum length =  1
		"""
		try :
			self._cookiedomain = cookiedomain
		except Exception as e:
			raise e

	@property
	def cookietimeout(self) :
		r""".<br/>Minimum value =  0<br/>Maximum value =  1440.
		"""
		try :
			return self._cookietimeout
		except Exception as e:
			raise e

	@cookietimeout.setter
	def cookietimeout(self, cookietimeout) :
		r""".<br/>Minimum value =  0<br/>Maximum value =  1440
		"""
		try :
			self._cookietimeout = cookietimeout
		except Exception as e:
			raise e

	@property
	def appflowlog(self) :
		r"""Enable logging appflow flow information.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._appflowlog
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(csvserver_domain_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.csvserver_domain_binding
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
		try :
			if resource and type(resource) is not list :
				updateresource = csvserver_domain_binding()
				updateresource.name = resource.name
				updateresource.domainname = resource.domainname
				updateresource.ttl = resource.ttl
				updateresource.backupip = resource.backupip
				updateresource.cookiedomain = resource.cookiedomain
				updateresource.cookietimeout = resource.cookietimeout
				updateresource.sitedomainttl = resource.sitedomainttl
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [csvserver_domain_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].domainname = resource[i].domainname
						updateresources[i].ttl = resource[i].ttl
						updateresources[i].backupip = resource[i].backupip
						updateresources[i].cookiedomain = resource[i].cookiedomain
						updateresources[i].cookietimeout = resource[i].cookietimeout
						updateresources[i].sitedomainttl = resource[i].sitedomainttl
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = csvserver_domain_binding()
				deleteresource.name = resource.name
				deleteresource.domainname = resource.domainname
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [csvserver_domain_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].name = resource[i].name
						deleteresources[i].domainname = resource[i].domainname
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, name="", option_="") :
		r""" Use this API to fetch csvserver_domain_binding resources.
		"""
		try :
			if not name :
				obj = csvserver_domain_binding()
				response = obj.get_resources(service, option_)
			else :
				obj = csvserver_domain_binding()
				obj.name = name
				response = obj.get_resources(service)
				return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, name, filter_) :
		r""" Use this API to fetch filtered set of csvserver_domain_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = csvserver_domain_binding()
			obj.name = name
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, name) :
		r""" Use this API to count csvserver_domain_binding resources configued on NetScaler.
		"""
		try :
			obj = csvserver_domain_binding()
			obj.name = name
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, name, filter_) :
		r""" Use this API to count the filtered set of csvserver_domain_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = csvserver_domain_binding()
			obj.name = name
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	class Bindpoint:
		REQUEST = "REQUEST"
		RESPONSE = "RESPONSE"

	class Appflowlog:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Labeltype:
		reqvserver = "reqvserver"
		resvserver = "resvserver"
		policylabel = "policylabel"

class csvserver_domain_binding_response(base_response) :
	def __init__(self, length=1) :
		self.csvserver_domain_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.csvserver_domain_binding = [csvserver_domain_binding() for _ in range(length)]

