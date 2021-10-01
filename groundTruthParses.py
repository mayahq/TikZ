import re
from utilities import *
from language import *

import pickle


groundTruth = {}
groundTruth["drawings/expert-101.png"] = set(
    [
        "Rectangle((1,8), (3,9))",
        "Rectangle((1,10), (3,11))",
        "Rectangle((1,12), (3,13))",
        "Rectangle((4,8), (6,9))",
        "Rectangle((4,10), (6,11))",
        "Rectangle((4,12), (6,13))",
        "Rectangle((7,8), (9,9))",
        "Rectangle((1,14), (3,15))",
        "Rectangle((7,10), (9,11))",
        "Rectangle((4,14), (6,15))",
        "Rectangle((7,12), (9,13))",
        "Rectangle((10,8), (12,9))",
        "Rectangle((10,12), (12,13))",
        "Rectangle((7,14), (9,15))",
        "Rectangle((10,10), (12,11))",
        "Rectangle((10,14), (12,15))",
    ]
)
# Automatically generated code
groundTruth["drawings/expert-0.png"] = set(
    [
        "Line((7,8), (4,8), arrow = True, solid = True)",
        "Line((4,13), (6,11), arrow = True, solid = True)",
        "Line((7,8), (7,9), arrow = False, solid = True)",
        "Rectangle((1,6), (9,15))",
        "Rectangle((2,12), (4,14))",
        "Rectangle((6,9), (8,12))",
        "Rectangle((2,7), (4,9))",
        "Line((4,8), (6,10), arrow = True, solid = True)",
    ]
)
groundTruth["drawings/expert-1.png"] = set(
    [
        "Line((4,7), (6,9), arrow = True, solid = True)",
        "Line((4,13), (6,11), arrow = True, solid = True)",
        "Line((9,11), (9,13), arrow = False, solid = False)",
        "Rectangle((12,9), (13,11))",
        "Line((9,13), (4,13), arrow = True, solid = False)",
        "Rectangle((2,12), (4,14))",
        "Line((7,10), (8,10), arrow = True, solid = True)",
        "Rectangle((2,6), (4,8))",
        "Circle(center = (9,10), radius = 1)",
        "Line((11,10), (12,10), arrow = True, solid = True)",
        "Rectangle((14,9), (15,11))",
        "Line((13,10), (14,10), arrow = True, solid = True)",
        "Rectangle((6,8), (7,12))",
        "Rectangle((1,5), (11,15))",
    ]
)
groundTruth["drawings/expert-2.png"] = set(
    [
        "Line((3,14), (5,12), arrow = True, solid = True)",
        "Rectangle((5,10), (7,13))",
        "Rectangle((1,13), (3,15))",
        "Line((3,9), (5,11), arrow = True, solid = True)",
        "Rectangle((1,8), (3,10))",
    ]
)
groundTruth["drawings/expert-3.png"] = set(
    [
        "Line((4,7), (6,9), arrow = True, solid = True)",
        "Line((4,13), (6,11), arrow = True, solid = True)",
        "Rectangle((6,8), (8,12))",
        "Rectangle((1,5), (13,15))",
        "Rectangle((2,12), (4,14))",
        "Rectangle((2,6), (4,8))",
        "Circle(center = (11,10), radius = 1)",
        "Line((8,10), (10,10), arrow = True, solid = True)",
    ]
)
groundTruth["drawings/expert-4.png"] = set(
    [
        "Line((12,8), (4,8), arrow = True, solid = False)",
        "Rectangle((2,7), (4,9))",
        "Line((12,8), (12,10), arrow = False, solid = False)",
        "Line((9,11), (11,11), arrow = True, solid = True)",
        "Circle(center = (12,11), radius = 1)",
        "Rectangle((6,9), (9,13))",
        "Line((4,14), (6,12), arrow = True, solid = True)",
        "Rectangle((2,13), (4,15))",
        "Line((4,8), (6,10), arrow = True, solid = True)",
    ]
)
groundTruth["drawings/expert-5.png"] = set(
    [
        "Line((14,14), (14,5), arrow = True, solid = True)",
        "Rectangle((11,8), (13,14))",
        "Rectangle((5,13), (7,14))",
        "Rectangle((8,10), (10,14))",
        "Rectangle((2,12), (4,14))",
    ]
)
groundTruth["drawings/expert-6.png"] = set(
    [
        "Line((7,13), (9,12), arrow = False, solid = True)",
        "Line((4,10), (4,13), arrow = False, solid = True)",
        "Rectangle((6,9), (9,12))",
        "Line((4,10), (6,9), arrow = False, solid = True)",
        "Line((4,13), (7,13), arrow = False, solid = True)",
        "Line((4,13), (6,12), arrow = False, solid = True)",
    ]
)
groundTruth["drawings/expert-7.png"] = set(
    [
        "Line((5,11), (5,13), arrow = False, solid = True)",
        "Circle(center = (5,9), radius = 1)",
        "Circle(center = (5,14), radius = 1)",
        "Circle(center = (2,9), radius = 1)",
        "Circle(center = (2,14), radius = 1)",
        "Circle(center = (8,14), radius = 1)",
        "Circle(center = (8,9), radius = 1)",
        "Line((2,10), (2,13), arrow = False, solid = True)",
        "Line((8,12), (8,13), arrow = False, solid = True)",
    ]
)
groundTruth["drawings/expert-8.png"] = set(
    ["Line((5,11), (5,15), arrow = False, solid = True)"]
)
groundTruth["drawings/expert-10.png"] = set(["Rectangle((3,11), (6,15))"])
groundTruth["drawings/expert-11.png"] = set(["Circle(center = (3,14), radius = 1)"])
groundTruth["drawings/expert-12.png"] = set(
    [
        "Line((4,9), (7,9), arrow = False, solid = True)",
        "Line((8,10), (8,13), arrow = False, solid = True)",
        "Rectangle((7,13), (9,15))",
        "Circle(center = (3,9), radius = 1)",
        "Line((4,14), (7,14), arrow = False, solid = True)",
        "Circle(center = (8,9), radius = 1)",
        "Line((3,10), (3,13), arrow = False, solid = True)",
        "Rectangle((2,13), (4,15))",
    ]
)
groundTruth["drawings/expert-13.png"] = set(
    [
        "Line((4,14), (2,14), arrow = True, solid = True)",
        "Line((1,15), (3,15), arrow = True, solid = True)",
        "Line((6,12), (4,12), arrow = True, solid = True)",
        "Line((3,13), (5,13), arrow = True, solid = True)",
    ]
)
groundTruth["drawings/expert-14.png"] = set(
    [
        "Rectangle((7,8), (8,9))",
        "Rectangle((3,14), (4,15))",
        "Rectangle((5,12), (6,13))",
        "Rectangle((9,8), (10,9))",
        "Rectangle((7,10), (8,11))",
        "Rectangle((3,12), (4,13))",
        "Rectangle((5,10), (6,11))",
    ]
)
groundTruth["drawings/expert-15.png"] = set(
    [
        "Line((2,14), (4,14), arrow = False, solid = True)",
        "Line((1,15), (3,15), arrow = False, solid = False)",
        "Line((4,12), (6,12), arrow = False, solid = True)",
        "Line((3,13), (5,13), arrow = False, solid = False)",
    ]
)
groundTruth["drawings/expert-16.png"] = set(
    [
        "Line((5,8), (6,10), arrow = False, solid = True)",
        "Circle(center = (8,8), radius = 1)",
        "Circle(center = (10,5), radius = 1)",
        "Line((6,10), (7,8), arrow = False, solid = True)",
        "Circle(center = (6,11), radius = 1)",
        "Circle(center = (4,14), radius = 1)",
        "Line((8,7), (9,5), arrow = False, solid = True)",
        "Circle(center = (2,11), radius = 1)",
        "Line((3,11), (4,13), arrow = False, solid = True)",
        "Circle(center = (4,8), radius = 1)",
        "Line((4,13), (5,11), arrow = False, solid = True)",
        "Circle(center = (6,5), radius = 1)",
        "Line((7,5), (8,7), arrow = False, solid = True)",
    ]
)
groundTruth["drawings/expert-17.png"] = set(
    [
        "Line((5,13), (4,11), arrow = True, solid = True)",
        "Line((5,13), (6,11), arrow = True, solid = True)",
        "Rectangle((2,10), (4,12))",
        "Rectangle((4,7), (6,9))",
        "Rectangle((6,10), (8,12))",
        "Line((7,10), (8,8), arrow = True, solid = True)",
        "Rectangle((6,4), (8,6))",
        "Line((7,10), (6,8), arrow = True, solid = True)",
        "Rectangle((4,13), (6,15))",
        "Line((9,7), (8,5), arrow = True, solid = True)",
        "Rectangle((10,4), (12,6))",
        "Rectangle((8,7), (10,9))",
        "Line((9,7), (10,5), arrow = True, solid = True)",
    ]
)
groundTruth["drawings/expert-19.png"] = set(
    [
        "Line((8,13), (6,11), arrow = True, solid = True)",
        "Rectangle((4,9), (6,11))",
        "Rectangle((7,13), (9,15))",
    ]
)
groundTruth["drawings/expert-21.png"] = set(
    [
        "Line((3,11), (3,13), arrow = True, solid = True)",
        "Line((11,11), (11,13), arrow = True, solid = True)",
        "Line((10,10), (8,10), arrow = True, solid = True)",
        "Rectangle((10,9), (12,11))",
        "Line((6,10), (4,10), arrow = True, solid = True)",
        "Rectangle((10,13), (12,15))",
        "Circle(center = (3,14), radius = 1)",
        "Line((7,11), (7,13), arrow = True, solid = True)",
        "Rectangle((6,13), (8,15))",
        "Rectangle((6,9), (8,11))",
        "Rectangle((2,9), (4,11))",
    ]
)
groundTruth["drawings/expert-22.png"] = set(
    [
        "Line((9,14), (7,14), arrow = True, solid = True)",
        "Rectangle((9,13), (11,15))",
        "Line((10,13), (10,11), arrow = True, solid = True)",
        "Rectangle((5,13), (7,15))",
        "Rectangle((5,9), (7,11))",
        "Rectangle((9,9), (11,11))",
        "Line((6,13), (6,11), arrow = True, solid = True)",
        "Rectangle((1,13), (3,15))",
        "Line((5,14), (3,14), arrow = True, solid = True)",
        "Line((2,13), (2,11), arrow = True, solid = True)",
        "Rectangle((1,9), (3,11))",
    ]
)
groundTruth["drawings/expert-23.png"] = set(
    [
        "Circle(center = (2,14), radius = 1)",
        "Circle(center = (10,10), radius = 1)",
        "Line((10,11), (10,13), arrow = True, solid = True)",
        "Circle(center = (6,10), radius = 1)",
        "Line((9,10), (7,10), arrow = True, solid = True)",
        "Line((6,11), (6,13), arrow = True, solid = True)",
        "Circle(center = (10,14), radius = 1)",
        "Circle(center = (6,14), radius = 1)",
        "Line((2,11), (2,13), arrow = True, solid = True)",
        "Line((5,10), (3,10), arrow = True, solid = True)",
        "Circle(center = (2,10), radius = 1)",
    ]
)
groundTruth["drawings/expert-24.png"] = set(
    [
        "Line((6,9), (6,8), arrow = True, solid = True)",
        "Rectangle((3,13), (9,15))",
        "Rectangle((5,6), (7,8))",
        "Rectangle((3,9), (9,12))",
        "Line((8,13), (8,12), arrow = True, solid = True)",
        "Line((4,13), (4,12), arrow = True, solid = True)",
    ]
)
groundTruth["drawings/expert-26.png"] = set(
    [
        "Circle(center = (6,10), radius = 1)",
        "Circle(center = (6,6), radius = 1)",
        "Circle(center = (6,14), radius = 1)",
        "Line((6,9), (6,7), arrow = True, solid = True)",
        "Line((6,13), (6,11), arrow = True, solid = True)",
    ]
)
groundTruth["drawings/expert-28.png"] = set(
    [
        "Line((2,15), (4,15), arrow = False, solid = True)",
        "Line((2,13), (2,15), arrow = False, solid = True)",
    ]
)
groundTruth["drawings/expert-29.png"] = set(
    [
        "Line((2,15), (4,15), arrow = False, solid = True)",
        "Line((4,9), (4,13), arrow = False, solid = True)",
        "Line((3,11), (3,14), arrow = False, solid = True)",
        "Line((2,13), (2,15), arrow = False, solid = True)",
        "Line((3,14), (6,14), arrow = False, solid = True)",
        "Line((4,13), (8,13), arrow = False, solid = True)",
    ]
)
groundTruth["drawings/expert-31.png"] = set(
    [
        "Circle(center = (8,12), radius = 1)",
        "Rectangle((4,11), (6,15))",
        "Circle(center = (5,14), radius = 1)",
        "Circle(center = (8,10), radius = 1)",
        "Circle(center = (2,14), radius = 1)",
        "Circle(center = (8,14), radius = 1)",
        "Circle(center = (5,12), radius = 1)",
        "Rectangle((1,13), (3,15))",
        "Rectangle((7,9), (9,15))",
    ]
)
groundTruth["drawings/expert-33.png"] = set(
    [
        "Line((8,11), (8,14), arrow = False, solid = True)",
        "Line((2,14), (8,14), arrow = False, solid = False)",
        "Line((2,11), (8,11), arrow = False, solid = False)",
        "Line((2,11), (2,14), arrow = False, solid = True)",
    ]
)
groundTruth["drawings/expert-34.png"] = set(
    [
        "Line((5,13), (5,15), arrow = False, solid = True)",
        "Line((4,12), (6,12), arrow = False, solid = True)",
        "Line((6,13), (8,13), arrow = False, solid = True)",
        "Line((7,10), (9,10), arrow = False, solid = True)",
        "Line((3,15), (5,15), arrow = False, solid = True)",
        "Line((4,12), (4,14), arrow = False, solid = True)",
        "Line((7,10), (7,12), arrow = False, solid = True)",
        "Line((8,11), (8,13), arrow = False, solid = True)",
    ]
)
groundTruth["drawings/expert-35.png"] = set(
    [
        "Line((4,14), (8,10), arrow = True, solid = True)",
        "Circle(center = (3,9), radius = 1)",
        "Circle(center = (8,9), radius = 1)",
        "Line((3,13), (3,10), arrow = True, solid = True)",
        "Circle(center = (3,14), radius = 1)",
    ]
)
groundTruth["drawings/expert-36.png"] = set(
    [
        "Rectangle((9,8), (11,10))",
        "Rectangle((2,6), (6,10))",
        "Rectangle((10,6), (11,7))",
        "Rectangle((2,14), (3,15))",
        "Rectangle((2,11), (4,13))",
        "Rectangle((7,11), (11,15))",
    ]
)
groundTruth["drawings/expert-37.png"] = set(
    [
        "Line((4,12), (6,10), arrow = False, solid = True)",
        "Rectangle((7,5), (9,7))",
        "Circle(center = (4,13), radius = 1)",
        "Line((8,7), (8,10), arrow = False, solid = True)",
        "Rectangle((3,10), (9,14))",
    ]
)
groundTruth["drawings/expert-40.png"] = set(
    [
        "Circle(center = (9,13), radius = 1)",
        "Circle(center = (3,13), radius = 1)",
        "Circle(center = (6,13), radius = 1)",
    ]
)
groundTruth["drawings/expert-41.png"] = set(
    ["Rectangle((4,8), (5,14))", "Rectangle((2,8), (3,14))", "Rectangle((6,8), (7,14))"]
)
groundTruth["drawings/expert-42.png"] = set(
    [
        "Line((3,10), (3,15), arrow = False, solid = False)",
        "Line((7,11), (7,15), arrow = False, solid = False)",
        "Line((7,10), (7,11), arrow = False, solid = False)",
    ]
)
groundTruth["drawings/expert-43.png"] = set(
    [
        "Line((2,10), (2,15), arrow = False, solid = True)",
        "Line((6,10), (6,15), arrow = False, solid = True)",
    ]
)
groundTruth["drawings/expert-44.png"] = set(
    [
        "Rectangle((12,13), (14,15))",
        "Line((11,14), (12,14), arrow = False, solid = True)",
        "Line((4,14), (5,14), arrow = False, solid = True)",
        "Circle(center = (10,14), radius = 1)",
        "Circle(center = (6,14), radius = 1)",
        "Rectangle((2,13), (4,15))",
    ]
)
groundTruth["drawings/expert-45.png"] = set(
    [
        "Line((8,9), (10,9), arrow = True, solid = True)",
        "Rectangle((5,13), (7,15))",
        "Circle(center = (11,9), radius = 1)",
        "Line((6,13), (6,11), arrow = True, solid = True)",
        "Rectangle((4,7), (8,11))",
        "Rectangle((5,3), (7,5))",
        "Line((6,5), (6,7), arrow = True, solid = True)",
    ]
)
groundTruth["drawings/expert-47.png"] = set(
    [
        "Rectangle((9,12), (12,15))",
        "Rectangle((1,4), (4,7))",
        "Rectangle((5,13), (8,14))",
        "Rectangle((2,8), (3,11))",
        "Rectangle((9,4), (12,7))",
        "Rectangle((5,5), (8,6))",
        "Rectangle((1,12), (4,15))",
        "Rectangle((10,8), (11,11))",
    ]
)
groundTruth["drawings/expert-50.png"] = set(
    [
        "Line((3,14), (5,12), arrow = True, solid = True)",
        "Rectangle((10,10), (13,13))",
        "Line((9,11), (8,11), arrow = True, solid = True)",
        "Line((9,11), (10,11), arrow = False, solid = True)",
        "Rectangle((5,10), (8,13))",
        "Line((8,12), (10,12), arrow = True, solid = True)",
        "Rectangle((1,13), (3,15))",
        "Rectangle((1,8), (3,10))",
        "Line((3,9), (5,11), arrow = True, solid = True)",
    ]
)
groundTruth["drawings/expert-51.png"] = set(
    [
        "Rectangle((8,13), (11,14))",
        "Rectangle((6,11), (9,12))",
        "Rectangle((4,9), (7,10))",
    ]
)
groundTruth["drawings/expert-53.png"] = set(
    [
        "Line((2,14), (10,14), arrow = False, solid = True)",
        "Line((6,14), (6,6), arrow = True, solid = True)",
        "Line((8,14), (8,10), arrow = True, solid = True)",
        "Line((4,14), (4,12), arrow = True, solid = True)",
    ]
)
groundTruth["drawings/expert-55.png"] = set(
    [
        "Circle(center = (5,12), radius = 1)",
        "Rectangle((4,7), (6,9))",
        "Line((5,11), (5,9), arrow = True, solid = True)",
    ]
)
groundTruth["drawings/expert-57.png"] = set(
    [
        "Circle(center = (10,14), radius = 1)",
        "Circle(center = (2,8), radius = 1)",
        "Circle(center = (10,8), radius = 1)",
        "Circle(center = (10,11), radius = 1)",
        "Circle(center = (6,11), radius = 1)",
        "Circle(center = (2,14), radius = 1)",
        "Circle(center = (2,11), radius = 1)",
        "Circle(center = (6,14), radius = 1)",
        "Circle(center = (6,8), radius = 1)",
    ]
)
groundTruth["drawings/expert-58.png"] = set(
    [
        "Line((10,8), (2,8), arrow = True, solid = True)",
        "Rectangle((8,8), (9,13))",
        "Line((10,8), (10,15), arrow = True, solid = True)",
        "Rectangle((4,8), (5,11))",
        "Rectangle((6,8), (7,12))",
    ]
)
groundTruth["drawings/expert-59.png"] = set(
    ["Line((8,13), (4,13), arrow = False, solid = False)"]
)
groundTruth["drawings/expert-60.png"] = set(
    [
        "Circle(center = (5,7), radius = 1)",
        "Circle(center = (6,10), radius = 1)",
        "Circle(center = (8,7), radius = 1)",
        "Line((7,13), (6,11), arrow = True, solid = True)",
        "Line((6,9), (5,8), arrow = True, solid = True)",
        "Line((3,10), (5,10), arrow = True, solid = True)",
        "Circle(center = (8,13), radius = 1)",
        "Line((6,9), (8,8), arrow = True, solid = True)",
        "Rectangle((1,9), (3,11))",
    ]
)
groundTruth["drawings/expert-62.png"] = set(
    [
        "Rectangle((8,11), (11,14))",
        "Rectangle((3,13), (4,14))",
        "Rectangle((5,12), (7,14))",
    ]
)
groundTruth["drawings/expert-63.png"] = set(
    [
        "Rectangle((3,11), (6,14))",
        "Rectangle((2,10), (7,15))",
        "Rectangle((4,12), (5,13))",
    ]
)
groundTruth["drawings/expert-64.png"] = set(
    [
        "Line((2,11), (2,13), arrow = False, solid = True)",
        "Line((6,11), (6,13), arrow = False, solid = True)",
        "Rectangle((5,13), (7,15))",
        "Rectangle((5,9), (7,11))",
        "Rectangle((1,13), (3,15))",
        "Line((3,10), (5,10), arrow = False, solid = True)",
        "Line((3,14), (5,14), arrow = False, solid = True)",
        "Rectangle((1,9), (3,11))",
    ]
)
groundTruth["drawings/expert-65.png"] = set(
    [
        "Line((4,9), (6,9), arrow = False, solid = True)",
        "Circle(center = (3,13), radius = 1)",
        "Line((3,10), (3,12), arrow = False, solid = True)",
        "Line((4,13), (6,13), arrow = False, solid = True)",
        "Circle(center = (3,9), radius = 1)",
        "Circle(center = (7,13), radius = 1)",
        "Line((7,10), (7,12), arrow = False, solid = True)",
        "Circle(center = (7,9), radius = 1)",
    ]
)
groundTruth["drawings/expert-66.png"] = set(
    [
        "Line((4,12), (7,12), arrow = False, solid = True)",
        "Line((3,13), (8,13), arrow = False, solid = True)",
        "Line((2,14), (9,14), arrow = False, solid = True)",
    ]
)
groundTruth["drawings/expert-67.png"] = set(
    [
        "Line((4,15), (8,11), arrow = False, solid = True)",
        "Line((4,14), (8,10), arrow = False, solid = True)",
        "Rectangle((8,10), (9,11))",
        "Rectangle((3,14), (4,15))",
    ]
)
groundTruth["drawings/expert-68.png"] = set(
    [
        "Circle(center = (10,14), radius = 1)",
        "Rectangle((5,13), (7,15))",
        "Rectangle((9,13), (11,15))",
        "Circle(center = (2,14), radius = 1)",
        "Circle(center = (6,14), radius = 1)",
        "Rectangle((1,13), (3,15))",
    ]
)
groundTruth["drawings/expert-69.png"] = set(
    [
        "Circle(center = (5,10), radius = 1)",
        "Line((5,13), (5,11), arrow = True, solid = True)",
        "Line((8,13), (8,11), arrow = True, solid = True)",
        "Circle(center = (8,10), radius = 1)",
        "Rectangle((4,13), (9,15))",
    ]
)
groundTruth["drawings/expert-9.png"] = set(
    ["Line((7,14), (1,14), arrow = True, solid = True)"]
)
groundTruth["drawings/expert-18.png"] = set(
    [
        "Circle(center = (6,13), radius = 1)",
        "Circle(center = (9,11), radius = 1)",
        "Circle(center = (5,11), radius = 1)",
        "Circle(center = (3,14), radius = 1)",
        "Circle(center = (9,9), radius = 1)",
        "Circle(center = (7,9), radius = 1)",
    ]
)
groundTruth["drawings/expert-20.png"] = set(
    [
        "Circle(center = (3,10), radius = 1)",
        "Line((10,14), (8,14), arrow = True, solid = True)",
        "Circle(center = (11,10), radius = 1)",
        "Circle(center = (7,10), radius = 1)",
        "Line((6,14), (4,14), arrow = True, solid = True)",
        "Circle(center = (11,14), radius = 1)",
        "Line((3,13), (3,11), arrow = True, solid = True)",
        "Circle(center = (7,14), radius = 1)",
        "Line((7,13), (7,11), arrow = True, solid = True)",
        "Line((11,13), (11,11), arrow = True, solid = True)",
        "Rectangle((2,13), (4,15))",
    ]
)
groundTruth["drawings/expert-25.png"] = set(
    [
        "Line((10,11), (9,11), arrow = True, solid = True)",
        "Rectangle((7,10), (9,12))",
        "Rectangle((4,10), (6,12))",
        "Line((7,11), (6,11), arrow = True, solid = True)",
        "Rectangle((10,10), (12,12))",
    ]
)
groundTruth["drawings/expert-27.png"] = set(
    [
        "Line((4,13), (5,12), arrow = False, solid = True)",
        "Line((3,12), (4,13), arrow = False, solid = True)",
        "Line((4,11), (5,12), arrow = False, solid = True)",
        "Line((3,12), (4,11), arrow = False, solid = True)",
    ]
)
groundTruth["drawings/expert-30.png"] = set(
    [
        "Circle(center = (6,12), radius = 1)",
        "Rectangle((5,11), (7,15))",
        "Rectangle((1,13), (3,15))",
        "Circle(center = (2,14), radius = 1)",
        "Circle(center = (2,11), radius = 1)",
        "Circle(center = (6,14), radius = 1)",
        "Rectangle((1,10), (3,12))",
    ]
)
groundTruth["drawings/expert-32.png"] = set(
    [
        "Rectangle((2,9), (7,12))",
        "Circle(center = (7,14), radius = 1)",
        "Line((4,14), (6,14), arrow = False, solid = True)",
        "Rectangle((2,13), (4,15))",
    ]
)
groundTruth["drawings/expert-38.png"] = set(
    [
        "Circle(center = (5,8), radius = 1)",
        "Circle(center = (2,8), radius = 1)",
        "Circle(center = (8,11), radius = 1)",
        "Line((2,9), (2,10), arrow = False, solid = True)",
        "Circle(center = (8,8), radius = 1)",
        "Line((8,9), (8,10), arrow = False, solid = True)",
        "Line((5,12), (5,13), arrow = False, solid = True)",
        "Line((2,12), (2,13), arrow = False, solid = True)",
        "Line((3,8), (4,8), arrow = False, solid = True)",
        "Circle(center = (5,14), radius = 1)",
        "Line((5,9), (5,10), arrow = False, solid = True)",
        "Circle(center = (2,14), radius = 1)",
        "Circle(center = (2,11), radius = 1)",
        "Circle(center = (8,14), radius = 1)",
        "Circle(center = (5,11), radius = 1)",
        "Line((6,11), (7,11), arrow = False, solid = True)",
        "Line((3,14), (4,14), arrow = False, solid = True)",
        "Line((6,8), (7,8), arrow = False, solid = True)",
        "Line((8,12), (8,13), arrow = False, solid = True)",
        "Line((6,14), (7,14), arrow = False, solid = True)",
        "Line((3,11), (4,11), arrow = False, solid = True)",
    ]
)
groundTruth["drawings/expert-39.png"] = set(
    [
        "Line((6,8), (7,8), arrow = False, solid = True)",
        "Line((3,8), (4,8), arrow = False, solid = True)",
        "Rectangle((4,7), (6,9))",
        "Rectangle((4,10), (6,12))",
        "Line((3,11), (4,11), arrow = False, solid = True)",
        "Line((8,9), (8,10), arrow = False, solid = True)",
        "Rectangle((7,10), (9,12))",
        "Rectangle((4,13), (6,15))",
        "Line((5,9), (5,10), arrow = False, solid = True)",
        "Line((6,14), (7,14), arrow = False, solid = True)",
        "Line((5,12), (5,13), arrow = False, solid = True)",
        "Line((6,11), (7,11), arrow = False, solid = True)",
        "Rectangle((7,7), (9,9))",
        "Rectangle((1,7), (3,9))",
        "Line((2,12), (2,13), arrow = False, solid = True)",
        "Rectangle((1,10), (3,12))",
        "Line((3,14), (4,14), arrow = False, solid = True)",
        "Line((2,9), (2,10), arrow = False, solid = True)",
        "Rectangle((1,13), (3,15))",
        "Line((8,12), (8,13), arrow = False, solid = True)",
        "Rectangle((7,13), (9,15))",
    ]
)
groundTruth["drawings/expert-46.png"] = set(
    [
        "Line((10,9), (10,12), arrow = False, solid = True)",
        "Circle(center = (3,7), radius = 1)",
        "Line((5,14), (8,14), arrow = False, solid = True)",
        "Circle(center = (10,14), radius = 1)",
        "Line((3,9), (3,12), arrow = False, solid = True)",
        "Circle(center = (3,14), radius = 1)",
        "Line((5,7), (8,7), arrow = False, solid = True)",
        "Circle(center = (10,7), radius = 1)",
    ]
)
groundTruth["drawings/expert-48.png"] = set(
    [
        "Line((2,15), (4,15), arrow = False, solid = True)",
        "Line((5,12), (7,12), arrow = False, solid = True)",
        "Line((4,13), (6,13), arrow = False, solid = True)",
        "Line((7,10), (9,10), arrow = False, solid = True)",
        "Line((6,11), (8,11), arrow = False, solid = True)",
        "Line((3,14), (5,14), arrow = False, solid = True)",
    ]
)
groundTruth["drawings/expert-49.png"] = set(
    [
        "Rectangle((6,5), (8,6))",
        "Rectangle((9,4), (11,6))",
        "Rectangle((2,11), (5,14))",
        "Rectangle((3,8), (4,10))",
        "Rectangle((2,4), (5,7))",
    ]
)
groundTruth["drawings/expert-52.png"] = set(
    [
        "Line((5,13), (2,10), arrow = True, solid = True)",
        "Circle(center = (5,9), radius = 1)",
        "Line((5,13), (8,10), arrow = True, solid = True)",
        "Line((2,8), (2,6), arrow = True, solid = True)",
        "Circle(center = (5,14), radius = 1)",
        "Circle(center = (2,9), radius = 1)",
        "Circle(center = (8,5), radius = 1)",
        "Circle(center = (8,9), radius = 1)",
        "Line((5,13), (5,10), arrow = True, solid = True)",
        "Line((8,8), (8,6), arrow = True, solid = True)",
        "Circle(center = (5,5), radius = 1)",
        "Line((5,8), (5,6), arrow = True, solid = True)",
        "Circle(center = (2,5), radius = 1)",
    ]
)
groundTruth["drawings/expert-54.png"] = set(
    [
        "Rectangle((5,7), (9,15))",
        "Rectangle((6,8), (8,10))",
        "Line((7,10), (7,12), arrow = False, solid = True)",
        "Rectangle((6,12), (8,14))",
    ]
)
groundTruth["drawings/expert-56.png"] = set(
    [
        "Circle(center = (2,7), radius = 1)",
        "Circle(center = (6,12), radius = 1)",
        "Circle(center = (2,12), radius = 1)",
        "Circle(center = (6,10), radius = 1)",
        "Circle(center = (6,7), radius = 1)",
        "Circle(center = (2,14), radius = 1)",
        "Rectangle((1,6), (7,8))",
        "Rectangle((1,9), (3,15))",
        "Circle(center = (6,14), radius = 1)",
        "Rectangle((5,9), (7,15))",
        "Circle(center = (2,10), radius = 1)",
        "Circle(center = (4,7), radius = 1)",
    ]
)
groundTruth["drawings/expert-61.png"] = set(
    [
        "Circle(center = (4,10), radius = 1)",
        "Line((7,10), (5,10), arrow = True, solid = True)",
        "Circle(center = (8,10), radius = 1)",
        "Rectangle((2,9), (9,11))",
    ]
)
groundTruth["drawings/expert-70.png"] = set(
    [
        "Line((2,9), (4,7), arrow = True, solid = True)",
        "Circle(center = (6,10), radius = 1)",
        "Line((6,13), (6,11), arrow = True, solid = True)",
        "Circle(center = (2,14), radius = 1)",
        "Circle(center = (4,6), radius = 1)",
        "Circle(center = (6,14), radius = 1)",
        "Line((2,13), (5,10), arrow = True, solid = True)",
        "Line((6,9), (4,7), arrow = True, solid = True)",
        "Circle(center = (2,10), radius = 1)",
        "Line((6,13), (3,10), arrow = True, solid = True)",
        "Line((2,13), (2,11), arrow = True, solid = True)",
    ]
)
groundTruth["drawings/expert-71.png"] = set(
    [
        "Rectangle((6,14), (10,15))",
        "Line((8,6), (13,8), arrow = True, solid = True)",
        "Line((10,14), (11,10), arrow = True, solid = True)",
        "Line((5,14), (11,10), arrow = True, solid = True)",
        "Line((8,6), (8,8), arrow = True, solid = True)",
        "Rectangle((3,5), (13,6))",
        "Rectangle((1,8), (5,10))",
        "Rectangle((6,8), (10,10))",
        "Line((8,10), (8,14), arrow = True, solid = True)",
        "Line((5,14), (6,10), arrow = True, solid = True)",
        "Rectangle((1,14), (5,15))",
        "Line((8,6), (3,8), arrow = True, solid = True)",
        "Line((3,10), (3,14), arrow = True, solid = True)",
        "Rectangle((11,8), (15,10))",
        "Rectangle((11,14), (15,15))",
        "Line((13,10), (13,14), arrow = True, solid = True)",
    ]
)
groundTruth["drawings/expert-72.png"] = set(
    [
        "Circle(center = (2,8), radius = 1)",
        "Rectangle((6,9), (7,10))",
        "Circle(center = (8,8), radius = 1)",
        "Rectangle((6,12), (7,13))",
        "Rectangle((3,9), (4,10))",
        "Circle(center = (2,14), radius = 1)",
        "Circle(center = (8,14), radius = 1)",
        "Circle(center = (5,11), radius = 1)",
        "Rectangle((3,12), (4,13))",
    ]
)
groundTruth["drawings/expert-73.png"] = set(
    [
        "Rectangle((9,13), (11,15))",
        "Line((14,7), (14,9), arrow = True, solid = True)",
        "Rectangle((13,13), (15,15))",
        "Line((11,14), (13,10), arrow = True, solid = True)",
        "Rectangle((5,9), (7,11))",
        "Line((14,11), (14,13), arrow = True, solid = True)",
        "Rectangle((5,13), (7,15))",
        "Rectangle((9,9), (11,11))",
        "Line((3,7), (14,7), arrow = False, solid = True)",
        "Line((6,11), (6,13), arrow = True, solid = True)",
        "Line((7,14), (9,10), arrow = True, solid = True)",
        "Line((10,7), (10,9), arrow = True, solid = True)",
        "Line((6,7), (6,9), arrow = True, solid = True)",
        "Line((10,11), (10,13), arrow = True, solid = True)",
        "Rectangle((13,9), (15,11))",
        "Rectangle((1,6), (3,14))",
    ]
)
groundTruth["drawings/expert-74.png"] = set(
    [
        "Circle(center = (6,12), radius = 1)",
        "Circle(center = (2,12), radius = 1)",
        "Circle(center = (6,10), radius = 1)",
        "Circle(center = (4,14), radius = 1)",
        "Rectangle((3,11), (5,13))",
        "Circle(center = (2,14), radius = 1)",
        "Circle(center = (4,10), radius = 1)",
        "Circle(center = (6,14), radius = 1)",
        "Rectangle((1,9), (7,15))",
        "Circle(center = (4,12), radius = 1)",
        "Circle(center = (2,10), radius = 1)",
    ]
)
groundTruth["drawings/expert-75.png"] = set(
    [
        "Circle(center = (2,14), radius = 1)",
        "Circle(center = (10,10), radius = 1)",
        "Line((10,13), (10,11), arrow = True, solid = True)",
        "Line((7,14), (9,14), arrow = True, solid = True)",
        "Circle(center = (6,10), radius = 1)",
        "Circle(center = (14,14), radius = 1)",
        "Line((11,14), (13,14), arrow = True, solid = True)",
        "Line((3,14), (5,14), arrow = True, solid = True)",
        "Circle(center = (10,14), radius = 1)",
        "Circle(center = (14,10), radius = 1)",
        "Circle(center = (6,14), radius = 1)",
        "Line((6,13), (6,11), arrow = True, solid = True)",
        "Circle(center = (2,10), radius = 1)",
        "Line((14,13), (14,11), arrow = True, solid = True)",
        "Line((2,13), (2,11), arrow = True, solid = True)",
    ]
)
groundTruth["drawings/expert-76.png"] = set(
    [
        "Circle(center = (6,6), radius = 1)",
        "Line((6,10), (10,7), arrow = False, solid = True)",
        "Line((6,10), (6,15), arrow = False, solid = True)",
        "Circle(center = (9,13), radius = 1)",
        "Line((2,7), (6,10), arrow = False, solid = True)",
        "Circle(center = (3,13), radius = 1)",
    ]
)
groundTruth["drawings/expert-77.png"] = set(
    [
        "Circle(center = (10,14), radius = 1)",
        "Line((2,9), (5,7), arrow = False, solid = True)",
        "Rectangle((5,13), (7,15))",
        "Line((10,11), (10,13), arrow = False, solid = True)",
        "Circle(center = (6,7), radius = 1)",
        "Rectangle((9,9), (11,11))",
        "Circle(center = (2,14), radius = 1)",
        "Line((7,14), (9,14), arrow = False, solid = True)",
        "Line((2,11), (2,13), arrow = False, solid = True)",
        "Line((3,14), (5,14), arrow = False, solid = True)",
        "Line((7,7), (10,9), arrow = False, solid = True)",
        "Rectangle((1,9), (3,11))",
    ]
)
groundTruth["drawings/expert-78.png"] = set(
    [
        "Line((4,9), (6,11), arrow = True, solid = True)",
        "Line((7,13), (7,12), arrow = True, solid = True)",
        "Line((1,13), (13,13), arrow = False, solid = True)",
        "Line((9,10), (8,11), arrow = True, solid = True)",
        "Line((1,15), (9,7), arrow = False, solid = True)",
        "Line((5,7), (13,15), arrow = False, solid = True)",
    ]
)
groundTruth["drawings/expert-79.png"] = set(
    [
        "Line((7,5), (7,3), arrow = True, solid = True)",
        "Circle(center = (3,10), radius = 1)",
        "Circle(center = (7,6), radius = 1)",
        "Line((7,9), (7,7), arrow = True, solid = True)",
        "Line((11,9), (8,6), arrow = True, solid = True)",
        "Circle(center = (11,14), radius = 1)",
        "Circle(center = (11,10), radius = 1)",
        "Circle(center = (7,10), radius = 1)",
        "Line((3,13), (3,11), arrow = True, solid = True)",
        "Line((11,13), (11,11), arrow = True, solid = True)",
        "Circle(center = (3,14), radius = 1)",
        "Circle(center = (7,2), radius = 1)",
        "Circle(center = (7,14), radius = 1)",
        "Line((3,9), (6,6), arrow = True, solid = True)",
        "Line((7,13), (7,11), arrow = True, solid = True)",
    ]
)
groundTruth["drawings/expert-80.png"] = set(
    [
        "Circle(center = (10,14), radius = 1)",
        "Circle(center = (4,5), radius = 1)",
        "Circle(center = (10,8), radius = 1)",
        "Circle(center = (14,8), radius = 1)",
        "Circle(center = (2,8), radius = 1)",
        "Circle(center = (6,14), radius = 1)",
        "Line((6,7), (4,6), arrow = True, solid = True)",
        "Circle(center = (8,2), radius = 1)",
        "Circle(center = (12,11), radius = 1)",
        "Circle(center = (6,8), radius = 1)",
        "Line((12,10), (10,9), arrow = True, solid = True)",
        "Line((14,7), (12,6), arrow = True, solid = True)",
        "Line((2,7), (4,6), arrow = True, solid = True)",
        "Line((12,10), (14,9), arrow = True, solid = True)",
        "Line((11,11), (6,9), arrow = True, solid = True)",
        "Line((4,10), (6,9), arrow = True, solid = True)",
        "Circle(center = (4,11), radius = 1)",
        "Line((12,4), (8,3), arrow = True, solid = True)",
        "Circle(center = (12,5), radius = 1)",
        "Line((5,11), (10,9), arrow = True, solid = True)",
        "Circle(center = (2,14), radius = 1)",
        "Line((4,10), (2,9), arrow = True, solid = True)",
        "Line((6,13), (4,12), arrow = True, solid = True)",
        "Circle(center = (14,14), radius = 1)",
        "Line((4,4), (8,3), arrow = True, solid = True)",
        "Line((14,13), (12,12), arrow = True, solid = True)",
        "Line((2,13), (4,12), arrow = True, solid = True)",
        "Line((10,7), (12,6), arrow = True, solid = True)",
        "Line((10,13), (12,12), arrow = True, solid = True)",
    ]
)
groundTruth["drawings/expert-81.png"] = set(
    [
        "Circle(center = (2,14), radius = 1)",
        "Circle(center = (5,14), radius = 1)",
        "Rectangle((10,13), (12,15))",
        "Rectangle((7,13), (9,15))",
    ]
)
groundTruth["drawings/expert-82.png"] = set(
    [
        "Circle(center = (11,8), radius = 1)",
        "Line((9,14), (10,14), arrow = True, solid = True)",
        "Circle(center = (2,14), radius = 1)",
        "Line((8,7), (8,6), arrow = True, solid = True)",
        "Circle(center = (2,8), radius = 1)",
        "Circle(center = (8,11), radius = 1)",
        "Line((12,8), (14,10), arrow = True, solid = True)",
        "Line((9,11), (10,11), arrow = True, solid = True)",
        "Circle(center = (8,5), radius = 1)",
        "Circle(center = (11,11), radius = 1)",
        "Line((8,13), (8,12), arrow = True, solid = True)",
        "Line((2,7), (2,6), arrow = True, solid = True)",
        "Circle(center = (2,5), radius = 1)",
        "Line((4,9), (6,9), arrow = True, solid = True)",
        "Line((12,11), (13,11), arrow = True, solid = True)",
        "Line((12,14), (13,14), arrow = True, solid = True)",
        "Line((14,12), (14,13), arrow = True, solid = True)",
        "Circle(center = (2,11), radius = 1)",
        "Line((2,10), (2,9), arrow = True, solid = True)",
        "Circle(center = (8,8), radius = 1)",
        "Circle(center = (14,11), radius = 1)",
        "Line((2,13), (2,12), arrow = True, solid = True)",
        "Circle(center = (8,14), radius = 1)",
        "Line((8,10), (8,9), arrow = True, solid = True)",
        "Circle(center = (11,14), radius = 1)",
        "Line((9,8), (10,8), arrow = True, solid = True)",
        "Circle(center = (14,14), radius = 1)",
    ]
)
groundTruth["drawings/expert-83.png"] = set(
    [
        "Circle(center = (9,11), radius = 1)",
        "Line((4,13), (3,12), arrow = True, solid = True)",
        "Circle(center = (2,14), radius = 1)",
        "Line((2,13), (3,12), arrow = True, solid = True)",
        "Circle(center = (4,14), radius = 1)",
        "Line((8,13), (9,12), arrow = True, solid = True)",
        "Circle(center = (10,14), radius = 1)",
        "Circle(center = (8,14), radius = 1)",
        "Line((9,10), (6,9), arrow = True, solid = True)",
        "Circle(center = (3,11), radius = 1)",
        "Circle(center = (6,8), radius = 1)",
        "Line((10,13), (9,12), arrow = True, solid = True)",
        "Line((3,10), (6,9), arrow = True, solid = True)",
    ]
)
groundTruth["drawings/expert-84.png"] = set(
    [
        "Circle(center = (2,14), radius = 1)",
        "Line((7,8), (8,8), arrow = True, solid = True)",
        "Line((7,11), (8,11), arrow = True, solid = True)",
        "Line((2,13), (2,12), arrow = True, solid = True)",
        "Circle(center = (2,8), radius = 1)",
        "Line((10,11), (11,11), arrow = True, solid = True)",
        "Circle(center = (6,11), radius = 1)",
        "Line((7,14), (8,14), arrow = True, solid = True)",
        "Circle(center = (9,14), radius = 1)",
        "Circle(center = (6,14), radius = 1)",
        "Line((2,7), (2,6), arrow = True, solid = True)",
        "Circle(center = (2,5), radius = 1)",
        "Circle(center = (12,14), radius = 1)",
        "Circle(center = (12,11), radius = 1)",
        "Line((6,13), (6,12), arrow = True, solid = True)",
        "Line((10,8), (12,10), arrow = True, solid = True)",
        "Line((12,12), (12,13), arrow = True, solid = True)",
        "Circle(center = (2,11), radius = 1)",
        "Line((2,10), (2,9), arrow = True, solid = True)",
        "Circle(center = (6,5), radius = 1)",
        "Line((6,7), (6,6), arrow = True, solid = True)",
        "Line((6,10), (6,9), arrow = True, solid = True)",
        "Circle(center = (9,8), radius = 1)",
        "Circle(center = (9,11), radius = 1)",
        "Circle(center = (6,8), radius = 1)",
        "Line((10,14), (11,14), arrow = True, solid = True)",
    ]
)
groundTruth["drawings/expert-85.png"] = set(
    [
        "Line((3,13), (3,12), arrow = True, solid = True)",
        "Circle(center = (3,14), radius = 1)",
        "Line((3,7), (3,6), arrow = True, solid = True)",
        "Circle(center = (3,11), radius = 1)",
        "Line((3,10), (3,9), arrow = True, solid = True)",
        "Circle(center = (3,5), radius = 1)",
        "Circle(center = (3,8), radius = 1)",
    ]
)
groundTruth["drawings/expert-86.png"] = set(
    [
        "Rectangle((7,11), (9,13))",
        "Rectangle((6,7), (9,10))",
        "Rectangle((1,7), (2,8))",
        "Rectangle((1,12), (4,15))",
        "Rectangle((8,14), (9,15))",
        "Rectangle((1,9), (3,11))",
    ]
)
groundTruth["drawings/expert-87.png"] = set(
    [
        "Rectangle((8,7), (9,8))",
        "Rectangle((7,9), (9,11))",
        "Rectangle((1,7), (2,8))",
        "Rectangle((1,12), (4,15))",
        "Rectangle((6,12), (9,15))",
        "Rectangle((1,9), (3,11))",
    ]
)
groundTruth["drawings/expert-88.png"] = set(
    [
        "Rectangle((1,8), (9,15))",
        "Rectangle((3,9), (8,13))",
        "Rectangle((5,10), (7,11))",
    ]
)
groundTruth["drawings/expert-89.png"] = set(
    [
        "Line((10,8), (11,7), arrow = False, solid = True)",
        "Line((13,7), (13,11), arrow = False, solid = True)",
        "Line((4,7), (4,10), arrow = False, solid = True)",
        "Circle(center = (10,11), radius = 1)",
        "Line((9,11), (8,11), arrow = True, solid = True)",
        "Line((13,7), (11,7), arrow = True, solid = True)",
        "Line((10,12), (10,14), arrow = False, solid = True)",
        "Line((7,11), (5,11), arrow = True, solid = True)",
        "Line((11,11), (13,11), arrow = False, solid = True)",
        "Rectangle((2,6), (14,15))",
        "Rectangle((3,10), (5,12))",
        "Line((10,8), (10,10), arrow = True, solid = True)",
        "Line((7,10), (8,11), arrow = False, solid = True)",
        "Line((1,11), (3,11), arrow = True, solid = True)",
        "Line((10,14), (1,14), arrow = True, solid = True)",
        "Line((4,7), (9,7), arrow = True, solid = True)",
    ]
)
groundTruth["drawings/expert-90.png"] = set(
    [
        "Line((11,13), (8,13), arrow = True, solid = True)",
        "Circle(center = (7,8), radius = 1)",
        "Line((7,12), (7,9), arrow = True, solid = True)",
        "Circle(center = (7,13), radius = 1)",
        "Rectangle((5,6), (9,15))",
        "Circle(center = (12,13), radius = 1)",
        "Line((6,13), (3,13), arrow = True, solid = True)",
        "Circle(center = (2,13), radius = 1)",
    ]
)
groundTruth["drawings/expert-91.png"] = set(
    [
        "Line((4,15), (6,15), arrow = False, solid = True)",
        "Line((1,10), (3,10), arrow = False, solid = True)",
        "Line((6,10), (6,12), arrow = False, solid = True)",
        "Line((6,13), (6,15), arrow = False, solid = True)",
        "Line((1,15), (3,15), arrow = False, solid = True)",
        "Line((1,10), (1,12), arrow = False, solid = True)",
        "Line((1,13), (1,15), arrow = False, solid = True)",
        "Line((4,10), (6,10), arrow = False, solid = True)",
    ]
)
groundTruth["drawings/expert-92.png"] = set(
    [
        "Circle(center = (6,6), radius = 1)",
        "Rectangle((13,13), (15,15))",
        "Circle(center = (10,10), radius = 1)",
        "Line((3,6), (5,6), arrow = False, solid = True)",
        "Circle(center = (6,10), radius = 1)",
        "Line((11,14), (13,14), arrow = False, solid = True)",
        "Line((11,10), (13,10), arrow = False, solid = True)",
        "Line((3,10), (5,10), arrow = False, solid = True)",
        "Circle(center = (10,14), radius = 1)",
        "Rectangle((1,5), (3,7))",
        "Circle(center = (6,14), radius = 1)",
        "Line((11,6), (13,6), arrow = False, solid = True)",
        "Rectangle((1,13), (3,15))",
        "Circle(center = (10,6), radius = 1)",
        "Line((3,14), (5,14), arrow = False, solid = True)",
        "Rectangle((13,9), (15,11))",
        "Rectangle((1,9), (3,11))",
        "Rectangle((13,5), (15,7))",
    ]
)
groundTruth["drawings/expert-93.png"] = set(
    [
        "Circle(center = (2,14), radius = 1)",
        "Circle(center = (2,6), radius = 1)",
        "Line((2,7), (6,9), arrow = True, solid = True)",
        "Line((10,7), (6,9), arrow = True, solid = True)",
        "Circle(center = (6,10), radius = 1)",
        "Line((6,11), (10,13), arrow = True, solid = True)",
        "Circle(center = (10,14), radius = 1)",
        "Line((6,11), (2,13), arrow = True, solid = True)",
        "Circle(center = (10,6), radius = 1)",
    ]
)
groundTruth["drawings/expert-94.png"] = set(
    [
        "Line((1,5), (10,14), arrow = False, solid = True)",
        "Line((7,7), (7,8), arrow = True, solid = True)",
        "Line((11,12), (8,9), arrow = True, solid = True)",
        "Line((4,14), (13,5), arrow = False, solid = True)",
        "Line((1,7), (13,7), arrow = False, solid = True)",
        "Line((3,12), (6,9), arrow = True, solid = True)",
    ]
)
groundTruth["drawings/expert-95.png"] = set(
    [
        "Line((8,13), (2,10), arrow = True, solid = True)",
        "Line((2,13), (2,10), arrow = True, solid = True)",
        "Circle(center = (5,4), radius = 1)",
        "Line((2,8), (5,5), arrow = True, solid = True)",
        "Line((8,8), (5,5), arrow = True, solid = True)",
        "Line((2,13), (8,10), arrow = True, solid = True)",
        "Circle(center = (2,9), radius = 1)",
        "Circle(center = (2,14), radius = 1)",
        "Circle(center = (8,14), radius = 1)",
        "Circle(center = (8,9), radius = 1)",
        "Line((8,13), (8,10), arrow = True, solid = True)",
    ]
)
groundTruth["drawings/expert-96.png"] = set(
    [
        "Circle(center = (10,14), radius = 1)",
        "Circle(center = (8,12), radius = 1)",
        "Circle(center = (6,10), radius = 1)",
        "Circle(center = (2,14), radius = 1)",
        "Circle(center = (10,6), radius = 1)",
        "Circle(center = (4,8), radius = 1)",
        "Circle(center = (4,12), radius = 1)",
        "Circle(center = (2,6), radius = 1)",
        "Circle(center = (8,8), radius = 1)",
    ]
)
groundTruth["drawings/expert-97.png"] = set(
    [
        "Circle(center = (6,6), radius = 1)",
        "Line((2,11), (2,13), arrow = False, solid = True)",
        "Circle(center = (2,6), radius = 1)",
        "Line((3,6), (5,6), arrow = False, solid = True)",
        "Circle(center = (6,10), radius = 1)",
        "Line((2,7), (2,9), arrow = False, solid = True)",
        "Line((6,7), (6,9), arrow = False, solid = True)",
        "Circle(center = (2,14), radius = 1)",
        "Circle(center = (6,14), radius = 1)",
        "Line((6,11), (6,13), arrow = False, solid = True)",
        "Line((3,10), (5,10), arrow = False, solid = True)",
        "Line((3,14), (5,14), arrow = False, solid = True)",
        "Circle(center = (2,10), radius = 1)",
    ]
)
groundTruth["drawings/expert-98.png"] = set(
    [
        "Circle(center = (5,9), radius = 1)",
        "Rectangle((3,3), (7,12))",
        "Circle(center = (5,14), radius = 1)",
        "Line((5,13), (5,10), arrow = True, solid = True)",
        "Circle(center = (5,5), radius = 1)",
        "Line((5,8), (5,6), arrow = True, solid = True)",
    ]
)
groundTruth["drawings/expert-99.png"] = set(
    [
        "Circle(center = (2,8), radius = 1)",
        "Rectangle((4,7), (6,9))",
        "Rectangle((1,10), (3,12))",
        "Rectangle((1,4), (3,6))",
        "Circle(center = (2,14), radius = 1)",
        "Circle(center = (5,11), radius = 1)",
        "Rectangle((4,13), (6,15))",
        "Circle(center = (5,5), radius = 1)",
    ]
)


