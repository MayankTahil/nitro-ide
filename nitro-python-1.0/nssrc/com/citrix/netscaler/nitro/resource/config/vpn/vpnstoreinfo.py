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

class vpnstoreinfo(base_resource) :
	""" Configuration for Store information for a URL resource. """
	def __init__(self) :
		self._url = None
		self._storeserverstatus = None
		self._storeserverissf = None
		self._storeapisupport = None
		self._storelist = None
		self._storestatus = None
		self.___count = 0

	@property
	def url(self) :
		r"""StoreFront URL to be scanned.
		"""
		try :
			return self._url
		except Exception as e:
			raise e

	@url.setter
	def url(self, url) :
		r"""StoreFront URL to be scanned.
		"""
		try :
			self._url = url
		except Exception as e:
			raise e

	@property
	def storeserverstatus(self) :
		r"""Availability of the server for TCP connections.<br/>Possible values = UP, DOWN.
		"""
		try :
			return self._storeserverstatus
		except Exception as e:
			raise e

	@property
	def storeserverissf(self) :
		r"""Indicates if the server being scanned is running StoreFront.<br/>Possible values = YES, NO.
		"""
		try :
			return self._storeserverissf
		except Exception as e:
			raise e

	@property
	def storeapisupport(self) :
		r"""Indicates StoreFront API support status.<br/>Possible values = YES, NO.
		"""
		try :
			return self._storeapisupport
		except Exception as e:
			raise e

	@property
	def storelist(self) :
		r"""List of available stores return by StoreFront API.
		"""
		try :
			return self._storelist
		except Exception as e:
			raise e

	@property
	def storestatus(self) :
		r"""Availability of the specified StoreFront store.<br/>Possible values = UP, DOWN.
		"""
		try :
			return self._storestatus
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(vpnstoreinfo_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.vpnstoreinfo
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
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the vpnstoreinfo resources that are configured on netscaler.
		"""
		try :
			if type(name) is not list :
				if type(name) == cls :
					raise Exception('Invalid parameter name:{0}'.format(type(name)))
				option_ = options()
				option_.args = nitro_util.object_to_string_withoutquotes(name)
				response = name.get_resource(client, option_)
			else :
				if name and len(name) > 0 :
					if type(name[0]) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
					response = [vpnstoreinfo() for _ in range(len(name))]
					for i in range(len(name)) :
						option_ = options()
						option_.args = nitro_util.object_to_string_withoutquotes(name[i])
						response[i] = name[i].get_resource(client, option_)
				return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		r""" Use this API to fetch all the vpnstoreinfo resources that are configured on netscaler.
	# This uses vpnstoreinfo_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = vpnstoreinfo()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_, obj) :
		r""" Use this API to fetch filtered set of vpnstoreinfo resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			option_ = options()
			option_.filter = filter_
			option_.args = nitro_util.object_to_string_withoutquotes(obj)
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client, obj) :
		r""" Use this API to count the vpnstoreinfo resources configured on NetScaler.
		"""
		try :
			option_ = options()
			option_.count = True
			option_.args = nitro_util.object_to_string_withoutquotes(obj)
			response = obj.get_resources(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	@classmethod
	def count_filtered(cls, client, filter_, obj) :
		r""" Use this API to count filtered the set of vpnstoreinfo resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			option_ = options()
			option_.count = True
			option_.filter = filter_
			option_.args = nitro_util.object_to_string_withoutquotes(obj)
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Storestatus:
		UP = "UP"
		DOWN = "DOWN"

	class Storeserverstatus:
		UP = "UP"
		DOWN = "DOWN"

	class Storeserverissf:
		YES = "YES"
		NO = "NO"

	class Storeapisupport:
		YES = "YES"
		NO = "NO"

class vpnstoreinfo_response(base_response) :
	def __init__(self, length=1) :
		self.vpnstoreinfo = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.vpnstoreinfo = [vpnstoreinfo() for _ in range(length)]

