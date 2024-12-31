# Q&A ChatBot with LLaMA 3.2

This project is a custom-built Q&A chatbot that utilizes the LLaMA 3.2 large language model for generating insightful responses to user queries. The chatbot is developed using Streamlit, Langchain, and Ollama libraries to create an interactive user interface. It features an elegant and intuitive layout with custom styling to enhance the user experience.

## Features

- **Interactive Chatbot**: Users can ask any query, and the chatbot provides instant responses powered by LLaMA 3.2.
- **Streamlit Interface**: Streamlit is used to create a responsive and user-friendly UI for seamless interactions.
- **Customizable Styling**: The page is styled with a darker light theme, along with a chat interface that provides a comfortable and aesthetically pleasing experience.
- **Live Query Input**: Users can input their queries and receive real-time answers from the LLaMA model.

## Technologies Used

- **LLaMA 3.2**: The core language model powering the chatbot.
- **Streamlit**: Framework used for building the interactive web application.
- **Langchain**: For constructing custom prompts and parsing responses.
- **Ollama**: Library for interfacing with LLaMA and other models.

## Setup Instructions

- Install the necessary libraries by running:
   ```bash
   - pip install streamlit langchain olama python-dotenv

- Generate Your OWN api key and store it as LANGCHAIN_API_KEY=<Your_API_Key>
- Perform the Pipe lines in app.py for open ai api key , or ollama.py which will be free of cost
- streamlit run app.py

