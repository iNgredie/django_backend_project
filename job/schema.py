import graphene
from graphene_django import DjangoObjectType

from job.models import Occupation


class OccupationType(DjangoObjectType):
    class Meta:
        model = Occupation
        fields = '__all__'


class Query(graphene.ObjectType):
    occupation = graphene.Field(OccupationType, id=graphene.Int())

    def get_occupation(self, info, **kwargs):
        id = kwargs.get('id')
        return Occupation.objects.get(pk=id)

    def get_occupations(self, info, **kwargs):
        return Occupation.objects.all()



schema = graphene.Schema(query=Query)