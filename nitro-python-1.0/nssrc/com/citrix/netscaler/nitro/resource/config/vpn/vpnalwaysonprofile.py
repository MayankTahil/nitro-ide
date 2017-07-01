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

class vpnalwaysonprofile(base_resource) :
	""" Configuration for AlwyasON profile resource. """
	def __init__(self) :
		self._name = None
		self._networkaccessonvpnfailure = None
		self._clientcontrol = None
		self._locationbasedvpn = None
		self.___count = 0

	@property
	def name(self) :
		r"""name of AlwaysON profile.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""name of AlwaysON profile.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def networkaccessonvpnfailure(self) :
		r"""Option to block network traffic when tunnel is not established(and the config requires that tunnel be established). When set to onlyToGateway, the network traffic to and from the client (except Gateway IP) is blocked. When set to fullAccess, the network traffic is not blocked.<br/>Default value: fullAccess,<br/>Possible values = onlyToGateway, fullAccess.
		"""
		try :
			return self._networkaccessonvpnfailure
		except Exception as e:
			raise e

	@networkaccessonvpnfailure.setter
	def networkaccessonvpnfailure(self, networkaccessonvpnfailure) :
		r"""Option to block network traffic when tunnel is not established(and the config requires that tunnel be established). When set to onlyToGateway, the network traffic to and from the client (except Gateway IP) is blocked. When set to fullAccess, the network traffic is not blocked.<br/>Default value: fullAccess,<br/>Possible values = onlyToGateway, fullAccess
		"""
		try :
			self._networkaccessonvpnfailure = networkaccessonvpnfailure
		except Exception as e:
			raise e

	@property
	def clientcontrol(self) :
		r"""Allow/Deny user to log off and connect to another Gateway.<br/>Default value: DENY<br/>Possible values = ALLOW, DENY.
		"""
		try :
			return self._clientcontrol
		except Exception as e:
			raise e

	@clientcontrol.setter
	def clientcontrol(self, clientcontrol) :
		r"""Allow/Deny user to log off and connect to another Gateway.<br/>Default value: DENY<br/>Possible values = ALLOW, DENY
		"""
		try :
			self._clientcontrol = clientcontrol
		except Exception as e:
			raise e

	@property
	def locationbasedvpn(self) :
		r"""Option to decide if tunnel should be established when in enterprise network. When locationBasedVPN is remote, client tries to detect if it is located in enterprise network or not and establishes the tunnel if not in enterprise network. Dns suffixes configured using -add dns suffix- are used to decide if the client is in the enterprise network or not. If the resolution of the DNS suffix results in private IP, client is said to be in enterprise network. When set to EveryWhere, the client skips the check to detect if it is on the enterprise network and tries to establish the tunnel.<br/>Default value: Remote<br/>Possible values = Remote, Everywhere.
		"""
		try :
			return self._locationbasedvpn
		except Exception as e:
			raise e

	@locationbasedvpn.setter
	def locationbasedvpn(self, locationbasedvpn) :
		r"""Option to decide if tunnel should be established when in enterprise network. When locationBasedVPN is remote, client tries to detect if it is located in enterprise network or not and establishes the tunnel if not in enterprise network. Dns suffixes configured using -add dns suffix- are used to decide if the client is in the enterprise network or not. If the resolution of the DNS suffix results in private IP, client is said to be in enterprise network. When set to EveryWhere, the client skips the check to detect if it is on the enterprise network and tries to establish the tunnel.<br/>Default value: Remote<br/>Possible values = Remote, Everywhere
		"""
		try :
			self._locationbasedvpn = locationbasedvpn
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(vpnalwaysonprofile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.vpnalwaysonprofile
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
		r""" Use this API to add vpnalwaysonprofile.
		"""
		try :
			if type(resource) is not list :
				addresource = vpnalwaysonprofile()
				addresource.name = resource.name
				addresource.networkaccessonvpnfailure = resource.networkaccessonvpnfailure
				addresource.clientcontrol = resource.clientcontrol
				addresource.locationbasedvpn = resource.locationbasedvpn
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ vpnalwaysonprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].networkaccessonvpnfailure = resource[i].networkaccessonvpnfailure
						addresources[i].clientcontrol = resource[i].clientcontrol
						addresources[i].locationbasedvpn = resource[i].locationbasedvpn
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete vpnalwaysonprofile.
		"""
		try :
			if type(resource) is not list :
				deleteresource = vpnalwaysonprofile()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ vpnalwaysonprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ vpnalwaysonprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update vpnalwaysonprofile.
		"""
		try :
			if type(resource) is not list :
				updateresource = vpnalwaysonprofile()
				updateresource.name = resource.name
				updateresource.networkaccessonvpnfailure = resource.networkaccessonvpnfailure
				updateresource.clientcontrol = resource.clientcontrol
				updateresource.locationbasedvpn = resource.locationbasedvpn
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ vpnalwaysonprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].networkaccessonvpnfailure = resource[i].networkaccessonvpnfailure
						updateresources[i].clientcontrol = resource[i].clientcontrol
						updateresources[i].locationbasedvpn = resource[i].locationbasedvpn
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of vpnalwaysonprofile resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = vpnalwaysonprofile()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ vpnalwaysonprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ vpnalwaysonprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the vpnalwaysonprofile resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = vpnalwaysonprofile()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = vpnalwaysonprofile()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [vpnalwaysonprofile() for _ in range(len(name))]
						obj = [vpnalwaysonprofile() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = vpnalwaysonprofile()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of vpnalwaysonprofile resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = vpnalwaysonprofile()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the vpnalwaysonprofile resources configured on NetScaler.
		"""
		try :
			obj = vpnalwaysonprofile()
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
		r""" Use this API to count filtered the set of vpnalwaysonprofile resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = vpnalwaysonprofile()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Locationbasedvpn:
		Remote = "Remote"
		Everywhere = "Everywhere"

	class Clientcontrol:
		ALLOW = "ALLOW"
		DENY = "DENY"

	class Networkaccessonvpnfailure:
		onlyToGateway = "onlyToGateway"
		fullAccess = "fullAccess"

class vpnalwaysonprofile_response(base_response) :
	def __init__(self, length=1) :
		self.vpnalwaysonprofile = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.vpnalwaysonprofile = [vpnalwaysonprofile() for _ in range(length)]

