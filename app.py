import streamlit as st

'''
# TaxiFareModel User Interface
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''

import streamlit as st
import datetime
import re
status = False

date = st.date_input("Please enter the date like in the format below:",datetime.date(2019, 7, 6))

time = st.time_input("Please enter the date like in the format below:",datetime.time(8, 45))

datetime_ = str(date) + " " +str(time)

st.write('Your Datetime is:', datetime_)

inputs = ['pickup longitude','pickup latitude','dropoff longitude','dropoff latitude','passenger count']
inputdict = {}
for item in inputs:
    inputdict[item] =  st.text_input(f'Please enter the {item}', item)

st.text('  '.join(inputs))
st.text('  '.join(inputdict.values()))
#breakpoint()

if st.button('Calculate Fare'):
    print('Initializing....')
