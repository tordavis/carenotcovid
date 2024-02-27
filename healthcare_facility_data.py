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
st.set_page_config(page_title="Chicagoland Healthcare Facility Covid Safety Database", page_icon="😷")
# set up title on the web application
st.title("Chicagoland Healthcare Facility Covid Safety Database")
st.header("Crowdsourced Database for Covid Precautions at Healthcare Facilities Around Chicagoland")

##############################################################################

#### Reference Lists ####

# get hospital list
hospitals = [
    "Advocate Illinois Masonic Medical Center",
    "Chicago Lakeshore Hospital",
    "Chicago-Read Mental Health Center",
    "Comer Children's Hospital",
    "Gardiner General Hospital",
    "Holy Cross Hospital",
    "Humboldt Park Health",
    "Illinois Eye and Ear Infirmary",
    "John H. Stroger Jr. Hospital of Cook County",
    "La Rabida Children's Hospital",
    "Louis A. Weiss Memorial Hospital",
    "Lurie Children's Hospital",
    "Mercy Hospital and Medical Center",
    "Methodist Hospital of Chicago",
    "Mount Sinai Medical Center",
    "Northwestern Memorial Hospital",
    "Prentice Women's Hospital",
    "Provident Hospital",
    "Robert H. Lurie Comprehensive Cancer Center",
    "Rush University Medical Center",
    "Ruth M. Rothstein CORE Center",
    "Ryan AbilityLab",
    "Swedish Hospital",
    "University of Chicago Medical Center",
    "University of Illinois Hospital",
    "University of Illinois Hospital & Health Sciences System"
]

# get facility type list
facility_type = [
    "Hospital",
    "Clinic",
    "Dentist",
    "Optometrist",
    "Lab",
    "Speciality Treatment Center",
    "Other"
]

# hepa filters available
hepa = [
    "Yes",
    "No",
    "Maybe/Unknown"
]

# masks worn
masks = [
    "Respirators - N95s or better",
    "KN95s - better than surgical/proceedure but don't appear to be N95 quality",
    "Proceedure/Surgical",
    "Cloth",
    "Unknown/Cannot Determine",
    "Not Applicable - no masks"
]

##############################################################################

#### Create Random Table ####

# get random samples from the lists above
sample_hospitals = random.choices(hospitals, k=100)
sample_facility_type = random.choices(facility_type, k=100)
sample_hepa = random.choices(hepa, k=100)
sample_masks = random.choices(masks, k=100)

dict = {'hospital': sample_hospitals, 'facility type': sample_facility_type, 
        'hepa available': sample_hepa, 'masks worn': sample_masks} 

df = pd.DataFrame(dict)

##############################################################################

#### Main function ####

def main():

    ##############################################################################

    #### Allergen Selection ####


    # have the user choose an allergen
    user_mask_selection = st.selectbox("Please select your mask preference:", masks)
            
    # reduce OpenFoodFacts dataframe to just rows with allergen selected
    final_df = df[df['masks worn'].str.contains(user_mask_selection, na=False)]
    # if there are no facilities, tell the user
    if final_df.empty:
        st.write(
            "Based on the information available in our dataset, we did not find any potential facilities that matched your preference",
            user_mask_selection,
        )
    #if there are facilities
    else:
        # may not need this anymore?
        final_df = final_df.drop_duplicates()
        # get length of OFF dataset for allergen
        final_df_len = len(final_df)
        st.write("We found", final_df_len, "products containing", user_mask_selection,".")
        # present a dataframe of brand, product, ingredient, and allergen
        final_df.set_index(final_df.columns[0])
        st.write("### Ingredients with Mask Preference Present", final_df.sort_index())

if __name__ == "__main__":
    main()
