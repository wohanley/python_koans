#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#

# key: number of unique side lengths
triangleTypes = {
    1: 'equilateral',
    2: 'isosceles',
    3: 'scalene'
}

def triangle(a, b, c):
    uniqueEdgeLengths = {a, b, c}

    # fail if there are edges with negative lengths
    if [x for x in uniqueEdgeLengths if x <= 0]:
        raise TriangleError

    # fail if one edge is longer than the sum of the others
    if a >= b + c or b >= a + c or c >= a + b:
        raise TriangleError

    return triangleTypes[len(uniqueEdgeLengths)]

# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
