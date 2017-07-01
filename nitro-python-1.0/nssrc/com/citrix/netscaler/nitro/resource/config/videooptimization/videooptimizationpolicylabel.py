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

class videooptimizationpolicylabel(base_resource) :
	""" Configuration for video optimization policy label resource. """
	def __init__(self) :
		self._labelname = None
		self._policylabeltype = None
		self._comment = None
		self._newname = None
		self._numpol = None
		self._hits = None
		self._priority = None
		self._gotopriorityexpression = None
		self._labeltype = None
		self._invoke_labelname = None
		self.___count = 0

	@property
	def labelname(self) :
		r"""Name for the Video optimization policy label. Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (
		.) hash (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed after the videooptimization policy label is added.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my videooptimization policy label" or my videooptimization policy label').
		"""
		try :
			return self._labelname
		except Exception as e:
			raise e

	@labelname.setter
	def labelname(self, labelname) :
		r"""Name for the Video optimization policy label. Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (
		.) hash (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed after the videooptimization policy label is added.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my videooptimization policy label" or my videooptimization policy label').
		"""
		try :
			self._labelname = labelname
		except Exception as e:
			raise e

	@property
	def policylabeltype(self) :
		r"""Type of responses sent by the policies bound to this policy label. Types are:
		* HTTP - HTTP responses.
		* OTHERTCP - NON-HTTP TCP responses.<br/>Default value: NS_PLTMAP_RSP_REQ<br/>Possible values = videoopt_req, videoopt_res.
		"""
		try :
			return self._policylabeltype
		except Exception as e:
			raise e

	@policylabeltype.setter
	def policylabeltype(self, policylabeltype) :
		r"""Type of responses sent by the policies bound to this policy label. Types are:
		* HTTP - HTTP responses.
		* OTHERTCP - NON-HTTP TCP responses.<br/>Default value: NS_PLTMAP_RSP_REQ<br/>Possible values = videoopt_req, videoopt_res
		"""
		try :
			self._policylabeltype = policylabeltype
		except Exception as e:
			raise e

	@property
	def comment(self) :
		r"""Any comments to preserve information about this videooptimization policy label.
		"""
		try :
			return self._comment
		except Exception as e:
			raise e

	@comment.setter
	def comment(self, comment) :
		r"""Any comments to preserve information about this videooptimization policy label.
		"""
		try :
			self._comment = comment
		except Exception as e:
			raise e

	@property
	def newname(self) :
		r"""New name for the videooptimization policy label. Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (
		-), period (.) hash (#), space ( ), at (@), equals (=), colon (:), and underscore characters.<br/>Minimum length =  1.
		"""
		try :
			return self._newname
		except Exception as e:
			raise e

	@newname.setter
	def newname(self, newname) :
		r"""New name for the videooptimization policy label. Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (
		-), period (.) hash (#), space ( ), at (@), equals (=), colon (:), and underscore characters.<br/>Minimum length =  1
		"""
		try :
			self._newname = newname
		except Exception as e:
			raise e

	@property
	def numpol(self) :
		r"""number of polices bound to label.
		"""
		try :
			return self._numpol
		except Exception as e:
			raise e

	@property
	def hits(self) :
		r"""Number of times policy label was invoked.
		"""
		try :
			return self._hits
		except Exception as e:
			raise e

	@property
	def priority(self) :
		r"""Specifies the priority of the policy.
		"""
		try :
			return self._priority
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

	@property
	def labeltype(self) :
		r"""Type of policy label to invoke. Available settings function as follows:
		* vserver - Invoke an unnamed policy label associated with a virtual server.
		* policylabel - Invoke a user-defined policy label.<br/>Possible values = vserver, policylabel.
		"""
		try :
			return self._labeltype
		except Exception as e:
			raise e

	@property
	def invoke_labelname(self) :
		r"""* If labelType is policylabel, name of the policy label to invoke.
		* If labelType is reqvserver or resvserver, name of the virtual server.
		"""
		try :
			return self._invoke_labelname
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(videooptimizationpolicylabel_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.videooptimizationpolicylabel
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
	def add(cls, client, resource) :
		r""" Use this API to add videooptimizationpolicylabel.
		"""
		try :
			if type(resource) is not list :
				addresource = videooptimizationpolicylabel()
				addresource.labelname = resource.labelname
				addresource.policylabeltype = resource.policylabeltype
				addresource.comment = resource.comment
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ videooptimizationpolicylabel() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].labelname = resource[i].labelname
						addresources[i].policylabeltype = resource[i].policylabeltype
						addresources[i].comment = resource[i].comment
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete videooptimizationpolicylabel.
		"""
		try :
			if type(resource) is not list :
				deleteresource = videooptimizationpolicylabel()
				if type(resource) !=  type(deleteresource):
					deleteresource.labelname = resource
				else :
					deleteresource.labelname = resource.labelname
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ videooptimizationpolicylabel() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].labelname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ videooptimizationpolicylabel() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].labelname = resource[i].labelname
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def rename(cls, client, resource, new_labelname) :
		r""" Use this API to rename a videooptimizationpolicylabel resource.
		"""
		try :
			renameresource = videooptimizationpolicylabel()
			if type(resource) == cls :
				renameresource.labelname = resource.labelname
			else :
				renameresource.labelname = resource
			return renameresource.rename_resource(client,new_labelname)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the videooptimizationpolicylabel resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = videooptimizationpolicylabel()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = videooptimizationpolicylabel()
					obj.labelname = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [videooptimizationpolicylabel() for _ in range(len(name))]
						obj = [videooptimizationpolicylabel() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = videooptimizationpolicylabel()
							obj[i].labelname = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of videooptimizationpolicylabel resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = videooptimizationpolicylabel()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the videooptimizationpolicylabel resources configured on NetScaler.
		"""
		try :
			obj = videooptimizationpolicylabel()
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
		r""" Use this API to count filtered the set of videooptimizationpolicylabel resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = videooptimizationpolicylabel()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Policylabeltype:
		videoopt_req = "videoopt_req"
		videoopt_res = "videoopt_res"

	class Labeltype:
		vserver = "vserver"
		policylabel = "policylabel"

class videooptimizationpolicylabel_response(base_response) :
	def __init__(self, length=1) :
		self.videooptimizationpolicylabel = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.videooptimizationpolicylabel = [videooptimizationpolicylabel() for _ in range(length)]

