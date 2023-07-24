import random
from faker import Faker     
import numpy as np
import pandas as pd
import os

fake = Faker() 

def get_last_customer_id(path): 
    df = pd.read_csv(path)
    last_id = df['customer_id'].iloc[-1]
    return last_id

def random_phone_num_generator():
    first = str(random.randint(100, 999))
    second = str(random.randint(1, 888)).zfill(3)
    last = (str(random.randint(1, 9998)).zfill(4))
    return '{}-{}-{}'.format(first, second, last)

def create_data(start_range, total_numbers):
    customer = {}
    end_range = start_range + total_numbers
    for i in range(start_range, end_range): 
        customer[i] = {}
        customer[i]['customer_id'] = i+1
        customer[i]['first_name'] = fake.first_name()
        customer[i]['last_name'] = fake.last_name()
        customer[i]['email'] = fake.ascii_email()
        customer[i]['phone'] = fake.country_calling_code() + ' ' + random_phone_num_generator()
    return pd.DataFrame(customer).transpose()

path = './customer.csv'
is_exist = os.path.exists(path)
if is_exist:  
    last_created_id = get_last_customer_id(path)
    df = create_data(last_created_id, 20)
    df.to_csv("customer.csv",mode='a',index=False, header=False)
else:
    df = create_data(start_range=0, total_numbers=20)
    df.to_csv("customer.csv",mode='a',index=False, header=True)
