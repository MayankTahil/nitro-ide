'''
* Copyright (c) 2008-2015 Citrix Systems, Inc.
*
*   Licensed under the Apache License, Version 2.0 (the "License");
*   you may not use self file except in compliance with the License.
*   You may obtain a copy of the License at
*
*       http://www.apache.org/licenses/LICENSE-2.0
*
*  Unless required by applicable law or agreed to in writing, software
*   distributed under the License is distributed on an "AS IS" BASIS,
*   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
*   See the License for the specific language governing permissions and
*   limitations under the License.
'''
 

 
'''
* nitro_util class provides a way to create a string out of the object fields that are set. 
'''

class nitro_util:

    '''
    * encodes the given string using URLEncoder.
    * @param str_ String that is to be encoded.
    * @return  encoded string.
    '''
    @classmethod
    def encode(cls, str_):
        try:
            
            try :
                #check for whether user is using python version >= 3.0
                import urllib.parse
                return urllib.parse.quote_plus(str_)
            except ImportError:
                #check for whether user is using python version < 3.0
                import urllib
                return urllib.quote(str_, safe="")

        except Exception as e:
            raise e

    '''
    * create a string out of the object fields that are set
    * @param obj Object
    * @return String in Json format.
    * @throws Exception Nitro exception is thrown.
    '''
    @classmethod
    def object_to_string(cls, obj):
        try:
            str_ = ""
            flds = obj.__dict__
            flds = dict((k.replace('_',''), v) for k, v in flds.items() if v)
            if (flds):
                for k,v in flds.items() :
                    str_ = str_ + "\"" + k + "\":" 
                    if type(v) is bool :
                        str_ = str_ + v                     
                    elif type(v) is str :
                        str_ = str_ + "\"" + v + "\""                                        
                    elif type(v) is int :
                        str_ = str_ + "\"" + str(v) + "\""
                    if str_ :
                        str_ = str_ + ","
            return str_
        except Exception as e:
            raise e

    '''
    * create a string (without quotes)out of the object fields that are set
    * @param obj Object
    * @return String in Json format.
    * @throws Exception Nitro exception is thrown.
    '''
    @classmethod
    def object_to_string_withoutquotes(cls, obj):
        try:
            str_ = ""
            flds = obj.__dict__
            flds = dict((k.replace('_',''), v) for k, v in flds.items() if v)
            i = 0
            if (flds):
                for k,v in flds.items() :
                    str_ = str_ + k + ":" 
                    if type(v) is bool :
                        str_ = str_ + v                     
                    elif type(v) is str :
                        str_ = str_ + cls.encode(v)                                         
                    elif type(v) is int :
                        str_ = str_ + str(v)
                    i = i + 1 
                    if i != (len(flds.items())) and str_ :
                        str_ = str_ + ","
            print str_
            return str_
        except Exception as e:
            raise e


