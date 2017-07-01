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

class responderpolicylabel_stats(base_resource) :
	r""" Statistics for responder policy label resource.
	"""
	def __init__(self) :
		self._labelname = None
		self._clearstats = None
		self._pipolicylabelhits = 0
		self._pipolicylabelhitsrate = 0

		self.responderpolicy = []
	@property
	def labelname(self) :
		r"""Name of the responder policy label.<br/>Minimum length =  1.
		"""
		try :
			return self._labelname
		except Exception as e:
			raise e

	@labelname.setter
	def labelname(self, labelname) :
		r"""Name of the responder policy label.
		"""
		try :
			self._labelname = labelname
		except Exception as e:
			raise e

	@property
	def clearstats(self) :
		r"""Clear the statsistics / counters.<br/>Possible values = basic, full.
		"""
		try :
			return self._clearstats
		except Exception as e:
			raise e

	@clearstats.setter
	def clearstats(self, clearstats) :
		r"""Clear the statsistics / counters
		"""
		try :
			self._clearstats = clearstats
		except Exception as e:
			raise e

	@property
	def pipolicylabelhitsrate(self) :
		r"""Rate (/s) counter for pipolicylabelhits.
		"""
		try :
			return self._pipolicylabelhitsrate
		except Exception as e:
			raise e

	@property
	def pipolicylabelhits(self) :
		r"""Number of times policy label was invoked. .
		"""
		try :
			return self._pipolicylabelhits
		except Exception as e:
			raise e

	@property
	def responderpolicy(self) :
		r"""responderpolicy that are bound to responderpolicylabel.
		"""
		try :
			return self._responderpolicy
		except Exception as e:
			raise e

	@responderpolicy.setter
	def responderpolicy(self, responderpolicy) :
		r"""responderpolicy that are bound to responderpolicylabel.
		"""
		try :
			self._responderpolicy = responderpolicy
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(responderpolicylabel_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.responderpolicylabel
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.labelname is not None :
				return str(self.labelname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def  get(cls, service, name="", option_="") :
		r""" Use this API to fetch the statistics of all responderpolicylabel_stats resources that are configured on netscaler.
		 set statbindings=True in options to retrieve bindings.
		"""
		try :
			obj = responderpolicylabel_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			else :
				obj.labelname = name
				response = obj.stat_resource(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class responderpolicylabel_response(base_response) :
	def __init__(self, length=1) :
		self.responderpolicylabel = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.responderpolicylabel = [responderpolicylabel_stats() for _ in range(length)]

