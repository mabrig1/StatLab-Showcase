import unittest
from frequencies import summarize

class FrequencyTests(unittest.TestCase):
    def test_symmetric(self):
        r = summarize([1,2,4,2,1])
        self.assertEqual(r["n"], 10)
        self.assertEqual(r["mean"], 3)
        self.assertAlmostEqual(r["population_sd"]**2, 1.2)
        self.assertAlmostEqual(r["sample_sd"]**2, 12/9)
        self.assertAlmostEqual(sum(r["percentages"]), 100)
    def test_single(self):
        self.assertIsNone(summarize([1,0,0,0,0])["sample_sd"])
    def test_invalid(self):
        for counts in ([0]*5, [-1,2,3,4,5], [True,0,0,0,0], [1]):
            with self.subTest(counts=counts), self.assertRaises(ValueError):
                summarize(counts)

if __name__ == "__main__":
    unittest.main()
