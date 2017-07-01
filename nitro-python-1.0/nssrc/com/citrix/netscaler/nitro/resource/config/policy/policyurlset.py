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

class policyurlset(base_resource) :
	""" Configuration for URL set resource. """
	def __init__(self) :
		self._name = None
		self._comment = None
		self._overwrite = None
		self._delimiter = None
		self._rowseparator = None
		self._url = None
		self._interval = None
		self._privateset = None
		self._canaryurl = None
		self._patterncount = None
		self.___count = 0

	@property
	def name(self) :
		r"""Unique name of the url set. Not case sensitive. Must begin with an ASCII letter or underscore (_) character and must contain only alphanumeric and underscore characters. Must not be the name of an existing named expression, pattern set, dataset, string map, or HTTP callout.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Unique name of the url set. Not case sensitive. Must begin with an ASCII letter or underscore (_) character and must contain only alphanumeric and underscore characters. Must not be the name of an existing named expression, pattern set, dataset, string map, or HTTP callout.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def comment(self) :
		r"""Any comments to preserve information about this url set.
		"""
		try :
			return self._comment
		except Exception as e:
			raise e

	@comment.setter
	def comment(self, comment) :
		r"""Any comments to preserve information about this url set.
		"""
		try :
			self._comment = comment
		except Exception as e:
			raise e

	@property
	def overwrite(self) :
		r"""Overwrites the existing file.<br/>Default value: 0.
		"""
		try :
			return self._overwrite
		except Exception as e:
			raise e

	@overwrite.setter
	def overwrite(self, overwrite) :
		r"""Overwrites the existing file.<br/>Default value: 0
		"""
		try :
			self._overwrite = overwrite
		except Exception as e:
			raise e

	@property
	def delimiter(self) :
		r"""CSV file record delimiter.<br/>Default value: 44.
		"""
		try :
			return self._delimiter
		except Exception as e:
			raise e

	@delimiter.setter
	def delimiter(self, delimiter) :
		r"""CSV file record delimiter.<br/>Default value: 44
		"""
		try :
			self._delimiter = delimiter
		except Exception as e:
			raise e

	@property
	def rowseparator(self) :
		r"""CSV file row separator.<br/>Default value: 10.
		"""
		try :
			return self._rowseparator
		except Exception as e:
			raise e

	@rowseparator.setter
	def rowseparator(self, rowseparator) :
		r"""CSV file row separator.<br/>Default value: 10
		"""
		try :
			self._rowseparator = rowseparator
		except Exception as e:
			raise e

	@property
	def url(self) :
		r"""URL (protocol, host, path and file name) from where the CSV (comma separated file) file will be imported or exported. Each record/line will one entry within the urlset. The first field contains the URL pattern, subsequent fields contains the metadata, if available. HTTP, HTTPS and FTP protocols are supported. NOTE: The operation fails if the destination HTTPS server requires client certificate authentication for access.<br/>Minimum length =  1<br/>Maximum length =  2047.
		"""
		try :
			return self._url
		except Exception as e:
			raise e

	@url.setter
	def url(self, url) :
		r"""URL (protocol, host, path and file name) from where the CSV (comma separated file) file will be imported or exported. Each record/line will one entry within the urlset. The first field contains the URL pattern, subsequent fields contains the metadata, if available. HTTP, HTTPS and FTP protocols are supported. NOTE: The operation fails if the destination HTTPS server requires client certificate authentication for access.<br/>Minimum length =  1<br/>Maximum length =  2047
		"""
		try :
			self._url = url
		except Exception as e:
			raise e

	@property
	def interval(self) :
		r"""The interval, in seconds, rounded down to the nearest 15 minutes, at which the update of urlset occurs.<br/>Default value: 0<br/>Maximum length =  2592000.
		"""
		try :
			return self._interval
		except Exception as e:
			raise e

	@interval.setter
	def interval(self, interval) :
		r"""The interval, in seconds, rounded down to the nearest 15 minutes, at which the update of urlset occurs.<br/>Default value: 0<br/>Maximum length =  2592000
		"""
		try :
			self._interval = interval
		except Exception as e:
			raise e

	@property
	def privateset(self) :
		r"""Prevent this urlset from being exported.<br/>Default value: 0.
		"""
		try :
			return self._privateset
		except Exception as e:
			raise e

	@privateset.setter
	def privateset(self, privateset) :
		r"""Prevent this urlset from being exported.<br/>Default value: 0
		"""
		try :
			self._privateset = privateset
		except Exception as e:
			raise e

	@property
	def canaryurl(self) :
		r"""Add this URL to this urlset. Used for testing when contents of urlset is kept confidential.<br/>Minimum length =  1<br/>Maximum length =  2047.
		"""
		try :
			return self._canaryurl
		except Exception as e:
			raise e

	@canaryurl.setter
	def canaryurl(self, canaryurl) :
		r"""Add this URL to this urlset. Used for testing when contents of urlset is kept confidential.<br/>Minimum length =  1<br/>Maximum length =  2047
		"""
		try :
			self._canaryurl = canaryurl
		except Exception as e:
			raise e

	@property
	def patterncount(self) :
		r"""Number of patterns in this urlset.<br/>Default value: 0.
		"""
		try :
			return self._patterncount
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(policyurlset_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.policyurlset
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
		r""" Use this API to add policyurlset.
		"""
		try :
			if type(resource) is not list :
				addresource = policyurlset()
				addresource.name = resource.name
				addresource.comment = resource.comment
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ policyurlset() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].comment = resource[i].comment
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete policyurlset.
		"""
		try :
			if type(resource) is not list :
				deleteresource = policyurlset()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ policyurlset() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ policyurlset() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def Import(cls, client, resource) :
		r""" Use this API to Import policyurlset.
		"""
		try :
			if type(resource) is not list :
				Importresource = policyurlset()
				Importresource.name = resource.name
				Importresource.overwrite = resource.overwrite
				Importresource.delimiter = resource.delimiter
				Importresource.rowseparator = resource.rowseparator
				Importresource.url = resource.url
				Importresource.interval = resource.interval
				Importresource.privateset = resource.privateset
				Importresource.canaryurl = resource.canaryurl
				return Importresource.perform_operation(client,"Import")
			else :
				if (resource and len(resource) > 0) :
					Importresources = [ policyurlset() for _ in range(len(resource))]
					for i in range(len(resource)) :
						Importresources[i].name = resource[i].name
						Importresources[i].overwrite = resource[i].overwrite
						Importresources[i].delimiter = resource[i].delimiter
						Importresources[i].rowseparator = resource[i].rowseparator
						Importresources[i].url = resource[i].url
						Importresources[i].interval = resource[i].interval
						Importresources[i].privateset = resource[i].privateset
						Importresources[i].canaryurl = resource[i].canaryurl
				result = cls.perform_operation_bulk_request(client, Importresources,"Import")
			return result
		except Exception as e :
			raise e

	@classmethod
	def change(cls, client, resource) :
		r""" Use this API to change policyurlset.
		"""
		try :
			if type(resource) is not list :
				changeresource = policyurlset()
				changeresource.name = resource.name
				return changeresource.perform_operation(client,"update")
			else :
				if (resource and len(resource) > 0) :
					changeresources = [ policyurlset() for _ in range(len(resource))]
					for i in range(len(resource)) :
						changeresources[i].name = resource[i].name
				result = cls.perform_operation_bulk_request(client, changeresources,"update")
			return result
		except Exception as e :
			raise e

	@classmethod
	def export(cls, client, resource) :
		r""" Use this API to export policyurlset.
		"""
		try :
			if type(resource) is not list :
				exportresource = policyurlset()
				exportresource.name = resource.name
				exportresource.url = resource.url
				return exportresource.perform_operation(client,"export")
			else :
				if (resource and len(resource) > 0) :
					exportresources = [ policyurlset() for _ in range(len(resource))]
					for i in range(len(resource)) :
						exportresources[i].name = resource[i].name
						exportresources[i].url = resource[i].url
				result = cls.perform_operation_bulk_request(client, exportresources,"export")
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the policyurlset resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = policyurlset()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = policyurlset()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [policyurlset() for _ in range(len(name))]
						obj = [policyurlset() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = policyurlset()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of policyurlset resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = policyurlset()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the policyurlset resources configured on NetScaler.
		"""
		try :
			obj = policyurlset()
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
		r""" Use this API to count filtered the set of policyurlset resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = policyurlset()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


class policyurlset_response(base_response) :
	def __init__(self, length=1) :
		self.policyurlset = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.policyurlset = [policyurlset() for _ in range(length)]

