import os
import pathlib
import autogen
from autogen_chatter import AutoGenChatter

class AiAnalyzer:
    def __init__(self) -> None:
        self._load_data()
        self.autogen_chatter = AutoGenChatter()

    async def analyze(self, message, user_id=1):      
        response = await self.users_objects[user_id][task].chat(message)
        return response

    def _load_data(self):
         self.file_path = os.path.join(pathlib.Path(__file__).parent.parent.parent.absolute(), "data/system_arch.pdf")
         
    def _initialize_assistant(self):
        self.Goal_Definer_message = '''
                    Go through these questions one by one. Ask a question, get the answer, go to next one
                    * What is the goal?
                    * Who the owner of goal is?
                    * who are the other people related to this goal?
                    * Clarify the goal by asking some questions but don't ask about the execution plan, steps and milestones.
                    * Is goal private or it can be connected with other goals.
                '''

        self.user_proxy_message = '''

                '''
        
                
                '''
                    You are talking to a user who wants to define a goal in a system of goals.
                    Each goal has an AI-PM and an Owner (a person).
                    You will be this goal's AI-PM.
                    Go through the questions one by one. Ask a question, get the answer, go to the next one.
                '''

        self.goal_definer_assistant =  autogen.AssistantAgent(
            name="goal_definer",
            system_message=self.Goal_Definer_message,
            llm_config={"config_list": [{"model":os.environ.get("DEFAULT_MODEL"), "api_key":"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"}], "cache_seed": cache_seed, "timeout":360},
        )
        self.user_proxy = autogen.UserProxyAgent(
            name="Dave",
            human_input_mode="ALWAYS",
        )

        self.goal_definer_assistant.reset()
        self.autogen_chatter = AutoGenChatter(self.user_proxy, self.goal_definer_assistant)
if __name__ == "__main__":
    ai_analyzer = AiAnalyzer()