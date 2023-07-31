import re
import os
import openai
import openai.error
import logging
import sys
from dotenv import load_dotenv
import commentjson as json
from ...typing import sha256, Dict, get_type_hints

__all__ = [
    "my_api_key",
]

load_dotenv()

with open("config.json", "r", encoding="utf-8") as f:
    purgpt_api_key = json.load(f)["purgpt_api_key"]

purgpt_api_key = os.environ.get("PURGPT_API_KEY", purgpt_api_key)

openai.api_key = purgpt_api_key
openai.api_base = "https://beta.purgpt.xyz"

url = 'https://beta.purgpt.xyz'
model = [
    'babbage',
    'davinci',
    'text-davinci-001',
    'ada',
    'text-curie-001',
    'text-ada-001',
    'curie-instruct-beta',
    'davinci-instruct-beta',
    'text-davinci-003',
    'text-babbage-001',
    'curie',
    'text-davinci-002',
    'gpt-3.5-turbo',
    'gpt-3.5-turbo-16k',
]

supports_stream = False
needs_auth = False
working = True

def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            stream=stream
        )
        if stream:
            for chunk in response:
                yield chunk.choices[0].delta.get("content", "")
        else:
            yield response.choices[0]['message'].get("content", "")
            
    except openai.error.APIError as e:
        if e.http_status == 429:
            detail_pattern = re.compile(r'{"detail":"(.*?)"}')
            match = detail_pattern.search(e.user_message)
            if match:
                error_message = match.group(1)
                print(error_message)
                yield error_message
            else:
                print(e.user_message)
                yield e.user_message
        else:
            raise


params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    '(%s)' % ', '.join(
        [f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]])
