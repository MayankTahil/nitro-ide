'''
Copyright (c) 2008-2015 Citrix Systems, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''


from massrc.com.citrix.mas.nitro.resource.Base import *
from massrc.com.citrix.mas.nitro.service.options import options
from massrc.com.citrix.mas.nitro.exception.nitro_exception import nitro_exception
from massrc.com.citrix.mas.nitro.util.filtervalue import filtervalue
from massrc.com.citrix.mas.nitro.resource.Base.base_resource import base_resource
from massrc.com.citrix.mas.nitro.resource.Base.base_response import base_response


'''
Configuration for App Template Info resource
'''

class app_template_info(base_resource):
	_downloads= ""
	_version= ""
	_name= ""
	_comments=[]
	_rating= ""
	_updated_on= ""
	_desc= ""
	_download_link= ""
	__count=""
	'''
	get the resource id
	'''
	def get_resource_id(self) :
		try:
			if hasattr(self, 'id'):
				return self.id 
			else:
				return None 
		except Exception as e :
			raise e

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "app_template_info"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return None
		except Exception as e :
			raise e

	'''
	Returns the value of object file path argument.
	'''
	@property
	def file_path_value(self) :
		try:
			return None
		except Exception as e :
			raise e

	'''
	Returns the value of object file component name.
	'''
	@property
	def file_component_value(self) :
		try :
			return "app_template_infos"
		except Exception as e :
			raise e



	'''
	get Number of downloads for the template
	'''
	@property
	def downloads(self) :
		try:
			return self._downloads
		except Exception as e :
			raise e
	'''
	set Number of downloads for the template
	'''
	@downloads.setter
	def downloads(self,downloads):
		try :
			if not isinstance(downloads,str):
				raise TypeError("downloads must be set to str value")
			self._downloads = downloads
		except Exception as e :
			raise e


	'''
	get Version Supported
	'''
	@property
	def version(self) :
		try:
			return self._version
		except Exception as e :
			raise e
	'''
	set Version Supported
	'''
	@version.setter
	def version(self,version):
		try :
			if not isinstance(version,str):
				raise TypeError("version must be set to str value")
			self._version = version
		except Exception as e :
			raise e


	'''
	get Template Name
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Template Name
	'''
	@name.setter
	def name(self,name):
		try :
			if not isinstance(name,str):
				raise TypeError("name must be set to str value")
			self._name = name
		except Exception as e :
			raise e


	'''
	get Comments for the template
	'''
	@property
	def comments(self) :
		try:
			return self._comments
		except Exception as e :
			raise e
	'''
	set Comments for the template
	'''
	@comments.setter
	def comments(self,comments) :
		try :
			if not isinstance(comments,list):
				raise TypeError("comments must be set to array of str value")
			for item in comments :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._comments = comments
		except Exception as e :
			raise e


	'''
	get Rating for the template
	'''
	@property
	def rating(self) :
		try:
			return self._rating
		except Exception as e :
			raise e
	'''
	set Rating for the template
	'''
	@rating.setter
	def rating(self,rating):
		try :
			if not isinstance(rating,str):
				raise TypeError("rating must be set to str value")
			self._rating = rating
		except Exception as e :
			raise e


	'''
	get Updated date of the template
	'''
	@property
	def updated_on(self) :
		try:
			return self._updated_on
		except Exception as e :
			raise e
	'''
	set Updated date of the template
	'''
	@updated_on.setter
	def updated_on(self,updated_on):
		try :
			if not isinstance(updated_on,str):
				raise TypeError("updated_on must be set to str value")
			self._updated_on = updated_on
		except Exception as e :
			raise e


	'''
	get Description for the template
	'''
	@property
	def desc(self) :
		try:
			return self._desc
		except Exception as e :
			raise e
	'''
	set Description for the template
	'''
	@desc.setter
	def desc(self,desc):
		try :
			if not isinstance(desc,str):
				raise TypeError("desc must be set to str value")
			self._desc = desc
		except Exception as e :
			raise e


	'''
	get Download link for the template
	'''
	@property
	def download_link(self) :
		try:
			return self._download_link
		except Exception as e :
			raise e
	'''
	set Download link for the template
	'''
	@download_link.setter
	def download_link(self,download_link):
		try :
			if not isinstance(download_link,str):
				raise TypeError("download_link must be set to str value")
			self._download_link = download_link
		except Exception as e :
			raise e

	'''
	Use this operation to get App template information.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				app_template_info_obj=app_template_info()
				response = app_template_info_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of app_template_info resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			app_template_info_obj = app_template_info()
			option_ = options()
			option_._filter=filter_
			return app_template_info_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the app_template_info resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			app_template_info_obj = app_template_info()
			option_ = options()
			option_._count=True
			response = app_template_info_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of app_template_info resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			app_template_info_obj = app_template_info()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = app_template_info_obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['_count']
			return 0;
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(app_template_info_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.app_template_info
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(app_template_info_responses, response, "app_template_info_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.app_template_info_response_array
				i=0
				error = [app_template_info() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.app_template_info_response_array
			i=0
			app_template_info_objs = [app_template_info() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_app_template_info'):
					for props in obj._app_template_info:
						result = service.payload_formatter.string_to_bulk_resource(app_template_info_response,self.__class__.__name__,props)
						app_template_info_objs[i] = result.app_template_info
						i=i+1
			return app_template_info_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(app_template_info,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class app_template_info_response(base_response):
	def __init__(self,length=1) :
		self.app_template_info= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.app_template_info= [ app_template_info() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class app_template_info_responses(base_response):
	def __init__(self,length=1) :
		self.app_template_info_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.app_template_info_response_array = [ app_template_info() for _ in range(length)]
