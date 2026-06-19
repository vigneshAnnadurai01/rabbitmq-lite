from pydantic import BaseModel
from typing import Optional
import uuid


class UserRequest(BaseModel):
    query : str
    
    
class EventMessage(BaseModel):
    event_id:str
    agent_type:str
    query :str
    
    @classmethod
    def create(cls,agent_type,query):
                
        
        
        
        return cls(
            
            event_id = str(uuid.uuid4()),
            agent_type = agent_type,
            query = query
        ) 
        
