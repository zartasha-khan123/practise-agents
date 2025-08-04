#------------------------------------ this class use for making a simple agent 
import random

from agents import function_tool
from pydantic import BaseModel, Field


class ToolInfo(BaseModel):
    token_number:str = Field(description="This takes the token number..")
    wait_time: str = Field(description="This takes wait time...")
    message:str = Field(description="This takes message...")    
    service_type : str =Field(description=" This takes service type...")

#--------------------- this is class for tool info-----------------
class ServiceType(BaseModel):
    service:str
    confidence:float
    keyword_detected:list[str]
    reasoning:str


#----------------------------------------------
@function_tool
def identity_customer_purpose(customer_request:str):
    """ it is simple function to return the customer purpose """
    
    
    request = customer_request.lower()
    
    if ("balance" in request) or ("account" in request) or ("statements" in request) or ("creditCard"in request) or ("Users-current/saving account" in request):
        return ServiceType(
            service="account_service",
            confidence=0.7,
            keyword_detected=["balance","account", "statements"],
            reasoning="Customer want to check their account"            
        )
    
    elif ("transfer" in request) or ("send" in request) or ("payment" in request):
        return ServiceType(
            service="transfer_service",
            confidence=0.7,
            keyword_detected=["transfer", "send","payment"],
            reasoning="Customer wants to send money or make payments"            
        )
    elif ("loan" in request) or ("mortgage" in request) or ("borrow" in request):
        return ServiceType(
            service="loan_service",
            confidence=0.7,
            keyword_detected=["loan", "mortgage", "borrow"],
            reasoning="Customer needs help with loan"            
        )
        
        
    else:
         return ServiceType(
            service="general_banking",
            confidence=0.5,
            keyword_detected=["general", "fees", "charges", "billing"],
            reasoning="Customer needs general banking help ..."            
        )
           
#------------------------------------
@function_tool
def generate_customer_token(service_type:str = "general") -> ToolInfo:
    # Generate a random customer token
    """ Generate a random customer token the value of the service_type argument can be only these..
    
    args:
    service_type = "general"
    service_type = "account_service"
    service_type = "transfer_service"
    service_type = "loan_service"

    """
    if service_type == "account_service":
        prefix="A"
        wait_time = "5-10 minutes"
    elif service_type == "transfer_service":
        prefix="T"
        wait_time = "5- 4 minutes"
    elif service_type == "loan_service":
        prefix="L"
        wait_time = "15-20 minutes"
        
    else:
        prefix = "G"
        wait_time = "8-10 minutes"             
       
    token_number= f"{prefix}{random.randint(100,999)}"    
    
    return ToolInfo(
       token_number = token_number,
       wait_time= wait_time,
       message=f"please take {wait_time} to process your {service_type} request and {token_number} is your token number , have a seat and wait for your turn",
       service_type=service_type 
    )

    
