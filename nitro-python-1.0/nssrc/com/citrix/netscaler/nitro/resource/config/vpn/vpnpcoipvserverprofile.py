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

class vpnpcoipvserverprofile(base_resource) :
	""" Configuration for PCoIP vserver profile resource. """
	def __init__(self) :
		self._name = None
		self._logindomain = None
		self._udpport = None
		self.___count = 0

	@property
	def name(self) :
		r"""name of PCoIP vserver profile.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""name of PCoIP vserver profile.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def logindomain(self) :
		r"""Login domain for PCoIP users.
		"""
		try :
			return self._logindomain
		except Exception as e:
			raise e

	@logindomain.setter
	def logindomain(self, logindomain) :
		r"""Login domain for PCoIP users.
		"""
		try :
			self._logindomain = logindomain
		except Exception as e:
			raise e

	@property
	def udpport(self) :
		r"""UDP port for PCoIP data traffic.<br/>Default value: 4172<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API.
		"""
		try :
			return self._udpport
		except Exception as e:
			raise e

	@udpport.setter
	def udpport(self, udpport) :
		r"""UDP port for PCoIP data traffic.<br/>Default value: 4172<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API
		"""
		try :
			self._udpport = udpport
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(vpnpcoipvserverprofile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.vpnpcoipvserverprofile
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
		r""" Use this API to add vpnpcoipvserverprofile.
		"""
		try :
			if type(resource) is not list :
				addresource = vpnpcoipvserverprofile()
				addresource.name = resource.name
				addresource.logindomain = resource.logindomain
				addresource.udpport = resource.udpport
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ vpnpcoipvserverprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].logindomain = resource[i].logindomain
						addresources[i].udpport = resource[i].udpport
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete vpnpcoipvserverprofile.
		"""
		try :
			if type(resource) is not list :
				deleteresource = vpnpcoipvserverprofile()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ vpnpcoipvserverprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ vpnpcoipvserverprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update vpnpcoipvserverprofile.
		"""
		try :
			if type(resource) is not list :
				updateresource = vpnpcoipvserverprofile()
				updateresource.name = resource.name
				updateresource.udpport = resource.udpport
				updateresource.logindomain = resource.logindomain
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ vpnpcoipvserverprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].udpport = resource[i].udpport
						updateresources[i].logindomain = resource[i].logindomain
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of vpnpcoipvserverprofile resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = vpnpcoipvserverprofile()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ vpnpcoipvserverprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ vpnpcoipvserverprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the vpnpcoipvserverprofile resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = vpnpcoipvserverprofile()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = vpnpcoipvserverprofile()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [vpnpcoipvserverprofile() for _ in range(len(name))]
						obj = [vpnpcoipvserverprofile() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = vpnpcoipvserverprofile()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of vpnpcoipvserverprofile resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = vpnpcoipvserverprofile()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the vpnpcoipvserverprofile resources configured on NetScaler.
		"""
		try :
			obj = vpnpcoipvserverprofile()
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
		r""" Use this API to count filtered the set of vpnpcoipvserverprofile resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = vpnpcoipvserverprofile()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


class vpnpcoipvserverprofile_response(base_response) :
	def __init__(self, length=1) :
		self.vpnpcoipvserverprofile = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.vpnpcoipvserverprofile = [vpnpcoipvserverprofile() for _ in range(length)]

