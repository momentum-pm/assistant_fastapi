import os
import autogen
from autogen_chatter import AutoGenChatter

class GoalDefiner:
    def __init__(self, cache_seed=33) -> None:
        self.Goal_Definer_message = '''
                    Go through these questions one by one. Ask a question, get the answer, go to next one
                    * What is the goal?
                    * Who the owner of goal is?
                    * who are the other people related to this goal?
                    * Clarify the goal by asking some questions but don't ask about the execution plan, steps and milestones.
                    * Is goal private or it can be connected with other goals.
                '''

        self.user_proxy_message = '''
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

    async def _send_initial_message(self):
        r = await self.autogen_chatter.chat(self.user_proxy_message)
        print(r)

    def run(self):
        self.goal_definer_assistant.reset()
        self.user_proxy.initiate_chat(self.goal_definer_assistant, message=self.user_proxy_message)

    async def chat(self, message):
        response = await self.autogen_chatter.chat(message)
        print(response)
        return response


if __name__ == "__main__":
    goal_definer = GoalDefiner()
    goal_definer.run()