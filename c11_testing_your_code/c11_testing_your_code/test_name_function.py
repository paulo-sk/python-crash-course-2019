import unittest 
from name_function import get_formated_name

class NameTestCase(unittest.TestCase):
    """test for name_function.py"""

    def test_first_last_name(self):
        """Do names like 'Janis joplin' works? """
        formatted_name = get_formated_name('Janis','Joplin','Awdas')
        self.assertEqual(formatted_name,'Janis Joplin Awdas')

if __name__ == '__main__':
    unittest.main()