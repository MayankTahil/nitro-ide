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


from massrc.com.citrix.mas.nitro.util.nitro_util import nitro_util


'''
 * options class provides a way to specify additional arguments required while fetching the resource.
 '''
class options(object):
    _pageno=0
    _pagesize=0
    _detailview=False
    _compression=""
    _action=""
    _args=""
    _filter=""
    _duration=""
    _count=False
    _version ="v1"
    _onerror=""
    __count = False

    '''
    options class constructor.
    '''
    def __init__(self):
        self._compression =  True
        self._detailview = True
        self._pageno = 0
        self._pagesize = 0
        self._action = ""
        self._filter = ""
        self._count = False
        self._onerror = ""
        self._version = ""
        self._args = ""
        self._duration=""

    '''
    sets page number.
    @param no page number.
    '''
    @property
    def pageno(self):
        return self._pageno


    @pageno.setter
    def pageno(self, no):
        try :
            if not isinstance(no ,int):
                raise TypeError("page no must be set to int value")
            self._pageno = no
        except Exception as e :
            raise e


    '''
    sets the _pagesize.
    @param size number of pages to be retrieved.
    '''
    @property
    def pagesize(self):
        return self._pagesize;

    @pagesize.setter
    def pagesize(self, size):
        try :
            if not isinstance(size ,int):
                raise TypeError("page size must be set to int value")
            self._pagesize = size
        except Exception as e :
            raise e

    '''
    @return _action.
    '''
    @property
    def action(self):
        try:
            return self._action
        except Exception as e :
            raise e

    '''
    sets the _action to be performed.
    @param _action _action.
    '''
    @action.setter
    def action(self, action):
        try :
            if not isinstance(action ,str):
                raise TypeError("action must be set to str value")
            self._action = action
        except Exception as e :
            raise e


    '''
    @return _duration.
    '''
    @property
    def duration(self):
        try:
            return self._duration
        except Exception as e :
            raise e

    '''
    sets the _duration to be performed.
    @param _duration
    '''
    @duration.setter
    def duration(self, duration):
        try :
            self._duration = duration
        except Exception as e :
            raise e


    '''
    gets the onerror value
    '''
    @property
    def onerror(self):
        try :
            return self._onerror
        except Exception as e :
            raise e

    '''
    set the onerror value
    '''
    @onerror.setter
    def onerror(self ,onerror):
        try :
            if not isinstance(onerror ,str):
                raise TypeError("onerror must be set to str value")
            self._onerror = onerror
        except Exception as e :
            raise e




    '''
    returns the version set.
    '''
    @property
    def version(self):
        try :
            return self._version
        except Exception as e :
            raise e


    '''
    sets the version to @param version
    '''
    @version.setter
    def version(self, version):
        try :
            if not isinstance(version ,str):
                raise TypeError("version must be set to str value")
            self._version = version
        except Exception as e :
            raise e




    '''
    returns the compression.
    '''
    @property
    def compression(self):
        try :
            return self._compression
        except Exception as e :
            raise e

    '''
    sets the compression to value flag
    '''
    @compression.setter
    def compression(self, flag):
        try :
            if not isinstance(flag ,bool):
                raise TypeError("flag must be set to bool value")
            self._compression = flag
        except Exception as e :
            raise e

    '''
    @return detail view.
    '''
    @property
    def detailview(self):
        try :
            return self._detailview
        except Exception as e :
            raise e

    '''
    * sets the detail view. if detail view is needed set it to true.
    * @param flag
    '''
    @detailview.setter
    def detailview(self, flag):
        try :
            if not isinstance(flag ,bool):
                raise TypeError("detailview must be set to bool value")
            self._detailview = flag
        except Exception as e :
            raise e


    '''
    @return _count.
    '''
    @property
    def __count(self):
        try :
            return self.__count
        except Exception as e :
            raise e

    '''
    sets the _count.
    @param flag set self to true to find the number of resources of a type configured on NS
    '''
    @__count.setter
    def __count(self, flag):
        try :
            if not isinstance(flag ,bool):
                raise TypeError("count must be set to bool value")
            self.__count = flag
        except Exception as e :
            raise e



    # returns args field
    @property
    def args(self):
        return self._args
    '''
    sets _args field.
    @param _args optional _args required for any operation. self is in json format.
    '''
    @args.setter
    def args(self, args):
        try:
            if not isinstance(args ,str):
                raise TypeError("args must be set to str value")
            self._args = args
        except Exception as e :
            raise e


    '''
    @return returns _filter.
    '''
    @property
    def filter(self):
        try :
            return self._filter
        except Exception as e:
            raise e

    '''
    sets _filter field.
    @param _filter set self with the _filter string to perform filtered get operation.
    Set the _filter parameters in filtervalue object which is then converted to json string.
    '''
    @filter.setter
    def filter(self, filter_str):
        try:
            if not isinstance(filter_str ,str):
                raise TypeError("filter_str must be set to str value")
            self._filter = filter_str
        except Exception as e :
            raise e


    '''
    constructs a string for options object.
    @return String to be concatenated to the URL.
    '''
    def to_string(self):
        try:
            options_str = ""
            if (self._pageno > 0):
                options_str = "pageno="+ str(self._pageno)
            if (self._pagesize > 0):
                if (len(options_str) > 0):
                    options_str = options_str + "&"
                options_str = options_str +"pagesize="+ str(self._pagesize)

            if self._detailview is True:
                if options_str :
                    options_str = options_str + "&"
                options_str = options_str +"view=detail"

            if self._count is True :
                if options_str :
                    options_str = options_str + "&"
                options_str = options_str +"count=yes"

            if self._args :
                if options_str:
                    options_str = options_str + "&"
                options_str = options_str+"args="+self._args

            if self._filter :
                if options_str :
                    options_str = options_str + "&"
                options_str = options_str+"filter="+self._filter

            if self._duration:
                if options_str :
                    options_str = options_str + "&"
                options_str = options_str +"duration="+self._duration

            if self._version is not "v1" and self._action :
                if options_str :
                    options_str = options_str + "&"
                options_str = options_str + "action=" + self._action

            if self._version is not "v1" and self._onerror :
                if options_str :
                    options_str = options_str + "&"
                options_str = options_str + "onerror=" + self._onerror

            return options_str

        except Exception as e:
            raise e

