#create 1 mill random addresses

import json
import string
from app.valid_rules import RULE_VALID_COUNTRIES, RULE_REQUIRED_FIELDS, RULE_OPTIONAL_FIELDS, \
    RULE_VALID_POSTCODES, RULE_ALPHANUMERIC_POSTCODES, RULE_VALID_PROVINCES
import itertools

#select random country
import os
import random

with open('fake_streets.txt') as s:
    streets = [line.rstrip() for line in s]
with open('fake_towns.txt') as t:
    towns = [line.rstrip() for line in t]



def create_random_postcode(country):
    valid_alpha = True if country in RULE_ALPHANUMERIC_POSTCODES else False
    postcode_format = RULE_VALID_POSTCODES[country]
    random_pool = string.digits + string.ascii_uppercase if valid_alpha else string.digits
    if len(postcode_format) > 1:
        sep = postcode_format[-1]
        group1_len = postcode_format[0]
        group2_len = postcode_format[1]
        postcode = ''.join(random.choices(random_pool, k=group1_len)) + sep + ''.join(random.choices(random_pool, k=group2_len))
    else:
        group_len = postcode_format[0]
        postcode = ''.join(random.choices(random_pool, k=group_len))
    return(postcode)



def create_random_field(country, fieldname):

    if fieldname == 'Building Number':
        return(str(random.randint(1, 99999)))
    if fieldname == 'Floor':
        return(str(random.randint(1,20)) + '/F')
    if fieldname == 'County':
        return(random.choice(towns) + ' County')
    if fieldname == 'City':
        return(random.choice(towns))
    if fieldname == 'Street 1':
        return(str(random.randint(1, 99999)) + ' ' + random.choice(streets))
    if fieldname == 'Postcode':
        return(create_random_postcode(country))
    if fieldname == 'Province' or fieldname == 'State':
        if country in RULE_VALID_PROVINCES.keys():
            return(random.choice(list(RULE_VALID_PROVINCES[country])))
        else:
            return('SOME PROVINCE')
    if fieldname == 'Apt Number' or fieldname == 'House' or fieldname == 'Block':
        return(str(random.randint(1,999)))
    if fieldname == 'Building Name':
        return(random.choice(streets) + ' Building')
    if fieldname == 'District':
        return(str(random.randint(1,99)) + ' District')
    if fieldname == 'Post Office Code':
        return(' ' + str(random.randint(1,999)))

    if fieldname == 'Country':
        return(str.upper(country))

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


def collapse_fields_to_schema(full_address):
    collapsed_schema = {'apt':'', 'street1':'', 'street2':'',
                        'postcode': '', 'district':'', 'city':'', 'county':'', 'state':'', 'country':''}
    all_fields = {field : '' for field in FIELD_POOL}
    for field in all_fields:
        if field in full_address.keys():
            all_fields[field] = str(full_address[field])

    collapsed_schema['apt'] = '' + (all_fields['House']) + all_fields['Apt Number']
    collapsed_schema['street1'] = all_fields['Street 1'] + all_fields['Block']
    collapsed_schema['street2'] = all_fields['Building Name'] + all_fields['Building Number'] + all_fields['Floor']
    collapsed_schema['postcode'] = all_fields['Postcode']
    collapsed_schema['city'] = all_fields['City'] + all_fields['Post Office Code']
    collapsed_schema['district'] = all_fields['District']
    collapsed_schema['county'] = all_fields['District']
    collapsed_schema['state'] = all_fields['State'] + all_fields['Province']
    collapsed_schema['country'] = all_fields['Country']
    return(collapsed_schema)









if __name__ == '__main__':
    # print('testing')
    # address_list = []
    # for i in range(1000000):
    #     country = random.choice(list(RULE_VALID_COUNTRIES))
    #     req_fields = RULE_REQUIRED_FIELDS[country]
    #     address = {}
    #     for field in req_fields:
    #         address[field] = create_random_field(country, field)
    #     collapsed_addr = collapse_fields_to_schema(address)
    #     address_list.append(collapsed_addr)
    #     if i % 10000 == 0:
    #         print(i)
    # json_str = json.dumps(address_list)
    #
    # with open('test_addresses.json', 'w') as f:
    #     f.write(json_str)
    import itertools
    print(set(list(itertools.chain(*RULE_OPTIONAL_FIELDS.values()))))





