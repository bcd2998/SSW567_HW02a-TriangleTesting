# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    #Test cases that I added
    #Equilateral Tests
    def test_equilateral1(self):
        self.assertEqual(classifyTriangle(5, 5, 5), 'Equilateral', '5,5,5 should be a equilateral')

    def test_equilateral2(self):
        self.assertEqual(classifyTriangle(7, 7, 7), 'Equilateral', '7,7,7 should be equilateral')

    def test_equilateral3(self):
        self.assertEqual(classifyTriangle(2, 2, 2), 'Equilateral', '2,2,2 should be equilateral')

    def test_equilateral4(self):
        self.assertEqual(classifyTriangle(1.2, 1.2, 1.2), 'Equilateral')

    #Isosceles Test
    def test_isosceles1(self):
        self.assertEqual(classifyTriangle(3, 3, 5), 'Isosceles')

    def test_isosceles2(self):
        self.assertEqual(classifyTriangle(4, 4, 7), 'Isosceles')

    def test_isosceles3(self):
        self.assertEqual(classifyTriangle(2, 2, 3), 'Isosceles')

    def test_isosceles4(self):
        self.assertEqual(classifyTriangle(2.1, 2.1, 3.1), 'Isosceles')

    def test_isosceles5(self):
        self.assertEqual(classifyTriangle(7, 4, 4), 'Isosceles')


    #Test Isosceles Right
    #def test_isoscelesright1(self):
    #    self.assertEqual(classifyTriangle(1, 1, 2**0.5), 'Isosceles Right')

    #def test_isoscelesright2(self):
    #    self.assertEqual(classifyTriangle(6.5, 6.5, 9.19238815543), 'Isosceles Right')

    # def test_isoscelesright3(self):
    #     self.assertNotEqual(classifyTriangle(4, 5, 6), 'Isosceles Right')

    # def test_isoscelesright4(self):
    #     self.assertNotEqual(classifyTriangle(3, 3, 3), 'Isosceles Right')

    # def test_isoscelesright5(self):
    #     self.assertNotEqual(classifyTriangle(3, 4, 5), 'Isosceles Right')

    #Test Scalene
    def test_scalene1(self):
        self.assertEqual(classifyTriangle(4, 5, 6), 'Scalene')

    def test_scalene2(self):
        self.assertEqual(classifyTriangle(6, 7, 8), 'Scalene')

    def test_scalene3(test):
        self.assertEqual(classifyTriangle(2, 3, 4), 'Scalene')

    def test_scalene4(self):
        self.assertEqual(classifyTriangle(4.2, 5.2, 6.4), 'Scalene')

    def test_scalene5(self):
        self.assertEqual(classifyTriangle(6, 5, 4), 'Scalene')


    #Test Scalene Right
    def test_scaleneright1(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Scalene Right')

    def test_scaleneright2(self):
        self.assertEqual(classifyTriangle(5, 12, 13), 'Scalene Right')

    def test_scaleneright3(self):
        self.assertEqual(classifyTriangle(9, 12, 15), 'Scalene Right')

    def test_scaleneright4(self):
        self.assertEqual(classifyTriangle(5, 4, 3), 'Scalene Right')


    #Test Not a Triangle
    def test_NotTriangle1(self):
        self.assertEqual(classifyTriangle(3, 2, 8), 'NotATriangle')

    def test_NotTriangle2(self):
        self.assertEqual(classifyTriangle(1, 2, 7), 'NotATriangle')

    def test_NotTriangle3(self):
        self.assertEqual(classifyTriangle(4, 3, 9), 'NotATriangle')


    #Test Invalid Input
    def test_invalidInput1(self):
        self.assertEqual(classifyTriangle(-2, -3, -5), 'InvalidInput')

    def test_invalidInput2(self):
        self.assertEqual(classifyTriangle(0, 1, 3), 'InvalidInput')

    def test_invalidInput3(self):
        self.assertEqual(classifyTriangle(201, 300, 400), 'InvalidInput')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

