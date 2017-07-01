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

class vxlanvlanmap_vxlan_binding(base_resource) :
	""" Binding class showing the vxlan that can be bound to vxlanvlanmap.
	"""
	def __init__(self) :
		self._vxlan = None
		self._vlan = []
		self._name = None
		self.___count = 0

	@property
	def name(self) :
		r"""Name of the mapping table.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name of the mapping table.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def vxlan(self) :
		r"""The VXLAN assigned to the vlan inside the cloud.<br/>Minimum value =  1<br/>Maximum value =  16777215.
		"""
		try :
			return self._vxlan
		except Exception as e:
			raise e

	@vxlan.setter
	def vxlan(self, vxlan) :
		r"""The VXLAN assigned to the vlan inside the cloud.<br/>Minimum value =  1<br/>Maximum value =  16777215
		"""
		try :
			self._vxlan = vxlan
		except Exception as e:
			raise e

	@property
	def vlan(self) :
		r"""The vlan id or the range of vlan ids in the on-premise network.<br/>Minimum length =  1<br/>Maximum length =  4094.
		"""
		try :
			return self._vlan
		except Exception as e:
			raise e

	@vlan.setter
	def vlan(self, vlan) :
		r"""The vlan id or the range of vlan ids in the on-premise network.<br/>Minimum length =  1<br/>Maximum length =  4094
		"""
		try :
			self._vlan = vlan
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(vxlanvlanmap_vxlan_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.vxlanvlanmap_vxlan_binding
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
		try :
			if resource and type(resource) is not list :
				updateresource = vxlanvlanmap_vxlan_binding()
				updateresource.name = resource.name
				updateresource.vxlan = resource.vxlan
				updateresource.vlan = resource.vlan
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [vxlanvlanmap_vxlan_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].vxlan = resource[i].vxlan
						updateresources[i].vlan = resource[i].vlan
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = vxlanvlanmap_vxlan_binding()
				deleteresource.name = resource.name
				deleteresource.vxlan = resource.vxlan
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [vxlanvlanmap_vxlan_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].name = resource[i].name
						deleteresources[i].vxlan = resource[i].vxlan
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, name="", option_="") :
		r""" Use this API to fetch vxlanvlanmap_vxlan_binding resources.
		"""
		try :
			if not name :
				obj = vxlanvlanmap_vxlan_binding()
				response = obj.get_resources(service, option_)
			else :
				obj = vxlanvlanmap_vxlan_binding()
				obj.name = name
				response = obj.get_resources(service)
				return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, name, filter_) :
		r""" Use this API to fetch filtered set of vxlanvlanmap_vxlan_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = vxlanvlanmap_vxlan_binding()
			obj.name = name
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, name) :
		r""" Use this API to count vxlanvlanmap_vxlan_binding resources configued on NetScaler.
		"""
		try :
			obj = vxlanvlanmap_vxlan_binding()
			obj.name = name
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, name, filter_) :
		r""" Use this API to count the filtered set of vxlanvlanmap_vxlan_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = vxlanvlanmap_vxlan_binding()
			obj.name = name
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

class vxlanvlanmap_vxlan_binding_response(base_response) :
	def __init__(self, length=1) :
		self.vxlanvlanmap_vxlan_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.vxlanvlanmap_vxlan_binding = [vxlanvlanmap_vxlan_binding() for _ in range(length)]

