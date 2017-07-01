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

class nd6(base_resource) :
	""" Configuration for nd6 resource. """
	def __init__(self) :
		self._neighbor = None
		self._mac = None
		self._ifnum = None
		self._vlan = None
		self._vxlan = None
		self._vtep = None
		self._td = None
		self._nodeid = None
		self._state = None
		self._timeout = None
		self._flags = None
		self._controlplane = None
		self._channel = None
		self.___count = 0

	@property
	def neighbor(self) :
		r"""Link-local IPv6 address of the adjacent network device to add to the ND6 table.
		"""
		try :
			return self._neighbor
		except Exception as e:
			raise e

	@neighbor.setter
	def neighbor(self, neighbor) :
		r"""Link-local IPv6 address of the adjacent network device to add to the ND6 table.
		"""
		try :
			self._neighbor = neighbor
		except Exception as e:
			raise e

	@property
	def mac(self) :
		r"""MAC address of the adjacent network device.
		"""
		try :
			return self._mac
		except Exception as e:
			raise e

	@mac.setter
	def mac(self, mac) :
		r"""MAC address of the adjacent network device.
		"""
		try :
			self._mac = mac
		except Exception as e:
			raise e

	@property
	def ifnum(self) :
		r"""Interface through which the adjacent network device is available, specified in slot/port notation (for example, 1/3). Use spaces to separate multiple entries.
		"""
		try :
			return self._ifnum
		except Exception as e:
			raise e

	@ifnum.setter
	def ifnum(self, ifnum) :
		r"""Interface through which the adjacent network device is available, specified in slot/port notation (for example, 1/3). Use spaces to separate multiple entries.
		"""
		try :
			self._ifnum = ifnum
		except Exception as e:
			raise e

	@property
	def vlan(self) :
		r"""Integer value that uniquely identifies the VLAN on which the adjacent network device exists.<br/>Minimum length =  1<br/>Maximum length =  4094.
		"""
		try :
			return self._vlan
		except Exception as e:
			raise e

	@vlan.setter
	def vlan(self, vlan) :
		r"""Integer value that uniquely identifies the VLAN on which the adjacent network device exists.<br/>Minimum length =  1<br/>Maximum length =  4094
		"""
		try :
			self._vlan = vlan
		except Exception as e:
			raise e

	@property
	def vxlan(self) :
		r"""ID of the VXLAN on which the IPv6 address of this ND6 entry is reachable.<br/>Minimum length =  1<br/>Maximum length =  16777215.
		"""
		try :
			return self._vxlan
		except Exception as e:
			raise e

	@vxlan.setter
	def vxlan(self, vxlan) :
		r"""ID of the VXLAN on which the IPv6 address of this ND6 entry is reachable.<br/>Minimum length =  1<br/>Maximum length =  16777215
		"""
		try :
			self._vxlan = vxlan
		except Exception as e:
			raise e

	@property
	def vtep(self) :
		r"""IP address of the VXLAN tunnel endpoint (VTEP) through which the IPv6 address of this ND6 entry is reachable.<br/>Minimum length =  1.
		"""
		try :
			return self._vtep
		except Exception as e:
			raise e

	@vtep.setter
	def vtep(self, vtep) :
		r"""IP address of the VXLAN tunnel endpoint (VTEP) through which the IPv6 address of this ND6 entry is reachable.<br/>Minimum length =  1
		"""
		try :
			self._vtep = vtep
		except Exception as e:
			raise e

	@property
	def td(self) :
		r"""Integer value that uniquely identifies the traffic domain in which you want to configure the entity. If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of 0.<br/>Maximum length =  4094.
		"""
		try :
			return self._td
		except Exception as e:
			raise e

	@td.setter
	def td(self, td) :
		r"""Integer value that uniquely identifies the traffic domain in which you want to configure the entity. If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of 0.<br/>Maximum length =  4094
		"""
		try :
			self._td = td
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
	def state(self) :
		r"""ND6 state.<br/>Default value: REACHABLE<br/>Possible values = INCOMPLETE, REACHABLE, STALE, DELAY, PROBE.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@property
	def timeout(self) :
		r"""Time elapsed.
		"""
		try :
			return self._timeout
		except Exception as e:
			raise e

	@property
	def flags(self) :
		r"""flag for static/permanent entry.
		"""
		try :
			return self._flags
		except Exception as e:
			raise e

	@property
	def controlplane(self) :
		r"""This nd6 entry is populated by a control plane protocol.
		"""
		try :
			return self._controlplane
		except Exception as e:
			raise e

	@property
	def channel(self) :
		r"""The tunnel that is bound to a netbridge.
		"""
		try :
			return self._channel
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nd6_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nd6
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.neighbor is not None :
				return str(self.neighbor)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add nd6.
		"""
		try :
			if type(resource) is not list :
				addresource = nd6()
				addresource.neighbor = resource.neighbor
				addresource.mac = resource.mac
				addresource.ifnum = resource.ifnum
				addresource.vlan = resource.vlan
				addresource.vxlan = resource.vxlan
				addresource.vtep = resource.vtep
				addresource.td = resource.td
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ nd6() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].neighbor = resource[i].neighbor
						addresources[i].mac = resource[i].mac
						addresources[i].ifnum = resource[i].ifnum
						addresources[i].vlan = resource[i].vlan
						addresources[i].vxlan = resource[i].vxlan
						addresources[i].vtep = resource[i].vtep
						addresources[i].td = resource[i].td
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def clear(cls, client, resource) :
		r""" Use this API to clear nd6.
		"""
		try :
			if type(resource) is not list :
				clearresource = nd6()
				return clearresource.perform_operation(client,"clear")
			else :
				if (resource and len(resource) > 0) :
					clearresources = [ nd6() for _ in range(len(resource))]
				result = cls.perform_operation_bulk_request(client, clearresources,"clear")
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete nd6.
		"""
		try :
			if type(resource) is not list :
				deleteresource = nd6()
				if type(resource) !=  type(deleteresource):
					deleteresource.neighbor = resource
				else :
					deleteresource.neighbor = resource.neighbor
					deleteresource.vlan = resource.vlan
					deleteresource.vxlan = resource.vxlan
					deleteresource.td = resource.td
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ nd6() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].neighbor = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ nd6() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].neighbor = resource[i].neighbor
							deleteresources[i].vlan = resource[i].vlan
							deleteresources[i].vxlan = resource[i].vxlan
							deleteresources[i].td = resource[i].td
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the nd6 resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nd6()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) != cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					option_ = options()
					option_.args = nitro_util.object_to_string_withoutquotes(name)
					response = name.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) != cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [nd6() for _ in range(len(name))]
						for i in range(len(name)) :
							option_ = options()
							option_.args = nitro_util.object_to_string_withoutquotes(name[i])
							response[i] = name[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		r""" Use this API to fetch all the nd6 resources that are configured on netscaler.
	# This uses nd6_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = nd6()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of nd6 resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nd6()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the nd6 resources configured on NetScaler.
		"""
		try :
			obj = nd6()
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
		r""" Use this API to count filtered the set of nd6 resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nd6()
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
		INCOMPLETE = "INCOMPLETE"
		REACHABLE = "REACHABLE"
		STALE = "STALE"
		DELAY = "DELAY"
		PROBE = "PROBE"

class nd6_response(base_response) :
	def __init__(self, length=1) :
		self.nd6 = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nd6 = [nd6() for _ in range(length)]

