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

from massrc.com.citrix.mas.nitro.datatypes.MPSDatatype import MPSDatatype
from massrc.com.citrix.mas.nitro.datatypes.MPSConstants import MPSConstants

class MPSIPAddress(MPSDatatype):
	value =""
	constraints = []
	
	def __init__(self,_value):
		if _value :
			constraints = MPSConstraintIP[MPSConstants.GENERIC_CONSTRAINT]
			length = len(constraints)
			self.constraints[i]= [ MPSConstraintIP() for _ in range(length)]
			self.value =_value


	def setConstraintIsReq(self,constraintType,isRequired):
		if(constraintType == MPSConstants.GENERIC_CONSTRAINT):
			for _ttype in range(0,MPSConstants.GENERIC_CONSTRAINT) :
				self.constraints[_type].setIsRequired(isRequired)
		else :
			self.constraints[_type].setIsRequired(isRequired)


	def validate(self,operationType,_value,label):
		self.value = str(_value)
		constraintType = getConstraintType(operationType)
		if(constraintType == MPSConstants.INVALID_CONSTRAINT):
			raise Exception(label+" Invalid operation type");
		
		
		self.constraints[constraintType].validate(value,label)
		
