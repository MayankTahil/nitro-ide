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

class vpnicaconnection(base_resource) :
	""" Configuration for active ica connections resource. """
	def __init__(self) :
		self._username = None
		self._transproto = None
		self._nodeid = None
		self._all = None
		self._domain = None
		self._srcip = None
		self._srcport = None
		self._destip = None
		self._destport = None
		self._peid = None
		self.___count = 0

	@property
	def username(self) :
		r"""User name for which to display connections.<br/>Minimum length =  1.
		"""
		try :
			return self._username
		except Exception as e:
			raise e

	@username.setter
	def username(self, username) :
		r"""User name for which to display connections.<br/>Minimum length =  1
		"""
		try :
			self._username = username
		except Exception as e:
			raise e

	@property
	def transproto(self) :
		r"""Transport type for the existing Existing ICA conenction.<br/>Possible values = TCP, UDP.
		"""
		try :
			return self._transproto
		except Exception as e:
			raise e

	@transproto.setter
	def transproto(self, transproto) :
		r"""Transport type for the existing Existing ICA conenction.<br/>Possible values = TCP, UDP
		"""
		try :
			self._transproto = transproto
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
		r"""Terminate all active icaconnections.
		"""
		try :
			return self._all
		except Exception as e:
			raise e

	@all.setter
	def all(self, all) :
		r"""Terminate all active icaconnections.
		"""
		try :
			self._all = all
		except Exception as e:
			raise e

	@property
	def domain(self) :
		r"""The domain name.
		"""
		try :
			return self._domain
		except Exception as e:
			raise e

	@property
	def srcip(self) :
		r"""The client IP address.
		"""
		try :
			return self._srcip
		except Exception as e:
			raise e

	@property
	def srcport(self) :
		r"""The client port.<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API.
		"""
		try :
			return self._srcport
		except Exception as e:
			raise e

	@property
	def destip(self) :
		r"""The CPS server IP address.
		"""
		try :
			return self._destip
		except Exception as e:
			raise e

	@property
	def destport(self) :
		r"""The CPS server port.<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API.
		"""
		try :
			return self._destport
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
			result = service.payload_formatter.string_to_resource(vpnicaconnection_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.vpnicaconnection
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
		r""" Use this API to kill vpnicaconnection.
		"""
		try :
			if type(resource) is not list :
				killresource = vpnicaconnection()
				killresource.username = resource.username
				killresource.transproto = resource.transproto
				killresource.all = resource.all
				return killresource.perform_operation(client,"kill")
			else :
				if (resource and len(resource) > 0) :
					killresources = [ vpnicaconnection() for _ in range(len(resource))]
					for i in range(len(resource)) :
						killresources[i].username = resource[i].username
						killresources[i].transproto = resource[i].transproto
						killresources[i].all = resource[i].all
				result = cls.perform_operation_bulk_request(client, killresources,"kill")
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the vpnicaconnection resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = vpnicaconnection()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		r""" Use this API to fetch all the vpnicaconnection resources that are configured on netscaler.
	# This uses vpnicaconnection_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = vpnicaconnection()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of vpnicaconnection resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = vpnicaconnection()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the vpnicaconnection resources configured on NetScaler.
		"""
		try :
			obj = vpnicaconnection()
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
		r""" Use this API to count filtered the set of vpnicaconnection resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = vpnicaconnection()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Transproto:
		TCP = "TCP"
		UDP = "UDP"

class vpnicaconnection_response(base_response) :
	def __init__(self, length=1) :
		self.vpnicaconnection = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.vpnicaconnection = [vpnicaconnection() for _ in range(length)]

