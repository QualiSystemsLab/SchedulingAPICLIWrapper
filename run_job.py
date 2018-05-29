import job_handler
import rest_api_handler
import handle_inputs

input_handler = handle_inputs.input_data()
input_handler.get_user_inputs()
rest_handler = rest_api_handler.rest_handler(login_data=input_handler.creds_json)
job_info = rest_handler.run_job(test_name=input_handler.test,
                                blueprint=input_handler.blueprint,
                                duration=input_handler.duration,
                                parameters=input_handler.parameters,
                                global_inputs=input_handler.globalinputs)
job_runner = job_handler.run_job().execute(job_info, rest_handler, input_handler)