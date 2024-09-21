export AZURE_OPENAI_ENDPOINT=******

export AZURE_OPENAI_API_KEY=******

export AZURE_DEPLOYMENT=******

```
python3 main.py

Query:  帮我修改 gateway 的配置，vendor 修改为 alipay

ChatGPT want to call function:  [ChatCompletionMessageToolCall(id='call_zKdBUNj1NAaGWQ0VyJmEYWKd', function=Function(arguments='{"service_name":"gateway","key":"vendor","value":"alipay"}', name='modify_config'), type='function')]


Query:  帮我重启 gateway 服务

ChatGPT want to call function:  [ChatCompletionMessageToolCall(id='call_T3JF7BkjHEnZXAhEHxDhpX87', function=Function(arguments='{"service_name":"gateway"}', name='restart_service'), type='function')]


Query:  帮我部署一个 deployment，镜像是 nginx

ChatGPT want to call function:  [ChatCompletionMessageToolCall(id='call_QbUdUjBGKs8HuIoldbQa7gpT', function=Function(arguments='{"resource_type":"deployment","image":"nginx"}', name='apply_manifest'), type='function')]


Query:  帮我介绍一个Jenkins

ChatGPT want to call function:  None       
```

