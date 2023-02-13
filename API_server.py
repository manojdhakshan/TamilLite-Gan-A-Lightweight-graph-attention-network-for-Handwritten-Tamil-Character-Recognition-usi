from flask import Flask, request
from flask_graphql import GraphQLView
import graphene

app = Flask(__name__)

class Branch(graphene.ObjectType):
    branch = graphene.String()
    bank = graphene.Field(lambda: Bank)
    ifsc = graphene.String()

class Bank(graphene.ObjectType):
    name = graphene.String()

class Query(graphene.ObjectType):
    branches = graphene.List(Branch)

    def resolve_branches(self, info):
        # Code to retrieve branches data from the database and return it
        # as a list of Branch objects goes here.
        pass

schema = graphene.Schema(query=Query)

app.add_url_rule('/gql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    app.run()
