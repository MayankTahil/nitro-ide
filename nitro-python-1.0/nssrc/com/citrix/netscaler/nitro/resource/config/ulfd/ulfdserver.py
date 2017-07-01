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

class ulfdserver(base_resource) :
	""" Configuration for ulfd server resource. """
	def __init__(self) :
		self._loggerip = None
		self._state = None
		self.___count = 0

	@property
	def loggerip(self) :
		r"""IP address of the server where ulfd service is running.<br/>Minimum length =  1.
		"""
		try :
			return self._loggerip
		except Exception as e:
			raise e

	@loggerip.setter
	def loggerip(self, loggerip) :
		r"""IP address of the server where ulfd service is running.<br/>Minimum length =  1
		"""
		try :
			self._loggerip = loggerip
		except Exception as e:
			raise e

	@property
	def state(self) :
		r"""ULFD server state.<br/>Possible values = UP, DOWN, UNKNOWN, BUSY, OUT OF SERVICE, GOING OUT OF SERVICE, DOWN WHEN GOING OUT OF SERVICE, NS_EMPTY_STR, Unknown, DISABLED.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(ulfdserver_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ulfdserver
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.loggerip is not None :
				return str(self.loggerip)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add ulfdserver.
		"""
		try :
			if type(resource) is not list :
				addresource = ulfdserver()
				addresource.loggerip = resource.loggerip
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ ulfdserver() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].loggerip = resource[i].loggerip
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete ulfdserver.
		"""
		try :
			if type(resource) is not list :
				deleteresource = ulfdserver()
				if type(resource) !=  type(deleteresource):
					deleteresource.loggerip = resource
				else :
					deleteresource.loggerip = resource.loggerip
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ ulfdserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].loggerip = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ ulfdserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].loggerip = resource[i].loggerip
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the ulfdserver resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = ulfdserver()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = ulfdserver()
					obj.loggerip = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [ulfdserver() for _ in range(len(name))]
						obj = [ulfdserver() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = ulfdserver()
							obj[i].loggerip = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of ulfdserver resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = ulfdserver()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the ulfdserver resources configured on NetScaler.
		"""
		try :
			obj = ulfdserver()
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
		r""" Use this API to count filtered the set of ulfdserver resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = ulfdserver()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class State:
		UP = "UP"
		DOWN = "DOWN"
		UNKNOWN = "UNKNOWN"
		BUSY = "BUSY"
		OUT_OF_SERVICE = "OUT OF SERVICE"
		GOING_OUT_OF_SERVICE = "GOING OUT OF SERVICE"
		DOWN_WHEN_GOING_OUT_OF_SERVICE = "DOWN WHEN GOING OUT OF SERVICE"
		NS_EMPTY_STR = "NS_EMPTY_STR"
		Unknown = "Unknown"
		DISABLED = "DISABLED"

class ulfdserver_response(base_response) :
	def __init__(self, length=1) :
		self.ulfdserver = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.ulfdserver = [ulfdserver() for _ in range(length)]

