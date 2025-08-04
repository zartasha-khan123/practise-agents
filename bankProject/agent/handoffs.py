
from agents import Agent

from bankProject.agent.outputGuardrail import  quardrails_output


account_agent = Agent(
    name="bank_account_agent",
    instructions="You are a helpfull bank agent.you help user in their query of account balance, statements, and account information, Always use the `generate_customer_token` tool with service_type='account_service'. always generate a token.",
    model="gpt-4.1-mini",
    output_guardrails=[quardrails_output]

)


#---------------------------------------------

transfer_agent= Agent(
    name="bank_transfer_agent",
    instructions=" You are a bank transfer agent. You will assist the customer with their bank transfer needs, Always use the `generate_customer_token` tool with service_type='transfer_service'. , always generate a token.",
    model="gpt-4.1-mini",
    output_guardrails=[quardrails_output]

)

#-----------------------------------------------

loan_agent= Agent(
    name="bank_loan_agent",
    instructions=" You are a bank loan agent. You will assist the customer with their loan needs, Always use the `generate_customer_token` tool with service_type='loan_service',always generate a token.",
    model="gpt-4.1-mini",
    output_guardrails=[quardrails_output]
)