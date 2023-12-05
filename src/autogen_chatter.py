import os
import autogen
from define_assistant import AssistantDefiner

class AutoGenChatter:
  def __init__(self, autogen_user_proxy, autogen_assistant):
    self.user_proxy = autogen_user_proxy
    self.assistant = autogen_assistant

  async def chat(self, message, silent=False):
    sender = self.user_proxy
    self.assistant._process_received_message(message, sender, silent)
    response = await self.assistant.a_generate_reply(sender=sender)
    return response
  
if __name__ == "__main__":
  config_list = [
        {
            'model': 'gpt-3.5-turbo-16k',
            'api_key': os.getenv("OPENAI_API_KEY"),
        }
    ]
  
  llm_config = {"config_list": config_list, "cache_seed": 35, "timeout":360}
  assistant_message = '''
                    Answer any question user asks you politely with details.
                '''

  user_proxy_message = '''
                You are a helpful assistant who answers any questions.
            '''

  test_assistant = AssistantDefiner(llm_config=llm_config, name="test_assistant", system_message=assistant_message).define_assistant()
  test_user_proxy = autogen.UserProxyAgent(
        name="Dave",
        human_input_mode="ALWAYS",

    )
  test_assistant.reset()
  autogen_chatter = AutoGenChatter(test_user_proxy, test_assistant)
  response = autogen_chatter.chat(user_proxy_message)
  print(response)