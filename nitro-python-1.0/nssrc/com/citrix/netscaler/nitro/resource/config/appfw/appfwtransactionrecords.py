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

class appfwtransactionrecords(base_resource) :
	""" Configuration for Application firewall transaction record resource. """
	def __init__(self) :
		self._nodeid = None
		self._httptransactionid = None
		self._packetengineid = None
		self._appfwsessionid = None
		self._profilename = None
		self._url = None
		self._clientip = None
		self._destip = None
		self._starttime = None
		self._endtime = None
		self._requestcontentlength = None
		self._requestyields = None
		self._requestmaxprocessingtime = None
		self._responsecontentlength = None
		self._responseyields = None
		self._responsemaxprocessingtime = None
		self.___count = 0

	@property
	def nodeid(self) :
		r"""Unique number that identifies the cluster node.<br/>Maximum length =  31.
		"""
		try :
			return self._nodeid
		except Exception as e:
			raise e

	@nodeid.setter
	def nodeid(self, nodeid) :
		r"""Unique number that identifies the cluster node.<br/>Maximum length =  31
		"""
		try :
			self._nodeid = nodeid
		except Exception as e:
			raise e

	@property
	def httptransactionid(self) :
		r"""The http transaction identifier.
		"""
		try :
			return self._httptransactionid
		except Exception as e:
			raise e

	@property
	def packetengineid(self) :
		r"""The packet engine identifier.
		"""
		try :
			return self._packetengineid
		except Exception as e:
			raise e

	@property
	def appfwsessionid(self) :
		r"""The session identifier set by the Application Firewall to track the user session.
		"""
		try :
			return self._appfwsessionid
		except Exception as e:
			raise e

	@property
	def profilename(self) :
		r"""Application Firewall profile name.
		"""
		try :
			return self._profilename
		except Exception as e:
			raise e

	@property
	def url(self) :
		r"""Request URL.
		"""
		try :
			return self._url
		except Exception as e:
			raise e

	@property
	def clientip(self) :
		r"""The IP address of client.
		"""
		try :
			return self._clientip
		except Exception as e:
			raise e

	@property
	def destip(self) :
		r"""The IP address of destination.
		"""
		try :
			return self._destip
		except Exception as e:
			raise e

	@property
	def starttime(self) :
		r"""Conveys time at which request processing started.
		"""
		try :
			return self._starttime
		except Exception as e:
			raise e

	@property
	def endtime(self) :
		r"""Conveys time at which request processing end.
		"""
		try :
			return self._endtime
		except Exception as e:
			raise e

	@property
	def requestcontentlength(self) :
		r"""The content length of request.
		"""
		try :
			return self._requestcontentlength
		except Exception as e:
			raise e

	@property
	def requestyields(self) :
		r"""The number of times yielded during request processing to send heart beat packets.
		"""
		try :
			return self._requestyields
		except Exception as e:
			raise e

	@property
	def requestmaxprocessingtime(self) :
		r"""The maximum processing time across yields during request processing.
		"""
		try :
			return self._requestmaxprocessingtime
		except Exception as e:
			raise e

	@property
	def responsecontentlength(self) :
		r"""The content length of response.
		"""
		try :
			return self._responsecontentlength
		except Exception as e:
			raise e

	@property
	def responseyields(self) :
		r"""The number of times yielded during response processing to send heart beat packets.
		"""
		try :
			return self._responseyields
		except Exception as e:
			raise e

	@property
	def responsemaxprocessingtime(self) :
		r"""The maximum processing time across yields during response processing.
		"""
		try :
			return self._responsemaxprocessingtime
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(appfwtransactionrecords_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.appfwtransactionrecords
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
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the appfwtransactionrecords resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = appfwtransactionrecords()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		r""" Use this API to fetch all the appfwtransactionrecords resources that are configured on netscaler.
	# This uses appfwtransactionrecords_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = appfwtransactionrecords()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of appfwtransactionrecords resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = appfwtransactionrecords()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the appfwtransactionrecords resources configured on NetScaler.
		"""
		try :
			obj = appfwtransactionrecords()
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
		r""" Use this API to count filtered the set of appfwtransactionrecords resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = appfwtransactionrecords()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


class appfwtransactionrecords_response(base_response) :
	def __init__(self, length=1) :
		self.appfwtransactionrecords = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.appfwtransactionrecords = [appfwtransactionrecords() for _ in range(length)]

