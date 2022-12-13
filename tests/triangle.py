from ..src.bidimensional.polygons.triangle import Triangle
from ..src.bidimensional.coordinates import Coordinate
from math import sqrt
from itertools import combinations


class TestTriangle:

    def test_generation(self):
        triangle = Triangle(
            Coordinate(0, 0),
            Coordinate(1, 1),
            Coordinate(1, 0)
        )

        assert triangle.a.x == 0
        assert triangle.a.y == 0

        assert triangle.b.x == 1
        assert triangle.b.y == 1

        assert triangle.c.x == 1
        assert triangle.c.y == 0

    def test_definition_order(self):
        coordinates = (
            Coordinate(0, 0),
            Coordinate(1, 1),
            Coordinate(1, 0)
        )

        triangles = [
            Triangle(*triplet)
            for triplet in combinations(coordinates, 3)
        ]

        assert all(
            pair[0] == pair[1]
            for pair in combinations(triangles, 2)
        )

    def test_area(self):
        triangle = Triangle(
            Coordinate(0, 0),
            Coordinate(1, 1),
            Coordinate(1, 0)
        )

        assert triangle.area == 0.5

    def test_perimeter(self):
        triangle = Triangle(
            Coordinate(0, 0),
            Coordinate(1, 1),
            Coordinate(1, 0)
        )

        assert triangle.perimeter == sqrt(2) + 2

    def test_collinear_1(self):
        triangle = Triangle(
            Coordinate(0, 0),
            Coordinate(1, 1),
            Coordinate(2, 2)
        )

        assert triangle.is_collinear() is True

    def test_collinear_2(self):
        triangle = Triangle(
            Coordinate(0, 0),
            Coordinate(1, 1),
            Coordinate(2, 3)
        )

        assert triangle.is_collinear() is False

    def test_collinear_3(self):
        triangle = Triangle(
            Coordinate(0, 0),
            Coordinate(0, 1),
            Coordinate(0, -1)
        )

        assert triangle.is_collinear() is True

    def test_collinear_4(self):
        triangle = Triangle(
            Coordinate(0, 0),
            Coordinate(1, 0),
            Coordinate(-1, 0)
        )

        assert triangle.is_collinear() is True

    def test_collinear_5(self):
        triangle = Triangle(
            Coordinate(0, 0),
            Coordinate(1, 1),
            Coordinate(2, 3)
        )

        assert triangle.is_collinear() is False

    def test_eq(self):
        triangle_1 = Triangle(
            Coordinate(0, 0),
            Coordinate(1, 1),
            Coordinate(1, 0)
        )

        triangle_2 = Triangle(
            Coordinate(1, 1),
            Coordinate(0, 0),
            Coordinate(1, 0)
        )

        assert triangle_1 == triangle_2

    def test_neq(self):
        triangle_1 = Triangle(
            Coordinate(0, 0),
            Coordinate(1, 1),
            Coordinate(1, 0)
        )

        triangle_2 = Triangle(
            Coordinate(0, 0),
            Coordinate(1, 1),
            Coordinate(1, 1)
        )

        assert triangle_1 != triangle_2

    def test_gt(self):
        triangle_1 = Triangle(
            Coordinate(0, 0),
            Coordinate(1, 1),
            Coordinate(1, 0)
        )

        triangle_2 = Triangle(
            Coordinate(0, 0),
            Coordinate(1, 1),
            Coordinate(1.1, 0)
        )

        assert triangle_1 > triangle_2

    def test_lt(self):
        triangle_1 = Triangle(
            Coordinate(0, 0),
            Coordinate(1, 1),
            Coordinate(1.1, 0)
        )

        triangle_2 = Triangle(
            Coordinate(0, 0),
            Coordinate(1, 1),
            Coordinate(1, 0)
        )

        assert triangle_1 < triangle_2

    def test_ge(self):
        triangle_1 = Triangle(
            Coordinate(0, 0),
            Coordinate(1, 1),
            Coordinate(1, 0)
        )

        triangle_2 = Triangle(
            Coordinate(0, 0),
            Coordinate(1, 1),
            Coordinate(1.1, 0)
        )

        assert triangle_1 >= triangle_2

    def test_le(self):
        triangle_1 = Triangle(
            Coordinate(0, 0),
            Coordinate(1, 1),
            Coordinate(1.1, 0)
        )

        triangle_2 = Triangle(
            Coordinate(0, 0),
            Coordinate(1, 1),
            Coordinate(1, 0)
        )

        assert triangle_1 <= triangle_2
