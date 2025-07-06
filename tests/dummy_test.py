# from neo4j.neo4j.dummy import output

from dummy import output


def test_dummy():
    assert output() == "Neo4j"
