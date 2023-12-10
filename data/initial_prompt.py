from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

config_list = [
    {
        'model': 'gpt-3.5-turbo-16k',
        'api_key': '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',
    }
]

system_message = '''You are the project-manager of 'Create a Personalized Virtual Health Assistant' goal which said with details in context.
                    You are responsible for all factors of the project and you should update project factors due to any new information will be given to you about the project.
                    Just update the timeline according to the changes
                    For example if someone gets sick, you should extend project timeline.
                    If a task is done or finished already, you should remove its time from timeline. 
                    If a new subtask is added to project, you should estimate its time and update project timeline.
                    If any event happened that affects the project's time significantly, the risks should be updated.
                    You should list all of changes and updates should be applied in the system based on the new information and events user will gave you.
                    The new information will be given in messages. 
                    Handle the project carefully. You are the project-manager. 
                    Any new information come to you specify any change in all of the variables of the system specially the execution plan and timeline of the project.
                    '''

message = '''You are the project manager of this goal: 'Create a Personalized Virtual Health Assistant' '''
message += '''
            Context is: {context}
           '''.format(context=context)
llm_config = {"config_list": config_list, "cache_seed": 120}
assistant = AssistantAgent( name="assistant",
                            system_message=system_message,
                            llm_config=llm_config,)
user_proxy = UserProxyAgent("user_proxy", human_input_mode="ALWAYS")
assistant.reset()
user_proxy.initiate_chat(assistant, message=message)
# This initiates an automated chat between the two agents to solve the task