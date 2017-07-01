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

class appflowaction(base_resource) :
	""" Configuration for AppFlow action resource. """
	def __init__(self) :
		self._name = None
		self._collectors = []
		self._clientsidemeasurements = None
		self._pagetracking = None
		self._webinsight = None
		self._securityinsight = None
		self._videoanalytics = None
		self._distributionalgorithm = None
		self._metricslog = None
		self._transactionlog = None
		self._comment = None
		self._newname = None
		self._hits = None
		self._referencecount = None
		self._description = None
		self.___count = 0

	@property
	def name(self) :
		r"""Name for the action. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my appflow action" or 'my appflow action').
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name for the action. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my appflow action" or 'my appflow action').
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def collectors(self) :
		r"""Name(s) of collector(s) to be associated with the AppFlow action.<br/>Minimum length =  1.
		"""
		try :
			return self._collectors
		except Exception as e:
			raise e

	@collectors.setter
	def collectors(self, collectors) :
		r"""Name(s) of collector(s) to be associated with the AppFlow action.<br/>Minimum length =  1
		"""
		try :
			self._collectors = collectors
		except Exception as e:
			raise e

	@property
	def clientsidemeasurements(self) :
		r"""On enabling this option, the NetScaler will collect the time required to load and render the mainpage on the client.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._clientsidemeasurements
		except Exception as e:
			raise e

	@clientsidemeasurements.setter
	def clientsidemeasurements(self, clientsidemeasurements) :
		r"""On enabling this option, the NetScaler will collect the time required to load and render the mainpage on the client.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._clientsidemeasurements = clientsidemeasurements
		except Exception as e:
			raise e

	@property
	def pagetracking(self) :
		r"""On enabling this option, the NetScaler will start tracking the page for waterfall chart by inserting a NS_ESNS cookie in the response.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._pagetracking
		except Exception as e:
			raise e

	@pagetracking.setter
	def pagetracking(self, pagetracking) :
		r"""On enabling this option, the NetScaler will start tracking the page for waterfall chart by inserting a NS_ESNS cookie in the response.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._pagetracking = pagetracking
		except Exception as e:
			raise e

	@property
	def webinsight(self) :
		r"""On enabling this option, the netscaler will send the webinsight records to the configured collectors.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._webinsight
		except Exception as e:
			raise e

	@webinsight.setter
	def webinsight(self, webinsight) :
		r"""On enabling this option, the netscaler will send the webinsight records to the configured collectors.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._webinsight = webinsight
		except Exception as e:
			raise e

	@property
	def securityinsight(self) :
		r"""On enabling this option, the netscaler will send the security insight records to the configured collectors.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._securityinsight
		except Exception as e:
			raise e

	@securityinsight.setter
	def securityinsight(self, securityinsight) :
		r"""On enabling this option, the netscaler will send the security insight records to the configured collectors.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._securityinsight = securityinsight
		except Exception as e:
			raise e

	@property
	def videoanalytics(self) :
		r"""On enabling this option, the netscaler will send the videoinsight records to the configured collectors.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._videoanalytics
		except Exception as e:
			raise e

	@videoanalytics.setter
	def videoanalytics(self, videoanalytics) :
		r"""On enabling this option, the netscaler will send the videoinsight records to the configured collectors.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._videoanalytics = videoanalytics
		except Exception as e:
			raise e

	@property
	def distributionalgorithm(self) :
		r"""On enabling this option, the netscaler will distribute records among the collectors. Else, all records will be sent to all the collectors.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._distributionalgorithm
		except Exception as e:
			raise e

	@distributionalgorithm.setter
	def distributionalgorithm(self, distributionalgorithm) :
		r"""On enabling this option, the netscaler will distribute records among the collectors. Else, all records will be sent to all the collectors.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._distributionalgorithm = distributionalgorithm
		except Exception as e:
			raise e

	@property
	def metricslog(self) :
		r"""If only the stats records are to be exported, turn on this option.
		"""
		try :
			return self._metricslog
		except Exception as e:
			raise e

	@metricslog.setter
	def metricslog(self, metricslog) :
		r"""If only the stats records are to be exported, turn on this option.
		"""
		try :
			self._metricslog = metricslog
		except Exception as e:
			raise e

	@property
	def transactionlog(self) :
		r"""If over stats channel, transactions logs also need to be sent, set this option appropriately. By default netscaler sends anomalous transaction logs over metrics channel. This can be changed to ALL or NONE transactions.<br/>Default value: ANOMALOUS<br/>Possible values = ANOMALOUS, NONE, ALL.
		"""
		try :
			return self._transactionlog
		except Exception as e:
			raise e

	@transactionlog.setter
	def transactionlog(self, transactionlog) :
		r"""If over stats channel, transactions logs also need to be sent, set this option appropriately. By default netscaler sends anomalous transaction logs over metrics channel. This can be changed to ALL or NONE transactions.<br/>Default value: ANOMALOUS<br/>Possible values = ANOMALOUS, NONE, ALL
		"""
		try :
			self._transactionlog = transactionlog
		except Exception as e:
			raise e

	@property
	def comment(self) :
		r"""Any comments about this action.  In the CLI, if including spaces between words, enclose the comment in quotation marks. (The quotation marks are not required in the configuration utility.).<br/>Maximum length =  256.
		"""
		try :
			return self._comment
		except Exception as e:
			raise e

	@comment.setter
	def comment(self, comment) :
		r"""Any comments about this action.  In the CLI, if including spaces between words, enclose the comment in quotation marks. (The quotation marks are not required in the configuration utility.).<br/>Maximum length =  256
		"""
		try :
			self._comment = comment
		except Exception as e:
			raise e

	@property
	def newname(self) :
		r"""New name for the AppFlow action. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at
		(@), equals (=), and hyphen (-) characters. 
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my appflow action" or 'my appflow action').<br/>Minimum length =  1.
		"""
		try :
			return self._newname
		except Exception as e:
			raise e

	@newname.setter
	def newname(self, newname) :
		r"""New name for the AppFlow action. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at
		(@), equals (=), and hyphen (-) characters. 
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my appflow action" or 'my appflow action').<br/>Minimum length =  1
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
	def description(self) :
		r"""Description of the action.
		"""
		try :
			return self._description
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(appflowaction_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.appflowaction
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
		r""" Use this API to add appflowaction.
		"""
		try :
			if type(resource) is not list :
				addresource = appflowaction()
				addresource.name = resource.name
				addresource.collectors = resource.collectors
				addresource.clientsidemeasurements = resource.clientsidemeasurements
				addresource.pagetracking = resource.pagetracking
				addresource.webinsight = resource.webinsight
				addresource.securityinsight = resource.securityinsight
				addresource.videoanalytics = resource.videoanalytics
				addresource.distributionalgorithm = resource.distributionalgorithm
				addresource.metricslog = resource.metricslog
				addresource.transactionlog = resource.transactionlog
				addresource.comment = resource.comment
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ appflowaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].collectors = resource[i].collectors
						addresources[i].clientsidemeasurements = resource[i].clientsidemeasurements
						addresources[i].pagetracking = resource[i].pagetracking
						addresources[i].webinsight = resource[i].webinsight
						addresources[i].securityinsight = resource[i].securityinsight
						addresources[i].videoanalytics = resource[i].videoanalytics
						addresources[i].distributionalgorithm = resource[i].distributionalgorithm
						addresources[i].metricslog = resource[i].metricslog
						addresources[i].transactionlog = resource[i].transactionlog
						addresources[i].comment = resource[i].comment
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete appflowaction.
		"""
		try :
			if type(resource) is not list :
				deleteresource = appflowaction()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ appflowaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ appflowaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update appflowaction.
		"""
		try :
			if type(resource) is not list :
				updateresource = appflowaction()
				updateresource.name = resource.name
				updateresource.collectors = resource.collectors
				updateresource.clientsidemeasurements = resource.clientsidemeasurements
				updateresource.comment = resource.comment
				updateresource.pagetracking = resource.pagetracking
				updateresource.webinsight = resource.webinsight
				updateresource.securityinsight = resource.securityinsight
				updateresource.videoanalytics = resource.videoanalytics
				updateresource.distributionalgorithm = resource.distributionalgorithm
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ appflowaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].collectors = resource[i].collectors
						updateresources[i].clientsidemeasurements = resource[i].clientsidemeasurements
						updateresources[i].comment = resource[i].comment
						updateresources[i].pagetracking = resource[i].pagetracking
						updateresources[i].webinsight = resource[i].webinsight
						updateresources[i].securityinsight = resource[i].securityinsight
						updateresources[i].videoanalytics = resource[i].videoanalytics
						updateresources[i].distributionalgorithm = resource[i].distributionalgorithm
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of appflowaction resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = appflowaction()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ appflowaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ appflowaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def rename(cls, client, resource, new_name) :
		r""" Use this API to rename a appflowaction resource.
		"""
		try :
			renameresource = appflowaction()
			if type(resource) == cls :
				renameresource.name = resource.name
			else :
				renameresource.name = resource
			return renameresource.rename_resource(client,new_name)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the appflowaction resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = appflowaction()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = appflowaction()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [appflowaction() for _ in range(len(name))]
						obj = [appflowaction() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = appflowaction()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of appflowaction resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = appflowaction()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the appflowaction resources configured on NetScaler.
		"""
		try :
			obj = appflowaction()
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
		r""" Use this API to count filtered the set of appflowaction resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = appflowaction()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Transactionlog:
		ANOMALOUS = "ANOMALOUS"
		NONE = "NONE"
		ALL = "ALL"

	class Webinsight:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Videoanalytics:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Distributionalgorithm:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Securityinsight:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Pagetracking:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Clientsidemeasurements:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class appflowaction_response(base_response) :
	def __init__(self, length=1) :
		self.appflowaction = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.appflowaction = [appflowaction() for _ in range(length)]

