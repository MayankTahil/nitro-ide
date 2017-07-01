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

class MPSConstraintDouble(MPSConstraint):
	isRequired=False
	maxValue=0
	minValue=0
	defaultValue=0


	def __init__(self):
		self.isRequired= False
		self.maxValue=0
		self.minValue=0
		self.defaultValue= long(-1)

	def setIsRequired(self,isRequired):
		self.isRequired = isRequired

	def setMaxValue(self,maxValue):
		self.maxValue = maxValue

	def setMinValue(self,minValue):
		self.minValue = minValue
		
	def setDefaultValue(self,defaultValue):
		self.defaultValue = defaultValue


	def  validate(self,_value,label):
		if not _value :
			_value = long(defaultValue)
			
		value = long(_value)

		if(self.isRequired == False and value== self.defaultValue):
			return
		

		if(value < self.minValue) :
			raise Exception(label+" value: "+value+" is less than minimum value: "+ self.minValue)

		if(value > self.maxValue) :
			raise Exception(label+" value: "+value+" is less than minimum value: "+ self.maxValue)
				
		return

