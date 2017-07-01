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

class snmpmib(base_resource) :
	""" Configuration for SNMP mib resource. """
	def __init__(self) :
		self._contact = None
		self._name = None
		self._location = None
		self._customid = None
		self._ownernode = None
		self._sysdesc = None
		self._sysuptime = None
		self._sysservices = None
		self._sysoid = None
		self.___count = 0

	@property
	def contact(self) :
		r"""Name of the administrator for this NetScaler appliance. Along with the name, you can include information on how to contact this person, such as a phone number or an email address. Can consist of 1 to 127 characters that include uppercase and  lowercase letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at sign (@), equals (=), colon (:), and underscore (_) characters.
		The following requirement applies only to the NetScaler CLI:
		If the information includes one or more spaces, enclose it in double or single quotation marks (for example, "my contact" or 'my contact').<br/>Default value: "WebMaster (default)"<br/>Minimum length =  1.
		"""
		try :
			return self._contact
		except Exception as e:
			raise e

	@contact.setter
	def contact(self, contact) :
		r"""Name of the administrator for this NetScaler appliance. Along with the name, you can include information on how to contact this person, such as a phone number or an email address. Can consist of 1 to 127 characters that include uppercase and  lowercase letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at sign (@), equals (=), colon (:), and underscore (_) characters.
		The following requirement applies only to the NetScaler CLI:
		If the information includes one or more spaces, enclose it in double or single quotation marks (for example, "my contact" or 'my contact').<br/>Default value: "WebMaster (default)"<br/>Minimum length =  1
		"""
		try :
			self._contact = contact
		except Exception as e:
			raise e

	@property
	def name(self) :
		r"""Name for this NetScaler appliance. Can consist of 1 to 127 characters that include uppercase and lowercase letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at sign (@), equals (=), colon (:), and underscore (_) characters.  You should choose a name that helps identify the NetScaler appliance.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose it in double or single quotation marks (for example, "my name" or 'my name').<br/>Default value: "NetScaler"<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name for this NetScaler appliance. Can consist of 1 to 127 characters that include uppercase and lowercase letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at sign (@), equals (=), colon (:), and underscore (_) characters.  You should choose a name that helps identify the NetScaler appliance.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose it in double or single quotation marks (for example, "my name" or 'my name').<br/>Default value: "NetScaler"<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def location(self) :
		r"""Physical location of the NetScaler appliance. For example, you can specify building name, lab number, and rack number. Can consist of 1 to 127 characters that include uppercase and lowercase letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at sign (@), equals (=), colon (:), and underscore (_) characters.
		The following requirement applies only to the NetScaler CLI:
		If the location includes one or more spaces, enclose it in double or single quotation marks (for example, "my location" or 'my location').<br/>Default value: "POP (default)"<br/>Minimum length =  1.
		"""
		try :
			return self._location
		except Exception as e:
			raise e

	@location.setter
	def location(self, location) :
		r"""Physical location of the NetScaler appliance. For example, you can specify building name, lab number, and rack number. Can consist of 1 to 127 characters that include uppercase and lowercase letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at sign (@), equals (=), colon (:), and underscore (_) characters.
		The following requirement applies only to the NetScaler CLI:
		If the location includes one or more spaces, enclose it in double or single quotation marks (for example, "my location" or 'my location').<br/>Default value: "POP (default)"<br/>Minimum length =  1
		"""
		try :
			self._location = location
		except Exception as e:
			raise e

	@property
	def customid(self) :
		r"""Custom identification number for the NetScaler appliance. Can consist of 1 to 127 characters that include uppercase and lowercase letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at sign (@), equals (=), colon (:), and underscore (_) characters. You should choose a custom identification that helps identify the NetScaler appliance.
		The following requirement applies only to the NetScaler CLI:
		If the ID includes one or more spaces, enclose it in double or single quotation marks (for example, "my ID" or 'my ID').<br/>Default value: "Default"<br/>Minimum length =  1.
		"""
		try :
			return self._customid
		except Exception as e:
			raise e

	@customid.setter
	def customid(self, customid) :
		r"""Custom identification number for the NetScaler appliance. Can consist of 1 to 127 characters that include uppercase and lowercase letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at sign (@), equals (=), colon (:), and underscore (_) characters. You should choose a custom identification that helps identify the NetScaler appliance.
		The following requirement applies only to the NetScaler CLI:
		If the ID includes one or more spaces, enclose it in double or single quotation marks (for example, "my ID" or 'my ID').<br/>Default value: "Default"<br/>Minimum length =  1
		"""
		try :
			self._customid = customid
		except Exception as e:
			raise e

	@property
	def ownernode(self) :
		r"""ID of the cluster node for which we are setting the mib. This is a mandatory argument to set snmp mib on CLIP.<br/>Default value: -1<br/>Maximum length =  31.
		"""
		try :
			return self._ownernode
		except Exception as e:
			raise e

	@ownernode.setter
	def ownernode(self, ownernode) :
		r"""ID of the cluster node for which we are setting the mib. This is a mandatory argument to set snmp mib on CLIP.<br/>Default value: -1<br/>Maximum length =  31
		"""
		try :
			self._ownernode = ownernode
		except Exception as e:
			raise e

	@property
	def sysdesc(self) :
		r"""The description of the system.
		"""
		try :
			return self._sysdesc
		except Exception as e:
			raise e

	@property
	def sysuptime(self) :
		r"""The UP time of the system in 100th of a second.
		"""
		try :
			return self._sysuptime
		except Exception as e:
			raise e

	@property
	def sysservices(self) :
		r"""The services offered by the system.
		"""
		try :
			return self._sysservices
		except Exception as e:
			raise e

	@property
	def sysoid(self) :
		r"""The OID of the system's management system.
		"""
		try :
			return self._sysoid
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(snmpmib_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.snmpmib
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.ownernode is not None :
				return str(self.ownernode)
			return None
		except Exception as e :
			raise e



	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update snmpmib.
		"""
		try :
			if type(resource) is not list :
				updateresource = snmpmib()
				updateresource.contact = resource.contact
				updateresource.name = resource.name
				updateresource.location = resource.location
				updateresource.customid = resource.customid
				updateresource.ownernode = resource.ownernode
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ snmpmib() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].contact = resource[i].contact
						updateresources[i].name = resource[i].name
						updateresources[i].location = resource[i].location
						updateresources[i].customid = resource[i].customid
						updateresources[i].ownernode = resource[i].ownernode
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of snmpmib resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = snmpmib()
				if type(resource) !=  type(unsetresource):
					unsetresource.ownernode = resource
				else :
					unsetresource.ownernode = resource.ownernode
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ snmpmib() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].ownernode = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ snmpmib() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].ownernode = resource[i].ownernode
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the snmpmib resources that are configured on netscaler (on ncore deployment).
		"""
		try :
			if not name :
				obj = snmpmib()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_cluster(cls, client, name="", option_="") :
		r""" Use this API to fetch all the snmpmib resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = snmpmib()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = snmpmib()
					obj.ownernode = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [snmpmib() for _ in range(len(name))]
						obj = [snmpmib() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = snmpmib()
							obj[i].ownernode = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of snmpmib resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = snmpmib()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the snmpmib resources configured on NetScaler.
		"""
		try :
			obj = snmpmib()
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
		r""" Use this API to count filtered the set of snmpmib resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = snmpmib()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


class snmpmib_response(base_response) :
	def __init__(self, length=1) :
		self.snmpmib = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.snmpmib = [snmpmib() for _ in range(length)]

