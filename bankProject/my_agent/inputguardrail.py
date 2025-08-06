from agents import Agent, GuardrailFunctionOutput, RunContextWrapper, Runner, TResponseInputItem, input_guardrail
from pydantic import BaseModel, Field

#-------- class of quardrail function output-------------

class CheckSlangClass(BaseModel):
    is_slang : bool = Field(description="Value will be true if user slang is detected")
    resoning : str = Field(description=" This takes the reasoning and the keyword detected...")


#-------quardrail agent for function quardrails---------------
quardrailAgent= Agent(
    name="quardrailAgent",
    instructions="This is a quardrail agent... always check slangs if user is asking for something bad in the chat ...",
    model="gpt-4.1-mini",
    output_type=CheckSlangClass
)


#------------------------------------------ decorator of function quardrail-------------------
@input_guardrail
async def check_slangs (ctx:RunContextWrapper, agent:Agent, input:str | list[TResponseInputItem])-> GuardrailFunctionOutput:
    res = await Runner.run(quardrailAgent , input , context=ctx)
    
    return GuardrailFunctionOutput(
        output_info=res.final_output,
        tripwire_triggered=res.final_output.is_slang
    )
