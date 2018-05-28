# SchedulingAPICLIWrapper
to install , unpack the Job_Scheduling_API.zip and run using python from the folder you have unpacked into

a cli wrapper for job scheduling via CLI

usage: python run_job.py [-h] [-t TEST] [-b BLUEPRINT] [-d DURATION] [-p PARAMETER]

optional arguments:
  -h, --help            show this help message and exit
  -t TEST, --test TEST  The name of the test to run. note: it must be in
                        Shared
  -b BLUEPRINT, --blueprint BLUEPRINT
                        The name of the blueprint to reserve
  -d DURATION, --duration DURATION
                        The duration of the test to run, in minutes. the
                        default is 5 minutes
  -p PARAMETER, --parameter PARAMETER
                        parameters required by the test. usage: parameter1Name
                        :parameter1Value,parameter2Name:parameter2Value
                       
the creds.json contains the credentials and server location used.

example:

C:\github\quali\debuging\Job_Scheduling_API>python run_job.py -t ASharedTest_nobp -d 3 -p leInput:22,leInput1:cndeg
no blueprint name recieved!
Job request has been recieved. expected duration is 3 minutes
The current status of the Job is Scheduled
The current status of the Job is Running
The current status of the Job is Running
The current status of the Job is Done
The Job result is Passed
Link to Report: http://QS-IL-LT-YOAVE:88/Test/Report?ReportId=85a7de63-cbb9-44bd-9be2-2b86ccc5d097
