import logging
from org_pipeline_automation import *


class kafka_pipeline_manager:
    def create (self, org_name):
        resp = self.__appendPipeline(org_name)
        return resp
    
    def __appendPipeline(self, org_name):
        line1 = "- pipeline.id: pcf_%s" % org_name
        line2 = "  pipeline.workers: 5"
        line3 = "  pipeline.batch.size: 1000"
        line4 = "  path.config: \"/etc/logstash/conf.d/pcf_%s.conf\"" % org_name
        try:
            with open ("/etc/logstash/pipelines.yml", 'w') as out:
                out.writelines([line1, line2, line3, line4])
            return "Successfully appended pipelines.yml for org {0}".format(org_name)
        except Exception as e:
            logging.error(e)
            return "Failed to append pipelines.yml for org {0}".format(org_name)

if __name__ == "__main__":
    pass