import re
import logging

class AddressParse:
    def __init__(self, address):
        self.address = address

    def get_street_name_and_number(self):
        logging.info('----- Trying to get street name and house number for: {} ...'.format(self.address))
        # Most specific case with 'No'
        pattern = re.compile(r'(.+)\s+((No|no)\s?\d+\s?[a-cA-c]?)')
        match = pattern.search(self.address)
        # If a match is found, return a JSON object
        if match:
            return {
                'housenumber': match.group(2),
                'street': match.group(1)
            }
        # Try several regular expression patterns to match the street name and number, if house number at the end:
        pattern = re.compile(r'(.+)\s+(\d+\s?[a-cA-c]?)')
        match = pattern.search(self.address)
        # If a match is found, return a JSON object
        if match:
            return {
                'housenumber': match.group(2),
                'street': re.sub(',', '', match.group(1))
            }
        # If no match is found, try another pattern, if house number at the begining:
        pattern = re.compile(r'(\d+\s?[a-cA-c]?)\s?\W?\s+(.+)')
        match = pattern.search(self.address)
        
        if match:
            return {
                'housenumber': match.group(1),
                'street': match.group(2)
            }
        # If still no match is found, return None
        return None
