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

class gslbldnsentries(base_resource) :
	""" Configuration for LDNS entry resource. """
	def __init__(self) :
		self._nodeid = None
		self._sitename = None
		self._numsites = None
		self._ipaddress = None
		self._ttl = None
		self._name = None
		self._rtt = []
		self.___count = 0

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
	def sitename(self) :
		r"""The GSLB site name.
		"""
		try :
			return self._sitename
		except Exception as e:
			raise e

	@property
	def numsites(self) :
		r"""Specifies the number of gslb sites.
		"""
		try :
			return self._numsites
		except Exception as e:
			raise e

	@property
	def ipaddress(self) :
		r"""IP address of the LDNS server.
		"""
		try :
			return self._ipaddress
		except Exception as e:
			raise e

	@property
	def ttl(self) :
		r"""TTL value of the LDNS entry.
		"""
		try :
			return self._ttl
		except Exception as e:
			raise e

	@property
	def name(self) :
		r"""Monitor that is currently being used to monitor the LDNS ip..
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@property
	def rtt(self) :
		r"""RTT value of the LDNS entry for all gslb sites.
		"""
		try :
			return self._rtt
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(gslbldnsentries_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.gslbldnsentries
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
	def clear(cls, client, resource="") :
		r""" Use this API to clear gslbldnsentries.
		"""
		try :
			if type(resource) is not list :
				clearresource = gslbldnsentries()
				return clearresource.perform_operation(client,"clear")
			else :
				if (resource and len(resource) > 0) :
					clearresources = [ gslbldnsentries() for _ in range(len(resource))]
				result = cls.perform_operation_bulk_request(client, clearresources,"clear")
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the gslbldnsentries resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = gslbldnsentries()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		r""" Use this API to fetch all the gslbldnsentries resources that are configured on netscaler.
	# This uses gslbldnsentries_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = gslbldnsentries()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of gslbldnsentries resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = gslbldnsentries()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the gslbldnsentries resources configured on NetScaler.
		"""
		try :
			obj = gslbldnsentries()
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
		r""" Use this API to count filtered the set of gslbldnsentries resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = gslbldnsentries()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


class gslbldnsentries_response(base_response) :
	def __init__(self, length=1) :
		self.gslbldnsentries = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.gslbldnsentries = [gslbldnsentries() for _ in range(length)]

