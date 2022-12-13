
import unittest
from AddressParse import AddressParse

test_addresses = [('Winterallee 3', {'street': 'Winterallee', 'housenumber': '3'}) 
    , ( 'Musterstrasse 45' , {'street': 'Musterstrasse', 'housenumber': '45'} )
    , ( 'Blaufeldweg 123B' , {'street': 'Blaufeldweg', 'housenumber': '123B'} )
    , ( 'Am Bächle 23' , {'street': 'Am Bächle', 'housenumber': '23'} )
    , ( 'Auf der Vogelwiese 23 b' , {'street': 'Auf der Vogelwiese', 'housenumber': '23 b'} )
    , ( '4, rue de la revolution' , {'street': 'rue de la revolution', 'housenumber': '4'} )
    , ( '200 Broadway Av' , {'street': 'Broadway Av', 'housenumber': '200'} )
    , ( 'Calle Aduana, 29' , {'street': 'Calle Aduana', 'housenumber': '29'} )
    , ( 'Calle 39 No 1540' , {'street': 'Calle 39', 'housenumber': 'No 1540'} )
]

class TestAddress(unittest.TestCase):
    def __init__(self, input, output):
        super(TestAddress, self).__init__()
        self.input = input
        self.output = output
    def runTest(self):
        self.assertEqual(AddressParse(self.input).get_street_name_and_number(), self.output)

def suite():
    suite = unittest.TestSuite()
    suite.addTests(TestAddress(input, output) for input, output in test_addresses)
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())