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

class authenticationepaaction(base_resource) :
	""" Configuration for epa action resource. """
	def __init__(self) :
		self._name = None
		self._csecexpr = None
		self._killprocess = None
		self._deletefiles = None
		self._defaultepagroup = None
		self._quarantinegroup = None
		self.___count = 0

	@property
	def name(self) :
		r"""Name for the epa action. Must begin with a
		letter, number, or the underscore character (_), and must consist
		only of letters, numbers, and the hyphen (-), period (.) pound
		(#), space ( ), at (@), equals (=), colon (:), and underscore
		characters. Cannot be changed after epa action is created.The following requirement applies only to the NetScaler CLI:If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my aaa action" or 'my aaa action').<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name for the epa action. Must begin with a
		letter, number, or the underscore character (_), and must consist
		only of letters, numbers, and the hyphen (-), period (.) pound
		(#), space ( ), at (@), equals (=), colon (:), and underscore
		characters. Cannot be changed after epa action is created.The following requirement applies only to the NetScaler CLI:If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my aaa action" or 'my aaa action').<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def csecexpr(self) :
		r"""it holds the ClientSecurityExpression to be sent to the client.
		"""
		try :
			return self._csecexpr
		except Exception as e:
			raise e

	@csecexpr.setter
	def csecexpr(self, csecexpr) :
		r"""it holds the ClientSecurityExpression to be sent to the client.
		"""
		try :
			self._csecexpr = csecexpr
		except Exception as e:
			raise e

	@property
	def killprocess(self) :
		r"""String specifying the name of a process to be terminated by the endpoint analysis (EPA) tool. Multiple processes to be delimited by comma.
		"""
		try :
			return self._killprocess
		except Exception as e:
			raise e

	@killprocess.setter
	def killprocess(self, killprocess) :
		r"""String specifying the name of a process to be terminated by the endpoint analysis (EPA) tool. Multiple processes to be delimited by comma.
		"""
		try :
			self._killprocess = killprocess
		except Exception as e:
			raise e

	@property
	def deletefiles(self) :
		r"""String specifying the path(s) and name(s) of the files to be deleted by the endpoint analysis (EPA) tool. Multiple files to be delimited by comma.
		"""
		try :
			return self._deletefiles
		except Exception as e:
			raise e

	@deletefiles.setter
	def deletefiles(self, deletefiles) :
		r"""String specifying the path(s) and name(s) of the files to be deleted by the endpoint analysis (EPA) tool. Multiple files to be delimited by comma.
		"""
		try :
			self._deletefiles = deletefiles
		except Exception as e:
			raise e

	@property
	def defaultepagroup(self) :
		r"""This is the default group that is chosen when the EPA check succeeds.<br/>Maximum length =  64.
		"""
		try :
			return self._defaultepagroup
		except Exception as e:
			raise e

	@defaultepagroup.setter
	def defaultepagroup(self, defaultepagroup) :
		r"""This is the default group that is chosen when the EPA check succeeds.<br/>Maximum length =  64
		"""
		try :
			self._defaultepagroup = defaultepagroup
		except Exception as e:
			raise e

	@property
	def quarantinegroup(self) :
		r"""This is the quarantine group that is chosen when the EPA check fails
		if configured.<br/>Maximum length =  64.
		"""
		try :
			return self._quarantinegroup
		except Exception as e:
			raise e

	@quarantinegroup.setter
	def quarantinegroup(self, quarantinegroup) :
		r"""This is the quarantine group that is chosen when the EPA check fails
		if configured.<br/>Maximum length =  64
		"""
		try :
			self._quarantinegroup = quarantinegroup
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(authenticationepaaction_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.authenticationepaaction
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
		r""" Use this API to add authenticationepaaction.
		"""
		try :
			if type(resource) is not list :
				addresource = authenticationepaaction()
				addresource.name = resource.name
				addresource.csecexpr = resource.csecexpr
				addresource.killprocess = resource.killprocess
				addresource.deletefiles = resource.deletefiles
				addresource.defaultepagroup = resource.defaultepagroup
				addresource.quarantinegroup = resource.quarantinegroup
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ authenticationepaaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].csecexpr = resource[i].csecexpr
						addresources[i].killprocess = resource[i].killprocess
						addresources[i].deletefiles = resource[i].deletefiles
						addresources[i].defaultepagroup = resource[i].defaultepagroup
						addresources[i].quarantinegroup = resource[i].quarantinegroup
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete authenticationepaaction.
		"""
		try :
			if type(resource) is not list :
				deleteresource = authenticationepaaction()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ authenticationepaaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ authenticationepaaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update authenticationepaaction.
		"""
		try :
			if type(resource) is not list :
				updateresource = authenticationepaaction()
				updateresource.name = resource.name
				updateresource.csecexpr = resource.csecexpr
				updateresource.killprocess = resource.killprocess
				updateresource.deletefiles = resource.deletefiles
				updateresource.defaultepagroup = resource.defaultepagroup
				updateresource.quarantinegroup = resource.quarantinegroup
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ authenticationepaaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].csecexpr = resource[i].csecexpr
						updateresources[i].killprocess = resource[i].killprocess
						updateresources[i].deletefiles = resource[i].deletefiles
						updateresources[i].defaultepagroup = resource[i].defaultepagroup
						updateresources[i].quarantinegroup = resource[i].quarantinegroup
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of authenticationepaaction resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = authenticationepaaction()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ authenticationepaaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ authenticationepaaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the authenticationepaaction resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = authenticationepaaction()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = authenticationepaaction()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [authenticationepaaction() for _ in range(len(name))]
						obj = [authenticationepaaction() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = authenticationepaaction()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of authenticationepaaction resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = authenticationepaaction()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the authenticationepaaction resources configured on NetScaler.
		"""
		try :
			obj = authenticationepaaction()
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
		r""" Use this API to count filtered the set of authenticationepaaction resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = authenticationepaaction()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


class authenticationepaaction_response(base_response) :
	def __init__(self, length=1) :
		self.authenticationepaaction = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.authenticationepaaction = [authenticationepaaction() for _ in range(length)]

