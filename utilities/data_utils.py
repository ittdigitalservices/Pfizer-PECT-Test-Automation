import json


class get_My_Data:
    def my_data(self, my_test_data_key="", key_id=None):
        jsondata = ""
        mydata = ""
        try:
            json_file = "./data/TestData.json"
            with open(json_file, "r") as json_data_file:
                jsondata = json.loads(json_data_file.read())
                if (key_id == None):
                    mydata = jsondata[my_test_data_key]
                else:
                    mydata = jsondata[my_test_data_key][key_id]
                print("\nData Collected = ", mydata)
            return(mydata)
        except Exception as e:
            print(str(e))

    def my_data_json(self, json_data=None, my_test_data_key="", key_id=None):
        if (key_id == None):
            mydata = json_data[my_test_data_key]
        else:
            mydata = json_data[my_test_data_key][key_id]

        return(mydata)


"""
print(get_My_Data().my_data(my_test_data_key='staging_url', key_id=None))
test_data = get_My_Data().my_data(my_test_data_key='test_EPIC_PECT_001_A-Login', key_id=0)
print(get_My_Data().my_data_json(json_data=test_data, my_test_data_key='Employee-ID'))

test_data = get_My_Data().my_data(my_test_data_key="preprod_url")
print(test_data)
"""
