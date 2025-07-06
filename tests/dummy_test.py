from Neo4j.neo4j.dummy import output


def test_dummy():
    assert output() == "Neo4j"
