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
import re
from abc import ABCMeta, abstractmethod, abstractproperty


class MPSConstraint:
    __metaclass__ = ABCMeta


    @abstractmethod
    def validate(self,operationType, _value,label):
        pass

	def isValidIP4(self,addr):
		st =  addr.split(".")
		if len(st)!=4 :
			return False
		for i in iter(str):
			try :
				if not i.isdigit() :
					raise Exception("Type Error For Ip Address Provided")
				val = int(i)
				if (val > 255 or val < 0 ) :
					return False
			except ValueError:
				return False
		return True		

	
	def isValidIP6(self,addr):
		#code here for validation
		print "ipv6"

		
	def isValidIP(self,addr):
		if (self.isValidIP4(addr)):
			return True
		if (self.isValidIP4(addr)):
			return True
		return False
	
	def isValidIPv6Net(self,addr):
		list = addr.split("/");
		if(len(list)!=2):
			return False;
		ipv6 = list[0];
		prefix = int(list[1]);		
		if (not self.isValidIP4(ipv6)):
			return False;			
		if(prefix < 0 or prefix > 128 ):
			return False;
		return True;

	def isValidHostName(self,addr):
		
		#Internet Hostname consists of labels separated by '.'
		#The entire hostname length cannot exceed 255 characters
		#It allows only alpha-numeric characters, '-' and '_'	
		if (len(addr) > 255 ):
			return False
		
		#Regular Expression for a label in the hostname
      	#'-' and '_' cannot start or end a label in the hostname
		#Also, each label should not exceed 63 characters
		
		regEx ="^[A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9_-]*[A-Za-z0-9]$"
		pattern = re.compile(regEx)
		
		tokens = addr.split(".")
		for i in tokens :
			if len(i)>63 :
				return False
			
			if not pattern.match(i):
				return False
		return True	
		

	def isValidInternetHost(self,addr):
		
		if self.isValidIP(addr) :
			return True
			
		if self.isValidHostName(addr):
			return True
			
		return False 