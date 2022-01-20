import pytest
from invana_py.ogm.exceptions import FieldValidationError
from invana_py.ogm.fields import StringProperty, DoubleProperty
from invana_py.ogm.models import VertexModel
from gremlin_python.statics import long
from invana_py import InvanaGraph
from invana_py.connector.data_types import DoubleType
import os

gremlin_url = os.environ.get("GREMLIN_SERVER_URL", "ws://megamind-ws:8182/gremlin")
graph = InvanaGraph(gremlin_url)

DEFAULT_USERNAME = "rrmerugu"
DEFAULT_POINTS_VALUE = long(5)


class Star(VertexModel):
    graph = graph

    properties = {
        'name': StringProperty(min_length=3, max_length=30, trim_whitespaces=True),
        'distance_from_earth_double': DoubleProperty(default=DEFAULT_POINTS_VALUE, min_value=5,
                                              max_value=1989000000000000000000000000000 * 100),
    }


class TestDoubleField:

    def test_field(self):
        graph.g.V().drop()
        star = Star.objects.create(name="Sun", distance_from_earth_double=DoubleType(1989000000000000000000000000000))
        assert isinstance(star.properties.distance_from_earth_double, DoubleType)

    def test_field_max_value(self):
        graph.g.V().drop()
        with pytest.raises(FieldValidationError) as exec_info:
            Star.objects.create(name="Sun", distance_from_earth_double=DoubleType(1989000000000000000000000000000) * 10000)
        assert "max_value for field" in exec_info.value.__str__()

    def test_field_min_value(self):
        graph.g.V().drop()
        with pytest.raises(FieldValidationError) as exec_info:
            Star.objects.create(name="Sun", distance_from_earth_double=DoubleType(2))
        assert "min_value for field " in exec_info.value.__str__()

    def test_field_default(self):
        graph.g.V().drop()
        star = Star.objects.create(name="Ravi")
        assert star.properties.distance_from_earth_double == DEFAULT_POINTS_VALUE
