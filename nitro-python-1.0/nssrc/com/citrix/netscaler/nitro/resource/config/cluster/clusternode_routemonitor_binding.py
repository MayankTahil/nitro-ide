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

class clusternode_routemonitor_binding(base_resource) :
	""" Binding class showing the routemonitor that can be bound to clusternode.
	"""
	def __init__(self) :
		self._routemonitor = None
		self._netmask = None
		self._routemonstate = None
		self._nodeid = None
		self.___count = 0

	@property
	def nodeid(self) :
		r"""A number that uniquely identifies the cluster node. .<br/>Minimum value =  0<br/>Maximum value =  31.
		"""
		try :
			return self._nodeid
		except Exception as e:
			raise e

	@nodeid.setter
	def nodeid(self, nodeid) :
		r"""A number that uniquely identifies the cluster node. .<br/>Minimum value =  0<br/>Maximum value =  31
		"""
		try :
			self._nodeid = nodeid
		except Exception as e:
			raise e

	@property
	def routemonitor(self) :
		r"""The IP address (IPv4 or IPv6).
		"""
		try :
			return self._routemonitor
		except Exception as e:
			raise e

	@routemonitor.setter
	def routemonitor(self, routemonitor) :
		r"""The IP address (IPv4 or IPv6).
		"""
		try :
			self._routemonitor = routemonitor
		except Exception as e:
			raise e

	@property
	def netmask(self) :
		r"""The netmask.
		"""
		try :
			return self._netmask
		except Exception as e:
			raise e

	@netmask.setter
	def netmask(self, netmask) :
		r"""The netmask.
		"""
		try :
			self._netmask = netmask
		except Exception as e:
			raise e

	@property
	def routemonstate(self) :
		r"""Current routemonstate.
		"""
		try :
			return self._routemonstate
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(clusternode_routemonitor_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.clusternode_routemonitor_binding
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
	def add(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				updateresource = clusternode_routemonitor_binding()
				updateresource.nodeid = resource.nodeid
				updateresource.routemonitor = resource.routemonitor
				updateresource.netmask = resource.netmask
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [clusternode_routemonitor_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].nodeid = resource[i].nodeid
						updateresources[i].routemonitor = resource[i].routemonitor
						updateresources[i].netmask = resource[i].netmask
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = clusternode_routemonitor_binding()
				deleteresource.nodeid = resource.nodeid
				deleteresource.routemonitor = resource.routemonitor
				deleteresource.netmask = resource.netmask
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [clusternode_routemonitor_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].nodeid = resource[i].nodeid
						deleteresources[i].routemonitor = resource[i].routemonitor
						deleteresources[i].netmask = resource[i].netmask
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, nodeid="", option_="") :
		r""" Use this API to fetch clusternode_routemonitor_binding resources.
		"""
		try :
			if not nodeid :
				obj = clusternode_routemonitor_binding()
				response = obj.get_resources(service, option_)
			else :
				obj = clusternode_routemonitor_binding()
				obj.nodeid = nodeid
				response = obj.get_resources(service)
				return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, nodeid, filter_) :
		r""" Use this API to fetch filtered set of clusternode_routemonitor_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = clusternode_routemonitor_binding()
			obj.nodeid = nodeid
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, nodeid) :
		r""" Use this API to count clusternode_routemonitor_binding resources configued on NetScaler.
		"""
		try :
			obj = clusternode_routemonitor_binding()
			obj.nodeid = nodeid
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, nodeid, filter_) :
		r""" Use this API to count the filtered set of clusternode_routemonitor_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = clusternode_routemonitor_binding()
			obj.nodeid = nodeid
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

class clusternode_routemonitor_binding_response(base_response) :
	def __init__(self, length=1) :
		self.clusternode_routemonitor_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.clusternode_routemonitor_binding = [clusternode_routemonitor_binding() for _ in range(length)]

