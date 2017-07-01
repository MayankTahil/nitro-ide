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

class videooptimizationaction(base_resource) :
	""" Configuration for videooptimization action resource. """
	def __init__(self) :
		self._name = None
		self._type = None
		self._rate = None
		self._comment = None
		self._newname = None
		self._hits = None
		self._referencecount = None
		self._undefhits = None
		self._builtin = []
		self.___count = 0

	@property
	def name(self) :
		r"""Name for the video optimization action. Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) hash (#), space ( ), at (@), equals (=), colon (:), and underscore characters.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name for the video optimization action. Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) hash (#), space ( ), at (@), equals (=), colon (:), and underscore characters.
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def type(self) :
		r"""Type of video optimization action. Available settings function as follows:
		* clear_text_pd - Cleartext PD type is detected.
		* clear_text_abr - Cleartext ABR is detected.
		* encrypted_abr - Encrypted ABR is detected.
		* trigger_enc_abr - Possible encrypted ABR is detected.
		* optimize_abr - Optimize detected ABR.<br/>Possible values = clear_text_pd, clear_text_abr, encrypted_abr, trigger_enc_abr, optimize_abr.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@type.setter
	def type(self, type) :
		r"""Type of video optimization action. Available settings function as follows:
		* clear_text_pd - Cleartext PD type is detected.
		* clear_text_abr - Cleartext ABR is detected.
		* encrypted_abr - Encrypted ABR is detected.
		* trigger_enc_abr - Possible encrypted ABR is detected.
		* optimize_abr - Optimize detected ABR.<br/>Possible values = clear_text_pd, clear_text_abr, encrypted_abr, trigger_enc_abr, optimize_abr
		"""
		try :
			self._type = type
		except Exception as e:
			raise e

	@property
	def rate(self) :
		r"""ABR Optimization Rate (in Kbps).<br/>Default value: 1000<br/>Minimum length =  1<br/>Maximum length =  2147483647.
		"""
		try :
			return self._rate
		except Exception as e:
			raise e

	@rate.setter
	def rate(self, rate) :
		r"""ABR Optimization Rate (in Kbps).<br/>Default value: 1000<br/>Minimum length =  1<br/>Maximum length =  2147483647
		"""
		try :
			self._rate = rate
		except Exception as e:
			raise e

	@property
	def comment(self) :
		r"""Comment. Any type of information about this video optimization action.
		"""
		try :
			return self._comment
		except Exception as e:
			raise e

	@comment.setter
	def comment(self, comment) :
		r"""Comment. Any type of information about this video optimization action.
		"""
		try :
			self._comment = comment
		except Exception as e:
			raise e

	@property
	def newname(self) :
		r"""New name for the videooptimization action.
		Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) hash (#), space ( ), at (@), equals (=), colon (:), and underscore characters.<br/>Minimum length =  1.
		"""
		try :
			return self._newname
		except Exception as e:
			raise e

	@newname.setter
	def newname(self, newname) :
		r"""New name for the videooptimization action.
		Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) hash (#), space ( ), at (@), equals (=), colon (:), and underscore characters.<br/>Minimum length =  1
		"""
		try :
			self._newname = newname
		except Exception as e:
			raise e

	@property
	def hits(self) :
		r"""The number of times the action has been taken.
		"""
		try :
			return self._hits
		except Exception as e:
			raise e

	@property
	def referencecount(self) :
		r"""The number of references to the action.
		"""
		try :
			return self._referencecount
		except Exception as e:
			raise e

	@property
	def undefhits(self) :
		r"""The number of times the action resulted in UNDEF.
		"""
		try :
			return self._undefhits
		except Exception as e:
			raise e

	@property
	def builtin(self) :
		r"""Flag to determine whether video optimization action is built-in or not.<br/>Possible values = MODIFIABLE, DELETABLE, IMMUTABLE, PARTITION_ALL.
		"""
		try :
			return self._builtin
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(videooptimizationaction_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.videooptimizationaction
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
	def add(cls, client, resource) :
		r""" Use this API to add videooptimizationaction.
		"""
		try :
			if type(resource) is not list :
				addresource = videooptimizationaction()
				addresource.name = resource.name
				addresource.type = resource.type
				addresource.rate = resource.rate
				addresource.comment = resource.comment
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ videooptimizationaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].type = resource[i].type
						addresources[i].rate = resource[i].rate
						addresources[i].comment = resource[i].comment
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete videooptimizationaction.
		"""
		try :
			if type(resource) is not list :
				deleteresource = videooptimizationaction()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ videooptimizationaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ videooptimizationaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update videooptimizationaction.
		"""
		try :
			if type(resource) is not list :
				updateresource = videooptimizationaction()
				updateresource.name = resource.name
				updateresource.type = resource.type
				updateresource.rate = resource.rate
				updateresource.comment = resource.comment
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ videooptimizationaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].type = resource[i].type
						updateresources[i].rate = resource[i].rate
						updateresources[i].comment = resource[i].comment
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of videooptimizationaction resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = videooptimizationaction()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ videooptimizationaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ videooptimizationaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def rename(cls, client, resource, new_name) :
		r""" Use this API to rename a videooptimizationaction resource.
		"""
		try :
			renameresource = videooptimizationaction()
			if type(resource) == cls :
				renameresource.name = resource.name
			else :
				renameresource.name = resource
			return renameresource.rename_resource(client,new_name)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the videooptimizationaction resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = videooptimizationaction()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = videooptimizationaction()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [videooptimizationaction() for _ in range(len(name))]
						obj = [videooptimizationaction() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = videooptimizationaction()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of videooptimizationaction resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = videooptimizationaction()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the videooptimizationaction resources configured on NetScaler.
		"""
		try :
			obj = videooptimizationaction()
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
		r""" Use this API to count filtered the set of videooptimizationaction resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = videooptimizationaction()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Builtin:
		MODIFIABLE = "MODIFIABLE"
		DELETABLE = "DELETABLE"
		IMMUTABLE = "IMMUTABLE"
		PARTITION_ALL = "PARTITION_ALL"

	class Type:
		clear_text_pd = "clear_text_pd"
		clear_text_abr = "clear_text_abr"
		encrypted_abr = "encrypted_abr"
		trigger_enc_abr = "trigger_enc_abr"
		optimize_abr = "optimize_abr"

class videooptimizationaction_response(base_response) :
	def __init__(self, length=1) :
		self.videooptimizationaction = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.videooptimizationaction = [videooptimizationaction() for _ in range(length)]

