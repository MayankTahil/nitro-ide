'''
* Copyright (c) 2008-2015 Citrix Systems, Inc.
*
*   Licensed under the Apache License, Version 2.0 (the "License");
*   you may not use this file except in compliance with the License.
*   You may obtain a copy of the License at
*
*       http://www.apache.org/licenses/LICENSE-2.0
*
*   Unless required by applicable law or agreed to in writing, software
*   distributed under the License is distributed on an "AS IS" BASIS,
*   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
*   See the License for the specific language governing permissions and
*   limitations under the License.
'''

import json
from massrc.com.citrix.mas.nitro.util.nitro_util import nitro_util
from massrc.com.citrix.mas.nitro.resource.Base.ipayload_formatter import ipayload_formatter
from massrc.com.citrix.mas.nitro.resource.Base.base_resource import base_resource
from massrc.com.citrix.mas.nitro.service.options import options

'''
* Json class implements the methods in ipayload_formatter interface.
'''

class Json(ipayload_formatter):
    '''
    * Converts resource to Json string.
    * @param resrc nitro resource.
    * @return returns a String
    '''
    def resource_to_string_convert(self, resrc):
        try:
            return json.dumps(self.resource_to_object_convert(resrc)) 
        except Exception as e:
            raise
    
    def resource_to_object_convert(self, resrc):
        try:
            dict_valid_values={}

            for k,v in resrc.__dict__.items() :
                k=k[1:]
                if(not resrc.is_body_property(k)):
                    continue
                if isinstance(v, base_resource):
                    dict_valid_values[k] = self.resource_to_object_convert(v)
                elif type(v) is not list : 
                    # value is a primitive
                    dict_valid_values[k] =v
                    
                else: # value is a list
                    result=[]
                    for item in v :
                        if isinstance(item, base_resource):
                            # list item is embedded obj.
                            result.append(self.resource_to_object_convert(item))

                        else:
                            # list item is primitive.
                            result.append(item)
                        dict_valid_values[k] = result
            return dict_valid_values 
        except Exception as e:
            raise e


    '''
    * Converts Json string to resource.
    * @param responseClass Type of the class to which the string has to be converted to.
    * @param response input string.
    * @return returns nitro resource object.
    '''

    def string_to_resource(self, responseClass, response_dict, resrc_type ,bulk = "", class_name = None):
        try:
            temp_dict = json.loads(response_dict)
            underscore_dict = {}
            plural_name = None
            if class_name:
                plural_name = class_name.get_plural_object_name()
                if plural_name:
                    orig_resrc_type = resrc_type
                    resrc_type = plural_name
            if resrc_type.lower() in temp_dict.keys() :
                if (type(json.loads(response_dict)[resrc_type.lower()]) is list) :
                    length = len(json.loads(response_dict)[resrc_type.lower()])
                else :
                    length = 1
                response = responseClass(length)
            elif resrc_type in temp_dict.keys() :
                if (type(json.loads(response_dict)[resrc_type]) is list) :
                    length = len(json.loads(response_dict)[resrc_type])
                else :
                    length = 1
                response = responseClass(length)
            else :
                response = responseClass()
            if plural_name:
                response.__dict__[plural_name] = response.__dict__[orig_resrc_type]
            
            for key in temp_dict.keys() :
                if key == 'additionalInfo':
                    pass
                    
                elif key in response.__dict__ and type(response.__dict__[key]) is list :
                
                    if type(temp_dict[key]) is list :
                        for i in range(length) :
                            underscore_dict = {}
                            for each_key in (temp_dict[key][i]).keys() :
                                underscore_dict['_'+each_key] = (temp_dict[key][i])[each_key]
                            (response.__dict__[key])[i].__dict__ = underscore_dict

                    else :
                        for item in temp_dict[key].keys() :
                            (response.__dict__[key])[0].__dict__['_'+item] = (temp_dict[key])[item]

                else :
                    response.__dict__[key] = temp_dict[key]
            return response
        except Exception as e:
            raise e



    def string_to_bulk_resource(self,responseClass,object_type,props):
        try:
            json_value = json.dumps(props, separators=(',',':'))
            list_obj='{ "errorcode": 0, "message": "Done", "'+object_type+'":['+json_value+']}'
            list_obj=unicode(list_obj)
            return self.string_to_resource(responseClass, list_obj, object_type)
        except Exception as e:
            raise e



    '''
    * Converts resource to Json string.
    * @param resrc nitro resource.
    * @param id sessionId.
    * @param option options class object.
    * @return returns a String
    '''
    def resource_to_string(self, resrc ,option ="",onerror=""):
        try:
            objtype = resrc.__class__.__name__
            result = "{ "
            if option:
                if option.version=="v1":
                    result = result + "\"params\":{"
                    if option.action :
                        result = result + "\"action\":\"" + option.action + "\","
                    if onerror :
                        result = result +"\"onerror\":\"" + onerror +"\"";

                    result = result + "},"

            result = result + "\"" + objtype + "\":" + self.resource_to_string_convert(resrc) + "}"
            return result

        except Exception as e:
            raise e

    '''
    * Converts resources to Json string.
    * @param resources nitro resources.
    * @param id sessionId.
    * @param option options class object.
    * @return returns a String
    '''
    def resource_to_string_bulk(self, resources,option ="",onerror=""):
        try :
            plural_name = resources[0].__class__.get_plural_object_name()
            if plural_name:
                objecttype = plural_name
            else:
                objecttype = resources[0].__class__.__name__

            request = "{"

            if option:
                if option.version=="v1":
                    request = request + "\"params\":{"
                    if option.action :
                        request = request + "\"action\":\"" + option.action + "\","
                    if onerror :
                        request = request +"\"onerror\":\"" + onerror +"\"";

                    request = request + "},"

            request = request + "\"" + objecttype + "\":["
            for i in range(len(resources)):
                str_ = self.resource_to_string_convert(resources[i])
                request = request + str_
                if i!= (len(resources)-1):
                    request = request + ","
            request = request + "]}"
            return request
        except Exception as e:
            raise e




    '''
    * Converts nitro resource to Json string. This is exclusively for
    * forming unset string.
    * @param resrc nitro resource.
    * @param id sessionId.
    * @param option options class object.
    * @param args Array of arguments of resource that are to be unset.
    * @return returns a String
    '''
    def unset_string(self, resrc, args):
        try:
            result = "{ "
            objstr = nitro_util.object_to_string(resrc)
            if objstr :
                result = result + objstr
            if args :
                for i in range(len(args)):
                    result = result + "\"" + args[i] + "\": true"
                    if i != (len(args)-1) :
                        result = result + ","
                    else :
                        result = result + "}"
            return result
        except Exception as e:
            raise e


    def unset_string_bulk(self, resources, args):
        try:
            objecttype = resources[0].__class__.get_object_type()
            result = "{ "
            result = result + "\"" + objecttype + "\": ["
            for i in range(len(resources)):
                objstr = self.unset_string(resources[i],args)
                if objstr :
                    result = result + objstr
                if i != (len(resources)-1) :
                    result = result + ","
            result = result + "]}"
            return result
        except Exception as e:
            raise e

