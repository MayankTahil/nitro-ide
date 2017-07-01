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

class authenticationstorefrontauthaction(base_resource) :
	""" Configuration for Storefront authentication action resource. """
	def __init__(self) :
		self._name = None
		self._serverurl = None
		self._domain = None
		self._defaultauthenticationgroup = None
		self._success = None
		self._failure = None
		self.___count = 0

	@property
	def name(self) :
		r"""Name for the Storefront Authentication action. 
		Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed after the profile is created.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my authentication action" or 'my authentication action').<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name for the Storefront Authentication action. 
		Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed after the profile is created.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my authentication action" or 'my authentication action').<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def serverurl(self) :
		r"""URL of the Storefront server. This is the FQDN of the Storefront server. example: https://storefront.com/.  Authentication endpoints are learned dynamically by Gateway.
		"""
		try :
			return self._serverurl
		except Exception as e:
			raise e

	@serverurl.setter
	def serverurl(self, serverurl) :
		r"""URL of the Storefront server. This is the FQDN of the Storefront server. example: https://storefront.com/.  Authentication endpoints are learned dynamically by Gateway.
		"""
		try :
			self._serverurl = serverurl
		except Exception as e:
			raise e

	@property
	def domain(self) :
		r"""Domain of the server that is used for authentication. If users enter name without domain, this parameter is added to username in the authentication request to server.
		"""
		try :
			return self._domain
		except Exception as e:
			raise e

	@domain.setter
	def domain(self, domain) :
		r"""Domain of the server that is used for authentication. If users enter name without domain, this parameter is added to username in the authentication request to server.
		"""
		try :
			self._domain = domain
		except Exception as e:
			raise e

	@property
	def defaultauthenticationgroup(self) :
		r"""This is the default group that is chosen when the authentication succeeds in addition to extracted groups.
		"""
		try :
			return self._defaultauthenticationgroup
		except Exception as e:
			raise e

	@defaultauthenticationgroup.setter
	def defaultauthenticationgroup(self, defaultauthenticationgroup) :
		r"""This is the default group that is chosen when the authentication succeeds in addition to extracted groups.
		"""
		try :
			self._defaultauthenticationgroup = defaultauthenticationgroup
		except Exception as e:
			raise e

	@property
	def success(self) :
		try :
			return self._success
		except Exception as e:
			raise e

	@property
	def failure(self) :
		try :
			return self._failure
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(authenticationstorefrontauthaction_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.authenticationstorefrontauthaction
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
		r""" Use this API to add authenticationstorefrontauthaction.
		"""
		try :
			if type(resource) is not list :
				addresource = authenticationstorefrontauthaction()
				addresource.name = resource.name
				addresource.serverurl = resource.serverurl
				addresource.domain = resource.domain
				addresource.defaultauthenticationgroup = resource.defaultauthenticationgroup
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ authenticationstorefrontauthaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].serverurl = resource[i].serverurl
						addresources[i].domain = resource[i].domain
						addresources[i].defaultauthenticationgroup = resource[i].defaultauthenticationgroup
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete authenticationstorefrontauthaction.
		"""
		try :
			if type(resource) is not list :
				deleteresource = authenticationstorefrontauthaction()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ authenticationstorefrontauthaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ authenticationstorefrontauthaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update authenticationstorefrontauthaction.
		"""
		try :
			if type(resource) is not list :
				updateresource = authenticationstorefrontauthaction()
				updateresource.name = resource.name
				updateresource.serverurl = resource.serverurl
				updateresource.domain = resource.domain
				updateresource.defaultauthenticationgroup = resource.defaultauthenticationgroup
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ authenticationstorefrontauthaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].serverurl = resource[i].serverurl
						updateresources[i].domain = resource[i].domain
						updateresources[i].defaultauthenticationgroup = resource[i].defaultauthenticationgroup
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of authenticationstorefrontauthaction resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = authenticationstorefrontauthaction()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ authenticationstorefrontauthaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ authenticationstorefrontauthaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the authenticationstorefrontauthaction resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = authenticationstorefrontauthaction()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = authenticationstorefrontauthaction()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [authenticationstorefrontauthaction() for _ in range(len(name))]
						obj = [authenticationstorefrontauthaction() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = authenticationstorefrontauthaction()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of authenticationstorefrontauthaction resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = authenticationstorefrontauthaction()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the authenticationstorefrontauthaction resources configured on NetScaler.
		"""
		try :
			obj = authenticationstorefrontauthaction()
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
		r""" Use this API to count filtered the set of authenticationstorefrontauthaction resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = authenticationstorefrontauthaction()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


class authenticationstorefrontauthaction_response(base_response) :
	def __init__(self, length=1) :
		self.authenticationstorefrontauthaction = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.authenticationstorefrontauthaction = [authenticationstorefrontauthaction() for _ in range(length)]

