RULE_VALID_COUNTRIES = {"Argentina", "Australia", "Austria", "Belgium", "Brazil", "Canada", "Chile", "Costa Rica",
                        "Czech Republic", "Denmark", "Estonia", "Fiji", "Finland", "France", "Germany", "Great Britain",
                        "Greenland", "Hong Kong", "Iceland", "India", "Indonesia", "Ireland", "Isle of Man", "Israel",
                        "Italy", "Japan", "Latvia", "Luxembourg", "Malaysia", "Mexico", "Netherlands", "New Zealand",
                        "Northern Ireland", "Norway", "Oman", "Pakistan", "People's Republic of China", "Poland", "Portugal",
                        "Puerto Rico", "Taiwan", "Romania", "Russia", "Scotland", "Singapore", "South Africa", "South Korea",
                        "Spain", "Sweden", "Switzerland", "Ukraine", "United States", "Uruguay", "Venezuela"}


RULE_VALID_PROVINCES = {'Australia': {'NSW', 'NT', 'QLD', 'SA', 'TAS', 'VIC', 'WA'},
                        'Brazil': {"AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA",
                                   "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN",
                                   "RS", "RO", "RR", "SC", "SP", "SE", "TO"},
                        'Canada': {"AB", "BC", "MB", "NB", "NL", "NT", "NS", "NU", "ON", "PE", "QC", "SK", "YT"},
                        'Hong Kong': {'HONG KONG', 'KOWLOON', 'NEW TERRITORIES'},
                        'Mexico': {"AGS", "MOR", "NAY", "BCS", "CAM", "OAX", "COAH", "PUE", "COL", "QRO", "CHIS",
                                   "Q ROO", "CHIH", "SLP", "SIN", "DGO", "SON", "GTO", "TAB", "GRO",
                                   "TAMPS", "HGO", "TLAX", "JAL", "VER", "MEX", "YUC", "MICH", "ZAC"},
                        'United States': {"AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
                                          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
                                          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
                                          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
                                          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"}
                        }

# standard is street, postcode, country and optional

# postcode validation done with list of elems by country
# first element describes length of postcode, if multiple fields indicates format


# If country in alphanumeric don't enforce numeric restriction
RULE_ALPHANUMERIC_POSTCODES = {'Argentina', 'Canada', 'Great Britain', 'Ireland',
                               'Isle of Man', 'Northern Ireland', 'Scotland', 'Netherlands'}

RULE_VALID_POSTCODES = {"Argentina": [8], "Australia": [4], "Austria": [4], "Belgium": [4],
                        "Brazil": [5, 3, '-'], "Canada": [3, 3, '-'], "Chile": [4], "Costa Rica": [5],
                        "Czech Republic": [3, 2, '-'], "Denmark": [4], "Estonia": [5], "Finland": [5],
                        "France": [5], "Germany": [5], "Great Britain": [4, 3, ' '], "Greenland": [4],
                        "Iceland": [3], "India": [6], "Indonesia": [5], "Ireland": [3, 4, ' '],
                        "Isle of Man": [4, 3, ' '], "Israel": [5], "Italy": [5], "Japan": [3, 4, '-'],
                        "Latvia": [4], "Luxembourg": [4], "Malaysia": [5], "Mexico": [5], "Netherlands": [4, 2, ' '],
                        "New Zealand": [4], "Northern Ireland": [4, 3, ' '], "Norway": [4], "Oman": [3],
                        "Pakistan": [5], "People's Republic of China": [6], "Poland": [2, 3, '-'],
                        "Portugal": [4, 3, '-'], "Puerto Rico": [5, 4, '-'], "Taiwan": [5], "Romania": [6],
                        "Russia": [6], "Scotland": [4, 3, ' '], "Singapore": [6],
                        "South Africa": [4], "Spain": [5], "Sweden": [3, 2, ' '], "Switzerland": [4],
                        "Ukraine": [5], "United States": [5], "Uruguay": [5], "Venezuela": [4]}

#standard fields
#since validity on these is checked before translating to standard fields we
#need to use the specific field names in some cases

#rename city to city/locality
standard = ['Street 1', 'City', 'Postcode', 'Country']
street1 = ['Street 1']
city = ['City']
postcode = ['Postcode']
country = ['Country']
state = ['State']
street2 = ['Street 2']
district = ['District']
province = ['Province']
locality = ['Locality']
apt = ['Apt Number']
floor = ['Floor']
building_name = ['Building Name']
house = ['House']
county = ['County']
block = ['Block']
building_number = ['Building Number']
department = ['Department']
post_office_code = ['Post Office Code']
zone = ['Zone']
entrance = ['Entrance']

#TODO place field ordering logic in different section
RULE_REQUIRED_FIELDS = {"Argentina": standard,
                        "Australia": standard + state,
                        "Austria": standard,
                        "Belgium": standard,
                        "Brazil": standard + province,
                        "Canada": standard + province,
                        "Chile": standard,
                        "Costa Rica": standard + province + district,
                        "Czech Republic": standard + post_office_code,
                        "Denmark": standard,
                        "Estonia": standard,
                        "Fiji": street1 + city + country,
                        "Finland": standard,
                        "France": standard,
                        "Germany": standard,
                        "Great Britain": standard,
                        "Greenland": standard,
                        "Hong Kong": apt + floor + building_name + street1 + district + country,
                        "Iceland": standard,
                        "India": standard,
                        "Indonesia": standard + district,
                        "Ireland": standard,
                        "Isle of Man": standard,
                        "Israel": standard,
                        "Italy": standard + province,
                        "Japan": block + building_number + district + province + city + country,
                        "Latvia": standard,
                        "Luxembourg": standard,
                        "Malaysia": standard,
                        "Mexico": standard + state,
                        "Netherlands": standard,
                        "New Zealand": standard,
                        "Northern Ireland": standard,
                        "Norway": standard,
                        "Oman": standard,
                        "Pakistan": standard + house + district,
                        "People's Republic of China": standard + province,
                        "Poland": standard,
                        "Portugal": standard,
                        "Puerto Rico": standard,
                        "Taiwan": standard,
                        "Romania": standard + county,
                        "Russia": standard + district,
                        "Scotland": standard,
                        "Singapore": standard,
                        "South Africa": standard,
                        "South Korea": house + district + city + province + country,
                        "Spain": standard,
                        "Sweden": standard,
                        "Switzerland": standard,
                        "Ukraine": standard,
                        "United States": standard + state,
                        "Uruguay": standard,
                        "Venezuela": standard}

#cases where apt or house is required (HKG) keep apt or house as a field,
#or if it's the only field (CAN). If address 2 keep apt under that

RULE_OPTIONAL_FIELDS = {"Argentina": floor + department,
                        "Australia": street2,
                        "Brazil": district,
                        "Canada": apt,
                        "Costa Rica": floor,
                        "Czech Republic": block + building_number,
                        "Great Britain": county + building_name,
                        "Greenland": street2,
                        "Hong Kong": province,
                        "India": street2,
                        "Indonesia": street2,
                        "Ireland": street2 + zone,
                        "Isle of Man": county + building_name,
                        "Latvia": apt + floor,
                        "Malaysia": floor + building_name,
                        "New Zealand": apt + district,
                        "Northern Ireland": county + building_name,
                        "Puerto Rico": apt,
                        "Taiwan": street2,
                        "Romania": street2 + apt,
                        "Russia": district + province,
                        "Scotland": county + building_name,
                        "Singapore": street2,
                        "Sweden": apt,
                        "Switzerland": building_number + apt,
                        "Ukraine": apt,
                        "United States": street2,
                        "Uruguay": province,
                        "Venezuela": street2}
