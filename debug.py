import rest_api_handler
import handle_inputs
import job_handler

class parameter():
    def __init__(self, name, value):
        self.Name = name
        self.Value = value


input_handler = handle_inputs.input_data()
input_handler.duration = '5'
input_handler.test = 'ASharedTest_nobp'
input_handler.parameters = [
    parameter('leInput', 'aaa'),
    parameter('leInput1','1qazxsw2')
]
input_handler.blueprint = 'Hrvatski Telekom Demo'
input_handler.globalinputs = [
    parameter('CPE Name', 'CPE 1'),
    parameter('DSLAM Name','DSLAM 1')
]

rest_handler = rest_api_handler.rest_handler(login_data=input_handler.creds_json)
job_info = rest_handler.run_job(test_name=input_handler.test,
                                blueprint=input_handler.blueprint,
                                duration=input_handler.duration,
                                parameters=input_handler.parameters,
                                global_inputs=input_handler.globalinputs)
job_runner = job_handler.run_job().execute(job_info, rest_handler, input_handler)
pass