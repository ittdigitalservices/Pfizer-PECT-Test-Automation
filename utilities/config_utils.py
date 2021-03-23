import json

class get_My_Config:
    def my_config(self, my_test_config_key="", key_id=None):
        try:           
            json_file = "./config/TestConfig.json"
            with open(json_file, "r") as json_data_file:
                data = json.loads(json_data_file.read())
                if (key_id == None):
                    mydata = data[my_test_config_key]
                else:
                    mydata = data[my_test_config_key][key_id]
            #print(mydata)
            return(mydata)
        except Exception as e:
            print(str(e))
    
    
    def my_config_json(self, json_data=None, my_test_config_key="", key_id=None):
        try:
            if (my_test_config_key==""):
                mydata = json_data[key_id]
            elif (key_id == None):
                mydata = json_data[my_test_config_key]
            else:
                mydata = json_data[my_test_config_key][key_id]
    
            return(mydata)
        except Exception as e:
            print(str(e))


"""
var0 = get_My_Test_Config().config(my_test_config_key="test_host_environment", key_id=1)
print("\nvar0 = ", var0)
#my_test_config = get_My_Test_Config().config(my_test_config_key="test_host_environment", key_id=0)
#print(get_My_Test_Config().test_config_json(json_data=my_test_config, my_test_config_key='webdriver1'))
#print("\nvar0 = %s", my_test_config)
var1 = get_My_Test_Config().test_config_json(json_data=var0, my_test_config_key="win", key_id=1)
print(var1)
var2 = get_My_Test_Config().test_config_json(json_data=var1, my_test_config_key="webdriver2")

print(var2)

"""
