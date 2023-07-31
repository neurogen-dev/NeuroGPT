import random
from g4f import Provider


class Model:
    class model:
        name: str
        base_provider: str
        best_provider: str

    class gpt_35_turbo:
        name: str = 'gpt-3.5-turbo'
        base_provider: str = 'openai'
        best_provider: Provider.Provider = Provider.Yqcloud
        #best_provider: Provider.Provider = random.choice([Provider.Gravityengine, Provider.Yqcloud, Provider.AItianhu])
        best_providers: list = [Provider.Chatty, Provider.Wewordle, Provider.AItianhu]

    class gpt_35_turbo_0613:
        name: str = 'gpt-3.5-turbo-0613'
        base_provider: str = 'openai'
        best_provider: Provider.Provider = Provider.Zeabur
        #best_provider: Provider.Provider = random.choice([Provider.Zeabur])
        best_providers: list = [Provider.Zeabur]
        

    class gpt_35_turbo_16k_0613:
        name: str = 'gpt-3.5-turbo-16k-0613'
        base_provider: str = 'openai'
        #best_provider: Provider.Provider = Provider.Easychat
        best_provider: Provider.Provider = Provider.Zeabur
        best_providers: list = [Provider.Zeabur]

    class gpt_35_turbo_16k:
        name: str = 'gpt-3.5-turbo-16k'
        base_provider: str = 'openai'
        best_provider: Provider.Provider = Provider.CharFree
        #best_provider: Provider.Provider = random.choice([Provider.Zeabur, Provider.Gravityengine])
        best_providers: list = [Provider.EasyChat, Provider.CharFree]

    #POE

    class gpt_35_turbo_poe:
        name: str = 'gpt-3.5-turbo-poe'
        base_provider: str = 'poe'
        best_provider: Provider.Provider = Provider.Chimera
        best_providers: list = [Provider.Chimera]

    class gpt_35_turbo_openai:
        name: str = 'gpt-3.5-turbo-openai'
        base_provider: str = 'openai'
        best_provider: Provider.Provider = Provider.Chimera
        best_providers: list = [Provider.Chimera]

    class gpt_35_turbo_16k_openai:
        name: str = 'gpt-3.5-turbo-16k-openai'
        base_provider: str = 'openai'
        best_provider: Provider.Provider = Provider.Chimera
        best_providers: list = [Provider.Chimera]

    class gpt_35_turbo_16k_poe:
        name: str = 'gpt-3.5-turbo-16k-poe'
        base_provider: str = 'poe'
        best_provider: Provider.Provider = Provider.Chimera
        best_providers: list = [Provider.Chimera]

    class gpt_4:
        name: str = 'gpt-4'
        base_provider: str = 'openai'
        best_provider: Provider.Provider = Provider.Chimera
        best_providers: list = [Provider.Chimera]
        
    class gpt_4_standart:
        name: str = 'gpt-4-standart'
        base_provider: str = 'openai'
        best_provider: Provider.Provider = Provider.DfeHub
        best_providers: list = [Provider.DfeHub]
    
    class gpt_4_0613:
        name: str = 'gpt-4-0613'
        base_provider: str = 'openai'
        best_provider: Provider.Provider = Provider.Chimera
        best_providers: list = [Provider.Chimera]

    class gpt_4_poe:
        name: str = 'gpt-4-poe'
        base_provider: str = 'poe'
        best_provider: Provider.Provider = Provider.Chimera
        best_providers: list = [Provider.Chimera]

    class gpt_4_32k:
        name: str = 'gpt-4-32k'
        base_provider: str = 'reversed'
        best_provider: Provider.Provider = Provider.Chimera
        best_providers: list = [Provider.Chimera]

    class gpt_4_32k_poe:
        name: str = 'gpt-4-32k-poe'
        base_provider: str = 'poe'
        best_provider: Provider.Provider = Provider.Chimera
        best_providers: list = [Provider.Chimera]

    class claude_instant_100k:
        name: str = 'claude-instant-100k'
        base_provider: str = 'anthropic'
        best_provider: Provider.Provider = Provider.Chimera
        best_providers: list = [Provider.Chimera]

    class claude_instant:
        name: str = 'claude-instant'
        base_provider: str = 'anthropic'
        best_provider: Provider.Provider = Provider.Chimera
        best_providers: list = [Provider.Chimera]

    class claude_2_100k:
        name: str = 'claude-2-100k'
        base_provider: str = 'anthropic'
        best_provider: Provider.Provider = Provider.Chimera
        best_providers: list = [Provider.Chimera]

    class claude_2:
        name: str = 'claude-2'
        base_provider: str = 'anthropic'
        best_provider: Provider.Provider = Provider.ClaudeAI

    class sage:
        name: str = 'sage'
        base_provider: str = 'poe'
        best_provider: Provider.Provider = Provider.Chimera
        best_providers: list = [Provider.Chimera]

    class claude_instant_v1:
        name: str = 'claude-instant-v1'
        base_provider: str = 'anthropic'
        best_provider: Provider.Provider = Provider.Vercel

    class claude_v1_100k:
        name: str = 'claude-v1-100k'
        base_provider: str = 'anthropic'
        best_provider: Provider.Provider = Provider.Vercel

    class claude_v1:
        name: str = 'claude-v1'
        base_provider: str = 'anthropic'
        best_provider: Provider.Provider = Provider.Vercel

    class code_cushman_001:
        name: str = 'code-cushman-001'
        base_provider: str = 'openai'
        best_provider: Provider.Provider = Provider.Vercel

    class code_davinci_002:
        name: str = 'code-davinci-002'
        base_provider: str = 'openai'
        best_provider: Provider.Provider = Provider.Vercel

    class text_ada_001:
        name: str = 'text-ada-001'
        base_provider: str = 'openai'
        best_provider: Provider.Provider = Provider.Vercel

    class text_babbage_001:
        name: str = 'text-babbage-001'
        base_provider: str = 'openai'
        best_provider: Provider.Provider = Provider.Vercel

    class text_curie_001:
        name: str = 'text-curie-001'
        base_provider: str = 'openai'
        best_provider: Provider.Provider = Provider.Vercel

    class text_davinci_002:
        name: str = 'text-davinci-002'
        base_provider: str = 'openai'
        best_provider: Provider.Provider = Provider.Vercel

    class text_davinci_003:
        name: str = 'text-davinci-003'
        base_provider: str = 'openai'
        best_provider: Provider.Provider = Provider.Vercel

    class ada:
        name: str = 'ada'
        base_provider: str = 'openai'
        best_provider: Provider.Provider = Provider.PurGPT
        
    class palm:
        name: str = 'palm2'
        base_provider: str = 'google'
        best_provider: Provider.Provider = Provider.Bard
        
    class llama_13b:
        name: str = 'llama-13b'
        base_provider: str = 'huggingface'
        best_provider: Provider.Provider = Provider.H2o

    class llama_2_70b_chat:
        name: str = 'llama-2-70b-chat'
        base_provider: str = 'huggingface'
        best_provider: Provider.Provider = Provider.Chimera
    class bing:
        name: str = 'bing'
        base_provider: str = 'openai'
        best_provider: Provider.Provider = Provider.BingHuan
    
