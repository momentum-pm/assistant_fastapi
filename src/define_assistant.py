import autogen

class AssistantDefiner:
    def __init__(self, llm_config={}, name="assistant", system_message="") -> None:
        self.llm_config = llm_config
        self.name = name
        self.system_message = system_message

    def define_assistant(self):
        return autogen.AssistantAgent(
            name=self.name,
            system_message=self.system_message,
            llm_config=self.llm_config,
        )

if __name__ == "__main__":
    assistant_definer = AssistantDefiner()
    assistant_definer.define_assistant()