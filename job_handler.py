import json
import time
import sys


class run_job():
    def __init__(self):
        pass

    def execute(self, job_info=None, rest_handler=None, input_handler=None):
        if not job_info:
            print ("Cannot Start Job! exiting")
            sys.exit(100)
        print ("Job request has been recieved. expected duration is {0} minutes".format(input_handler.duration))
        job_state = ''
        job_status = ''
        while job_state not in ['Done', 'Cancelled']:
            job_status = json.loads(rest_handler.get_job_details(job_id=job_info.text[1:-1]).text)
            job_state = job_status.get('JobState')
            time.sleep(10)
            print "The current status of the Job is {0}".format(job_state)
        print "The Job result is {0}".format(job_status.get('JobResult'))
        print "Link to Report: {}".format(job_status.get('Tests')[0].get('ReportLink'))