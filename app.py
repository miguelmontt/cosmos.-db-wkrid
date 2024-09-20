
from azure.identity import ManagedIdentityCredential
from azure.cosmos import CosmosClient

# Use ManagedIdentityCredential with the correct audience for Cosmos DB
credential = ManagedIdentityCredential()

# Cosmos DB endpoint
cosmos_url = "https://workloadidentity-poc.documents.azure.com:443/"

# Pass the correct resource (audience) to the CosmosClient
client = CosmosClient(cosmos_url, credential=credential, consistency_level='Session')

# Access database and container
database_name = 'ToDoList'
container_name = 'Items'

# Get the database client
database = client.get_database_client(database_name)
# Get the container client
container = database.get_container_client(container_name)

# Querying documents from the container
for item in container.query_items(
        query="SELECT * FROM c WHERE c.id='some-id'",
        enable_cross_partition_query=True):
    print(item)
