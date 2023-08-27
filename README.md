# SMU Libraries GPT
SMU Libraries GPT is a web-based application that can be deployed using Streamlit (currently not publicly deployed due to keeping the API key a secret) that takes in user prompts and uses LangChain with OpenAI to generate answers.

## Features
- <b>Intelligent Recommendation:</b> Users can describe their interests or conditions to receive a more personalised answer.
- <b>Q&A Search Enginge:</b> Based on our dataset, the chatbot can provide direct answers to FAQ.

## Deployment
To deploy the project locally, make sure to:
- Put your own OpenAI API key in the constants.py file
- Download and open the project folder, then type 'streamlit run app.py' in the terminal
- Open [http://localhost:8501](http://localhost:8501) using your browser to see the project
- Simply input your prompts in the text box to receive an answer!