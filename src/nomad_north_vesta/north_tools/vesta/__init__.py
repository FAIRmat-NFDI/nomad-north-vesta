#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD. See https://nomad-lab.eu for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from nomad.config.models.north import NORTHTool
from nomad.config.models.plugins import NorthToolEntryPoint

vesta = NORTHTool(
    image='ghcr.io/FAIRmat-NFDI/nomad-north-vesta:latest',
    description="""### **VESTA**: Visualization for Electronic and STructural Analysis

    VESTA is a software program used for visualizing and analyzing crystal structures.
    [Homepage](https://jp-minerals.org/vesta/en/).""",
    short_description='Visualization for Electronic Structural Analysis in NOMAD',
    external_mounts=[],
    file_extensions=['vesta, cif, cry, exp, fcf, ics, ins, in, min, mol, pdb, struct, vasp, wrl, xyz'],
    icon='vesta.png',
    image_pull_policy='Always',
    default_url='/desktop',
    maintainer=[{'email': 'markus.kuehbach@physik.hu-berlin.de', 'name': 'Markus Kühbach'}],
    mount_path='/home/jovyan',
    path_prefix='lab/tree',
    privileged=False,
    with_path=True,
    display_name='vesta',
)

north_tool_entry_point = NorthToolEntryPoint(
    id_url_safe='nomad_north_vesta', north_tool=vesta
)
