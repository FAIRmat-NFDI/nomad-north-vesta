def test_importing_north_tool():
    # this will raise an exception if pydantic model validation fails
    from nomad_north_vesta.north_tools import vesta

    assert vesta.id_url_safe == 'vesta' or vesta.id == 'nomad-north-vesta', (
        'NORTHTool entry point has incorrect id or id_url_safe'
    )
