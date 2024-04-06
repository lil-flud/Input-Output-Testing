# from main import *
# import unittest


# class Test(unittest.TestCase):
#     def test_(self):
#         self.assertEqual(find_all_by_artist([
#             ('Title 1', 'Artist 1', ["Artist 2"], 'Album 1', 200, True),
#             ('Title 2', 'Artist 1', [], 'Album 1', 220, False),
#             ('Title 3', 'Artist 2', [], 'Album 2', 160, True),
#             ('Title 4', 'Artist 3', ["Artist 1",
#                                      "Artist 2", "Artist 5"], 'Album 3', 260, True),
#             ('Title 5', 'Artist 3', ["Artist 1",
#              "Artist 5"], 'Album 3', 260, True)

#         ], "Artist 2"), [
#             ('Title 1', 'Artist 1', ["Artist 2"], 'Album 1', 200, True),
#             ('Title 3', 'Artist 2', [], 'Album 2', 160, True),
#             ('Title 4', 'Artist 3', [
#                 "Artist 1", "Artist 2", "Artist 5"], 'Album 3', 260, True),
#         ])

#     def test2_(self):
#         self.assertEqual(find_all_shorter_than([
#             ('Title 1', 'Artist 1', [], 'Album 1', 200, True),
#             ('Title 2', 'Artist 1', [], 'Album 1', 220, False),
#             ('Title 3', 'Artist 2', [], 'Album 2', 160, True),
#             ('Title 4', 'Artist 3', [], 'Album 3', 260, True),
#         ], 250), [
#             ('Title 1', 'Artist 1', [], 'Album 1', 200, True),
#             ('Title 2', 'Artist 1', [], 'Album 1', 220, False),
#             ('Title 3', 'Artist 2', [], 'Album 2', 160, True),
#         ])

#     def test3_(self):
#         self.assertEqual(find_all_by_artist([
#             ('Title 1', 'Artist 1', ["Artist 2"], 'Album 1', 200, True),
#             ('Title 2', 'Artist 1', [], 'Album 1', 220, False),
#             ('Title 3', 'Artist 2', [], 'Album 2', 160, True),
#             ('Title 4', 'Artist 3', [
#                 "Artist 1", "Artist 2", "Artist 5"], 'Album 3', 260, True)
#         ], "Artist 2"), [
#             ('Title 1', 'Artist 1', ["Artist 2"], 'Album 1', 200, True),
#             ('Title 3', 'Artist 2', [], 'Album 2', 160, True),
#             ('Title 4', 'Artist 3', [
#              "Artist 1", "Artist 2", "Artist 5"], 'Album 3', 260, True),
#         ])

#     def test4_(self):
#         self.assertEqual(find_all_favorites([]), [])

#     def test5_(self):
#         self.assertEqual(find_all_favorites([
#             ('Title 1', 'Artist 1', [], 'Album 1', 200, False),
#             ('Title 2', 'Artist 1', [], 'Album 1', 220, False),
#             ('Title 3', 'Artist 2', [], 'Album 2', 160, False),
#             ('Title 4', 'Artist 3', [], 'Album 3', 260, False)
#         ]), [])

#     def test6_(self):
#         self.assertEqual(find_all_favorites([
#             ('Title 1', 'Artist 1', [], 'Album 1', 200, True),
#             ('Title 2', 'Artist 1', [], 'Album 1', 220, False),
#             ('Title 3', 'Artist 2', [], 'Album 2', 160, True),
#             ('Title 4', 'Artist 3', [], 'Album 3', 260, True),
#         ]), [
#             ('Title 1', 'Artist 1', [], 'Album 1', 200, True),
#             ('Title 3', 'Artist 2', [], 'Album 2', 160, True),
#             ('Title 4', 'Artist 3', [], 'Album 3', 260, True),
#         ])

#     def test7_(self):
#         self.assertEqual(find_all_by_artist([], 'Artist #'), [])

#     def test8_(self):
#         self.assertEqual(find_all_by_artist([
#             ('Title 1', 'Artist 1', [], 'Album 1', 200, True),
#             ('Title 2', 'Artist 1', [], 'Album 1', 220, False),
#             ('Title 3', 'Artist 2', [], 'Album 2', 160, True),
#             ('Title 4', 'Artist 3', [], 'Album 3', 260, True),
#         ], 'Artist 1'), [
#             ('Title 1', 'Artist 1', [], 'Album 1', 200, True),
#             ('Title 2', 'Artist 1', [], 'Album 1', 220, False)
#         ])

#     def test9_(self):
#         self.assertEqual(find_all_shorter_than([], 200), [])

#     def test10_(self):
#         self.assertEqual(find_all_shorter_than([
#             ('Title 1', 'Artist 1', [], 'Album 1', 200, True),
#             ('Title 2', 'Artist 1', [], 'Album 1', 220, False),
#             ('Title 3', 'Artist 2', [], 'Album 2', 160, True),
#             ('Title 4', 'Artist 3', [], 'Album 3', 260, True),
#         ], 200), [
#             ('Title 3', 'Artist 2', [], 'Album 2', 160, True),
#         ])

#     def test11_(self):
#         self.assertEqual(find_all_shorter_than([
#             ('Title 1', 'Artist 1', [], 'Album 1', 200, True),
#             ('Title 2', 'Artist 1', [], 'Album 1', 220, False),
#             ('Title 3', 'Artist 2', [], 'Album 2', 160, True),
#             ('Title 4', 'Artist 3', [], 'Album 3', 260, True),
#         ], 100),  [])


