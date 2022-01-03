#   Copyright 2021 Invana
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#    http:www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#
from invana_py import InvanaGraph
import pytest


@pytest.mark.asyncio
async def test_janusgraph_schema_reader(graph: InvanaGraph):
    schema_data = await graph.schema.get_graph_schema()


@pytest.mark.asyncio
async def test_janusgraph_schema_vertex_reader(graph: InvanaGraph):
    schema_data = await graph.schema.get_vertex_schema("Star")
    assert schema_data.name == "Star"


@pytest.mark.asyncio
async def test_janusgraph_get_all_vertices_schema(graph: InvanaGraph):
    schema_data = await graph.schema.get_all_vertices_schema()
