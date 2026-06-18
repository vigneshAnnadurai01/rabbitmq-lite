from shared.schemas import UserRequest

class MCPRouter:
    def route (self, query:str):
        query = query.lower()
        
        if "account" in query:
            return"account"
        if "bill" in query or "payment" in query:
            return "billing"
        if "support" in query or "issue" in query:
            return "support"
        if "document" in query or "pdf" in query :
            return  "document"
        return"support"
