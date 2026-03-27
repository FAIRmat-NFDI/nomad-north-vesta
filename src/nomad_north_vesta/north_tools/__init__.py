from nomad.config.models.north import NORTHTool
from nomad.config.models.plugins import NorthToolEntryPoint

vesta_north_tool = NORTHTool(
    short_description='Use VESTA (Visualization for Electronic STructural Analysis) in NOMAD.',
    image='ghcr.io/fairmat-nfdi/nomad-north-vesta:main',
    description="""### **VESTA**:

    [VESTA is a software program used for visualizing and analyzing crystal structures.](https://jp-minerals.org/vesta/en/)

    [Research article about the software](https://doi.org/10.1107/S0021889808012016)""",
    external_mounts=[],
    file_extensions=['vesta, cif, cry, exp, fcf, ics, ins, in, min, mol, pdb, struct, vasp, wrl, xyz'],
    icon='https://raw.githubusercontent.com/FAIRmat-NFDI/nomad-north-vesta/main/src/nomad_north_vesta/north_tools/vesta/vesta.png',
    image_pull_policy='Always',
    default_url='/desktop',
    maintainer=[{'email': 'markus.kuehbach@physik.hu-berlin.de', 'name': 'Markus Kühbach'}],
    mount_path='/home/jovyan',
    path_prefix='lab/tree',
    privileged=False,
    with_path=True,
    display_name='vesta',
)

vesta = NorthToolEntryPoint(
    id_url_safe='vesta',
    north_tool=vesta_north_tool,
)
