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

class ipsecalgsession(base_resource) :
	""" Configuration for IPSEC ALG session resource. """
	def __init__(self) :
		self._sourceip_alg = None
		self._natip_alg = None
		self._destip_alg = None
		self._sourceip = None
		self._natip = None
		self._destip = None
		self._spiin = None
		self._spiout = None
		self.___count = 0

	@property
	def sourceip_alg(self) :
		r"""Original Source IP address.<br/>Minimum length =  1.
		"""
		try :
			return self._sourceip_alg
		except Exception as e:
			raise e

	@sourceip_alg.setter
	def sourceip_alg(self, sourceip_alg) :
		r"""Original Source IP address.<br/>Minimum length =  1
		"""
		try :
			self._sourceip_alg = sourceip_alg
		except Exception as e:
			raise e

	@property
	def natip_alg(self) :
		r"""Natted Source IP address.<br/>Minimum length =  1.
		"""
		try :
			return self._natip_alg
		except Exception as e:
			raise e

	@natip_alg.setter
	def natip_alg(self, natip_alg) :
		r"""Natted Source IP address.<br/>Minimum length =  1
		"""
		try :
			self._natip_alg = natip_alg
		except Exception as e:
			raise e

	@property
	def destip_alg(self) :
		r"""Destination IP address.<br/>Minimum length =  1.
		"""
		try :
			return self._destip_alg
		except Exception as e:
			raise e

	@destip_alg.setter
	def destip_alg(self, destip_alg) :
		r"""Destination IP address.<br/>Minimum length =  1
		"""
		try :
			self._destip_alg = destip_alg
		except Exception as e:
			raise e

	@property
	def sourceip(self) :
		r"""Original Source IP address.<br/>Minimum length =  1.
		"""
		try :
			return self._sourceip
		except Exception as e:
			raise e

	@sourceip.setter
	def sourceip(self, sourceip) :
		r"""Original Source IP address.<br/>Minimum length =  1
		"""
		try :
			self._sourceip = sourceip
		except Exception as e:
			raise e

	@property
	def natip(self) :
		r"""Natted Source IP address.<br/>Minimum length =  1.
		"""
		try :
			return self._natip
		except Exception as e:
			raise e

	@natip.setter
	def natip(self, natip) :
		r"""Natted Source IP address.<br/>Minimum length =  1
		"""
		try :
			self._natip = natip
		except Exception as e:
			raise e

	@property
	def destip(self) :
		r"""Destination IP address.<br/>Minimum length =  1.
		"""
		try :
			return self._destip
		except Exception as e:
			raise e

	@destip.setter
	def destip(self, destip) :
		r"""Destination IP address.<br/>Minimum length =  1
		"""
		try :
			self._destip = destip
		except Exception as e:
			raise e

	@property
	def spiin(self) :
		r"""Client SPI for ESP.
		"""
		try :
			return self._spiin
		except Exception as e:
			raise e

	@property
	def spiout(self) :
		r"""Server SPI for ESP.
		"""
		try :
			return self._spiout
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(ipsecalgsession_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ipsecalgsession
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
	def flush(cls, client, resource) :
		r""" Use this API to flush ipsecalgsession.
		"""
		try :
			if type(resource) is not list :
				flushresource = ipsecalgsession()
				flushresource.sourceip = resource.sourceip
				flushresource.natip = resource.natip
				flushresource.destip = resource.destip
				return flushresource.perform_operation(client,"flush")
			else :
				if (resource and len(resource) > 0) :
					flushresources = [ ipsecalgsession() for _ in range(len(resource))]
					for i in range(len(resource)) :
						flushresources[i].sourceip = resource[i].sourceip
						flushresources[i].natip = resource[i].natip
						flushresources[i].destip = resource[i].destip
				result = cls.perform_operation_bulk_request(client, flushresources,"flush")
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the ipsecalgsession resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = ipsecalgsession()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		r""" Use this API to fetch all the ipsecalgsession resources that are configured on netscaler.
	# This uses ipsecalgsession_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = ipsecalgsession()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of ipsecalgsession resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = ipsecalgsession()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the ipsecalgsession resources configured on NetScaler.
		"""
		try :
			obj = ipsecalgsession()
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
		r""" Use this API to count filtered the set of ipsecalgsession resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = ipsecalgsession()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


class ipsecalgsession_response(base_response) :
	def __init__(self, length=1) :
		self.ipsecalgsession = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.ipsecalgsession = [ipsecalgsession() for _ in range(length)]

