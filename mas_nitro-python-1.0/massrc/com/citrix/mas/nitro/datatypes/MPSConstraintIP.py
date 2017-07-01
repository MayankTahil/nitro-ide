'''
* Copyright (c) 2008-2015 Citrix Systems, Inc.
*
* Licensed under the Apache License, Version 2.0 (the "License");
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at
*
*    http://www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS,
* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
* See the License for the specific language governing permissions and
* limitations under the License.
'''

from massrc.com.citrix.mas.nitro.datatypes.MPSConstraint import MPSConstraint

class MPSConstraintIP(MPSConstraint):

	isRequired=False
	
	def __init__(self):
		self.isRequired= False
		
	def setIsRequired(self,isRequired):
		self.isRequired = isRequired
	
	def validate(self, _value,label):
		if not _value :
			_value = ""
		value = str(_value)

		if(self.isRequired == False and len(value)==0):
			return
	
		if(self.isValidIP(value)==False):
			raise Exception(label+" Invalid IP Address: "+value)
			
		return

