from Neo4j.Neo4j.dummy import output


def test_dummy():
    assert output() == "Neo4j"
