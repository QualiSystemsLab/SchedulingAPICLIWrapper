import json
import time
import sys
import argparse

class parameter():
    def __init__(self, name, value):
        self.Name = name
        self.Value = value


class input_data(object):
    def __init__(self):
        creds = open('creds.json', 'r')
        self.creds_json = json.loads(creds.read())
        creds.close()
        self.test = ''
        self.blueprint = ''
        self.duration = ''
        self.parameters = []


    def get_user_inputs(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-t","--test",
                            help="The name of the test to run. note: it must be in Shared")
        parser.add_argument("-b", "--blueprint",
                            help="The name of the blueprint to reserve")
        parser.add_argument("-d", "--duration",
                            help="The duration of the test to run, in minutes. the default is 5 minutes ")
        parser.add_argument("-p", "--parameter",
                            help="parameters required by the test. usage: parameter1Name:parameter1Value,parameter2Name:parameter2Value")
        args = parser.parse_args()
        # handle the test input:
        if args.test:
            self.test = args.test
        else:
            print ("no test name recieved! exiting")
            sys.exit(4)
        # handle the blueprint input:
        if args.blueprint:
            self.blueprint = args.blueprint
        else:
            print ("no blueprint name recieved!")
        # handle the blueprint input:
        if args.duration:
            self.duration = args.duration
        else:
            print ("no duration recieved! using default value of 5 minutes")
        # handle the parameters input:
        if args.parameter:
            parameters = args.parameter.split(',')
            for param in parameters:
                self.parameters.append(parameter(param.split(':')[0],param.split(':')[1]))
        else:
            print ("no input parameters for the test have been recieved!")


        # if sys.argv.__len__() < 2:
        #     print ("no test name recieved!")
        #     print ("USAGE python run_job.py <test_name> <blueprint_name> <duration>")
        #     print ("default duration is 5 minutes")
        #     sys.exit(2)
        # self.test = sys.argv[1]
        # if self.test in ['help', 'h' , '--help', '?']:
        #     print "USAGE python run_job.py <test_name> <blueprint_name> <duration>"
        #     print "default duration is 5 minutes"
        #     sys.exit()
        # if sys.argv.__len__() == 3:
        #     self.blueprint = sys.argv[2]
        # else:
        #     self.blueprint = ''
        # if sys.argv.__len__() == 4:
        #     self.duration = sys.argv[3]
        # else:
        #     self.duration = '5'