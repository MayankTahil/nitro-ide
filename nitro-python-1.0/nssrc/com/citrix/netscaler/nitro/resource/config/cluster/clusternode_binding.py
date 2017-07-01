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

class clusternode_binding(base_resource):
	""" Binding class showing the resources that can be bound to clusternode_binding. 
	"""
	def __init__(self) :
		self._nodeid = None
		self.clusternode_routemonitor_binding = []

	@property
	def nodeid(self) :
		r"""ID of the cluster node for which to display information. If an ID is not provided, information about all nodes is shown.<br/>Default value: 255<br/>Minimum value =  0<br/>Maximum value =  31.
		"""
		try :
			return self._nodeid
		except Exception as e:
			raise e

	@nodeid.setter
	def nodeid(self, nodeid) :
		r"""ID of the cluster node for which to display information. If an ID is not provided, information about all nodes is shown.<br/>Default value: 255<br/>Minimum value =  0<br/>Maximum value =  31
		"""
		try :
			self._nodeid = nodeid
		except Exception as e:
			raise e

	@property
	def clusternode_routemonitor_bindings(self) :
		r"""routemonitor that can be bound to clusternode.
		"""
		try :
			return self._clusternode_routemonitor_binding
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(clusternode_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.clusternode_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.nodeid is not None :
				return str(self.nodeid)
			return None
		except Exception as e :
			raise e



	@classmethod
	def get(self, service, nodeid="", option_="") :
		r""" Use this API to fetch clusternode_binding resource.
		"""
		try :
			if not nodeid :
				obj = clusternode_binding()
				response = obj.get_resources(service, option_)
			elif type(nodeid) is not list :
				obj = clusternode_binding()
				obj.nodeid = nodeid
				response = obj.get_resource(service)
			else :
				if nodeid and len(nodeid) > 0 :
					obj = [clusternode_binding() for _ in range(len(nodeid))]
					for i in range(len(nodeid)) :
						obj[i].nodeid = nodeid[i];
						response[i] = obj[i].get_resource(service)
			return response
		except Exception as e:
			raise e

class clusternode_binding_response(base_response) :
	def __init__(self, length=1) :
		self.clusternode_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.clusternode_binding = [clusternode_binding() for _ in range(length)]

