# TextToSpeech-Agent-Tutorial

This tutorial guides you through setting up and running a Text-to-Speech conversion project using LangChain and OpenAI's GPT models, enhanced with a tool for converting text into speech files. This project is designed to create an agent that not only generates creative content (like children's stories) but also converts this content into an audio format, making it accessible in a variety of applications, including educational and entertainment products.

## Prerequisites

Before you dive into this tutorial, ensure you have the following setup ready:

* Python 3 installed on your system.

## Installing and Running the Project

Follow these steps to get your Text-to-Speech project up and running:

### Environment Setup

1. **Prepare your environment**

   Start by setting up a suitable Python environment for your project. This can involve creating a virtual environment if you prefer to manage dependencies in an isolated manner.

2. **Acquire the project code**

    Clone the repository containing the essential project files. This repository is hypothetical and serves as an example for this tutorial:
    
    ```bash
    git clone https://github.com/yourrepository/TextToSpeech-Agent-Tutorial.git
    cd TextToSpeech-Agent-Tutorial
    ```

3. **Install required packages**

    Install the necessary Python packages listed in the `requirements.txt` file. These packages include LangChain, gTTS for text-to-speech conversion, and any other dependencies your project might need.
    
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

Execute the application with the following steps:

1. **Set your OpenAI API key**

   Before running the application, you need to set your OpenAI API key as an environment variable. Replace `<OPENAI_API_KEY>` with your actual API key.

    ```bash
    export OPENAI_API_KEY=<OPENAI_API_KEY>
    ```

    If you're using Windows, use the `set` command instead:

    ```cmd
    set OPENAI_API_KEY=<OPENAI_API_KEY>
    ```

2. **Run the Text-to-Speech application**

    With all setup complete, you can now run the application. This script will invoke the agent to generate content based on a given prompt and then convert the generated text into speech, saving it as a file.

    ```bash
    python your_script_name.py
    ```

    Replace `your_script_name.py` with the actual script file name that contains the code for invoking the agent and converting text to speech.

## Conclusion

This tutorial walks you through setting up a LangChain and OpenAI GPT-based agent for generating content and converting it to speech. The project showcases the integration of AI-generated content with text-to-speech technology, offering a broad range of applications from storytelling to educational tools.