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

class feoaction(base_resource) :
	""" Configuration for Front end optimization action resource. """
	def __init__(self) :
		self._name = None
		self._pageextendcache = None
		self._cachemaxage = None
		self._imgshrinktoattrib = None
		self._imggiftopng = None
		self._imgtowebp = None
		self._imgtojpegxr = None
		self._imginline = None
		self._cssimginline = None
		self._jpgoptimize = None
		self._imglazyload = None
		self._cssminify = None
		self._cssinline = None
		self._csscombine = None
		self._convertimporttolink = None
		self._jsminify = None
		self._jsinline = None
		self._htmlminify = None
		self._cssmovetohead = None
		self._jsmovetoend = None
		self._domainsharding = None
		self._dnsshards = []
		self._clientsidemeasurements = None
		self._imgadddimensions = None
		self._imgshrinkformobile = None
		self._imgweaken = None
		self._jpgprogressive = None
		self._cssflattenimports = None
		self._jscombine = None
		self._htmlrmdefaultattribs = None
		self._htmlrmattribquotes = None
		self._htmltrimurls = None
		self._hits = None
		self._undefhits = None
		self._builtin = []
		self.___count = 0

	@property
	def name(self) :
		r"""The name of the front end optimization action.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""The name of the front end optimization action.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def pageextendcache(self) :
		r"""Extend the time period during which the browser can use the cached resource.
		"""
		try :
			return self._pageextendcache
		except Exception as e:
			raise e

	@pageextendcache.setter
	def pageextendcache(self, pageextendcache) :
		r"""Extend the time period during which the browser can use the cached resource.
		"""
		try :
			self._pageextendcache = pageextendcache
		except Exception as e:
			raise e

	@property
	def cachemaxage(self) :
		r"""Maxage for cache extension.<br/>Default value: 30<br/>Maximum length =  360.
		"""
		try :
			return self._cachemaxage
		except Exception as e:
			raise e

	@cachemaxage.setter
	def cachemaxage(self, cachemaxage) :
		r"""Maxage for cache extension.<br/>Default value: 30<br/>Maximum length =  360
		"""
		try :
			self._cachemaxage = cachemaxage
		except Exception as e:
			raise e

	@property
	def imgshrinktoattrib(self) :
		r"""Shrink image dimensions as per the height and width attributes specified in the <img> tag.
		"""
		try :
			return self._imgshrinktoattrib
		except Exception as e:
			raise e

	@imgshrinktoattrib.setter
	def imgshrinktoattrib(self, imgshrinktoattrib) :
		r"""Shrink image dimensions as per the height and width attributes specified in the <img> tag.
		"""
		try :
			self._imgshrinktoattrib = imgshrinktoattrib
		except Exception as e:
			raise e

	@property
	def imggiftopng(self) :
		r"""Convert GIF image formats to PNG formats.
		"""
		try :
			return self._imggiftopng
		except Exception as e:
			raise e

	@imggiftopng.setter
	def imggiftopng(self, imggiftopng) :
		r"""Convert GIF image formats to PNG formats.
		"""
		try :
			self._imggiftopng = imggiftopng
		except Exception as e:
			raise e

	@property
	def imgtowebp(self) :
		r"""Convert JPEG, GIF, PNG image formats to WEBP format.
		"""
		try :
			return self._imgtowebp
		except Exception as e:
			raise e

	@imgtowebp.setter
	def imgtowebp(self, imgtowebp) :
		r"""Convert JPEG, GIF, PNG image formats to WEBP format.
		"""
		try :
			self._imgtowebp = imgtowebp
		except Exception as e:
			raise e

	@property
	def imgtojpegxr(self) :
		r"""Convert JPEG, GIF, PNG image formats to JXR format.
		"""
		try :
			return self._imgtojpegxr
		except Exception as e:
			raise e

	@imgtojpegxr.setter
	def imgtojpegxr(self, imgtojpegxr) :
		r"""Convert JPEG, GIF, PNG image formats to JXR format.
		"""
		try :
			self._imgtojpegxr = imgtojpegxr
		except Exception as e:
			raise e

	@property
	def imginline(self) :
		r"""Inline images whose size is less than 2KB.
		"""
		try :
			return self._imginline
		except Exception as e:
			raise e

	@imginline.setter
	def imginline(self, imginline) :
		r"""Inline images whose size is less than 2KB.
		"""
		try :
			self._imginline = imginline
		except Exception as e:
			raise e

	@property
	def cssimginline(self) :
		r"""Inline small images (less than 2KB) referred within CSS files as background-URLs.
		"""
		try :
			return self._cssimginline
		except Exception as e:
			raise e

	@cssimginline.setter
	def cssimginline(self, cssimginline) :
		r"""Inline small images (less than 2KB) referred within CSS files as background-URLs.
		"""
		try :
			self._cssimginline = cssimginline
		except Exception as e:
			raise e

	@property
	def jpgoptimize(self) :
		r"""Remove non-image data such as comments from JPEG images.
		"""
		try :
			return self._jpgoptimize
		except Exception as e:
			raise e

	@jpgoptimize.setter
	def jpgoptimize(self, jpgoptimize) :
		r"""Remove non-image data such as comments from JPEG images.
		"""
		try :
			self._jpgoptimize = jpgoptimize
		except Exception as e:
			raise e

	@property
	def imglazyload(self) :
		r"""Download images, only when the user scrolls the page to view them.
		"""
		try :
			return self._imglazyload
		except Exception as e:
			raise e

	@imglazyload.setter
	def imglazyload(self, imglazyload) :
		r"""Download images, only when the user scrolls the page to view them.
		"""
		try :
			self._imglazyload = imglazyload
		except Exception as e:
			raise e

	@property
	def cssminify(self) :
		r"""Remove comments and whitespaces from CSSs.
		"""
		try :
			return self._cssminify
		except Exception as e:
			raise e

	@cssminify.setter
	def cssminify(self, cssminify) :
		r"""Remove comments and whitespaces from CSSs.
		"""
		try :
			self._cssminify = cssminify
		except Exception as e:
			raise e

	@property
	def cssinline(self) :
		r"""Inline CSS files, whose size is less than 2KB, within the main page.
		"""
		try :
			return self._cssinline
		except Exception as e:
			raise e

	@cssinline.setter
	def cssinline(self, cssinline) :
		r"""Inline CSS files, whose size is less than 2KB, within the main page.
		"""
		try :
			self._cssinline = cssinline
		except Exception as e:
			raise e

	@property
	def csscombine(self) :
		r"""Combine one or more CSS files into one file.
		"""
		try :
			return self._csscombine
		except Exception as e:
			raise e

	@csscombine.setter
	def csscombine(self, csscombine) :
		r"""Combine one or more CSS files into one file.
		"""
		try :
			self._csscombine = csscombine
		except Exception as e:
			raise e

	@property
	def convertimporttolink(self) :
		r"""Convert CSS import statements to HTML link tags.
		"""
		try :
			return self._convertimporttolink
		except Exception as e:
			raise e

	@convertimporttolink.setter
	def convertimporttolink(self, convertimporttolink) :
		r"""Convert CSS import statements to HTML link tags.
		"""
		try :
			self._convertimporttolink = convertimporttolink
		except Exception as e:
			raise e

	@property
	def jsminify(self) :
		r"""Remove comments and whitespaces from JavaScript.
		"""
		try :
			return self._jsminify
		except Exception as e:
			raise e

	@jsminify.setter
	def jsminify(self, jsminify) :
		r"""Remove comments and whitespaces from JavaScript.
		"""
		try :
			self._jsminify = jsminify
		except Exception as e:
			raise e

	@property
	def jsinline(self) :
		r"""Convert linked JavaScript files (less than 2KB) to inline JavaScript files.
		"""
		try :
			return self._jsinline
		except Exception as e:
			raise e

	@jsinline.setter
	def jsinline(self, jsinline) :
		r"""Convert linked JavaScript files (less than 2KB) to inline JavaScript files.
		"""
		try :
			self._jsinline = jsinline
		except Exception as e:
			raise e

	@property
	def htmlminify(self) :
		r"""Remove comments and whitespaces from an HTML page.
		"""
		try :
			return self._htmlminify
		except Exception as e:
			raise e

	@htmlminify.setter
	def htmlminify(self, htmlminify) :
		r"""Remove comments and whitespaces from an HTML page.
		"""
		try :
			self._htmlminify = htmlminify
		except Exception as e:
			raise e

	@property
	def cssmovetohead(self) :
		r"""Move any CSS file present within the body tag of an HTML page to the head tag.
		"""
		try :
			return self._cssmovetohead
		except Exception as e:
			raise e

	@cssmovetohead.setter
	def cssmovetohead(self, cssmovetohead) :
		r"""Move any CSS file present within the body tag of an HTML page to the head tag.
		"""
		try :
			self._cssmovetohead = cssmovetohead
		except Exception as e:
			raise e

	@property
	def jsmovetoend(self) :
		r"""Move any JavaScript present in the body tag to the end of the body tag.
		"""
		try :
			return self._jsmovetoend
		except Exception as e:
			raise e

	@jsmovetoend.setter
	def jsmovetoend(self, jsmovetoend) :
		r"""Move any JavaScript present in the body tag to the end of the body tag.
		"""
		try :
			self._jsmovetoend = jsmovetoend
		except Exception as e:
			raise e

	@property
	def domainsharding(self) :
		r"""Domain name of the server.
		"""
		try :
			return self._domainsharding
		except Exception as e:
			raise e

	@domainsharding.setter
	def domainsharding(self, domainsharding) :
		r"""Domain name of the server.
		"""
		try :
			self._domainsharding = domainsharding
		except Exception as e:
			raise e

	@property
	def dnsshards(self) :
		r"""Set of domain names that replaces the parent domain.
		"""
		try :
			return self._dnsshards
		except Exception as e:
			raise e

	@dnsshards.setter
	def dnsshards(self, dnsshards) :
		r"""Set of domain names that replaces the parent domain.
		"""
		try :
			self._dnsshards = dnsshards
		except Exception as e:
			raise e

	@property
	def clientsidemeasurements(self) :
		r"""Send AppFlow records about the web pages optimized by this action. The records provide FEO statistics, such as the number of HTTP requests that have been reduced for this page. You must enable the Appflow feature before enabling this parameter.
		"""
		try :
			return self._clientsidemeasurements
		except Exception as e:
			raise e

	@clientsidemeasurements.setter
	def clientsidemeasurements(self, clientsidemeasurements) :
		r"""Send AppFlow records about the web pages optimized by this action. The records provide FEO statistics, such as the number of HTTP requests that have been reduced for this page. You must enable the Appflow feature before enabling this parameter.
		"""
		try :
			self._clientsidemeasurements = clientsidemeasurements
		except Exception as e:
			raise e

	@property
	def imgadddimensions(self) :
		r"""Add dimension attributes to images, if not specified within the <img> tag.
		"""
		try :
			return self._imgadddimensions
		except Exception as e:
			raise e

	@property
	def imgshrinkformobile(self) :
		r"""Serve smaller images for mobile users.
		"""
		try :
			return self._imgshrinkformobile
		except Exception as e:
			raise e

	@property
	def imgweaken(self) :
		r"""Reduce the image quality.
		"""
		try :
			return self._imgweaken
		except Exception as e:
			raise e

	@property
	def jpgprogressive(self) :
		r"""Convert JPEG image formats to progressive formats.
		"""
		try :
			return self._jpgprogressive
		except Exception as e:
			raise e

	@property
	def cssflattenimports(self) :
		r"""Replace CSS import statements with the file content.
		"""
		try :
			return self._cssflattenimports
		except Exception as e:
			raise e

	@property
	def jscombine(self) :
		r"""Combine one or more JavaScript files into one file.
		"""
		try :
			return self._jscombine
		except Exception as e:
			raise e

	@property
	def htmlrmdefaultattribs(self) :
		r"""Remove default redundant attributes from an HTML file.
		"""
		try :
			return self._htmlrmdefaultattribs
		except Exception as e:
			raise e

	@property
	def htmlrmattribquotes(self) :
		r"""Remove unnecessary quotes present within the HTML attributes.
		"""
		try :
			return self._htmlrmattribquotes
		except Exception as e:
			raise e

	@property
	def htmltrimurls(self) :
		r"""Trim URLs.
		"""
		try :
			return self._htmltrimurls
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
	def undefhits(self) :
		r"""Total number of undefined policy hits.
		"""
		try :
			return self._undefhits
		except Exception as e:
			raise e

	@property
	def builtin(self) :
		r"""Flag to determine if front end optimization action is built-in or not.<br/>Possible values = MODIFIABLE, DELETABLE, IMMUTABLE, PARTITION_ALL.
		"""
		try :
			return self._builtin
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(feoaction_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.feoaction
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
		r""" Use this API to add feoaction.
		"""
		try :
			if type(resource) is not list :
				addresource = feoaction()
				addresource.name = resource.name
				addresource.pageextendcache = resource.pageextendcache
				addresource.cachemaxage = resource.cachemaxage
				addresource.imgshrinktoattrib = resource.imgshrinktoattrib
				addresource.imggiftopng = resource.imggiftopng
				addresource.imgtowebp = resource.imgtowebp
				addresource.imgtojpegxr = resource.imgtojpegxr
				addresource.imginline = resource.imginline
				addresource.cssimginline = resource.cssimginline
				addresource.jpgoptimize = resource.jpgoptimize
				addresource.imglazyload = resource.imglazyload
				addresource.cssminify = resource.cssminify
				addresource.cssinline = resource.cssinline
				addresource.csscombine = resource.csscombine
				addresource.convertimporttolink = resource.convertimporttolink
				addresource.jsminify = resource.jsminify
				addresource.jsinline = resource.jsinline
				addresource.htmlminify = resource.htmlminify
				addresource.cssmovetohead = resource.cssmovetohead
				addresource.jsmovetoend = resource.jsmovetoend
				addresource.domainsharding = resource.domainsharding
				addresource.dnsshards = resource.dnsshards
				addresource.clientsidemeasurements = resource.clientsidemeasurements
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ feoaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].pageextendcache = resource[i].pageextendcache
						addresources[i].cachemaxage = resource[i].cachemaxage
						addresources[i].imgshrinktoattrib = resource[i].imgshrinktoattrib
						addresources[i].imggiftopng = resource[i].imggiftopng
						addresources[i].imgtowebp = resource[i].imgtowebp
						addresources[i].imgtojpegxr = resource[i].imgtojpegxr
						addresources[i].imginline = resource[i].imginline
						addresources[i].cssimginline = resource[i].cssimginline
						addresources[i].jpgoptimize = resource[i].jpgoptimize
						addresources[i].imglazyload = resource[i].imglazyload
						addresources[i].cssminify = resource[i].cssminify
						addresources[i].cssinline = resource[i].cssinline
						addresources[i].csscombine = resource[i].csscombine
						addresources[i].convertimporttolink = resource[i].convertimporttolink
						addresources[i].jsminify = resource[i].jsminify
						addresources[i].jsinline = resource[i].jsinline
						addresources[i].htmlminify = resource[i].htmlminify
						addresources[i].cssmovetohead = resource[i].cssmovetohead
						addresources[i].jsmovetoend = resource[i].jsmovetoend
						addresources[i].domainsharding = resource[i].domainsharding
						addresources[i].dnsshards = resource[i].dnsshards
						addresources[i].clientsidemeasurements = resource[i].clientsidemeasurements
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update feoaction.
		"""
		try :
			if type(resource) is not list :
				updateresource = feoaction()
				updateresource.name = resource.name
				updateresource.pageextendcache = resource.pageextendcache
				updateresource.cachemaxage = resource.cachemaxage
				updateresource.imgshrinktoattrib = resource.imgshrinktoattrib
				updateresource.imggiftopng = resource.imggiftopng
				updateresource.imgtowebp = resource.imgtowebp
				updateresource.imgtojpegxr = resource.imgtojpegxr
				updateresource.imginline = resource.imginline
				updateresource.cssimginline = resource.cssimginline
				updateresource.jpgoptimize = resource.jpgoptimize
				updateresource.imglazyload = resource.imglazyload
				updateresource.cssminify = resource.cssminify
				updateresource.cssinline = resource.cssinline
				updateresource.csscombine = resource.csscombine
				updateresource.convertimporttolink = resource.convertimporttolink
				updateresource.jsminify = resource.jsminify
				updateresource.jsinline = resource.jsinline
				updateresource.htmlminify = resource.htmlminify
				updateresource.cssmovetohead = resource.cssmovetohead
				updateresource.jsmovetoend = resource.jsmovetoend
				updateresource.domainsharding = resource.domainsharding
				updateresource.dnsshards = resource.dnsshards
				updateresource.clientsidemeasurements = resource.clientsidemeasurements
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ feoaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].pageextendcache = resource[i].pageextendcache
						updateresources[i].cachemaxage = resource[i].cachemaxage
						updateresources[i].imgshrinktoattrib = resource[i].imgshrinktoattrib
						updateresources[i].imggiftopng = resource[i].imggiftopng
						updateresources[i].imgtowebp = resource[i].imgtowebp
						updateresources[i].imgtojpegxr = resource[i].imgtojpegxr
						updateresources[i].imginline = resource[i].imginline
						updateresources[i].cssimginline = resource[i].cssimginline
						updateresources[i].jpgoptimize = resource[i].jpgoptimize
						updateresources[i].imglazyload = resource[i].imglazyload
						updateresources[i].cssminify = resource[i].cssminify
						updateresources[i].cssinline = resource[i].cssinline
						updateresources[i].csscombine = resource[i].csscombine
						updateresources[i].convertimporttolink = resource[i].convertimporttolink
						updateresources[i].jsminify = resource[i].jsminify
						updateresources[i].jsinline = resource[i].jsinline
						updateresources[i].htmlminify = resource[i].htmlminify
						updateresources[i].cssmovetohead = resource[i].cssmovetohead
						updateresources[i].jsmovetoend = resource[i].jsmovetoend
						updateresources[i].domainsharding = resource[i].domainsharding
						updateresources[i].dnsshards = resource[i].dnsshards
						updateresources[i].clientsidemeasurements = resource[i].clientsidemeasurements
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of feoaction resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = feoaction()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ feoaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ feoaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete feoaction.
		"""
		try :
			if type(resource) is not list :
				deleteresource = feoaction()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ feoaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ feoaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the feoaction resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = feoaction()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = feoaction()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [feoaction() for _ in range(len(name))]
						obj = [feoaction() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = feoaction()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of feoaction resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = feoaction()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the feoaction resources configured on NetScaler.
		"""
		try :
			obj = feoaction()
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
		r""" Use this API to count filtered the set of feoaction resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = feoaction()
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

class feoaction_response(base_response) :
	def __init__(self, length=1) :
		self.feoaction = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.feoaction = [feoaction() for _ in range(length)]

