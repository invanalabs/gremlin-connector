#   Copyright 2021 Invana
#  #
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#  #
#    http:www.apache.org/licenses/LICENSE-2.0
#  #
#    Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#
from invana_py import InvanaGraph
import uuid
import pytest


@pytest.mark.asyncio
async def test_update_one(graph: InvanaGraph):
    ids = await graph.execute_query("g.V().limit(1).id().toList()")
    query_kwargs = {"has__id__within": ids}
    data = await graph.vertex.read_one(**query_kwargs)
    old_name = data.properties.name
    new_name = f"Hello world - {uuid.uuid4().__str__()}"
    data = await  graph.vertex.update_one(query_kwargs=query_kwargs,
                                          properties={"name": new_name})
    assert data.properties.name == new_name
    assert old_name != new_name
