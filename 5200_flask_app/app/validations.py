from app.valid_rules import RULE_REQUIRED_FIELDS, RULE_VALID_COUNTRIES, \
    RULE_ALPHANUMERIC_POSTCODES, RULE_OPTIONAL_FIELDS, RULE_VALID_POSTCODES, RULE_VALID_PROVINCES
import json
import app.db_functions as db_funcs


def validate_upload(data):
    if 'Country' not in data.keys():
        if 'country' in data.keys():
            data['Country'] = data.pop('country')
        else:
            return ({'status': 'Failure', 'message': 'No Country Provided'})
    try:
        if data['Country'] not in RULE_VALID_COUNTRIES:
            return ({'status': 'Failure', 'message': 'Invalid Country'})
        country = data['Country']
        required_fields = RULE_REQUIRED_FIELDS[country]
        print(required_fields)
        for field in required_fields:
            if field not in data.keys():
                return ({'status': 'Failure', 'message': 'Required Field not Found'})
        if country in RULE_VALID_POSTCODES.keys():
            postcode = str(data['Postcode'])
            print(postcode)
            valid_alpha = False
            if country in RULE_ALPHANUMERIC_POSTCODES:
                valid_alpha = True
            postcode_format = RULE_VALID_POSTCODES[country]
            if len(postcode_format) > 1:
                sep = postcode_format[-1]
                group1_len = postcode_format[0]
                group2_len = postcode_format[1]
                postcode_parsed = str.split(postcode, sep=sep, maxsplit=1)
                print('postcode parsed')
                print(postcode_parsed)
                if len(postcode_parsed[0]) != group1_len or len(postcode_parsed[1]) != group2_len:
                    return ({'status': 'Failure', 'message': 'Invalid Postcode'})
                if not valid_alpha:
                    if (str.isnumeric(postcode_parsed[0]) == False) or (str.isnumeric(postcode_parsed[1]) == False):
                        return ({'status': 'Failure', 'message': 'Invalid Postcode'})
            else:
                group_len = postcode_format[0]
                if len(postcode) != group_len:
                    return ({'status': 'Failure', 'message': 'Invalid Postcode'})
                if not valid_alpha:
                    if not str.isnumeric(postcode):
                        return ({'status': 'Failure', 'message':'Invalid Postcode'})
        if country in RULE_VALID_PROVINCES.keys():
            province_field = 'Province' if 'Province' in required_fields else 'State'
            print('province field')
            print(province_field)
            if data[province_field] not in RULE_VALID_PROVINCES[country]:
                return ({'status': 'Failure', 'message': 'Missing required province field'})
        #make database call here
        print('DATABASE CALL')
        data = collapse_to_schema(data)
        db_query = db_funcs.query(data)
        print(db_query)
        if(len(db_query) > 0):
            return({'status': 'Failure', 'message': 'Entry already in database'})
        id = db_funcs.create(data)
        print(id)
        #get guid on success
        return({'status': 'Success', 'data':'{}'.format(id)})
    except Exception as e:
        print(e)
        return json.dumps({'status': 'Failure', 'message':'Unknown Error occurred'})


#Enforce ordering
def validate_query(data):
    if 'Country' not in data.keys():
        if 'country' in data.keys():
            data['Country'] = data.pop('country')
        else:
            return ({'status': 'Failure', 'message': 'No Country Provided'})
    try:
        if data['Country'] == 'All Countries':
            data.pop('Country')
            data = db_funcs.query(data)
            return({'status': 'Success', 'data': data})
        if data['Country'] not in RULE_VALID_COUNTRIES:
            return ({'status': 'Failure', 'message': 'Invalid Country'})
        country = data['Country']
        required_fields = RULE_REQUIRED_FIELDS[country]
        print(required_fields)
        for field in required_fields:
            if field not in data.keys():
                return ({'status': 'Failure', 'message': 'Required Field not Found'})
        if country in RULE_VALID_POSTCODES.keys():
            postcode = str(data['Postcode'])
            print(postcode)
            valid_alpha = False
            if country in RULE_ALPHANUMERIC_POSTCODES:
                valid_alpha = True
            postcode_format = RULE_VALID_POSTCODES[country]
            if len(postcode_format) > 1:
                sep = postcode_format[-1]
                group1_len = postcode_format[0]
                group2_len = postcode_format[1]
                postcode_parsed = str.split(postcode, sep=sep, maxsplit=1)
                print('postcode parsed')
                print(postcode_parsed)
                if len(postcode_parsed[0]) != group1_len or len(postcode_parsed[1]) != group2_len:
                    return ({'status': 'Failure', 'message': 'Invalid Postcode'})
                if not valid_alpha:
                    if (str.isnumeric(postcode_parsed[0]) == False) or (str.isnumeric(postcode_parsed[1]) == False):
                        return ({'status': 'Failure', 'message': 'Invalid Postcode'})
            else:
                group_len = postcode_format[0]
                if len(postcode) != group_len:
                    return ({'status': 'Failure', 'message': 'Invalid Postcode'})
                if not valid_alpha:
                    if not str.isnumeric(postcode):
                        return ({'status': 'Failure', 'message':'Invalid Postcode'})
        if country in RULE_VALID_PROVINCES.keys():
            province_field = 'Province' if 'Province' in required_fields else 'State'
            print('province field')
            print(province_field)
            if data[province_field] not in RULE_VALID_PROVINCES[country]:
                return ({'status': 'Failure', 'message': 'Missing required province field'})
        #make database call here
        print('DATABASE CALL')
        res = db_funcs.query(data)
        return({'status': 'Success', 'data': res})
    except:
        return({'status': 'Failure', 'message': 'Unknown error'})




