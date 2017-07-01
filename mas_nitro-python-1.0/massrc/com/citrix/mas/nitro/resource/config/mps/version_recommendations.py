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
Configuration for Recommendation For Version Matrix resource
'''

class version_recommendations(base_resource):
	_xen_hotfix_recommendation= ""
	_xen_hotfix= ""
	_xen_recommendation= ""
	_suggestion= ""
	_xen_version= ""
	_br_version= ""
	_ns_recommendation= ""
	_svm_version= ""
	_ns_version= ""
	_xen_supplemental_pack_recommendation= ""
	_xen_supplemental_pack_version= ""
	_br_recommendation= ""
	_svm_recommendation= ""
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
			return "version_recommendations"
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
			return "version_recommendationss"
		except Exception as e :
			raise e



	'''
	get Recommendations for Xen HotFix
	'''
	@property
	def xen_hotfix_recommendation(self) :
		try:
			return self._xen_hotfix_recommendation
		except Exception as e :
			raise e


	'''
	get xen hotfix is applied or not
	'''
	@property
	def xen_hotfix(self) :
		try:
			return self._xen_hotfix
		except Exception as e :
			raise e


	'''
	get Recommendations for XenServer
	'''
	@property
	def xen_recommendation(self) :
		try:
			return self._xen_recommendation
		except Exception as e :
			raise e


	'''
	get Suggestion for user regarding version matrix
	'''
	@property
	def suggestion(self) :
		try:
			return self._suggestion
		except Exception as e :
			raise e


	'''
	get Xen Version
	'''
	@property
	def xen_version(self) :
		try:
			return self._xen_version
		except Exception as e :
			raise e


	'''
	get Branch Repeater Version: All Branch Repeater Instances of this formation should be of same verison
	'''
	@property
	def br_version(self) :
		try:
			return self._br_version
		except Exception as e :
			raise e


	'''
	get Recommendations for NetScaler
	'''
	@property
	def ns_recommendation(self) :
		try:
			return self._ns_recommendation
		except Exception as e :
			raise e


	'''
	get Service Management Version
	'''
	@property
	def svm_version(self) :
		try:
			return self._svm_version
		except Exception as e :
			raise e


	'''
	get NetScaler Version: All NetScaler's Instances of this formation should be of same verison
	'''
	@property
	def ns_version(self) :
		try:
			return self._ns_version
		except Exception as e :
			raise e


	'''
	get Recommendations for Xen Supplemantal Pack
	'''
	@property
	def xen_supplemental_pack_recommendation(self) :
		try:
			return self._xen_supplemental_pack_recommendation
		except Exception as e :
			raise e


	'''
	get Xen Supplemental Pack Version
	'''
	@property
	def xen_supplemental_pack_version(self) :
		try:
			return self._xen_supplemental_pack_version
		except Exception as e :
			raise e


	'''
	get Recommendations for Repeater
	'''
	@property
	def br_recommendation(self) :
		try:
			return self._br_recommendation
		except Exception as e :
			raise e


	'''
	get Recommendations for Management Service
	'''
	@property
	def svm_recommendation(self) :
		try:
			return self._svm_recommendation
		except Exception as e :
			raise e

	'''
	Use this operation to get recommendations for version matrix.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				version_recommendations_obj=version_recommendations()
				response = version_recommendations_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of version_recommendations resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			version_recommendations_obj = version_recommendations()
			option_ = options()
			option_._filter=filter_
			return version_recommendations_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the version_recommendations resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			version_recommendations_obj = version_recommendations()
			option_ = options()
			option_._count=True
			response = version_recommendations_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of version_recommendations resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			version_recommendations_obj = version_recommendations()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = version_recommendations_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(version_recommendations_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.version_recommendations
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(version_recommendations_responses, response, "version_recommendations_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.version_recommendations_response_array
				i=0
				error = [version_recommendations() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.version_recommendations_response_array
			i=0
			version_recommendations_objs = [version_recommendations() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_version_recommendations'):
					for props in obj._version_recommendations:
						result = service.payload_formatter.string_to_bulk_resource(version_recommendations_response,self.__class__.__name__,props)
						version_recommendations_objs[i] = result.version_recommendations
						i=i+1
			return version_recommendations_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(version_recommendations,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class version_recommendations_response(base_response):
	def __init__(self,length=1) :
		self.version_recommendations= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.version_recommendations= [ version_recommendations() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class version_recommendations_responses(base_response):
	def __init__(self,length=1) :
		self.version_recommendations_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.version_recommendations_response_array = [ version_recommendations() for _ in range(length)]
