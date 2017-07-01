
class nitro_exception :
    errorcode = ""
    message = ""
    severity =""

    def __init__(self, errorcode ,message ,severity):
        self.errorcode = errorcode
        self.message = message
        self.severity = severity


    def __str__(self):
        result=""
        if self.errorcode != "":
            result='"errorcode" : '+str(self.errorcode)
        if self.message != "" and result !="":
            result=result+' , "message" : "'+self.message+'"'
        if self.severity !="" and result !="":
            result=result+' , "severity" : "'+self.severity+'"'
        result='{ '+result+' }'
        return repr(result)

    def get_errorcode(self):
        return self.errorcode

    def get_message(self):
        return self.message