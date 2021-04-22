import boto3
from botocore.config import Config
import json
from fake_web_events import Simulation

my_config = Config(
    region_name = 'us-east-1'
)

client = boto3.client("firehose" , config=my_config)

def put_record(event):
    data = json.dumps(event) + "\n"
    response = client.put_record(
        DeliveryStreamName="firehose-develop-raw-delivery-stream",
        Record={"Data": data},
    )
    print(event)
    return response


simulation = Simulation(user_pool_size=100, sessions_per_day=1000)
events = simulation.run(duration_seconds=10000)

for event in events:
    put_record(event)
