from mcp import ClientSession , StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
import asyncio
import os
load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-exp",
    temperature=0,
    google_api_key=os.environ.get("GEMINI_API_KEY")
)

server_parameters = StdioServerParameters(
    command="npx",
    args=["firecrawl-mcp"],
    env= {
        "FIRECRAWL_API_KEY" : os.getenv("FIRECRAWL_API_KEY"),
    },
)

async def get_input():
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, input, "\nUser Input : ")

async def main():
    async with stdio_client(server_parameters) as (read,write) :
        async with ClientSession(read , write) as session :
            await session.initialize()
            tools = await load_mcp_tools(session)
            agent = create_react_agent(model,tools)

            messages = [
                SystemMessage(content="You're a smart and reliable assistant that can scrape websites, crawl through multiple pages, and extract structured or unstructured data using Firecrawl tools. You understand how to navigate links, follow sitemaps, and handle dynamic content when needed. Think through each step carefully: identify what the user wants, decide which pages or domains to access, choose the right Firecrawl function, and collect the data in a clean and usable format. Be thorough, avoid redundant requests, and always aim to give the user exactly what they're looking for with as little friction as possible.")

            print("Available Tools - " , *[tool.name for tool in tools])
            print("-"*60)

            while True:
                user_input = await get_input()
                if user_input == "quit":
                    print("Exiting...")
                    break
                messages.append(HumanMessage(content=user_input[:10000]))

                try :
                    agent_response = await agent.ainvoke({"messages" : messages})
                    ai_message = agent_response["messages"][-1]
                    print("\nAgent : ", ai_message.content)
                    messages.append(ai_message)
                except Exception as e :
                    print("Error Occurred : ",e)
                    

if __name__ == "__main__":
    asyncio.run(main())
    
