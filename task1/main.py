from openai import OpenAI

client = OpenAI(
    api_key="sk-T6SlqfUnyFytejvA3c1584F87d6343878232185e26243b1d",
    base_url="https://api.apiyi.com/v1",
)

query = input("输入指令: ")

messages = [
    {
        "role": "system", 
        "content": "你是一个 kubernetes 专家，你可以调用多个函数来帮助用户完成任务"
    },
    {
        "role": "user", 
        "content": query
    },
]

tools = [
    {
        "type": "function",
        "function": {
            "name": "modify_config",
            "description": "修改服务配置",
            "parameters": {
                "type": "object",
                "properties": {
                    "service_name": {
                        "type": "string",
                        "description": "修改的服务名称",
                    },
                    "key": {
                        "type": "string",
                        "description": "服务要修改的键",
                    },
                    "value": {
                        "type": "string",
                        "description": "服务要修改的键的值",
                    },
                },
                "required": ["service_name", "key", "value"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "restart_service",
            "description": "重启服务",
            "parameters": {
                "type": "object",
                "properties": {
                    "service_name": {
                        "type": "string",
                        "description": "修改的服务名称",
                    },
                },
                "required": ["service_name"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "apply_manifest",
            "description": "部署一个资源",
            "parameters": {
                "type": "object",
                "properties": {
                    "resource_type": {
                        "type": "string",
                        "description": "部署的资源名称",
                    },
                    "image": {
                        "type": "string",
                        "description": "部署的资源镜像",
                    },
                },
                "required": ["resource_type", "image"]
            }
        }
    }
 ]

reponse = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    tools=tools,
    tool_choice="auto",
)

response_message = reponse.choices[0].message
tool_calls = response_message.tool_calls

print("\nChatGPT want to call function: ", tool_calls)