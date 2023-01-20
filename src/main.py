import base64
from google.cloud import container_v1
import json

def pubsub_trigger(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    #{
    #   "project_id": "luegnix",
    #   "cluster_id": "luegnix-gke",
    #   "name": "small-burst-on-demand",
    #   "node_count": 0,
    
    #}
    #print(pubsub_message)
    print(event)
    client = container_v1.ClusterManagerClient()

    # Initialize request argument(s)
   #name (str):
   #        The name (project, location, cluster, node pool id) of the
   #        node pool to set size. Specified in the format
   #        ``projects/*/locations/*/clusters/*/nodePools/*``.

    data_dict = json.loads(pubsub_message)
    node_count = data_dict['node_count']
    project_id = data_dict['project_id']
    location = data_dict['location']
    cluster_id = data_dict['cluster_id']
    node_pool_id = data_dict['node_pool_id']
    request = container_v1.SetNodePoolSizeRequest(
        node_count=node_count,
        name = f"projects/{project_id}/locations/{location}/clusters/{cluster_id}/nodePools/{node_pool_id}",
        #        projects/*/locations/*/clusters/*/nodePools/*
    )


    # Make the request
    response = client.set_node_pool_size(request=request)

    # Handle the response
    print(response) 
