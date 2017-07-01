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

class sslcipher_sslciphersuite_binding(base_resource) :
	""" Binding class showing the sslciphersuite that can be bound to sslcipher.
	"""
	def __init__(self) :
		self._ciphername = None
		self._ciphergroupname = None
		self._description = None
		self._cipherpriority = None
		self._cipheroperation = None
		self._ciphgrpals = None
		self.___count = 0

	@property
	def ciphername(self) :
		r"""Cipher name.
		"""
		try :
			return self._ciphername
		except Exception as e:
			raise e

	@ciphername.setter
	def ciphername(self, ciphername) :
		r"""Cipher name.
		"""
		try :
			self._ciphername = ciphername
		except Exception as e:
			raise e

	@property
	def ciphgrpals(self) :
		r"""A cipher-suite can consist of an individual cipher name, the system predefined cipher-alias name, or user defined cipher-group name.<br/>Minimum length =  1.
		"""
		try :
			return self._ciphgrpals
		except Exception as e:
			raise e

	@ciphgrpals.setter
	def ciphgrpals(self, ciphgrpals) :
		r"""A cipher-suite can consist of an individual cipher name, the system predefined cipher-alias name, or user defined cipher-group name.<br/>Minimum length =  1
		"""
		try :
			self._ciphgrpals = ciphgrpals
		except Exception as e:
			raise e

	@property
	def cipherpriority(self) :
		r"""This indicates priority assigned to the particular cipher.<br/>Minimum value =  1.
		"""
		try :
			return self._cipherpriority
		except Exception as e:
			raise e

	@cipherpriority.setter
	def cipherpriority(self, cipherpriority) :
		r"""This indicates priority assigned to the particular cipher.<br/>Minimum value =  1
		"""
		try :
			self._cipherpriority = cipherpriority
		except Exception as e:
			raise e

	@property
	def description(self) :
		r"""Cipher suite description.
		"""
		try :
			return self._description
		except Exception as e:
			raise e

	@description.setter
	def description(self, description) :
		r"""Cipher suite description.
		"""
		try :
			self._description = description
		except Exception as e:
			raise e

	@property
	def ciphergroupname(self) :
		r"""Name for the user-defined cipher group. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the cipher group is created.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my ciphergroup" or 'my ciphergroup').<br/>Minimum length =  1.
		"""
		try :
			return self._ciphergroupname
		except Exception as e:
			raise e

	@ciphergroupname.setter
	def ciphergroupname(self, ciphergroupname) :
		r"""Name for the user-defined cipher group. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the cipher group is created.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my ciphergroup" or 'my ciphergroup').<br/>Minimum length =  1
		"""
		try :
			self._ciphergroupname = ciphergroupname
		except Exception as e:
			raise e

	@property
	def cipheroperation(self) :
		r"""The operation that is performed when adding the cipher-suite.
		Possible cipher operations are:
		ADD - Appends the given cipher-suite to the existing one configured for the virtual server.
		REM - Removes the given cipher-suite from the existing one configured for the virtual server.
		ORD - Overrides the current configured cipher-suite for the virtual server with the given cipher-suite.<br/>Default value: 0<br/>Possible values = ADD, REM, ORD.
		"""
		try :
			return self._cipheroperation
		except Exception as e:
			raise e

	@cipheroperation.setter
	def cipheroperation(self, cipheroperation) :
		r"""The operation that is performed when adding the cipher-suite.
		Possible cipher operations are:
		ADD - Appends the given cipher-suite to the existing one configured for the virtual server.
		REM - Removes the given cipher-suite from the existing one configured for the virtual server.
		ORD - Overrides the current configured cipher-suite for the virtual server with the given cipher-suite.<br/>Default value: 0<br/>Possible values = ADD, REM, ORD
		"""
		try :
			self._cipheroperation = cipheroperation
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(sslcipher_sslciphersuite_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sslcipher_sslciphersuite_binding
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
	def add(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				updateresource = sslcipher_sslciphersuite_binding()
				updateresource.ciphergroupname = resource.ciphergroupname
				updateresource.cipheroperation = resource.cipheroperation
				updateresource.ciphgrpals = resource.ciphgrpals
				updateresource.ciphername = resource.ciphername
				updateresource.cipherpriority = resource.cipherpriority
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [sslcipher_sslciphersuite_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].ciphergroupname = resource[i].ciphergroupname
						updateresources[i].cipheroperation = resource[i].cipheroperation
						updateresources[i].ciphgrpals = resource[i].ciphgrpals
						updateresources[i].ciphername = resource[i].ciphername
						updateresources[i].cipherpriority = resource[i].cipherpriority
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = sslcipher_sslciphersuite_binding()
				deleteresource.ciphergroupname = resource.ciphergroupname
				deleteresource.ciphername = resource.ciphername
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [sslcipher_sslciphersuite_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].ciphergroupname = resource[i].ciphergroupname
						deleteresources[i].ciphername = resource[i].ciphername
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get_filtered(cls, service, obj, filter_) :
		r""" Use this API to fetch filtered set of sslcipher_sslciphersuite_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			option_ = options()
			option_.filter = filter_
			option_.args = nitro_util.object_to_string_withoutquotes(obj)
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, obj) :
		r""" Use this API to count sslcipher_sslciphersuite_binding resources configued on NetScaler.
		"""
		try :
			option_ = options()
			option_.count = True
			option_.args = nitro_util.object_to_string_withoutquotes(obj)
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, obj, filter_) :
		r""" Use this API to count the filtered set of sslcipher_sslciphersuite_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			option_ = options()
			option_.count = True
			option_.filter = filter_
			option_.args = nitro_util.object_to_string_withoutquotes(obj)
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	class Cipheroperation:
		ADD = "ADD"
		REM = "REM"
		ORD = "ORD"

class sslcipher_sslciphersuite_binding_response(base_response) :
	def __init__(self, length=1) :
		self.sslcipher_sslciphersuite_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.sslcipher_sslciphersuite_binding = [sslcipher_sslciphersuite_binding() for _ in range(length)]

