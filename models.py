from pydantic import BaseModel


class Request(BaseModel):
    pub_name: str
    queue_name: str
    data: str
    
class Response(BaseModel):
    sub_name: str
    queue_name: str