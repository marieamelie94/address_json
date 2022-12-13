import logging
from AddressParse import AddressParse

def main():
    sample_addresses = ['Winterallee 3'
        ,  'Musterstrasse 45'
        ,  'Blaufeldweg 123B' 
        ,  'Am Bächle 23' 
        ,  'Auf der Vogelwiese 23 b'
        ,  '4, rue de la revolution'
        ,  '200 Broadway Av'
        ,  'Calle Aduana, 29'
        ,  'Calle 39 No 1540'
    ]
    for address in sample_addresses:
        try:
            logging.info(AddressParse(address).get_street_name_and_number())
        except:
            logging.error('Address extraction failed for: {}'.format(address))

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s',
                        datefmt='[%Y-%m-%d %H:%M:%S]', level=logging.INFO)
    main()