from python_graphql_client import GraphqlClient

client = GraphqlClient(endpoint='http://web-url.com:8080/v1/graphql')

query = """
    query MyQuery {
        projects {
            id
        }
    }
"""

result = client.execute(query)
print(result)