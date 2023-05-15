# bAIdyChat

This is an AI Chatbot by baidy

___The chats folder should be empty. I left two jsons as examples which I used in description on how my project works.___

## Installation:
* Run command "pip install -r requirements.txt"
* Create OpenAI API Key
* Create a configuration to run chatbot and add to the run configuration OPENAI_API_KEY env variable:
![Creating an env variable](https://res.cloudinary.com/dbtmzypoa/image/upload/v1683846970/AI%20Chat%20screenshots/q8pr2fysdf1x8ed2qvba.png)
* Run the program!

## Let's create a new conversation
![Creating a new conversation](https://res.cloudinary.com/dbtmzypoa/image/upload/v1684146416/AI%20Chat%20screenshots/l0pobpzvkxcd7hqubay2.png)

## Let's retrieve the previous conversation context
![Retrieving previous conversations](https://res.cloudinary.com/dbtmzypoa/image/upload/v1684146416/AI%20Chat%20screenshots/h9wc2xxdihrhyisxibwu.png)

## Chatbot can also handle huge conversations which exceed token limitations of LLM (web_frameworks.json conversation is much longer than 4k tokens)
![Working with huge conversations](https://res.cloudinary.com/dbtmzypoa/image/upload/v1684147601/AI%20Chat%20screenshots/deph0q3yz84kts56kqai.png)