def validate_update(data, route_id):
    try:
        if 'addressID' not in data.keys():
            return {'status': 'Failure', 'message': 'Missing addressID'}
        id = data['addressID']
        if str(id) != str(route_id):
            return {'status': 'Failure', 'message': 'Route must match address id in payload'}
        if data['Country'] not in RULE_VALID_COUNTRIES:
            return ({'status': 'Failure', 'message': 'Invalid Country'})
        country = data['Country']
        required_fields = RULE_REQUIRED_FIELDS[country]
        print(required_fields)
        for field in required_fields:
            if field not in data.keys():
                return ({'status': 'Failure', 'message': 'Required Field not Found'})
        if country in RULE_VALID_POSTCODES.keys():
            postcode = str(data['Postcode'])
            print(postcode)
            valid_alpha = False
            if country in RULE_ALPHANUMERIC_POSTCODES:
                valid_alpha = True
            postcode_format = RULE_VALID_POSTCODES[country]
            if len(postcode_format) > 1:
                sep = postcode_format[-1]
                group1_len = postcode_format[0]
                group2_len = postcode_format[1]
                postcode_parsed = str.split(postcode, sep=sep, maxsplit=1)
                print('postcode parsed')
                print(postcode_parsed)
                if len(postcode_parsed[0]) != group1_len or len(postcode_parsed[1]) != group2_len:
                    return ({'status': 'Failure', 'message': 'Invalid Postcode'})
                if not valid_alpha:
                    if (str.isnumeric(postcode_parsed[0]) == False) or (str.isnumeric(postcode_parsed[1]) == False):
                        return ({'status': 'Failure', 'message': 'Invalid Postcode'})
            else:
                group_len = postcode_format[0]
                if len(postcode) != group_len:
                    return ({'status': 'Failure', 'message': 'Invalid Postcode'})
                if not valid_alpha:
                    if not str.isnumeric(postcode):
                        return ({'status': 'Failure', 'message':'Invalid Postcode'})
        if country in RULE_VALID_PROVINCES.keys():
            province_field = 'Province' if 'Province' in required_fields else 'State'
            print('province field')
            print(province_field)
            if data[province_field] not in RULE_VALID_PROVINCES[country]:
                return ({'status': 'Failure', 'message': 'Missing required province field'})
        #make database call here
        print('DATABASE CALL')
        query = db_funcs.query({'_id': id})
        if len(query) < 1:
            return ({'status': 'Failure', 'message': 'Entry not found'})
        updated_data = db_funcs.update(id)
        return({'status': 'Success', 'data': updated_data})
    except:
        return {'status': 'Failure', 'message': 'Unknown error'}

FIELD_POOL = {'Building Number',
               'Floor',
               'County',
               'Street 1',
               'City',
               'Postcode',
               'Province',
               'Post Office Code',
               'Building Name',
               'Block',
               'District',
               'Country',
               'State',
               'Apt Number',
               'House'}

