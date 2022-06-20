from fastapi import FastAPI
import uvicorn
from collections import defaultdict
import json
from models import Request,Response
from queues import Node, LinkedList


app = FastAPI()

def deffunc():
    return LinkedList()


queue_subs = {}

queue_data = defaultdict(deffunc)



@app.post("/pub/")
async def publisher_queue(data: Request):

    node = Node(data.data)
    ll = queue_data[data.queue_name]
    if ll.head is None:
        ll.head = node
    else:
        nw = ll.last_node()
        nw.next = node
    
    return json.dumps({"Response":"SUCESS"})


@app.post("/sub/")
async def subscriber_queue(response: Response):
    res = []

    if response.queue_name in queue_data.keys():
        if response.sub_name not in queue_subs.keys() or response.queue_name not in queue_subs[response.sub_name].keys():
            queue_hd = queue_data[response.queue_name].head
            queue_subs[response.sub_name] = {}
        else:
            queue_hd = queue_subs[response.sub_name][response.queue_name].next
    else:
        return json.dumps({"Response":"queue not present"})
              

    while True:

        if queue_hd is None:
            break
        else:
            queue_subs[response.sub_name][response.queue_name] = queue_hd
            res.append(queue_hd.data)
            queue_hd = queue_hd.next

    return json.dumps({"Response":"SUCESS","data" : res})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

 