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
        self.globalinputs = []


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
        parser.add_argument("-g", "--globalinputs",
                            help="parameters required by the blueprint. usage: parameter1Name:parameter1Value,parameter2Name:parameter2Value")
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
            if args.globalinputs:
                g_parameters = args.globalinputs.split(',')
                for g_param in g_parameters:
                    self.globalinputs.append(parameter(g_param.split(':')[0], g_param.split(':')[1]))
            else:
                print ("no input parameters for the blueprint have been recieved!")
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
                self.parameters.append(parameter(param.split(':')[0], param.split(':')[1]))
                print self.parameters[0].Name
                print self.parameters[0].Value
        else:
            print ("no input parameters for the test have been recieved!")
