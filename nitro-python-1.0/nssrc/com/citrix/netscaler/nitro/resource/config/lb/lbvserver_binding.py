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

class lbvserver_binding(base_resource):
	""" Binding class showing the resources that can be bound to lbvserver_binding. 
	"""
	def __init__(self) :
		self._name = None
		self.lbvserver_spilloverpolicy_binding = []
		self.lbvserver_csvserver_binding = []
		self.lbvserver_capolicy_binding = []
		self.lbvserver_auditnslogpolicy_binding = []
		self.lbvserver_filterpolicy_binding = []
		self.lbvserver_cmppolicy_binding = []
		self.lbvserver_appflowpolicy_binding = []
		self.lbvserver_responderpolicy_binding = []
		self.lbvserver_transformpolicy_binding = []
		self.lbvserver_dospolicy_binding = []
		self.lbvserver_servicegroupmember_binding = []
		self.lbvserver_feopolicy_binding = []
		self.lbvserver_authorizationpolicy_binding = []
		self.lbvserver_dnspolicy64_binding = []
		self.lbvserver_cachepolicy_binding = []
		self.lbvserver_rewritepolicy_binding = []
		self.lbvserver_scpolicy_binding = []
		self.lbvserver_pqpolicy_binding = []
		self.lbvserver_service_binding = []
		self.lbvserver_servicegroup_binding = []
		self.lbvserver_tmtrafficpolicy_binding = []
		self.lbvserver_auditsyslogpolicy_binding = []
		self.lbvserver_appqoepolicy_binding = []
		self.lbvserver_videooptimizationpolicy_binding = []
		self.lbvserver_appfwpolicy_binding = []

	@property
	def name(self) :
		r"""Name of the virtual server. If no name is provided, statistical data of all configured virtual servers is displayed.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name of the virtual server. If no name is provided, statistical data of all configured virtual servers is displayed.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def lbvserver_auditsyslogpolicy_bindings(self) :
		r"""auditsyslogpolicy that can be bound to lbvserver.
		"""
		try :
			return self._lbvserver_auditsyslogpolicy_binding
		except Exception as e:
			raise e

	@property
	def lbvserver_pqpolicy_bindings(self) :
		r"""pqpolicy that can be bound to lbvserver.
		"""
		try :
			return self._lbvserver_pqpolicy_binding
		except Exception as e:
			raise e

	@property
	def lbvserver_dnspolicy64_bindings(self) :
		r"""dnspolicy64 that can be bound to lbvserver.
		"""
		try :
			return self._lbvserver_dnspolicy64_binding
		except Exception as e:
			raise e

	@property
	def lbvserver_appfwpolicy_bindings(self) :
		r"""appfwpolicy that can be bound to lbvserver.
		"""
		try :
			return self._lbvserver_appfwpolicy_binding
		except Exception as e:
			raise e

	@property
	def lbvserver_rewritepolicy_bindings(self) :
		r"""rewritepolicy that can be bound to lbvserver.
		"""
		try :
			return self._lbvserver_rewritepolicy_binding
		except Exception as e:
			raise e

	@property
	def lbvserver_spilloverpolicy_bindings(self) :
		r"""spilloverpolicy that can be bound to lbvserver.
		"""
		try :
			return self._lbvserver_spilloverpolicy_binding
		except Exception as e:
			raise e

	@property
	def lbvserver_auditnslogpolicy_bindings(self) :
		r"""auditnslogpolicy that can be bound to lbvserver.
		"""
		try :
			return self._lbvserver_auditnslogpolicy_binding
		except Exception as e:
			raise e

	@property
	def lbvserver_appqoepolicy_bindings(self) :
		r"""appqoepolicy that can be bound to lbvserver.
		"""
		try :
			return self._lbvserver_appqoepolicy_binding
		except Exception as e:
			raise e

	@property
	def lbvserver_transformpolicy_bindings(self) :
		r"""transformpolicy that can be bound to lbvserver.
		"""
		try :
			return self._lbvserver_transformpolicy_binding
		except Exception as e:
			raise e

	@property
	def lbvserver_filterpolicy_bindings(self) :
		r"""filterpolicy that can be bound to lbvserver.
		"""
		try :
			return self._lbvserver_filterpolicy_binding
		except Exception as e:
			raise e

	@property
	def lbvserver_scpolicy_bindings(self) :
		r"""scpolicy that can be bound to lbvserver.
		"""
		try :
			return self._lbvserver_scpolicy_binding
		except Exception as e:
			raise e

	@property
	def lbvserver_feopolicy_bindings(self) :
		r"""feopolicy that can be bound to lbvserver.
		"""
		try :
			return self._lbvserver_feopolicy_binding
		except Exception as e:
			raise e

	@property
	def lbvserver_csvserver_bindings(self) :
		r"""csvserver that can be bound to lbvserver.
		"""
		try :
			return self._lbvserver_csvserver_binding
		except Exception as e:
			raise e

	@property
	def lbvserver_appflowpolicy_bindings(self) :
		r"""appflowpolicy that can be bound to lbvserver.
		"""
		try :
			return self._lbvserver_appflowpolicy_binding
		except Exception as e:
			raise e

	@property
	def lbvserver_capolicy_bindings(self) :
		r"""capolicy that can be bound to lbvserver.
		"""
		try :
			return self._lbvserver_capolicy_binding
		except Exception as e:
			raise e

	@property
	def lbvserver_authorizationpolicy_bindings(self) :
		r"""authorizationpolicy that can be bound to lbvserver.
		"""
		try :
			return self._lbvserver_authorizationpolicy_binding
		except Exception as e:
			raise e

	@property
	def lbvserver_servicegroup_bindings(self) :
		r"""servicegroup that can be bound to lbvserver.
		"""
		try :
			return self._lbvserver_servicegroup_binding
		except Exception as e:
			raise e

	@property
	def lbvserver_cachepolicy_bindings(self) :
		r"""cachepolicy that can be bound to lbvserver.
		"""
		try :
			return self._lbvserver_cachepolicy_binding
		except Exception as e:
			raise e

	@property
	def lbvserver_videooptimizationpolicy_bindings(self) :
		r"""videooptimizationpolicy that can be bound to lbvserver.
		"""
		try :
			return self._lbvserver_videooptimizationpolicy_binding
		except Exception as e:
			raise e

	@property
	def lbvserver_service_bindings(self) :
		r"""service that can be bound to lbvserver.
		"""
		try :
			return self._lbvserver_service_binding
		except Exception as e:
			raise e

	@property
	def lbvserver_servicegroupmember_bindings(self) :
		r"""servicegroupmember that can be bound to lbvserver.
		"""
		try :
			return self._lbvserver_servicegroupmember_binding
		except Exception as e:
			raise e

	@property
	def lbvserver_responderpolicy_bindings(self) :
		r"""responderpolicy that can be bound to lbvserver.
		"""
		try :
			return self._lbvserver_responderpolicy_binding
		except Exception as e:
			raise e

	@property
	def lbvserver_dospolicy_bindings(self) :
		r"""dospolicy that can be bound to lbvserver.
		"""
		try :
			return self._lbvserver_dospolicy_binding
		except Exception as e:
			raise e

	@property
	def lbvserver_tmtrafficpolicy_bindings(self) :
		r"""tmtrafficpolicy that can be bound to lbvserver.
		"""
		try :
			return self._lbvserver_tmtrafficpolicy_binding
		except Exception as e:
			raise e

	@property
	def lbvserver_cmppolicy_bindings(self) :
		r"""cmppolicy that can be bound to lbvserver.
		"""
		try :
			return self._lbvserver_cmppolicy_binding
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(lbvserver_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lbvserver_binding
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
	def get(self, service, name="", option_="") :
		r""" Use this API to fetch lbvserver_binding resource.
		"""
		try :
			if not name :
				obj = lbvserver_binding()
				response = obj.get_resources(service, option_)
			elif type(name) is not list :
				obj = lbvserver_binding()
				obj.name = name
				response = obj.get_resource(service)
			else :
				if name and len(name) > 0 :
					obj = [lbvserver_binding() for _ in range(len(name))]
					for i in range(len(name)) :
						obj[i].name = name[i];
						response[i] = obj[i].get_resource(service)
			return response
		except Exception as e:
			raise e

class lbvserver_binding_response(base_response) :
	def __init__(self, length=1) :
		self.lbvserver_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.lbvserver_binding = [lbvserver_binding() for _ in range(length)]

