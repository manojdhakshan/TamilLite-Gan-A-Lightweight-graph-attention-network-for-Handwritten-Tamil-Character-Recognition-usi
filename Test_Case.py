import requests
import json

def test_graphql_query():
    query = """
    query {
        branches {
            edges {
                node {
                    branch
                    bank {
                        name
                    }
                    ifsc
                }
            }
        }
    }
    """

    response = requests.post("http://localhost:5000/gql", json={'query': query})
    content = json.loads(response.content)

    assert response.status_code == 200
    assert 'data' in content
    assert 'branches' in content['data']
    assert len(content['data']['branches']['edges']) > 0

    for branch in content['data']['branches']['edges']:
        assert 'node' in branch
        assert 'branch' in branch['node']
        assert 'bank' in branch['node']
        assert 'name' in branch['node']['bank']
        assert 'ifsc' in branch['node']
