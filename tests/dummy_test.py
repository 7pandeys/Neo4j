from Neo4j.src.dummy import output


def test_dummy():
    assert output() == "Neo4j"
