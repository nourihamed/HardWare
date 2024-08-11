import graphene
from Equipment import queries , mutations


schema = graphene.Schema(query=queries.Query , mutation=mutations.Mutation)
