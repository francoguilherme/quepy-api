# coding: utf-8

# Copyright (c) 2012, Machinalis S.R.L.
# This file is part of quepy and is distributed under the Modified BSD License.
# You should have received a copy of license in the LICENSE file.
#
# Authors: Rafael Carrascosa <rcarrascosa@machinalis.com>
#          Gonzalo Garcia Berrotaran <ggarcia@machinalis.com>

"""
Domain specific language for DBpedia quepy.
"""

from quepy.dsl import FixedType, HasKeyword, FixedRelation, FixedDataRelation

# Setup the Keywords for this application
HasKeyword.relation = "rdfs:label"
HasKeyword.language = "en"


class IsPerson(FixedType):
    fixedtype = "foaf:Person"


class IsPlace(FixedType):
    fixedtype = "dbpedia:Place"


class IsCountry(FixedType):
    fixedtype = "dbo:Country"


class IsPopulatedPlace(FixedType):
    fixedtype = "dbo:PopulatedPlace"


class IsBand(FixedType):
    fixedtype = "dbo:Band"


class IsAlbum(FixedType):
    fixedtype = "dbo:Album"


class IsTvShow(FixedType):
    fixedtype = "dbo:TelevisionShow"


class IsMovie(FixedType):
    fixedtype = "dbo:Film"


class HasShowName(FixedDataRelation):
    relation = "rdfs:label"
    language = "en"


class HasName(FixedDataRelation):
    relation = "rdfs:label"
    language = "en"


class DefinitionOf(FixedRelation):
    relation = "rdfs:comment"
    reverse = True


class LabelOf(FixedRelation):
    relation = "rdfs:label"
    reverse = True


class UTCof(FixedRelation):
    relation = "dbp:utcOffset"
    reverse = True


class PresidentOf(FixedRelation):
    relation = "dbp:leaderTitle"
    reverse = True


class IncumbentOf(FixedRelation):
    relation = "dbp:incumbent"
    reverse = True


class CapitalOf(FixedRelation):
    relation = "dbo:capital"
    reverse = True


class LanguageOf(FixedRelation):
    relation = "dbp:officialLanguages"
    reverse = True


class PopulationOf(FixedRelation):
    relation = "dbp:populationCensus"
    reverse = True


class IsMemberOf(FixedRelation):
    relation = "dbo:bandMember"
    reverse = True


class ActiveYears(FixedRelation):
    relation = "dbp:yearsActive"
    reverse = True


class MusicGenreOf(FixedRelation):
    relation = "dbo:genre"
    reverse = True


class ProducedBy(FixedRelation):
    relation = "dbo:producer"


class BirthDateOf(FixedRelation):
    relation = "dbo:birthDate"
    reverse = True


class BirthPlaceOf(FixedRelation):
    relation = "dbo:birthPlace"
    reverse = True


class ReleaseDateOf(FixedRelation):
    relation = "dbo:releaseDate"
    reverse = True


class StarsIn(FixedRelation):
    relation = "dbp:starring"
    reverse = True


class NumberOfEpisodesIn(FixedRelation):
    relation = "dbo:numberOfEpisodes"
    reverse = True


class ShowNameOf(FixedRelation):
    relation = "dbp:showName"
    reverse = True


class HasActor(FixedRelation):
    relation = "dbp:starring"


class CreatorOf(FixedRelation):
    relation = "dbo:creator"
    reverse = True


class NameOf(FixedRelation):
    relation = "foaf:name"
    # relation = "dbp:name"
    reverse = True


class DirectedBy(FixedRelation):
    relation = "dbo:director"


class DirectorOf(FixedRelation):
    relation = "dbo:director"
    reverse = True


class DurationOf(FixedRelation):
    # DBpedia throws an error if the relation it's
    # dbo:Work/runtime so we expand the prefix
    # by giving the whole URL.
    relation = "<http://dbpedia.org/ontology/Work/runtime>"
    reverse = True


class HasAuthor(FixedRelation):
    relation = "dbp:author"


class AuthorOf(FixedRelation):
    relation = "dbp:author"
    reverse = True


class IsBook(FixedType):
    fixedtype = "yago:Book106410904"


class LocationOf(FixedRelation):
    relation = "dbo:location"
    reverse = True