def collapse_to_schema(country_dict):
    collapsed_schema = {'apt': '', 'street1': '', 'street2': '',
                        'postcode': '', 'district': '', 'city': '', 'county': '', 'state': '', 'country': ''}
    current_country = country_dict['Country']
    country_fields = country_dict.keys()
    if 'Province' in country_fields:
        collapsed_schema['state'] = country_dict['Province']
    elif 'State' in country_fields:
        collapsed_schema['state'] = country_dict['State']
    if 'Street 2' in country_fields:
        collapsed_schema['street2'] = country_dict['Street 2']
    if 'Postcode' in country_fields:
        collapsed_schema['postcode'] = country_dict['Postcode']
    if 'Street 2' in country_fields:
        collapsed_schema['street2'] = country_dict['Street 2']
    if 'District' in country_fields:
        collapsed_schema['district'] = country_dict['District']
    if 'City' in country_fields:
        collapsed_schema['city'] = country_dict['City']
    if 'County' in country_fields:
        collapsed_schema['county'] = country_dict['County']
    if 'Country' in country_fields:
        collapsed_schema['country'] = country_dict['Country']
    if current_country == 'Argentina'.upper():
        if 'Floor' in country_dict.keys():
            collapsed_schema['street2'] = country_dict['Floor']
        if 'Department' in country_dict.keys():
            collapsed_schema['apt'] = country_dict['Department']
    if current_country == 'Costa Rica'.upper():
        if 'Floor' in country_dict.keys():
            country_dict['street2'] = 'floor'
    if current_country == 'Czech Republic'.upper():
        if 'Post Office Code' in country_dict.keys():
            collapsed_schema['city'] = '{},{}'.format(collapsed_schema['city'], country_dict['Post Office Code'])
        if 'Building Number' in country_dict.keys():
            collapsed_schema['street2'] = country_dict['Building Number']
    if current_country in ['Great Britain'.upper(), 'Isle of Man'.upper(), 'Malaysia'.upper(), 'Northern Ireland'.upper(), 'Scotland'.upper()] and 'Building Name' in country_dict.keys():
        collapsed_schema['street2'] = country_dict['Building Name']
    if current_country == 'Ireland' and 'Zone' in country_dict.keys():
        collapsed_schema['city'] = '{},{}'.format(collapsed_schema['city'], country_dict['Zone'])
    if current_country == 'Hong Kong'.upper():
        collapsed_schema['street2'] = '{},{}'.format(country_dict['Building Name'], country_dict['Floor'])
    if current_country == 'Japan'.upper():
        collapsed_schema['street2'] = '{},{}'.format(country_dict['Block'], country_dict['Building Number'])
    if current_country == 'Pakistan'.upper():
        collapsed_schema['apt'] = country_dict['House']
    if current_country == 'South Korea'.upper():
        collapsed_schema['apt'] = country_dict['House']
    if current_country == 'Switzerland'.upper() and 'Building Number' in country_dict.keys():
        collapsed_schema['street2'] = country_dict['Building Number']
    print(json.dumps(collapsed_schema))
    return(collapsed_schema)



def expand_from_schema(query):
    query = json.loads(query)
    expanded_doc = {}
    if query['state'] != '':
        if query['country'] in ['Australia'.upper(), 'Mexico'.upper(), 'United States'.upper()]:
            expanded_doc['State'] = query['state']
        else:
            expanded_doc['Province'] = query['state']
    if query['street1'] != '':
        expanded_doc['Street 1'] = query['street1']
    if query['postcode'] != '':
        expanded_doc['Postcode'] = query['postcode']
    if query['apt'] != '':
        expanded_doc['Apt Number'] = query['apt']
    if query['district'] != '':
        expanded_doc['District'] = query['district']
    if query['city'] != '':
        expanded_doc['City'] = query['city']
    if query['county'] != '':
        expanded_doc['County'] = query['county']
    expanded_doc['_id'] = query['_id']
    expanded_doc['Country'] = query['country']
    current_country = query['country']
    if current_country == 'Argentina'.upper():
        if query['street2'] != '':
            expanded_doc['Floor'] = query['street2']
        if query['apt'] != '':
            expanded_doc['Departmnet'] = query['apt']
    if current_country == 'Costa Rica':
        if query['street2'] != '':
            expanded_doc['Floor'] = query['street2']
    if current_country == 'Czech Republic'.upper():
        if ',' in query['city']:
            expanded_doc['City'] = query['city'].split(',', maxsplit=1)[0]
            expanded_doc['Post Office Code'] = query['city'].split(',', maxsplit=1)[1]
        if query['street2'] != '':
           expanded_doc['Building Number'] = query['street 2']
    if current_country in ['Great Britain'.upper(), 'Isle of Man'.upper(), 'Malaysia'.upper(), 'Northern Ireland'.upper(),
                           'Scotland'.upper()] and query['street2'] != '':
        expanded_doc['Building Name'] = query['street2']
    if current_country == 'Ireland'.upper():
        if ',' in query['city']:
            expanded_doc['City'] = query['city'].split(',', maxsplit=1)[0]
            expanded_doc['Zone'] = query['city'].split(',', maxsplit=1)[1]
    if current_country == 'Hong Kong'.upper():
        if ',' in query['street2']:
            expanded_doc['Building Name'] = query['street2'].split(',', maxsplit=1)[0]
            expanded_doc['Floor'] = query['street2'].split(',', maxsplit=1)[1]
    if current_country == 'Japan'.upper():
        if ',' in query['street2']:
            expanded_doc['Block'] = query['street2'].split(',', maxsplit=1)[0]
            expanded_doc['Building Number'] = query['street2'].split(',', maxsplit=1)[1]
    if current_country == 'Pakistan'.upper():
        if query['apt'] != '':
            expanded_doc['House'] = query['apt']
    if current_country == 'South Korea'.upper():
        if query['apt'] != '':
            expanded_doc['House'] = query['apt']
    if current_country == 'Switzerland'.upper():
        if query['street2'] != '':
            expanded_doc['Building Number'] = query['street2']
    print(json.dumps(expanded_doc))
    return json.dumps(expanded_doc)



# if __name__ == '__main__':
#     example_data = '{"Country": "United States", "State": "WA", "City": "Seattle", "Street 1": "123 Main St", "Postcode": 123435}'
#     res = (validate_upload(example_data))
#     print(res)