# import io
# import unittest
# from contextlib import redirect_stdout
# from main import *


# class TestOutput(unittest.TestCase):
#     def test_output(self):
#         # Arrange
#         expected_output = "Yolo, fam!\n"

#         # Act
#         with io.StringIO() as buffer, redirect_stdout(buffer):
#             my_function_output = myFunction()

#             # Assert
#             self.assertEqual(buffer.getvalue(), expected_output,
#                              "Output does not match expected output")


# if __name__ == '__main__':
#     unittest.main()

# import io
# from contextlib import redirect_stdout
# import unittest
# from unittest.mock import patch

# from main import *


# class TestCollectBlessings(unittest.TestCase):
#     @patch('builtins.input', side_effect=['First blessing', 'Second blessing', 'q'])
#     def test_collect_blessings(self, mock_input):
#         # Arrange
#         expected_output = "Enter the things you are thankful for or enter 'q' to quit.\n> " \
#                           "Enter the things you are thankful for or enter 'q' to quit.\n> " \
#                           "Enter the things you are thankful for or enter 'q' to quit.\n> "

#         # Act
#         with io.StringIO() as buffer, redirect_stdout(buffer):
#             blessings = collect_blessings()

#             # Assert
#             self.assertEqual(blessings, [
#                              'First blessing', 'Second blessing'], "Blessings not collected correctly")

#             self.assertEqual(buffer.getvalue(), expected_output,
#                              "Output does not match expected output")

#     def test_display_blessings(self):
#         # Arrange
#         blessings = ['First blessing', 'Second blessing']
#         expected_output = "Wow! You're thankful for 2 things!\n" \
#                           "Here they are again:\n" \
#                           "First blessing\n" \
#                           "Second blessing\n"

#         # Act
#         with io.StringIO() as buffer, redirect_stdout(buffer):
#             display_blessings(blessings)

#             # Assert
#             self.assertEqual(buffer.getvalue(), expected_output,
#                              "Output does not match expected output")


# if __name__ == '__main__':
#     unittest.main()


# import io
# import sys
# from contextlib import redirect_stdout
# import unittest
# from unittest.mock import patch

# from main import *

# class TestCollectBlessings(unittest.TestCase):


# @patch('builtins.input', side_effect=['First blessing', 'Second blessing', 'q'])
# def test_collect_blessings(self):
#     capturedOutput = io.StringIO()
#     sys.stdout = capturedOutput
#     blessings = collect_blessings()
#     sys.stdout = sys.__stdout__
#     assert blessings == ["First blessing", "Second blessing"]

# class TestCollectBlessings(unittest.TestCase):
#     @patch('builtins.input', side_effect=['First blessing', 'Second blessing', 'q'])
#     def test_collect_blessings(self, mock_input):
#         # Arrange
#         expected_output = "Enter the things you are thankful for or enter 'q' to quit.\n> " \
#                           "Enter the things you are thankful for or enter 'q' to quit.\n> " \
#                           "Enter the things you are thankful for or enter 'q' to quit.\n> "

#         # Act
#         with io.StringIO() as buffer, redirect_stdout(buffer):
#             blessings = collect_blessings()
#             outputs = "" + f"{buffer.getvalue()} "

#             # Assert
#             self.assertEqual(blessings, [
#                              'First blessing', 'Second blessing'], "Blessings not collected correctly")
#             self.assertEqual(outputs, expected_output,
#                              "Output does not match expected output")

#     def test_display_blessings(self):
#         # Arrange
#         blessings = ['First blessing', 'Second blessing']
#         expected_output = "Wow! You're thankful for 2 things!\n" \
#                           "Here they are again:\n" \
#                           "First blessing\n" \
#                           "Second blessing\n"

#         # Act
#         with io.StringIO() as buffer, redirect_stdout(buffer):
#             display_blessings(blessings)

#             # Assert
#             self.assertEqual(buffer.getvalue(), expected_output,
#                              "Output does not match expected output")


# if __name__ == '__main__':
#     unittest.main()


import io
from contextlib import redirect_stdout
import unittest
from unittest.mock import patch
from main import *


class TestMainFunction(unittest.TestCase):
    @patch('builtins.input', side_effect=['First blessing', 'q'])
    def test_one_bless(self, mock_input):
        # Arrange
        expected_output = "Welcome to Count Your Blessings\n" \
                          "Wow! You're thankful for 1 things!\n" \
                          "Here they are again:\n" \
                          "First blessing\n"

        # Act
        with io.StringIO() as buffer, redirect_stdout(buffer):
            main()

            # print(f"{buffer.getvalue()}")
            # Assert
            self.assertEqual(buffer.getvalue(), expected_output,
                             "Output does not match expected output")

    @patch('builtins.input', side_effect=['First blessing', "Second blessing", "Third blessing", 'q'])
    def test_three_bless(self, mock_input):
        # Arrange
        expected_output = "Welcome to Count Your Blessings\n" \
                          "Wow! You're thankful for 3 things!\n" \
                          "Here they are again:\n" \
                          "First blessing\n" \
                          "Second blessing\n" \
                          "Third blessing\n"

        # Act
        with io.StringIO() as buffer, redirect_stdout(buffer):
            main()

            # print(f"{buffer.getvalue()}")
            # Assert
            self.assertEqual(buffer.getvalue(), expected_output,
                             "Output does not match expected output")


if __name__ == '__main__':
    unittest.main()
