import homwork
import unittest

class TestStringMethods(unittest.TestCase):

    def test_frst_letr_upper(self):
        self.assertTrue(homwork.frst_lettr_upper("Movses Seyranyan"))
        self.assertTrue(homwork.frst_lettr_upper ("Movses going in the sity"))
        self.assertRaises(Exception, homwork.frst_lettr_upper , "hello")
        self.assertRaises(ValueError, homwork.frst_lettr_upper, ["20"] )
        self.assertRaises(ValueError, homwork.frst_lettr_upper,  20 )

    def test_this_string_is_sentence(self):
        self.assertTrue(homwork.this_string_is_sentence("Hello hou are you."))
        self.assertRaises(TypeError, homwork.this_string_is_sentence, 20)
        self.assertRaises(Exception, homwork.this_string_is_sentence , "Hello hou are you...")
        self.assertRaises(Exception, homwork.this_string_is_sentence , "hello hou are you.")


    def test_dis_string_is_natural_number(self):
        self.assertRaises(TypeError, homwork.natural_number, 20)
        self.assertRaises(TypeError, homwork.natural_number, -20)
        self.assertRaises(Exception, homwork.natural_number, " 20 ")
        self.assertRaises(Exception, homwork.natural_number, "020")
        self.assertRaises(Exception, homwork.natural_number, "j20")
        self.assertRaises(Exception, homwork.natural_number, "-20")
        self.assertTrue(homwork.natural_number, "20")
        
        
        


if __name__ == '__main__':
    unittest.main()