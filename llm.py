from openai import OpenAI
from .env import OPENAI_API_KEY


class LLM:
    client = OpenAI(api_key=OPENAI_API_KEY)

    def get_output(
        self, prompt, query, model="gpt-3.5-turbo", format="json_object", debug=False
    ):
        import json

        completion = self.client.chat.completions.create(
            model=model,
            response_format={"type": format},
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": query},
            ],
        )
        text_response = completion["choices"][0]["messages"]["content"]
        if format == "json_object":
            response = json.loads(text_response)
        else:
            response = text_response
        if debug:
            print(f"Response ({type(response)}): {text_response}")
        return response

    def get_moderation(self, key, text):
        completion = self.client.moderations.create(
            input=[text],
            model="text-embedding-ada-002",
        )
        embedding = completion.data[0].embedding
        return embedding
