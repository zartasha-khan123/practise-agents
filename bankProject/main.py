from agents import Agent, InputGuardrailTripwireTriggered, OutputGuardrailTripwireTriggered , Runner 
from dotenv import load_dotenv
from outputGuardrail import quardrails_output
from inputguardrail import check_slangs
from my_tools import generate_customer_token, identity_customer_purpose
from handoffs import account_agent , transfer_agent , loan_agent
import rich

#------------------------------------

load_dotenv()
# enable_verbose_stdout_logging()


#-------------------------------------


agent = Agent(
    name="bank_Greeting_agent",
    instructions=
    """
     you are a friendly bank greeting agent. 
     1- welcome customer nicely.
     2- always use generate_customer_token tool to generate a token number for the customer.
     3- use check_banking_purpose to understand user needs.
     4- if confidence > 0.8, sen user to the right specialist.
     5- for example ......
     args:
    service_type = "general"
    service_type = "account_service"
    service_type = "transfer_service"
    service_type = "loan_service"
    6-if user is asking about other than , transfer , loan , account , then use the following response , please contact our customer service for more information.
     Always me helpful
    
    """,
    handoffs=[account_agent,transfer_agent,loan_agent],
    tools=[generate_customer_token,identity_customer_purpose],
    input_guardrails=[check_slangs],
    output_guardrails=[quardrails_output]
)

# main.py
import asyncio
from agents import Agent, InputGuardrailTripwireTriggered, OutputGuardrailTripwireTriggered, Runner
from dotenv import load_dotenv
from outputGuardrail import quardrails_output
from inputguardrail import check_slangs
from my_tools import generate_customer_token, identity_customer_purpose
from handoffs import account_agent, transfer_agent, loan_agent

load_dotenv()

# Initialize agent
agent = Agent(
    name="bank_Greeting_agent",
    instructions="""
     You are a friendly bank greeting agent. 
     1- Welcome the customer nicely.
     2- Always use generate_customer_token tool to generate a token number for the customer.
     3- Use check_banking_purpose to understand user needs.
     4- If confidence > 0.8, send user to the right specialist.
     5- For example...
     service_type = "general" | "account_service" | "transfer_service" | "loan_service"
     6- If the user asks something else, respond: "Please contact our customer service for more information."
    """,
    handoffs=[account_agent, transfer_agent, loan_agent],
    tools=[generate_customer_token, identity_customer_purpose],
    input_guardrails=[check_slangs],
    output_guardrails=[quardrails_output]
)

def run_my_agent(user_input: str) -> str:
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        result = loop.run_until_complete(Runner.run(agent, user_input))
        return result.final_output

    except InputGuardrailTripwireTriggered as e:
        return f"❌ Input Issue: {str(e)}"

    except OutputGuardrailTripwireTriggered as e:
        return f"❌ Output Issue: {str(e)}"

    except Exception as e:
        return f"⚠️ Unexpected error: {str(e)}"

# while True:
#  try:
#     user_input = input("Welcome to the bank assistant. How can I help you today?\n ... > enter your question here...")
#     if user_input.lower() in ['quit','exit']:
#      break
#     result=Runner.run_sync( agent,user_input)
#     rich.print( result.final_output )
 
#  except InputGuardrailTripwireTriggered as e :
#     rich.print(f" ❌Input Guardrail Tripwire Triggered:",e)
    
#  except OutputGuardrailTripwireTriggered as e:
#      rich.print(f"❌Output Guardrail Tripwire Triggered" ,e )  
    