class ModelUtils:
    convert: dict = {
        'gpt-3.5-turbo': Model.gpt_35_turbo,
        'gpt-3.5-turbo-0613': Model.gpt_35_turbo_0613,
        'gpt-4': Model.gpt_4,
        'gpt-4-standart': Model.gpt_4_standart,
        'gpt-4-0613': Model.gpt_4_0613,
        'gpt-3.5-turbo-16k': Model.gpt_35_turbo_16k,
        'gpt-3.5-turbo-16k-0613': Model.gpt_35_turbo_16k_0613,

        #POE
        'gpt-3.5-turbo-poe': Model.gpt_35_turbo_poe,
        'gpt-3.5-turbo-openai': Model.gpt_35_turbo_openai,
        'gpt-3.5-turbo-16k-openai': Model.gpt_35_turbo_16k_openai,
        'gpt-3.5-turbo-16k-poe': Model.gpt_35_turbo_16k_poe,
        'gpt-4-poe': Model.gpt_4_poe,
        'gpt-4-32k': Model.gpt_4_32k,
        'gpt-4-32k-poe': Model.gpt_4_32k_poe,

        'claude-instant-100k': Model.claude_instant_100k,
        'claude-instant': Model.claude_instant,
        'claude-2-100k': Model.claude_2_100k,
        
        'claude-2': Model.claude_2,

        'claude-v1-100k': Model.claude_v1_100k,
        'claude-instant-v1': Model.claude_instant_v1,
        'claude-v1': Model.claude_v1,

        'sage': Model.sage,
        
        'code-cushman-001': Model.code_cushman_001,
        'code-davinci-002': Model.code_davinci_002,
        
        'text-ada-001': Model.text_ada_001,
        'text-babbage-001': Model.text_babbage_001,
        'text-curie-001': Model.text_curie_001,
        'text-davinci-002': Model.text_davinci_002,
        'text-davinci-003': Model.text_davinci_003,

        'ada': Model.ada,
        
        'palm2': Model.palm,
        'palm': Model.palm,
        'google': Model.palm,
        'google-bard': Model.palm,
        'google-palm': Model.palm,
        'bard': Model.palm,
        
        'llama-13b': Model.llama_13b,
        'llama-2-70b-chat': Model.llama_2_70b_chat,
        'bing': Model.bing,
    }
