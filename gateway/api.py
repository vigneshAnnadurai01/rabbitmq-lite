# import sys
# import os

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# from fastapi import FastAPI
# import uvicorn
# from shared.schemas import UserRequest
# from shared.schemas  import EventMessage

# from router.mcp_router import MCPRouter
# from messaging.publisher import publish

# app = FastAPI()

# router = MCPRouter()

# @app.post("/query")
# def process_request(request: UserRequest):
    
#     agent = router.route(request.query)
    
#     event = EventMessage.create(
#         agent_type = agent,
#         query=request.query
#         )
    
#     queue_map = {
#         "account":"account_queue",
#         "billing":"billing_queue",
#         "support":"support_queue",
#         "document": "document_queue"
#     }
#     publish(
#         queue_map[agent],
#         event.model_dump()
#     )
#     return{
#         "status":"accepted",
#         "event_id":event.event_id,
#         "agent":agent   
#     }
    
    
# import uvicorn
# if __name__ == "__main__":
#     uvicorn.run("gateway.api:app", host="127.0.0.1", port=8001, reload=True)
    
import sys
import os

from fastapi import FastAPI, HTTPException
import uvicorn
import logging
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from shared.schemas import UserRequest, EventMessage
from router.mcp_router import MCPRouter
from messaging.publisher import publish

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("gateway")

app = FastAPI(
    title="Multi-Agent Gateway",
    version="1.0.0"
)

router = MCPRouter()

QUEUE_MAP = {
    "account": "account_queue",
    "billing": "billing_queue",
    "support": "support_queue",
    "document": "document_queue"
}


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "gateway"
    }


@app.post("/query")
def process_request(request: UserRequest):

    try:
        # Route request
        agent = router.route(request.query)

        if agent not in QUEUE_MAP:
            raise HTTPException(
                status_code=400,
                detail=f"Unknown agent: {agent}"
            )

        # Create event
        event = EventMessage.create(
            agent_type=agent,
            query=request.query
        )

        queue_name = QUEUE_MAP[agent]

        # Publish to RabbitMQ
        publish(
            queue_name,
            event.model_dump()
        )

        logger.info(
            f"Event published | Agent={agent} | Queue={queue_name} | Event={event.event_id}"
        )

        return {
            "status": "accepted",
            "event_id": event.event_id,
            "agent": agent,
            "queue": queue_name
        }

    except HTTPException:
        raise

    except Exception as e:
        logger.error(f"Gateway Error: {str(e)}")

        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )


if __name__ == "__main__":
    uvicorn.run(
        "gateway.api:app",
        host="127.0.0.1",
        port=8001,
        reload=True
    )