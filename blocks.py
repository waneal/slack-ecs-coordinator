def create_url_service_detail(region, cluster, service) -> str:
    return f"https://{region}.console.aws.amazon.com/ecs/home?region={region}#/clusters/{cluster}/services/{service}/tasks"

def create_block_service_status(region, cluster, service, auto_scaling: str, desired_count, min_capacity, max_capacity: int) -> dict:
    return {
        "type": "section",
		"fields": [
			{
				"type": "mrkdwn",
				"text": f"*Name:*\n<{create_url_service_detail(region=region, cluster=cluster, service=service)}|{service}>"
			},
			{
				"type": "mrkdwn",
				"text": " "
			},
			{
				"type": "mrkdwn",
				"text": f"*Desired Count:*\n`{desired_count}`"
			},
			{
				"type": "mrkdwn",
				"text": f"*Auto Scaling:*\n`{auto_scaling}`"
			},
			{
				"type": "mrkdwn",
				"text": f"*Min Capacity:*\n`{min_capacity}`"
			},
			{
				"type": "mrkdwn",
				"text": f"*Max Capacity:*\n`{max_capacity}`"
			}
		]
    }
