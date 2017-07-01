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
import re

class MPSConstraintString(MPSConstraint):
	isRequired=False
	maxStrLen=0
	minStrLen=0
	charSetRegEx=""

	def __init__(self):
		print "mpscontraint"
		self.isRequired= False
		self.maxStrLen=0
		self.minStrLen=0
		self.charSetRegEx=False
		

	def setIsRequired(self,isRequired):
		self.isRequired = isRequired

	def setMaxStrLen(self,maxStrLen):
		self.maxStrLen = maxStrLen

	def setMinStrLen(self,minStrLen):
		self.minStrLen = minStrLen
		
	def setCharSetRegEx(self,charSetRegEx):
		self.charSetRegEx = charSetRegEx
	
	def validate(self, _value,label):
		if not _value :
			_value = ""
		
		value = str(_value)
		
		if(self.isRequired == False and len(value)==0):
			return
		
		if(len(value) < self.minStrLen):
			raise Exception(label+" String length: "+len(value)+" is less than minimum length: "+self.minStrLen)

		if(len(value) > self.maxStrLen):
			raise Exception(label+" String length: "+len(value)+" is greater than minimum length: "+self.maxStrLen)
				
		if(len(self.charSetRegEx)==0):
			return
		
		pattern = re.compile(self.charSetRegEx)
		
		if pattern.match(value):
			m = pattern.match(value)
			if m.start()==0 and m.end()==len(value) :
				return
			else :
				raise Exception (label+" String: "+value+" does not comply with characters: "+self.charSetRegEx)
			
		else :
			raise Exception (label+" String: " + value + " Null matcher value returned")
		
		