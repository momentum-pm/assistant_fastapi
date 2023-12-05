import autogen
from define_assistant import AssistantDefiner
from autogen_chatter import AutoGenChatter

class GoalDefiner:
    def __init__(self, config_list, cache_seed=33) -> None:
        self.goal_definer_llm_config = {"config_list": config_list, "cache_seed": cache_seed, "timeout":360}
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
        
        self.goal_definer_assistant = AssistantDefiner(llm_config=self.goal_definer_llm_config, name="goal_definer", system_message=self.Goal_Definer_message).define_assistant()
        self.user_proxy = autogen.UserProxyAgent(
            name="Dave",
            human_input_mode="ALWAYS",
        )

    def define_goal(self):
        goal_definer_assistant.reset()
        user_proxy.initiate_chat(goal_definer_assistant, message=self.user_proxy_message)

    async def chat(self):
        self.autogen_chatter = AutoGenChatter(user_proxy, goal_definer_assistant)


if __name__ == "__main__":
    goal_definer = GoalDefiner()
    goal_definer.define_goal()