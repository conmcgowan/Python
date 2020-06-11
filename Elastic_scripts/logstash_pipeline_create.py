import os
import fileinput
import logging
from org_pipeline_automation import *


class kafka_pipeline_manager:


    def create(self, org_name):
        respClone = self.__cloneTemplate(org_name)
        respReplace = self.__replaceOrg(org_name)
        return respClone
        return respReplace

   #Clone conf template to file location and rename   
    def __cloneTemplate(self, org_name):
        try:
            os.chdir(r"/etc/logstash/conf")
            os.system("cp pcf_org_template.conf pcf_%s.conf" % org_name)
            return "Template sucessfully cloned"
        except Exception as e:
            logging.error(e)
            return "Failed to clone template"
        
    #Search and replace place-holder org with new org name
    def __replaceOrg(self, org_name):
        filedata = filedata.replace('new_pcf_org', '%s' % org_name)
        try:
            with open('pcf_%s.conf', 'r' % org_name) as file :
                filedata = file.read()
            
            with open('pcf_%s.conf', 'w' % org_name) as file:
                file.write(filedata)
            return "Template successfully configured for {0}".format(org_name)
        except Exception as e:
            logging.error(e)
            return "Configuration failed for {0}".format(org_name)

if __name__ == "main":
   pass 