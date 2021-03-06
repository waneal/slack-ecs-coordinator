import os
import logging
logging.basicConfig(level=logging.INFO)

import boto3 
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

REGION = os.environ["AWS_DEFAULT_REGION"]

# Initialize boto3
ecs = boto3.client("ecs")
app_as= boto3.client("application-autoscaling")

# Install the Slack app and get xoxb- token in advance
app = App(token=os.environ["SLACK_BOT_TOKEN"])

# Add functionality here
@app.event("app_mention")
def handle_mention(body, say, logger):
    logger.info(body)
    say("hello")

@app.command("/list-services")
def handle_action_list_services(ack, body, say, logger):
    logger.info(body)
    ack()
    say("You typed {cluster}".format(cluster=body["text"]))

if __name__ == "__main__":
    # Create an app-level token with connections:write scope
    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    handler.start()