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

class icalatencyprofile(base_resource) :
	""" Configuration for Profile for Latency monitoring resource. """
	def __init__(self) :
		self._name = None
		self._l7latencymonitoring = None
		self._l7latencythresholdfactor = None
		self._l7latencywaittime = None
		self._l7latencynotifyinterval = None
		self._l7latencymaxnotifycount = None
		self._refcnt = None
		self._builtin = []
		self._isdefault = None
		self.___count = 0

	@property
	def name(self) :
		r"""Name for the ICA latencyprofile. Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and
		the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed after the ICA latency profile is added.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my ica l7latencyprofile" or 'my ica l7latencyprofile').<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name for the ICA latencyprofile. Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and
		the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed after the ICA latency profile is added.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my ica l7latencyprofile" or 'my ica l7latencyprofile').<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def l7latencymonitoring(self) :
		r"""Enable/Disable L7 Latency monitoring for L7 latency notifications.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._l7latencymonitoring
		except Exception as e:
			raise e

	@l7latencymonitoring.setter
	def l7latencymonitoring(self, l7latencymonitoring) :
		r"""Enable/Disable L7 Latency monitoring for L7 latency notifications.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._l7latencymonitoring = l7latencymonitoring
		except Exception as e:
			raise e

	@property
	def l7latencythresholdfactor(self) :
		r"""L7 Latency threshold factor. This is the factor by which the active latency should be greater than the minimum observed value to determine that the latency is high and may need to be reported.<br/>Default value: 4<br/>Minimum length =  2<br/>Maximum length =  65535.
		"""
		try :
			return self._l7latencythresholdfactor
		except Exception as e:
			raise e

	@l7latencythresholdfactor.setter
	def l7latencythresholdfactor(self, l7latencythresholdfactor) :
		r"""L7 Latency threshold factor. This is the factor by which the active latency should be greater than the minimum observed value to determine that the latency is high and may need to be reported.<br/>Default value: 4<br/>Minimum length =  2<br/>Maximum length =  65535
		"""
		try :
			self._l7latencythresholdfactor = l7latencythresholdfactor
		except Exception as e:
			raise e

	@property
	def l7latencywaittime(self) :
		r"""L7 Latency Wait time. This is the time for which the Netscaler waits after the threshold is exceeded before it sends out a Notification to the Insight Center.<br/>Default value: 20<br/>Minimum length =  1<br/>Maximum length =  65535.
		"""
		try :
			return self._l7latencywaittime
		except Exception as e:
			raise e

	@l7latencywaittime.setter
	def l7latencywaittime(self, l7latencywaittime) :
		r"""L7 Latency Wait time. This is the time for which the Netscaler waits after the threshold is exceeded before it sends out a Notification to the Insight Center.<br/>Default value: 20<br/>Minimum length =  1<br/>Maximum length =  65535
		"""
		try :
			self._l7latencywaittime = l7latencywaittime
		except Exception as e:
			raise e

	@property
	def l7latencynotifyinterval(self) :
		r"""L7 Latency Notify Interval. This is the interval at which the Netscaler sends out notifications to the Insight Center after the wait time has passed.<br/>Default value: 20<br/>Minimum length =  1<br/>Maximum length =  65535.
		"""
		try :
			return self._l7latencynotifyinterval
		except Exception as e:
			raise e

	@l7latencynotifyinterval.setter
	def l7latencynotifyinterval(self, l7latencynotifyinterval) :
		r"""L7 Latency Notify Interval. This is the interval at which the Netscaler sends out notifications to the Insight Center after the wait time has passed.<br/>Default value: 20<br/>Minimum length =  1<br/>Maximum length =  65535
		"""
		try :
			self._l7latencynotifyinterval = l7latencynotifyinterval
		except Exception as e:
			raise e

	@property
	def l7latencymaxnotifycount(self) :
		r"""L7 Latency Max notify Count. This is the upper limit on the number of notifications sent to the Insight Center within an interval where the Latency is above the threshold.<br/>Default value: 5<br/>Minimum length =  1<br/>Maximum length =  65535.
		"""
		try :
			return self._l7latencymaxnotifycount
		except Exception as e:
			raise e

	@l7latencymaxnotifycount.setter
	def l7latencymaxnotifycount(self, l7latencymaxnotifycount) :
		r"""L7 Latency Max notify Count. This is the upper limit on the number of notifications sent to the Insight Center within an interval where the Latency is above the threshold.<br/>Default value: 5<br/>Minimum length =  1<br/>Maximum length =  65535
		"""
		try :
			self._l7latencymaxnotifycount = l7latencymaxnotifycount
		except Exception as e:
			raise e

	@property
	def refcnt(self) :
		r"""Number of entities using this l7latencyprofile.
		"""
		try :
			return self._refcnt
		except Exception as e:
			raise e

	@property
	def builtin(self) :
		r"""Indicates that the ICA latencyprofile is a built-in (SYSTEM INTERNAL) type.<br/>Possible values = MODIFIABLE, DELETABLE, IMMUTABLE, PARTITION_ALL.
		"""
		try :
			return self._builtin
		except Exception as e:
			raise e

	@property
	def isdefault(self) :
		r"""A value of true is returned if it is a default l7latencyprofile.
		"""
		try :
			return self._isdefault
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(icalatencyprofile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.icalatencyprofile
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
		r""" Use this API to add icalatencyprofile.
		"""
		try :
			if type(resource) is not list :
				addresource = icalatencyprofile()
				addresource.name = resource.name
				addresource.l7latencymonitoring = resource.l7latencymonitoring
				addresource.l7latencythresholdfactor = resource.l7latencythresholdfactor
				addresource.l7latencywaittime = resource.l7latencywaittime
				addresource.l7latencynotifyinterval = resource.l7latencynotifyinterval
				addresource.l7latencymaxnotifycount = resource.l7latencymaxnotifycount
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ icalatencyprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].l7latencymonitoring = resource[i].l7latencymonitoring
						addresources[i].l7latencythresholdfactor = resource[i].l7latencythresholdfactor
						addresources[i].l7latencywaittime = resource[i].l7latencywaittime
						addresources[i].l7latencynotifyinterval = resource[i].l7latencynotifyinterval
						addresources[i].l7latencymaxnotifycount = resource[i].l7latencymaxnotifycount
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete icalatencyprofile.
		"""
		try :
			if type(resource) is not list :
				deleteresource = icalatencyprofile()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ icalatencyprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ icalatencyprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update icalatencyprofile.
		"""
		try :
			if type(resource) is not list :
				updateresource = icalatencyprofile()
				updateresource.name = resource.name
				updateresource.l7latencymonitoring = resource.l7latencymonitoring
				updateresource.l7latencythresholdfactor = resource.l7latencythresholdfactor
				updateresource.l7latencywaittime = resource.l7latencywaittime
				updateresource.l7latencynotifyinterval = resource.l7latencynotifyinterval
				updateresource.l7latencymaxnotifycount = resource.l7latencymaxnotifycount
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ icalatencyprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].l7latencymonitoring = resource[i].l7latencymonitoring
						updateresources[i].l7latencythresholdfactor = resource[i].l7latencythresholdfactor
						updateresources[i].l7latencywaittime = resource[i].l7latencywaittime
						updateresources[i].l7latencynotifyinterval = resource[i].l7latencynotifyinterval
						updateresources[i].l7latencymaxnotifycount = resource[i].l7latencymaxnotifycount
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of icalatencyprofile resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = icalatencyprofile()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ icalatencyprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ icalatencyprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the icalatencyprofile resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = icalatencyprofile()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = icalatencyprofile()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [icalatencyprofile() for _ in range(len(name))]
						obj = [icalatencyprofile() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = icalatencyprofile()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of icalatencyprofile resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = icalatencyprofile()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the icalatencyprofile resources configured on NetScaler.
		"""
		try :
			obj = icalatencyprofile()
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
		r""" Use this API to count filtered the set of icalatencyprofile resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = icalatencyprofile()
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

	class L7latencymonitoring:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class icalatencyprofile_response(base_response) :
	def __init__(self, length=1) :
		self.icalatencyprofile = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.icalatencyprofile = [icalatencyprofile() for _ in range(length)]

