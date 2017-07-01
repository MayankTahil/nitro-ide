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

class vpnpcoipprofile(base_resource) :
	""" Configuration for PCoIP session profile resource. """
	def __init__(self) :
		self._name = None
		self._conserverurl = None
		self._icvverification = None
		self._sessionidletimeout = None
		self.___count = 0

	@property
	def name(self) :
		r"""name of PCoIP profile.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""name of PCoIP profile.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def conserverurl(self) :
		r"""Connection server URL.
		"""
		try :
			return self._conserverurl
		except Exception as e:
			raise e

	@conserverurl.setter
	def conserverurl(self, conserverurl) :
		r"""Connection server URL.
		"""
		try :
			self._conserverurl = conserverurl
		except Exception as e:
			raise e

	@property
	def icvverification(self) :
		r"""ICV verification for PCOIP transport packets.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._icvverification
		except Exception as e:
			raise e

	@icvverification.setter
	def icvverification(self, icvverification) :
		r"""ICV verification for PCOIP transport packets.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._icvverification = icvverification
		except Exception as e:
			raise e

	@property
	def sessionidletimeout(self) :
		r"""PCOIP Idle Session timeout.<br/>Default value: 180<br/>Minimum length =  30<br/>Maximum length =  240.
		"""
		try :
			return self._sessionidletimeout
		except Exception as e:
			raise e

	@sessionidletimeout.setter
	def sessionidletimeout(self, sessionidletimeout) :
		r"""PCOIP Idle Session timeout.<br/>Default value: 180<br/>Minimum length =  30<br/>Maximum length =  240
		"""
		try :
			self._sessionidletimeout = sessionidletimeout
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(vpnpcoipprofile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.vpnpcoipprofile
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
		r""" Use this API to add vpnpcoipprofile.
		"""
		try :
			if type(resource) is not list :
				addresource = vpnpcoipprofile()
				addresource.name = resource.name
				addresource.conserverurl = resource.conserverurl
				addresource.icvverification = resource.icvverification
				addresource.sessionidletimeout = resource.sessionidletimeout
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ vpnpcoipprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].conserverurl = resource[i].conserverurl
						addresources[i].icvverification = resource[i].icvverification
						addresources[i].sessionidletimeout = resource[i].sessionidletimeout
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete vpnpcoipprofile.
		"""
		try :
			if type(resource) is not list :
				deleteresource = vpnpcoipprofile()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ vpnpcoipprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ vpnpcoipprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update vpnpcoipprofile.
		"""
		try :
			if type(resource) is not list :
				updateresource = vpnpcoipprofile()
				updateresource.name = resource.name
				updateresource.conserverurl = resource.conserverurl
				updateresource.icvverification = resource.icvverification
				updateresource.sessionidletimeout = resource.sessionidletimeout
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ vpnpcoipprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].conserverurl = resource[i].conserverurl
						updateresources[i].icvverification = resource[i].icvverification
						updateresources[i].sessionidletimeout = resource[i].sessionidletimeout
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of vpnpcoipprofile resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = vpnpcoipprofile()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ vpnpcoipprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ vpnpcoipprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the vpnpcoipprofile resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = vpnpcoipprofile()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = vpnpcoipprofile()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [vpnpcoipprofile() for _ in range(len(name))]
						obj = [vpnpcoipprofile() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = vpnpcoipprofile()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of vpnpcoipprofile resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = vpnpcoipprofile()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the vpnpcoipprofile resources configured on NetScaler.
		"""
		try :
			obj = vpnpcoipprofile()
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
		r""" Use this API to count filtered the set of vpnpcoipprofile resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = vpnpcoipprofile()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Icvverification:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class vpnpcoipprofile_response(base_response) :
	def __init__(self, length=1) :
		self.vpnpcoipprofile = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.vpnpcoipprofile = [vpnpcoipprofile() for _ in range(length)]