def parseLineOfCode(l):
    points = [
        AbsolutePoint((int(x)), (int(y)))
        for x, y in re.findall("\(([0-9]+),([0-9]+)\)", l)
    ]
    if l.startswith("Line"):
        arrow = "arrow = True" in l
        solid = "solid = True" in l
        return Line(points, arrow, solid)
    if l.startswith("Circle"):
        return Circle(points[0], (1))
    if l.startswith("Rectangle"):
        return Rectangle(points[0], points[1])
    assert False


groundTruthSequence = {}
for k in groundTruth:
    groundTruthSequence[k] = Sequence([parseLineOfCode(l) for l in groundTruth[k]])


def getGroundTruthParse(f):
    if f.startswith("/om/user/ellisk/"):
        f = f[len("/om/user/ellisk/") :]
    return groundTruthSequence.get(f, None)


def prettyGroundTruth(j):
    stuff = (
        "\n".join(groundTruth["drawings/expert-%d.png" % j])
        .replace(", radius = 1", "")
        .replace("center = ", "")
    )
    stuff = stuff.replace(", arrow = False", "")
    stuff = stuff.replace(", solid = True", "")
    stuff = (
        stuff.replace("((", "(")
        .replace("))", ")")
        .replace("), ", ",")
        .replace(",(", ",")
    )
    print(stuff)


if __name__ == "__main__":
    if False:
        print(
            "\n\n".join(
                [
                    "\n".join(groundTruth["drawings/expert-%d.png" % j])
                    for j in [29, 52, 38, 75, 72]
                ]
            )
        )
        assert False
        for k in groundTruthSequence:
            x = np.zeros((256 * 2, 256))
            print(k)
            print(groundTruthSequence[k])
            x[0:256, :] = loadImage(k)
            x[256:, :] = groundTruthSequence[k].draw()
            showImage(x)
    else:
        prettyGroundTruth(7)
