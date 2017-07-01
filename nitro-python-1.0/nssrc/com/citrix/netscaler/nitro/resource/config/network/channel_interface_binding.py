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

class channel_interface_binding(base_resource) :
	""" Binding class showing the interface that can be bound to channel.
	"""
	def __init__(self) :
		self._ifnum = []
		self._lamode = None
		self._slavestate = None
		self._slavemedia = None
		self._slavespeed = None
		self._slaveduplex = None
		self._slaveflowctl = None
		self._slavetime = None
		self._lractiveintf = None
		self._id = None
		self.___count = 0

	@property
	def ifnum(self) :
		r"""Interfaces to be bound to the LA channel of a NetScaler appliance or to the LA channel of a cluster configuration.
		For an LA channel of a NetScaler appliance, specify an interface in C/U notation (for example, 1/3). 
		For an LA channel of a cluster configuration, specify an interface in N/C/U notation (for example, 2/1/3).
		where C can take one of the following values:
		* 0 - Indicates a management interface.
		* 1 - Indicates a 1 Gbps port.
		* 10 - Indicates a 10 Gbps port.
		U is a unique integer for representing an interface in a particular port group.
		N is the ID of the node to which an interface belongs in a cluster configuration.
		Use spaces to separate multiple entries.
		"""
		try :
			return self._ifnum
		except Exception as e:
			raise e

	@ifnum.setter
	def ifnum(self, ifnum) :
		r"""Interfaces to be bound to the LA channel of a NetScaler appliance or to the LA channel of a cluster configuration.
		For an LA channel of a NetScaler appliance, specify an interface in C/U notation (for example, 1/3). 
		For an LA channel of a cluster configuration, specify an interface in N/C/U notation (for example, 2/1/3).
		where C can take one of the following values:
		* 0 - Indicates a management interface.
		* 1 - Indicates a 1 Gbps port.
		* 10 - Indicates a 10 Gbps port.
		U is a unique integer for representing an interface in a particular port group.
		N is the ID of the node to which an interface belongs in a cluster configuration.
		Use spaces to separate multiple entries.
		"""
		try :
			self._ifnum = ifnum
		except Exception as e:
			raise e

	@property
	def id(self) :
		r"""ID of the LA channel or the cluster LA channel to which you want to bind interfaces. Specify an LA channel in LA/x notation, where x can range from 1 to 8 or a cluster LA channel in CLA/x notation or  Link redundant channel in LR/x notation , where x can range from 1 to 4.
		"""
		try :
			return self._id
		except Exception as e:
			raise e

	@id.setter
	def id(self, id) :
		r"""ID of the LA channel or the cluster LA channel to which you want to bind interfaces. Specify an LA channel in LA/x notation, where x can range from 1 to 8 or a cluster LA channel in CLA/x notation or  Link redundant channel in LR/x notation , where x can range from 1 to 4.
		"""
		try :
			self._id = id
		except Exception as e:
			raise e

	@property
	def lamode(self) :
		r"""The  mode(AUTO/MANNUAL) for the LA channel.<br/>Possible values = MANUAL, AUTO.
		"""
		try :
			return self._lamode
		except Exception as e:
			raise e

	@property
	def slavespeed(self) :
		r"""Speed of the member interfaces.
		"""
		try :
			return self._slavespeed
		except Exception as e:
			raise e

	@property
	def slavemedia(self) :
		r"""Media type of the member interfaces.
		"""
		try :
			return self._slavemedia
		except Exception as e:
			raise e

	@property
	def slaveduplex(self) :
		r"""Duplex of the member interfaces.
		"""
		try :
			return self._slaveduplex
		except Exception as e:
			raise e

	@property
	def lractiveintf(self) :
		r"""LR set member interface state(active/inactive).
		"""
		try :
			return self._lractiveintf
		except Exception as e:
			raise e

	@property
	def slaveflowctl(self) :
		r"""Flowcontrol of the member interfaces.
		"""
		try :
			return self._slaveflowctl
		except Exception as e:
			raise e

	@property
	def slavetime(self) :
		r"""UP time of the member interfaces.
		"""
		try :
			return self._slavetime
		except Exception as e:
			raise e

	@property
	def slavestate(self) :
		r"""State of the member interfaces.
		"""
		try :
			return self._slavestate
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(channel_interface_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.channel_interface_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.id is not None :
				return str(self.id)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				updateresource = channel_interface_binding()
				updateresource.id = resource.id
				updateresource.ifnum = resource.ifnum
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [channel_interface_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].id = resource[i].id
						updateresources[i].ifnum = resource[i].ifnum
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = channel_interface_binding()
				deleteresource.id = resource.id
				deleteresource.ifnum = resource.ifnum
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [channel_interface_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].id = resource[i].id
						deleteresources[i].ifnum = resource[i].ifnum
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, id="", option_="") :
		r""" Use this API to fetch channel_interface_binding resources.
		"""
		try :
			if not id :
				obj = channel_interface_binding()
				response = obj.get_resources(service, option_)
			else :
				obj = channel_interface_binding()
				obj.id = id
				response = obj.get_resources(service)
				return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, id, filter_) :
		r""" Use this API to fetch filtered set of channel_interface_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = channel_interface_binding()
			obj.id = id
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, id) :
		r""" Use this API to count channel_interface_binding resources configued on NetScaler.
		"""
		try :
			obj = channel_interface_binding()
			obj.id = id
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, id, filter_) :
		r""" Use this API to count the filtered set of channel_interface_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = channel_interface_binding()
			obj.id = id
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	class Lamode:
		MANUAL = "MANUAL"
		AUTO = "AUTO"

class channel_interface_binding_response(base_response) :
	def __init__(self, length=1) :
		self.channel_interface_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.channel_interface_binding = [channel_interface_binding() for _ in range(length)]

