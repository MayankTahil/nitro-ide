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

class aaasession(base_resource) :
	""" Configuration for active connection resource. """
	def __init__(self) :
		self._username = None
		self._groupname = None
		self._iip = None
		self._netmask = None
		self._nodeid = None
		self._all = None
		self._publicip = None
		self._publicport = None
		self._ipaddress = None
		self._port = None
		self._privateip = None
		self._privateport = None
		self._destip = None
		self._destport = None
		self._intranetip = None
		self._intranetip6 = None
		self._peid = None
		self.___count = 0

	@property
	def username(self) :
		r"""Name of the AAA user.<br/>Minimum length =  1.
		"""
		try :
			return self._username
		except Exception as e:
			raise e

	@username.setter
	def username(self, username) :
		r"""Name of the AAA user.<br/>Minimum length =  1
		"""
		try :
			self._username = username
		except Exception as e:
			raise e

	@property
	def groupname(self) :
		r"""Name of the AAA group.<br/>Minimum length =  1.
		"""
		try :
			return self._groupname
		except Exception as e:
			raise e

	@groupname.setter
	def groupname(self, groupname) :
		r"""Name of the AAA group.<br/>Minimum length =  1
		"""
		try :
			self._groupname = groupname
		except Exception as e:
			raise e

	@property
	def iip(self) :
		r"""IP address or the first address in the intranet IP range.<br/>Minimum length =  1.
		"""
		try :
			return self._iip
		except Exception as e:
			raise e

	@iip.setter
	def iip(self, iip) :
		r"""IP address or the first address in the intranet IP range.<br/>Minimum length =  1
		"""
		try :
			self._iip = iip
		except Exception as e:
			raise e

	@property
	def netmask(self) :
		r"""Subnet mask for the intranet IP range.<br/>Minimum length =  1.
		"""
		try :
			return self._netmask
		except Exception as e:
			raise e

	@netmask.setter
	def netmask(self, netmask) :
		r"""Subnet mask for the intranet IP range.<br/>Minimum length =  1
		"""
		try :
			self._netmask = netmask
		except Exception as e:
			raise e

	@property
	def nodeid(self) :
		r"""Unique number that identifies the cluster node.<br/>Maximum length =  31.
		"""
		try :
			return self._nodeid
		except Exception as e:
			raise e

	@nodeid.setter
	def nodeid(self, nodeid) :
		r"""Unique number that identifies the cluster node.<br/>Maximum length =  31
		"""
		try :
			self._nodeid = nodeid
		except Exception as e:
			raise e

	@property
	def all(self) :
		r"""Terminate all active AAA-TM/VPN sessions.
		"""
		try :
			return self._all
		except Exception as e:
			raise e

	@all.setter
	def all(self, all) :
		r"""Terminate all active AAA-TM/VPN sessions.
		"""
		try :
			self._all = all
		except Exception as e:
			raise e

	@property
	def publicip(self) :
		r"""Client's public IP address.
		"""
		try :
			return self._publicip
		except Exception as e:
			raise e

	@property
	def publicport(self) :
		r"""Client's public port.<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API.
		"""
		try :
			return self._publicport
		except Exception as e:
			raise e

	@property
	def ipaddress(self) :
		r"""NetScaler's IP address.
		"""
		try :
			return self._ipaddress
		except Exception as e:
			raise e

	@property
	def port(self) :
		r"""NetScaler's port.<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API.
		"""
		try :
			return self._port
		except Exception as e:
			raise e

	@property
	def privateip(self) :
		r"""Client's private/mapped IP address.
		"""
		try :
			return self._privateip
		except Exception as e:
			raise e

	@property
	def privateport(self) :
		r"""Client's private/mapped port.<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API.
		"""
		try :
			return self._privateport
		except Exception as e:
			raise e

	@property
	def destip(self) :
		r"""Destination IP address.
		"""
		try :
			return self._destip
		except Exception as e:
			raise e

	@property
	def destport(self) :
		r"""Destination port.<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API.
		"""
		try :
			return self._destport
		except Exception as e:
			raise e

	@property
	def intranetip(self) :
		r"""Specifies the Intranet IP.
		"""
		try :
			return self._intranetip
		except Exception as e:
			raise e

	@property
	def intranetip6(self) :
		r"""Specifies the Intranet IP6.
		"""
		try :
			return self._intranetip6
		except Exception as e:
			raise e

	@property
	def peid(self) :
		r"""Core id of the session owner.
		"""
		try :
			return self._peid
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(aaasession_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.aaasession
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			return 0
		except Exception as e :
			raise e



	@classmethod
	def kill(cls, client, resource) :
		r""" Use this API to kill aaasession.
		"""
		try :
			if type(resource) is not list :
				killresource = aaasession()
				killresource.username = resource.username
				killresource.groupname = resource.groupname
				killresource.iip = resource.iip
				killresource.netmask = resource.netmask
				killresource.all = resource.all
				return killresource.perform_operation(client,"kill")
			else :
				if (resource and len(resource) > 0) :
					killresources = [ aaasession() for _ in range(len(resource))]
					for i in range(len(resource)) :
						killresources[i].username = resource[i].username
						killresources[i].groupname = resource[i].groupname
						killresources[i].iip = resource[i].iip
						killresources[i].netmask = resource[i].netmask
						killresources[i].all = resource[i].all
				result = cls.perform_operation_bulk_request(client, killresources,"kill")
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the aaasession resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = aaasession()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		r""" Use this API to fetch all the aaasession resources that are configured on netscaler.
	# This uses aaasession_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = aaasession()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of aaasession resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = aaasession()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the aaasession resources configured on NetScaler.
		"""
		try :
			obj = aaasession()
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
		r""" Use this API to count filtered the set of aaasession resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = aaasession()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


class aaasession_response(base_response) :
	def __init__(self, length=1) :
		self.aaasession = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.aaasession = [aaasession() for _ in range(length)]

