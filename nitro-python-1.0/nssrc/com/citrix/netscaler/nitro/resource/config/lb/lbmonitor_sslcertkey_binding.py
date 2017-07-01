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

class lbmonitor_sslcertkey_binding(base_resource) :
	""" Binding class showing the sslcertkey that can be bound to lbmonitor.
	"""
	def __init__(self) :
		self._certkeyname = None
		self._ca = None
		self._crlcheck = None
		self._ocspcheck = None
		self._monitorname = None
		self.___count = 0

	@property
	def crlcheck(self) :
		r"""The state of the CRL check parameter. (Mandatory/Optional).<br/>Possible values = Mandatory, Optional.
		"""
		try :
			return self._crlcheck
		except Exception as e:
			raise e

	@crlcheck.setter
	def crlcheck(self, crlcheck) :
		r"""The state of the CRL check parameter. (Mandatory/Optional).<br/>Possible values = Mandatory, Optional
		"""
		try :
			self._crlcheck = crlcheck
		except Exception as e:
			raise e

	@property
	def ca(self) :
		r"""The rule for use of CRL corresponding to this CA certificate during client authentication. If crlCheck is set to Mandatory, the system will deny all SSL clients if the CRL is missing, expired - NextUpdate date is in the past, or is incomplete with remote CRL refresh enabled. If crlCheck is set to optional, the system will allow SSL clients in the above error cases.However, in any case if the client certificate is revoked in the CRL, the SSL client will be denied access.
		"""
		try :
			return self._ca
		except Exception as e:
			raise e

	@ca.setter
	def ca(self, ca) :
		r"""The rule for use of CRL corresponding to this CA certificate during client authentication. If crlCheck is set to Mandatory, the system will deny all SSL clients if the CRL is missing, expired - NextUpdate date is in the past, or is incomplete with remote CRL refresh enabled. If crlCheck is set to optional, the system will allow SSL clients in the above error cases.However, in any case if the client certificate is revoked in the CRL, the SSL client will be denied access.
		"""
		try :
			self._ca = ca
		except Exception as e:
			raise e

	@property
	def certkeyname(self) :
		r"""The name of the certificate bound to the monitor.
		"""
		try :
			return self._certkeyname
		except Exception as e:
			raise e

	@certkeyname.setter
	def certkeyname(self, certkeyname) :
		r"""The name of the certificate bound to the monitor.
		"""
		try :
			self._certkeyname = certkeyname
		except Exception as e:
			raise e

	@property
	def monitorname(self) :
		r"""Name of the monitor.<br/>Minimum length =  1.
		"""
		try :
			return self._monitorname
		except Exception as e:
			raise e

	@monitorname.setter
	def monitorname(self, monitorname) :
		r"""Name of the monitor.<br/>Minimum length =  1
		"""
		try :
			self._monitorname = monitorname
		except Exception as e:
			raise e

	@property
	def ocspcheck(self) :
		r"""The state of the OCSP check parameter. (Mandatory/Optional).<br/>Possible values = Mandatory, Optional.
		"""
		try :
			return self._ocspcheck
		except Exception as e:
			raise e

	@ocspcheck.setter
	def ocspcheck(self, ocspcheck) :
		r"""The state of the OCSP check parameter. (Mandatory/Optional).<br/>Possible values = Mandatory, Optional
		"""
		try :
			self._ocspcheck = ocspcheck
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(lbmonitor_sslcertkey_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lbmonitor_sslcertkey_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.monitorname is not None :
				return str(self.monitorname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				updateresource = lbmonitor_sslcertkey_binding()
				updateresource.monitorname = resource.monitorname
				updateresource.certkeyname = resource.certkeyname
				updateresource.ca = resource.ca
				updateresource.crlcheck = resource.crlcheck
				updateresource.ocspcheck = resource.ocspcheck
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [lbmonitor_sslcertkey_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].monitorname = resource[i].monitorname
						updateresources[i].certkeyname = resource[i].certkeyname
						updateresources[i].ca = resource[i].ca
						updateresources[i].crlcheck = resource[i].crlcheck
						updateresources[i].ocspcheck = resource[i].ocspcheck
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = lbmonitor_sslcertkey_binding()
				deleteresource.monitorname = resource.monitorname
				deleteresource.certkeyname = resource.certkeyname
				deleteresource.ca = resource.ca
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [lbmonitor_sslcertkey_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].monitorname = resource[i].monitorname
						deleteresources[i].certkeyname = resource[i].certkeyname
						deleteresources[i].ca = resource[i].ca
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, monitorname="", option_="") :
		r""" Use this API to fetch lbmonitor_sslcertkey_binding resources.
		"""
		try :
			if not monitorname :
				obj = lbmonitor_sslcertkey_binding()
				response = obj.get_resources(service, option_)
			else :
				obj = lbmonitor_sslcertkey_binding()
				obj.monitorname = monitorname
				response = obj.get_resources(service)
				return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, monitorname, filter_) :
		r""" Use this API to fetch filtered set of lbmonitor_sslcertkey_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lbmonitor_sslcertkey_binding()
			obj.monitorname = monitorname
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, monitorname) :
		r""" Use this API to count lbmonitor_sslcertkey_binding resources configued on NetScaler.
		"""
		try :
			obj = lbmonitor_sslcertkey_binding()
			obj.monitorname = monitorname
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, monitorname, filter_) :
		r""" Use this API to count the filtered set of lbmonitor_sslcertkey_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lbmonitor_sslcertkey_binding()
			obj.monitorname = monitorname
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	class Dup_state:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Ocspcheck:
		Mandatory = "Mandatory"
		Optional = "Optional"

	class Crlcheck:
		Mandatory = "Mandatory"
		Optional = "Optional"

	class State:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class lbmonitor_sslcertkey_binding_response(base_response) :
	def __init__(self, length=1) :
		self.lbmonitor_sslcertkey_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.lbmonitor_sslcertkey_binding = [lbmonitor_sslcertkey_binding() for _ in range(length)]

