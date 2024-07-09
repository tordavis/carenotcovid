#### Care Not Covid Healthcare Facility Database Code ####
#### by Tori Davis ####

##############################################################################

#### Import Libraries ####

import streamlit as st
import pandas as pd
import csv
import numpy as np
import random

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

    # # have the user choose an allergen
    # user_mask_selection = st.selectbox("Please select your mask preference:", masks)
            
    # # reduce OpenFoodFacts dataframe to just rows with allergen selected
    # final_df = df[df['masks worn'].str.contains(user_mask_selection, na=False)]
    # # if there are no facilities, tell the user
    # if final_df.empty:
    #     st.write(
    #         "Based on the information available in our dataset, we did not find any potential facilities that matched your preference",
    #         user_mask_selection,
    #     )
    # #if there are facilities
    # else:
    #     # may not need this anymore?
    #     final_df = final_df.drop_duplicates()
    #     # get length of OFF dataset for allergen
    #     final_df_len = len(final_df)
    #     st.write("We found", final_df_len, "facilities with", user_mask_selection,".")
    #     # present a dataframe of brand, product, ingredient, and allergen
    #     final_df.set_index(final_df.columns[0])
    #     st.write("### Facilities with Mask Preference Present", final_df.sort_index())

if __name__ == "__main__":
    main()
