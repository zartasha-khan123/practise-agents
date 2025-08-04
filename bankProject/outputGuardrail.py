from agents import Agent, GuardrailFunctionOutput, RunContextWrapper, Runner , output_guardrail
from pydantic import BaseModel, Field
from typing import Any


class QuardrailOutputCheck(BaseModel):
    is_related:bool = Field(description="Set to True if NOT related to banking")
    reasoning:str =Field(description=" reasoning for the output")
    
guardrailOutputagent = Agent(
    name="guardrail_outputs",
    instructions="""
    
    You are a strict guardrail. Your job is to check if the following text is related to banking services like accounts, transfers, or loans.

    If the text is **NOT related**, set `is_related` = True.

    If the text **is related to banking**, set `is_related` = False.

    Also give a brief explanation in the `reasoning` field.
""",
    model="gpt-4.1-mini",
    output_type=QuardrailOutputCheck
)    

@output_guardrail
async def quardrails_output(ctx:RunContextWrapper ,agent:Agent ,output:Any)-> GuardrailFunctionOutput:
    res = await Runner.run(guardrailOutputagent, output, context=ctx)
    
    
    return GuardrailFunctionOutput(
        output_info=res.final_output , 
        tripwire_triggered=res.final_output.is_related
    )    