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

class rnat6(base_resource) :
	""" Configuration for IPv6 RNAT configured route resource. """
	def __init__(self) :
		self._name = None
		self._network = None
		self._acl6name = None
		self._redirectport = None
		self._td = None
		self._srcippersistency = None
		self._ownergroup = None
		self.___count = 0

	@property
	def name(self) :
		r"""Name for the RNAT6 rule. Must begin with a letter, number, or the underscore character (_), and can consist of letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at sign (@), equals (=), colon (:), and underscore characters. Cannot be changed after the rule is created. Choose a name that helps identify the RNAT6 rule.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name for the RNAT6 rule. Must begin with a letter, number, or the underscore character (_), and can consist of letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at sign (@), equals (=), colon (:), and underscore characters. Cannot be changed after the rule is created. Choose a name that helps identify the RNAT6 rule.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def network(self) :
		r"""IPv6 address of the network on whose traffic you want the NetScaler appliance to do RNAT processing.<br/>Minimum length =  1.
		"""
		try :
			return self._network
		except Exception as e:
			raise e

	@network.setter
	def network(self, network) :
		r"""IPv6 address of the network on whose traffic you want the NetScaler appliance to do RNAT processing.<br/>Minimum length =  1
		"""
		try :
			self._network = network
		except Exception as e:
			raise e

	@property
	def acl6name(self) :
		r"""Name of any configured ACL6 whose action is ALLOW. The rule of the ACL6 is used as an RNAT6 rule.<br/>Minimum length =  1.
		"""
		try :
			return self._acl6name
		except Exception as e:
			raise e

	@acl6name.setter
	def acl6name(self, acl6name) :
		r"""Name of any configured ACL6 whose action is ALLOW. The rule of the ACL6 is used as an RNAT6 rule.<br/>Minimum length =  1
		"""
		try :
			self._acl6name = acl6name
		except Exception as e:
			raise e

	@property
	def redirectport(self) :
		r"""Port number to which the IPv6 packets are redirected. Applicable to TCP and UDP protocols.<br/>Minimum length =  1<br/>Maximum length =  65535.
		"""
		try :
			return self._redirectport
		except Exception as e:
			raise e

	@redirectport.setter
	def redirectport(self, redirectport) :
		r"""Port number to which the IPv6 packets are redirected. Applicable to TCP and UDP protocols.<br/>Minimum length =  1<br/>Maximum length =  65535
		"""
		try :
			self._redirectport = redirectport
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
	def srcippersistency(self) :
		r"""Enable source ip persistency, which enables the NetScaler appliance to use the RNAT ips using source ip.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._srcippersistency
		except Exception as e:
			raise e

	@srcippersistency.setter
	def srcippersistency(self, srcippersistency) :
		r"""Enable source ip persistency, which enables the NetScaler appliance to use the RNAT ips using source ip.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._srcippersistency = srcippersistency
		except Exception as e:
			raise e

	@property
	def ownergroup(self) :
		r"""The owner node group in a Cluster for this rnat rule.<br/>Default value: DEFAULT_NG<br/>Minimum length =  1.
		"""
		try :
			return self._ownergroup
		except Exception as e:
			raise e

	@ownergroup.setter
	def ownergroup(self, ownergroup) :
		r"""The owner node group in a Cluster for this rnat rule.<br/>Default value: DEFAULT_NG<br/>Minimum length =  1
		"""
		try :
			self._ownergroup = ownergroup
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(rnat6_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.rnat6
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
		r""" Use this API to add rnat6.
		"""
		try :
			if type(resource) is not list :
				addresource = rnat6()
				addresource.name = resource.name
				addresource.network = resource.network
				addresource.acl6name = resource.acl6name
				addresource.redirectport = resource.redirectport
				addresource.td = resource.td
				addresource.srcippersistency = resource.srcippersistency
				addresource.ownergroup = resource.ownergroup
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ rnat6() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].network = resource[i].network
						addresources[i].acl6name = resource[i].acl6name
						addresources[i].redirectport = resource[i].redirectport
						addresources[i].td = resource[i].td
						addresources[i].srcippersistency = resource[i].srcippersistency
						addresources[i].ownergroup = resource[i].ownergroup
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update rnat6.
		"""
		try :
			if type(resource) is not list :
				updateresource = rnat6()
				updateresource.name = resource.name
				updateresource.redirectport = resource.redirectport
				updateresource.srcippersistency = resource.srcippersistency
				updateresource.ownergroup = resource.ownergroup
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ rnat6() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].redirectport = resource[i].redirectport
						updateresources[i].srcippersistency = resource[i].srcippersistency
						updateresources[i].ownergroup = resource[i].ownergroup
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of rnat6 resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = rnat6()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
					unsetresource.ownergroup = resource.ownergroup
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ rnat6() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ rnat6() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
							unsetresources[i].ownergroup = resource[i].ownergroup
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def clear(cls, client, resource) :
		r""" Use this API to clear rnat6.
		"""
		try :
			if type(resource) is not list :
				clearresource = rnat6()
				clearresource.name = resource.name
				clearresource.ownergroup = resource.ownergroup
				return clearresource.perform_operation(client,"clear")
			else :
				if (resource and len(resource) > 0) :
					clearresources = [ rnat6() for _ in range(len(resource))]
					for i in range(len(resource)) :
						clearresources[i].name = resource[i].name
						clearresources[i].ownergroup = resource[i].ownergroup
				result = cls.perform_operation_bulk_request(client, clearresources,"clear")
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the rnat6 resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = rnat6()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = rnat6()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [rnat6() for _ in range(len(name))]
						obj = [rnat6() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = rnat6()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of rnat6 resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = rnat6()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the rnat6 resources configured on NetScaler.
		"""
		try :
			obj = rnat6()
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
		r""" Use this API to count filtered the set of rnat6 resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = rnat6()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Srcippersistency:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class rnat6_response(base_response) :
	def __init__(self, length=1) :
		self.rnat6 = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.rnat6 = [rnat6() for _ in range(length)]

