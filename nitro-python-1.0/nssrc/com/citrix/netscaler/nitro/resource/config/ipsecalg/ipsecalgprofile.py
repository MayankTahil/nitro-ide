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

class ipsecalgprofile(base_resource) :
	""" Configuration for IPSEC ALG profile resource. """
	def __init__(self) :
		self._name = None
		self._ikesessiontimeout = None
		self._espsessiontimeout = None
		self._espgatetimeout = None
		self._connfailover = None
		self.___count = 0

	@property
	def name(self) :
		r"""The name of the ipsec alg profile.<br/>Minimum length =  1<br/>Maximum length =  32.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""The name of the ipsec alg profile.<br/>Minimum length =  1<br/>Maximum length =  32
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def ikesessiontimeout(self) :
		r"""IKE session timeout in minutes.<br/>Default value: 60<br/>Minimum length =  1<br/>Maximum length =  1440.
		"""
		try :
			return self._ikesessiontimeout
		except Exception as e:
			raise e

	@ikesessiontimeout.setter
	def ikesessiontimeout(self, ikesessiontimeout) :
		r"""IKE session timeout in minutes.<br/>Default value: 60<br/>Minimum length =  1<br/>Maximum length =  1440
		"""
		try :
			self._ikesessiontimeout = ikesessiontimeout
		except Exception as e:
			raise e

	@property
	def espsessiontimeout(self) :
		r"""ESP session timeout in minutes.<br/>Default value: 60<br/>Minimum length =  1<br/>Maximum length =  1440.
		"""
		try :
			return self._espsessiontimeout
		except Exception as e:
			raise e

	@espsessiontimeout.setter
	def espsessiontimeout(self, espsessiontimeout) :
		r"""ESP session timeout in minutes.<br/>Default value: 60<br/>Minimum length =  1<br/>Maximum length =  1440
		"""
		try :
			self._espsessiontimeout = espsessiontimeout
		except Exception as e:
			raise e

	@property
	def espgatetimeout(self) :
		r"""Timeout ESP in seconds as no ESP packets are seen after IKE negotiation.<br/>Default value: 60<br/>Minimum length =  30<br/>Maximum length =  1200.
		"""
		try :
			return self._espgatetimeout
		except Exception as e:
			raise e

	@espgatetimeout.setter
	def espgatetimeout(self, espgatetimeout) :
		r"""Timeout ESP in seconds as no ESP packets are seen after IKE negotiation.<br/>Default value: 60<br/>Minimum length =  30<br/>Maximum length =  1200
		"""
		try :
			self._espgatetimeout = espgatetimeout
		except Exception as e:
			raise e

	@property
	def connfailover(self) :
		r"""Mode in which the connection failover feature must operate for the IPSec Alg. After a failover, established UDP connections and ESP packet flows are kept active and resumed on the secondary appliance. Recomended setting is ENABLED.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._connfailover
		except Exception as e:
			raise e

	@connfailover.setter
	def connfailover(self, connfailover) :
		r"""Mode in which the connection failover feature must operate for the IPSec Alg. After a failover, established UDP connections and ESP packet flows are kept active and resumed on the secondary appliance. Recomended setting is ENABLED.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._connfailover = connfailover
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(ipsecalgprofile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ipsecalgprofile
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
		r""" Use this API to add ipsecalgprofile.
		"""
		try :
			if type(resource) is not list :
				addresource = ipsecalgprofile()
				addresource.name = resource.name
				addresource.ikesessiontimeout = resource.ikesessiontimeout
				addresource.espsessiontimeout = resource.espsessiontimeout
				addresource.espgatetimeout = resource.espgatetimeout
				addresource.connfailover = resource.connfailover
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ ipsecalgprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].ikesessiontimeout = resource[i].ikesessiontimeout
						addresources[i].espsessiontimeout = resource[i].espsessiontimeout
						addresources[i].espgatetimeout = resource[i].espgatetimeout
						addresources[i].connfailover = resource[i].connfailover
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update ipsecalgprofile.
		"""
		try :
			if type(resource) is not list :
				updateresource = ipsecalgprofile()
				updateresource.name = resource.name
				updateresource.ikesessiontimeout = resource.ikesessiontimeout
				updateresource.espsessiontimeout = resource.espsessiontimeout
				updateresource.espgatetimeout = resource.espgatetimeout
				updateresource.connfailover = resource.connfailover
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ ipsecalgprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].ikesessiontimeout = resource[i].ikesessiontimeout
						updateresources[i].espsessiontimeout = resource[i].espsessiontimeout
						updateresources[i].espgatetimeout = resource[i].espgatetimeout
						updateresources[i].connfailover = resource[i].connfailover
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of ipsecalgprofile resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = ipsecalgprofile()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ ipsecalgprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ ipsecalgprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete ipsecalgprofile.
		"""
		try :
			if type(resource) is not list :
				deleteresource = ipsecalgprofile()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ ipsecalgprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ ipsecalgprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the ipsecalgprofile resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = ipsecalgprofile()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = ipsecalgprofile()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [ipsecalgprofile() for _ in range(len(name))]
						obj = [ipsecalgprofile() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = ipsecalgprofile()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of ipsecalgprofile resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = ipsecalgprofile()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the ipsecalgprofile resources configured on NetScaler.
		"""
		try :
			obj = ipsecalgprofile()
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
		r""" Use this API to count filtered the set of ipsecalgprofile resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = ipsecalgprofile()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Connfailover:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class ipsecalgprofile_response(base_response) :
	def __init__(self, length=1) :
		self.ipsecalgprofile = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.ipsecalgprofile = [ipsecalgprofile() for _ in range(length)]

