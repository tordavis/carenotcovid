#### Care Not Covid Healthcare Facility Database Code ####
#### by Tori Davis ####

##############################################################################

#### Import Libraries ####

import streamlit as st
import pandas as pd
import csv
import numpy as np
import random
from streamlit_gsheets import GSheetsConnection

##############################################################################

##### Page Set Up #####

# set up page name
st.set_page_config(page_title="WORK IN PROGRESS: Chicagoland Healthcare Facility Covid Safety Database", page_icon="😷")
# set up title on the web application
st.title("WORK IN PROGRESS: Chicagoland Healthcare Facility Covid Safety Database")
st.header("Crowdsourced Database for Covid Precautions at Healthcare Facilities Around Chicagoland.")
st.write("NOTE: Due to covid denialism this information could be subject to change.")

##############################################################################

#### Read in Survey Date ####

df = pd.read_csv('responses/survey_data.csv')

#### Connect to Feedback Spreadsheet ####

conn = st.connection("gsheets", type=GSheetsConnection)

##############################################################################

#### Set Up Dataframe Filtering Function ####

def filter_dataframe(df: pd.DataFrame) -> pd.DataFrame:

    user_facility = st.selectbox("Please select the facility type you are interested in",df['facility_type'].unique())

    mask_selection = st.selectbox("Please select the mask requirement that was observed at the facility",df['mask_required'].unique())

    curated_df = df[(df['facility_type'] == user_facility) & (df['mask_required'] == mask_selection)]

    facility_df = curated_df[['timestamp',
                              'facility_name',
                              'address',
                              'address_2',
                              'city',
                              'zip',
                              'phone_number',
                              'email',
                              'website'
                              ]]

    mask_df = curated_df[['timestamp',
                          'facility_name',
                          'N95',
                          'KN95',
                          'surgical',
                          'none',
                          'unknown',
                          'mask_enforced',
                          'all_mask',
                          'all_mask_required',
                          'all_mask_enforced',
                          'patients_mask',
                          'patients_mask_required',
                          'patients_mask_enforced',
                          'mask_request'
                          ]]
    
    air_df = curated_df[['facility_name',
                         'hepa',
                         'hepa_on',
                         'co2',
                         'co2_reading',
                         'co2_location'
                         ]]
    
    accessibility_df = curated_df[['facility_name',
                                   'elevator',
                                   'ada_request']]


    
    table_selection = st.selectbox("What information are you interested in seeing",['Facility Information',
                                                                                    'Mask Information',
                                                                                    'Air Information',
                                                                                    'Accessibility Information'
                                                                                    ])
    
    if table_selection == 'Facility Information':
        final_df = facility_df
    elif table_selection == 'Mask Information':
        final_df = mask_df
    elif table_selection == 'Air Information':
        final_df = air_df
    elif table_selection == 'Accessibility Information':
        final_df = accessibility_df


    return final_df.sort_values('facility_name')

##############################################################################

#### Main function ####

def main():

    st.dataframe(
                    data = filter_dataframe(df),
                    width = 1000,
                    hide_index = 1
                    )

if __name__ == "__main__":
    main()

feedback = st.text_input("Please provide any feedback or bugs you find within this tool")

conn.update(
            worksheet="database feedback",
            data=feedback
)