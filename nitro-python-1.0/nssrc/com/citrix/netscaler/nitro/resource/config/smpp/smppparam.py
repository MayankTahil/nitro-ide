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

class smppparam(base_resource) :
	""" Configuration for SMPP configuration parameters resource. """
	def __init__(self) :
		self._clientmode = None
		self._msgqueue = None
		self._msgqueuesize = None
		self._addrton = None
		self._addrnpi = None
		self._addrrange = None

	@property
	def clientmode(self) :
		r"""Mode in which the client binds to the ADC. Applicable settings function as follows:
		* TRANSCEIVER - Client can send and receive messages to and from the message center.
		* TRANSMITTERONLY - Client can only send messages.
		* RECEIVERONLY - Client can only receive messages.<br/>Default value: TRANSCEIVER<br/>Possible values = TRANSCEIVER, TRANSMITTERONLY, RECEIVERONLY.
		"""
		try :
			return self._clientmode
		except Exception as e:
			raise e

	@clientmode.setter
	def clientmode(self, clientmode) :
		r"""Mode in which the client binds to the ADC. Applicable settings function as follows:
		* TRANSCEIVER - Client can send and receive messages to and from the message center.
		* TRANSMITTERONLY - Client can only send messages.
		* RECEIVERONLY - Client can only receive messages.<br/>Default value: TRANSCEIVER<br/>Possible values = TRANSCEIVER, TRANSMITTERONLY, RECEIVERONLY
		"""
		try :
			self._clientmode = clientmode
		except Exception as e:
			raise e

	@property
	def msgqueue(self) :
		r"""Queue SMPP messages if a client that is capable of receiving the destination address messages is not available.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._msgqueue
		except Exception as e:
			raise e

	@msgqueue.setter
	def msgqueue(self, msgqueue) :
		r"""Queue SMPP messages if a client that is capable of receiving the destination address messages is not available.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._msgqueue = msgqueue
		except Exception as e:
			raise e

	@property
	def msgqueuesize(self) :
		r"""Maximum number of SMPP messages that can be queued. After the limit is reached, the NetScaler ADC sends a deliver_sm_resp PDU, with an appropriate error message, to the message center.<br/>Default value: 10000.
		"""
		try :
			return self._msgqueuesize
		except Exception as e:
			raise e

	@msgqueuesize.setter
	def msgqueuesize(self, msgqueuesize) :
		r"""Maximum number of SMPP messages that can be queued. After the limit is reached, the NetScaler ADC sends a deliver_sm_resp PDU, with an appropriate error message, to the message center.<br/>Default value: 10000
		"""
		try :
			self._msgqueuesize = msgqueuesize
		except Exception as e:
			raise e

	@property
	def addrton(self) :
		r"""Type of Number, such as an international number or a national number, used in the ESME address sent in the bind request.<br/>Default value: 0<br/>Maximum length =  256.
		"""
		try :
			return self._addrton
		except Exception as e:
			raise e

	@addrton.setter
	def addrton(self, addrton) :
		r"""Type of Number, such as an international number or a national number, used in the ESME address sent in the bind request.<br/>Default value: 0<br/>Maximum length =  256
		"""
		try :
			self._addrton = addrton
		except Exception as e:
			raise e

	@property
	def addrnpi(self) :
		r"""Numbering Plan Indicator, such as landline, data, or WAP client, used in the ESME address sent in the bind request.<br/>Default value: 0<br/>Maximum length =  256.
		"""
		try :
			return self._addrnpi
		except Exception as e:
			raise e

	@addrnpi.setter
	def addrnpi(self, addrnpi) :
		r"""Numbering Plan Indicator, such as landline, data, or WAP client, used in the ESME address sent in the bind request.<br/>Default value: 0<br/>Maximum length =  256
		"""
		try :
			self._addrnpi = addrnpi
		except Exception as e:
			raise e

	@property
	def addrrange(self) :
		r"""Set of SME addresses, sent in the bind request, serviced by the ESME.<br/>Default value: "\\d*".
		"""
		try :
			return self._addrrange
		except Exception as e:
			raise e

	@addrrange.setter
	def addrrange(self, addrrange) :
		r"""Set of SME addresses, sent in the bind request, serviced by the ESME.<br/>Default value: "\\d*"
		"""
		try :
			self._addrrange = addrrange
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(smppparam_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.smppparam
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
		r""" Use this API to update smppparam.
		"""
		try :
			if type(resource) is not list :
				updateresource = smppparam()
				updateresource.clientmode = resource.clientmode
				updateresource.msgqueue = resource.msgqueue
				updateresource.msgqueuesize = resource.msgqueuesize
				updateresource.addrton = resource.addrton
				updateresource.addrnpi = resource.addrnpi
				updateresource.addrrange = resource.addrrange
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of smppparam resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = smppparam()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the smppparam resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = smppparam()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Clientmode:
		TRANSCEIVER = "TRANSCEIVER"
		TRANSMITTERONLY = "TRANSMITTERONLY"
		RECEIVERONLY = "RECEIVERONLY"

	class Msgqueue:
		ON = "ON"
		OFF = "OFF"

class smppparam_response(base_response) :
	def __init__(self, length=1) :
		self.smppparam = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.smppparam = [smppparam() for _ in range(length)]

