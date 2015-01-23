__author__ = 'zieghailo'

import unittest
import numpy.testing as nptest
from trimath import *

class MyTestCase(unittest.TestCase):
    def test_rand_point(self):
        tr = np.array([[1, 2, 3], [3, 1, 2]])

        for i in range(100):
            p = rand_point_in_triangle(tr)
            self.assertTrue(in_triangle(p, tr))

    def test_in_triangle(self):
        triang = np.array([[1, 2, 3], [3, 1, 2]])

        p1 = np.array([1.5, 1])
        self.assertFalse(in_triangle(p1, triang))

        p2 = np.array([1.5, 2.1])
        self.assertTrue(in_triangle(p2, triang))

        p3 = np.array([2, 1.1])
        self.assertTrue(in_triangle(p3, triang))

        p4 = np.array([2, 2.6])
        self.assertFalse(in_triangle(p4, triang))

        p5 = np.array([2.5, 1.4])
        self.assertFalse(in_triangle(p5, triang))

    def test_sum_row(self):
        from trimath import _sum_row

        img = np.array([range(100), range(100), range(100)])
        bounds = [0, 39]
        y = 0

        s, n = _sum_row(img, y, bounds)
        x = 39 * 20
        nptest.assert_array_equal(s, [x, x, x])

    def test_cv2_triangle_sum(self):
        #chessboard
        img = np.ones([1000, 1000, 3])
        for x in range(1000):
            for y in range(1000):
                for z in range(3):
                    img[x,y,z] = (x + y) % 2

        img *= 255

        tr = np.array([[100, 200, 300], [300, 100, 200]])

        from trimath import cv2_triangle_sum
        import numpy.testing as nptest

        res = cv2_triangle_sum(img, tr)
        color = res[0]
        error = res[1]
        nptest.assert_allclose(color[0], 0.5, atol=0.01)
        nptest.assert_allclose(color[1], 0.5, atol=0.01)
        nptest.assert_allclose(color[2], 0.5, atol=0.01)



if __name__ == '__main__':
    unittest.main()
