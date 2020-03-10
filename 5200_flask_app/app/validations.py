from app.valid_rules import RULE_REQUIRED_FIELDS, RULE_VALID_COUNTRIES, \
    RULE_ALPHANUMERIC_POSTCODES, RULE_OPTIONAL_FIELDS, RULE_VALID_POSTCODES, RULE_VALID_PROVINCES
import json




def validate_upload(json_str):
    data = json.loads(json_str)
    if 'Country' not in data.keys():
        return('Failure: No Country Provided')
    try:
        if data['Country'] not in RULE_VALID_COUNTRIES:
            return('Failure: Invalid Country')
        country = data['Country']
        required_fields = RULE_REQUIRED_FIELDS[country]
        print(required_fields)
        for field in required_fields:
            if field not in data.keys():
                return('Failure: Required field not found')
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
                    return('Failure: Invalid Postcode')
                if not valid_alpha:
                    if (str.isnumeric(postcode_parsed[0]) == False) or (str.isnumeric(postcode_parsed[1]) == False):
                        return('Faiure: Invalid Postcode')
            else:
                group_len = postcode_format[0]
                if len(postcode) != group_len:
                    return('Failure: Invalid Postcode')
                if not valid_alpha:
                    if not str.isnumeric(postcode):
                        return('Failure: Invalid Postcode')
        if country in RULE_VALID_PROVINCES.keys():
            province_field = 'Province' if 'Province' in required_fields else 'State'
            print('province field')
            print(province_field)
            if data[province_field] not in RULE_VALID_PROVINCES[country]:
                return('Failure: Invalid State or Province')
        #make database call here
        print('DATABASE CALL')
        return('Success: Uploaded data')
    except Exception as e:
        print(e)
        return('Failure: Unknown Error occurred')



def validate_update():
    pass




if __name__ == '__main__':
    example_data = '{"Country": "United States", "State": "WA", "City": "Seattle", "Street 1": "123 Main St", "Postcode": 123435}'
    res = (validate_upload(example_data))
    print(res)





