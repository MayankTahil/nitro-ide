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

class sslhsmkey(base_resource) :
	""" Configuration for HSM key resource. """
	def __init__(self) :
		self._hsmkeyname = None
		self._hsmtype = None
		self._key = None
		self._serialnum = None
		self._password = None
		self.___count = 0

	@property
	def hsmkeyname(self) :
		r""".<br/>Minimum length =  1.
		"""
		try :
			return self._hsmkeyname
		except Exception as e:
			raise e

	@hsmkeyname.setter
	def hsmkeyname(self, hsmkeyname) :
		r""".<br/>Minimum length =  1
		"""
		try :
			self._hsmkeyname = hsmkeyname
		except Exception as e:
			raise e

	@property
	def hsmtype(self) :
		r"""Type of HSM.<br/>Default value: THALES<br/>Possible values = THALES, SAFENET.
		"""
		try :
			return self._hsmtype
		except Exception as e:
			raise e

	@hsmtype.setter
	def hsmtype(self, hsmtype) :
		r"""Type of HSM.<br/>Default value: THALES<br/>Possible values = THALES, SAFENET
		"""
		try :
			self._hsmtype = hsmtype
		except Exception as e:
			raise e

	@property
	def key(self) :
		r"""Name of and, optionally, path to the HSM key file. /var/opt/nfast/kmdata/local/ is the default path. Applies only to THALES HSM.<br/>Maximum length =  63.
		"""
		try :
			return self._key
		except Exception as e:
			raise e

	@key.setter
	def key(self, key) :
		r"""Name of and, optionally, path to the HSM key file. /var/opt/nfast/kmdata/local/ is the default path. Applies only to THALES HSM.<br/>Maximum length =  63
		"""
		try :
			self._key = key
		except Exception as e:
			raise e

	@property
	def serialnum(self) :
		r"""Serial number of the partition on which the key is present. Applies only to SafeNet HSM.<br/>Maximum length =  16.
		"""
		try :
			return self._serialnum
		except Exception as e:
			raise e

	@serialnum.setter
	def serialnum(self, serialnum) :
		r"""Serial number of the partition on which the key is present. Applies only to SafeNet HSM.<br/>Maximum length =  16
		"""
		try :
			self._serialnum = serialnum
		except Exception as e:
			raise e

	@property
	def password(self) :
		r"""Password for a partition. Applies only to SafeNet HSM.<br/>Minimum length =  1.
		"""
		try :
			return self._password
		except Exception as e:
			raise e

	@password.setter
	def password(self, password) :
		r"""Password for a partition. Applies only to SafeNet HSM.<br/>Minimum length =  1
		"""
		try :
			self._password = password
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(sslhsmkey_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sslhsmkey
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.hsmkeyname is not None :
				return str(self.hsmkeyname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add sslhsmkey.
		"""
		try :
			if type(resource) is not list :
				addresource = sslhsmkey()
				addresource.hsmkeyname = resource.hsmkeyname
				addresource.hsmtype = resource.hsmtype
				addresource.key = resource.key
				addresource.serialnum = resource.serialnum
				addresource.password = resource.password
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ sslhsmkey() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].hsmkeyname = resource[i].hsmkeyname
						addresources[i].hsmtype = resource[i].hsmtype
						addresources[i].key = resource[i].key
						addresources[i].serialnum = resource[i].serialnum
						addresources[i].password = resource[i].password
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete sslhsmkey.
		"""
		try :
			if type(resource) is not list :
				deleteresource = sslhsmkey()
				if type(resource) !=  type(deleteresource):
					deleteresource.hsmkeyname = resource
				else :
					deleteresource.hsmkeyname = resource.hsmkeyname
					deleteresource.hsmtype = resource.hsmtype
					deleteresource.serialnum = resource.serialnum
					deleteresource.password = resource.password
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ sslhsmkey() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].hsmkeyname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ sslhsmkey() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].hsmkeyname = resource[i].hsmkeyname
							deleteresources[i].hsmtype = resource[i].hsmtype
							deleteresources[i].serialnum = resource[i].serialnum
							deleteresources[i].password = resource[i].password
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the sslhsmkey resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = sslhsmkey()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = sslhsmkey()
					obj.hsmkeyname = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [sslhsmkey() for _ in range(len(name))]
						obj = [sslhsmkey() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = sslhsmkey()
							obj[i].hsmkeyname = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of sslhsmkey resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslhsmkey()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the sslhsmkey resources configured on NetScaler.
		"""
		try :
			obj = sslhsmkey()
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
		r""" Use this API to count filtered the set of sslhsmkey resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslhsmkey()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Hsmtype:
		THALES = "THALES"
		SAFENET = "SAFENET"

class sslhsmkey_response(base_response) :
	def __init__(self, length=1) :
		self.sslhsmkey = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.sslhsmkey = [sslhsmkey() for _ in range(length)]

