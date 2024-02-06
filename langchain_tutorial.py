
from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import  tool
import os
from langchain.agents import  create_openai_tools_agent, AgentExecutor
from langchain_openai import ChatOpenAI
from langchain import hub
from gtts import gTTS 

class TextToSpeech(BaseModel):
    text: str = Field(description="The text to convert to speech")
    filename: str = Field(description="The name of the file to save the speech to.")

@tool("text-to-speech", args_schema=TextToSpeech)
def text_to_speech(text: str, filename: str) -> None:
    """Converts text to speech using Google Text-to-Speech API and saves it to a file."""
    language = 'en'
    myobj = gTTS(text=text, lang=language, slow=False) 
    myobj.save(filename) 
    



    
os.environ["OPENAI_API_KEY"] = "<OPENAI_API_KEY>"

llm=ChatOpenAI(model_name="gpt-3.5-turbo-1106", temperature=0.7)
prompt = hub.pull("hwchase17/openai-tools-agent")

tools = [text_to_speech]
agent = create_openai_tools_agent(llm, tools, prompt)

agent_executor = AgentExecutor(agent= agent, tools=tools, verbose=True)

result = agent_executor.invoke({"input": "Write a children's story about a dragon and convert it to speech."})
 

print(result["output"])
