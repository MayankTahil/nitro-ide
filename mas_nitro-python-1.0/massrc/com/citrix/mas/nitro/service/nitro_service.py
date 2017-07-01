
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

nitro_service is client interface through which Nitro operations are performed on resources.
'''

from massrc.com.citrix.mas.nitro.resource.Base.login import login
from massrc.com.citrix.mas.nitro.resource.Base.Json import Json


class nitro_service(object) :
    _username = None
    _password = None
    _timeout = ""
    _ipaddress = ""
    _version = "v1"
    _sessionid = None
    _action = ""
    _token = ""
    _protocol = ""
    _format = ""
    _onerror = "CONTINUE"
    _certverify = True
    _certbundlepath=""


    def __init__(self,ip=None,protocol="http",version = "v1",_format = Json()):
        try:
            if ip is not None and protocol is None and version is None and _format is None :
                self._ipaddress=ip
                self._protocol="http"
                self._version="v1"
            elif protocol is not None and version is None and _format is None :
                self._ipaddress=ip
                self._protocol=protocol
                self._version="v1"
            elif version is not None and _format is None :
                self._ipaddress=ip
                self._protocol=protocol
                self._version=version
            elif _format is not None :
                self._ipaddress=ip
                self._protocol=protocol
                self._version=version
            self._format = _format

        except Exception as e:
            raise e

    '''
    nitro_service class constructor specifying ip.
    @param ip IPAddress of the NetScaler SDX on which configuration is to be run.

    '''

    '''
    Gets the IPaddress of the NetScaler SDX.
    @return IPaddress.
    '''
    @property
    def ipaddress(self):
        try:
            return self._ipaddress
        except Exception as e:
            raise e

    '''
    sets the ipaddress
    '''

    @ipaddress.setter
    def ipaddress(self, ipaddress ):
        try :
            if not isinstance(ipaddress,str):
                raise TypeError("ipaddress must be set to str value")
            self._ipaddress = ipaddress
        except Exception as e:
            raise e


    # Gets the sessionId.
    # @return sessionId.
    @property
    def sessionid(self):
        try:
            return self._sessionid
        except Exception as e:
            raise e



    '''
    sets the session id.
    param session
    '''
    @sessionid.setter
    def sessionid(self,session):
        try:
            if not isinstance(session,str):
                raise TypeError("session must be set to str value")
            self._sessionid = session
        except Exception as e:
            raise e

    '''
    Gets the sessionId.
    @return sessionId.
    '''

    '''
    Gets the token.
    @return token.
    '''
    @property
    def token(self) :
        try:
            return self._token
        except Exception as e:
            raise e


    '''
    sets the token.
    @param token
    '''
    @token.setter
    def token(self,token):
        try :
            if not isinstance(token,str):
                raise TypeError("token must be set to str value")
            self._token = token
        except Exception as e:
            raise e




    '''
    sets the credentials for the NetScaler SDX.
    @param username Username of the NetScaler SDX
    @param password Password for the NetScaler SDX.
    '''
    def set_credential(self,username,password):
        try :
            if not isinstance(username,str):
                raise TypeError("username must be set to str value")
            if not isinstance(password,str):
                raise TypeError("password must be set to str value")
            self._username = username
            self._password = password
        except Exception as e:
            raise e



    '''
    Checks login status.
    @return true if logged-in else false.
    '''
    def  isLogin(self) :
        if self._sessionid == None :
            return False
        return True

    '''
    Gets the nitro version.
    @return nitro version.
    '''
    @property
    def version(self) :
        try :
            return self._version
        except Exception as e:
            raise e



    '''
    sets the version.
    @@param version The NITRO version to be set.
    '''
    @version.setter
    def version(self, version ):
        try :
            if not isinstance(version,str):
                raise TypeError("version must be set to str value")
            if version == "":
                self._version = "v1"
            elif version!="v1" and version!="v2" :
                raise Exception("error: version value not supported")
            self._version = version
        except Exception as e:
            raise e


    '''
    Gets the protocol.
    @return Returns the protocol.
    '''
    @property
    def protocol(self) :
        try:
            return self._protocol
        except Exception as e:
            raise e


    '''
    Sets the protocol.
    @param protocol The protocol to be set.
    '''
    @protocol.setter
    def protocol(self, protocol ):
        try :
            if not isinstance(protocol,str):
                raise TypeError("protocol must be set to str value")
            if protocol =="" or protocol !="http" or protocol == "https":
                raise Exception("Error Protocol not supported")
            self._protocol = protocol
        except Exception as e:
            raise e

    '''
    Gets the certbundlepath.
    @return Returns the certbundlepath.
    '''
    @property
    def certbundlepath(self) :
        try:
            return self._certbundlepath
        except Exception as e:
            raise e


    '''
    Sets the certbundlepath.
    @param certbundlepath The certbundlepath to be set.
    '''
    @certbundlepath.setter
    def certbundlepath(self, certbundlepath ):
        try :
            if not isinstance(certbundlepath,str):
                raise TypeError("certbundlepath must be set to str value")
            self._certbundlepath = certbundlepath
        except Exception as e:
            raise e


    '''
    Gets the certverify.
    @return Returns the certverify.
    '''
    @property
    def certverify(self) :
        try:
            return self._certverify
        except Exception as e:
            raise e


    '''
    Sets the certverify.
    @param certverify The certverify to be set.
    '''
    @certverify.setter
    def certverify(self, certverify ):
        try :
            if not isinstance(certverify,bool):
                raise TypeError("certverify must be set to bool value")
            self._certverify = certverify
        except Exception as e:
            raise e

    '''
    Gets the onerror status of the MPS Resource.
    @return onerror status.
    '''
    @property
    def onerror(self) :
        try:
            if self._onerror != "" :
                return self._onerror
            return ""
        except Exception as e:
            raise e

    '''
    Sets the onerror status of the MPS Resources.
    @param val This option is applicable for bulk requests.
    possible values: EXIT, CONTINUE.
    if set with EXIT: exists on the first encountered error.
    if set with CONTINUE: executes all the requests irrespective of individual response status.
    '''
    @onerror.setter
    def onerror(self,onerror):
        try:
            if not isinstance(onerror,str):
                raise TypeError("onerror must be set to str value")
            self._onerror = onerror
        except Exception as e:
            raise e

    '''
    @return action.
    '''
    @property
    def action(self) :
        try:
            if self._action !="" :
                return self._action
            return ""
        except Exception as e:
            raise e


    '''
    Sets the onerror status of the MPS Resources.
    @param val This option is applicable for bulk requests.
    possible values: EXIT, CONTINUE.
    if set with EXIT: exists on the first encountered error.
    if set with CONTINUE: executes all the requests irrespective of individual response status.

    '''
    @action.setter
    def action(self,action) :
        try:
            if not isinstance(action,str):
                raise TypeError("action must be set to str value")
            self._action = action
        except Exception as e:
            raise e

    '''
    gets the timeout
    '''
    @property
    def timeout(self):
        try:
            return self._timeout
        except Exception as e:
            raise e


    '''
    sets the credentials for the NetScaler SDX.
    @param timeout session timeout of the NetScaler SDX. Default is 5 mins.

    '''
    @timeout.setter
    def timeout(self,timeout):
        try :
            if not isinstance(timeout,int):
                raise TypeError("timeout must be set to int value")
            self._timeout = timeout
        except Exception as e:
            raise e

    '''
    gets the username
    '''
    @property
    def username(self):
        try:
            return self._username
        except Exception as e:
            raise e


    '''
    sets the credentials for the NetScaler SDX.
    @param username

    '''
    @username.setter
    def username(self,username):
        try :
            if not isinstance(username,str):
                raise TypeError("Username must be set to str value")
            self._username = username
        except Exception as e:
            raise e



    '''
    gets the password
    '''
    @property
    def password(self):
        try:
            return self._password
        except Exception as e:
            raise e


    '''
    sets the credentials for the NetScaler SDX.
    @param password

    '''
    @password.setter
    def password(self,password):
        try :
            if not isinstance(password,str):
                raise TypeError("Username must be set to str value")
            self._password = password
        except Exception as e:
            raise e


    '''
    Returns payload format.
    @return Returns the ijson.
    '''
    @property
    def  payload_formatter(self) :
        try:
            return self._format
        except Exception as e:
            raise e


    '''
    Use this API to login into NetScaler SDX.
    @param username Username
    @param password Password for the NetScaler SDX.
    @param timeout timeout for NetScaler SDX session. Default is 5 mins
    @return status of the operation performed.
    @throws Exception nitro exception is thrown.
    Based on the parameters provided it perform the operation
    '''

    def login(self,username=None,password=None,timeout=None) :
        try:
            self.action = "add"
            login_result =""
            if username is None and password is None :
                if self._username is not None and self._password is not None :
                    login_obj = login()
                    login_obj.username=self._username
                    login_obj.password=self._password
                    login_obj.session_timeout=self._timeout
                    login_result = login()
                    login_result = login.add(self,login_obj)
                else :
                    raise Exception("Either username/password or both are missing")
            elif username is not None and password is not None :
                self._username=username
                self._password=password
                if timeout is not None:
                    self.timeout=timeout
                login_obj = login()
                login_obj.username=self._username
                login_obj.password=self._password
                login_obj.session_timeout=self._timeout
                login_result = login.add(self,login_obj)
            elif username is None or password is None :
                if username is not None :
                    self._username = username
                if password is not None :
                    self._password = password
                if self._username is None :
                    raise Exception("Username is missing")
                elif self._password is None :
                    raise Exception("Password is missing")

            if self._protocol== 'https'and self._certverify==True and self._certbundlepath is None:
                raise Exception("Specify certbundlepath for https protocol/set certverify=false")

            return login_result
        except Exception as e:
            raise e


    '''
    login_request function is used to provide session id
    which can be used for further request

    '''


    '''
    Use this API to clear the current session.
    '''

    def clear_session(self) :
        try:
            self._sessionid = None
        except Exception as e:
            raise e


    '''
    Use this to API to re login into NetScaler SDX.
    @return status of the operation performed.
    @throws Exception nitro exception is thrown.
    '''

    def relogin(self) :
        try:
            self._sessionid =""
        except Exception as e:
            raise e


    '''
    Use this API to logout from current session.
    @return status of the operation performed.
    '''
    def logout(self) :
        try :
            if (self._sessionid is None or len(self._sessionid)<=0):
                raise Exception("User not logged-in")
            logout_obj = login()
            logout_obj.sessionid=self._sessionid
            logout_result = login.delete(self,logout_obj)

            self._username = None
            self._password = None
            self._sessionid = None
            return logout_result
        except Exception as e:
            raise e