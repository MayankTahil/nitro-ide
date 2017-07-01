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

class nssourceroutecachetable(base_resource) :
	""" Configuration for Source IP Mac Cache Table. resource. """

		#------- Read only Parameter ---------

	def __init__(self) :
		self._sourceip = None
		self._sourcemac = None
		self._vlan = None
		self._Interface = None
		self.___count = 0

	@property
	def sourceip(self) :
		r"""Source ip of the connection.
		"""
		try :
			return self._sourceip
		except Exception as e:
			raise e

	@property
	def sourcemac(self) :
		r"""source MAC address of an incoming IPv6 packet.
		"""
		try :
			return self._sourcemac
		except Exception as e:
			raise e

	@property
	def vlan(self) :
		r"""ID of the VLAN.
		"""
		try :
			return self._vlan
		except Exception as e:
			raise e

	@property
	def Interface(self) :
		r"""ID of an interface.
		"""
		try :
			return self._Interface
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nssourceroutecachetable_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nssourceroutecachetable
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
	def flush(cls, client, resource="") :
		r""" Use this API to flush nssourceroutecachetable.
		"""
		try :
			if type(resource) is not list :
				flushresource = nssourceroutecachetable()
				return flushresource.perform_operation(client,"flush")
			else :
				if (resource and len(resource) > 0) :
					flushresources = [ nssourceroutecachetable() for _ in range(len(resource))]
				result = cls.perform_operation_bulk_request(client, flushresources,"flush")
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the nssourceroutecachetable resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nssourceroutecachetable()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of nssourceroutecachetable resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nssourceroutecachetable()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the nssourceroutecachetable resources configured on NetScaler.
		"""
		try :
			obj = nssourceroutecachetable()
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
		r""" Use this API to count filtered the set of nssourceroutecachetable resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nssourceroutecachetable()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


class nssourceroutecachetable_response(base_response) :
	def __init__(self, length=1) :
		self.nssourceroutecachetable = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nssourceroutecachetable = [nssourceroutecachetable() for _ in range(length)]

