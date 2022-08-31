import unittest

from main import do_stuff


class TestMain(unittest.TestCase):
    def setUp(self):
        print('about to test a function')

    def test_do_stuff(self):
        test_param = 10
        result = do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'dsds'
        result = do_stuff(test_param)
        # self.assertEqual(result, TypeError)
        self.assertTrue(isinstance(result, ValueError))

    def test_do_stuff3(self):
        test_param = None
        result = do_stuff(test_param)
        # self.assertEqual(result, TypeError)

        self.assertIsInstance(result, TypeError)

    def test_do_stuff4(self):
        test_param = ()
        result = do_stuff(test_param)
        # self.assertEqual(result, TypeError)

        self.assertIsInstance(result, TypeError)

    def tearDown(self):
        print('cleaning up')


if (__name__) == '__main__':
    unittest.main()
