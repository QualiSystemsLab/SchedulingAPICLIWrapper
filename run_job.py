import job_handler
import rest_api_handler
import handle_inputs

input_handler = handle_inputs.input_data()
input_handler.get_user_inputs()
rest_handler = rest_api_handler.rest_handler(login_data=input_handler.creds_json)
job_info = rest_handler.run_job(test_name=input_handler.test,
                                blueprint=input_handler.blueprint,
                                jobDuration=input_handler.jobDuration,
                                parameters=input_handler.parameters,
                                global_inputs=input_handler.globalinputs,
                                executionServers=input_handler.executionServers,
                                testDuration=input_handler.testDuration)
job_runner = job_handler.run_job().execute(job_info, rest_handler, input_handler)