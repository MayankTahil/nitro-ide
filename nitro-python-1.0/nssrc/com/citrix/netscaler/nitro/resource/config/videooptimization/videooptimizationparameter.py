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

class videooptimizationparameter(base_resource) :
	""" Configuration for VideoOptimization parameter resource. """
	def __init__(self) :
		self._randomsamplingpercentage = None

	@property
	def randomsamplingpercentage(self) :
		r"""Random Sampling Percentage.<br/>Default value: 0<br/>Maximum length =  100.
		"""
		try :
			return self._randomsamplingpercentage
		except Exception as e:
			raise e

	@randomsamplingpercentage.setter
	def randomsamplingpercentage(self, randomsamplingpercentage) :
		r"""Random Sampling Percentage.<br/>Default value: 0<br/>Maximum length =  100
		"""
		try :
			self._randomsamplingpercentage = randomsamplingpercentage
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(videooptimizationparameter_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.videooptimizationparameter
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
	def update(cls, client, resource) :
		r""" Use this API to update videooptimizationparameter.
		"""
		try :
			if type(resource) is not list :
				updateresource = videooptimizationparameter()
				updateresource.randomsamplingpercentage = resource.randomsamplingpercentage
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of videooptimizationparameter resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = videooptimizationparameter()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the videooptimizationparameter resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = videooptimizationparameter()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


class videooptimizationparameter_response(base_response) :
	def __init__(self, length=1) :
		self.videooptimizationparameter = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.videooptimizationparameter = [videooptimizationparameter() for _ in range(length)]

