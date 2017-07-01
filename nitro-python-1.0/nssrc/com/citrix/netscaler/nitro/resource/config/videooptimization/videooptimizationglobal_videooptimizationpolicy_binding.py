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

class videooptimizationglobal_videooptimizationpolicy_binding(base_resource) :
	""" Binding class showing the videooptimizationpolicy that can be bound to videooptimizationglobal.
	"""
	def __init__(self) :
		self._policyname = None
		self._type = None
		self._priority = None
		self._gotopriorityexpression = None
		self._numpol = None
		self._globalbindtype = None
		self._invoke = None
		self._labeltype = None
		self._labelname = None
		self.___count = 0

	@property
	def priority(self) :
		r"""Specifies the priority of the policy.
		"""
		try :
			return self._priority
		except Exception as e:
			raise e

	@priority.setter
	def priority(self, priority) :
		r"""Specifies the priority of the policy.
		"""
		try :
			self._priority = priority
		except Exception as e:
			raise e

	@property
	def globalbindtype(self) :
		r""".<br/>Default value: SYSTEM_GLOBAL<br/>Possible values = SYSTEM_GLOBAL, VPN_GLOBAL, RNAT_GLOBAL.
		"""
		try :
			return self._globalbindtype
		except Exception as e:
			raise e

	@globalbindtype.setter
	def globalbindtype(self, globalbindtype) :
		r""".<br/>Default value: SYSTEM_GLOBAL<br/>Possible values = SYSTEM_GLOBAL, VPN_GLOBAL, RNAT_GLOBAL
		"""
		try :
			self._globalbindtype = globalbindtype
		except Exception as e:
			raise e

	@property
	def policyname(self) :
		r"""Name of the video optimization policy.
		"""
		try :
			return self._policyname
		except Exception as e:
			raise e

	@policyname.setter
	def policyname(self, policyname) :
		r"""Name of the video optimization policy.
		"""
		try :
			self._policyname = policyname
		except Exception as e:
			raise e

	@property
	def labelname(self) :
		r"""Name of the policy label to invoke. If the current policy evaluates to TRUE, the invoke parameter is set, and Label Type is policylabel.
		"""
		try :
			return self._labelname
		except Exception as e:
			raise e

	@labelname.setter
	def labelname(self, labelname) :
		r"""Name of the policy label to invoke. If the current policy evaluates to TRUE, the invoke parameter is set, and Label Type is policylabel.
		"""
		try :
			self._labelname = labelname
		except Exception as e:
			raise e

	@property
	def gotopriorityexpression(self) :
		r"""Expression specifying the priority of the next policy which will get evaluated if the current policy rule evaluates to TRUE.
		"""
		try :
			return self._gotopriorityexpression
		except Exception as e:
			raise e

	@gotopriorityexpression.setter
	def gotopriorityexpression(self, gotopriorityexpression) :
		r"""Expression specifying the priority of the next policy which will get evaluated if the current policy rule evaluates to TRUE.
		"""
		try :
			self._gotopriorityexpression = gotopriorityexpression
		except Exception as e:
			raise e

	@property
	def type(self) :
		r"""Specifies the bind point whose policies you want to display.<br/>Possible values = REQ_OVERRIDE, REQ_DEFAULT, RES_OVERRIDE, RES_DEFAULT.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@type.setter
	def type(self, type) :
		r"""Specifies the bind point whose policies you want to display.<br/>Possible values = REQ_OVERRIDE, REQ_DEFAULT, RES_OVERRIDE, RES_DEFAULT
		"""
		try :
			self._type = type
		except Exception as e:
			raise e

	@property
	def invoke(self) :
		r"""If the current policy evaluates to TRUE, terminate evaluation of policies bound to the current policy label, and then forward the request to the specified virtual server or
		evaluate the specified policy label.
		"""
		try :
			return self._invoke
		except Exception as e:
			raise e

	@invoke.setter
	def invoke(self, invoke) :
		r"""If the current policy evaluates to TRUE, terminate evaluation of policies bound to the current policy label, and then forward the request to the specified virtual server or
		evaluate the specified policy label.
		"""
		try :
			self._invoke = invoke
		except Exception as e:
			raise e

	@property
	def labeltype(self) :
		r"""Type of invocation, Available settings function as follows:
		* vserver - Forward the request to the specified virtual server.
		* policylabel - Invoke the specified policy label.
		"""
		try :
			return self._labeltype
		except Exception as e:
			raise e

	@labeltype.setter
	def labeltype(self, labeltype) :
		r"""Type of invocation, Available settings function as follows:
		* vserver - Forward the request to the specified virtual server.
		* policylabel - Invoke the specified policy label.
		"""
		try :
			self._labeltype = labeltype
		except Exception as e:
			raise e

	@property
	def numpol(self) :
		r"""number of polices bound.
		"""
		try :
			return self._numpol
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(videooptimizationglobal_videooptimizationpolicy_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.videooptimizationglobal_videooptimizationpolicy_binding
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
				updateresource = videooptimizationglobal_videooptimizationpolicy_binding()
				updateresource.policyname = resource.policyname
				updateresource.priority = resource.priority
				updateresource.gotopriorityexpression = resource.gotopriorityexpression
				updateresource.type = resource.type
				updateresource.invoke = resource.invoke
				updateresource.labeltype = resource.labeltype
				updateresource.labelname = resource.labelname
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [videooptimizationglobal_videooptimizationpolicy_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].policyname = resource[i].policyname
						updateresources[i].priority = resource[i].priority
						updateresources[i].gotopriorityexpression = resource[i].gotopriorityexpression
						updateresources[i].type = resource[i].type
						updateresources[i].invoke = resource[i].invoke
						updateresources[i].labeltype = resource[i].labeltype
						updateresources[i].labelname = resource[i].labelname
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = videooptimizationglobal_videooptimizationpolicy_binding()
				deleteresource.policyname = resource.policyname
				deleteresource.type = resource.type
				deleteresource.priority = resource.priority
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [videooptimizationglobal_videooptimizationpolicy_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].policyname = resource[i].policyname
						deleteresources[i].type = resource[i].type
						deleteresources[i].priority = resource[i].priority
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service) :
		r""" Use this API to fetch a videooptimizationglobal_videooptimizationpolicy_binding resources.
		"""
		try :
			obj = videooptimizationglobal_videooptimizationpolicy_binding()
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, filter_) :
		r""" Use this API to fetch filtered set of videooptimizationglobal_videooptimizationpolicy_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = videooptimizationglobal_videooptimizationpolicy_binding()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service) :
		r""" Use this API to count videooptimizationglobal_videooptimizationpolicy_binding resources configued on NetScaler.
		"""
		try :
			obj = videooptimizationglobal_videooptimizationpolicy_binding()
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, filter_) :
		r""" Use this API to count the filtered set of videooptimizationglobal_videooptimizationpolicy_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = videooptimizationglobal_videooptimizationpolicy_binding()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	class Globalbindtype:
		SYSTEM_GLOBAL = "SYSTEM_GLOBAL"
		VPN_GLOBAL = "VPN_GLOBAL"
		RNAT_GLOBAL = "RNAT_GLOBAL"

	class Type:
		REQ_OVERRIDE = "REQ_OVERRIDE"
		REQ_DEFAULT = "REQ_DEFAULT"
		RES_OVERRIDE = "RES_OVERRIDE"
		RES_DEFAULT = "RES_DEFAULT"

	class Labeltype:
		vserver = "vserver"
		policylabel = "policylabel"

class videooptimizationglobal_videooptimizationpolicy_binding_response(base_response) :
	def __init__(self, length=1) :
		self.videooptimizationglobal_videooptimizationpolicy_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.videooptimizationglobal_videooptimizationpolicy_binding = [videooptimizationglobal_videooptimizationpolicy_binding() for _ in range(length)]

