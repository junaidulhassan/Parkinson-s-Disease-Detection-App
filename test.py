import streamlit as st
import pandas as pd
import os
import pickle
import plotly.graph_objs as go

# Streamlit app
st.set_page_config(page_title="Parkinson's Disease Prediction", layout="wide")
st.title("Parkinson's Disease Prediction")

# Warning message to the user about the file format at the start
st.warning("⚠️ The file should be organized properly with all required columns.")

# Sidebar for file upload
with st.sidebar:
    st.header("Upload Files")
    uploaded_files = st.file_uploader(
        "Choose CSV files", 
        type="csv", accept_multiple_files=True
    )

# Ensure the output directory exists
output_directory = 'Final_CSV_File'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Function to rename columns with a prefix only if not already prefixed
def rename_columns_with_prefix(df, prefix):
    new_columns = []
    for col in df.columns:
        if not col.startswith(prefix):
            new_columns.append(f'{prefix}_{col}')
        else:
            new_columns.append(col)
    df.columns = new_columns
    return df

# Store DataFrames for each uploaded file
dataframes = []
file_names = []

# Process uploaded files
if uploaded_files:
    for uploaded_file in uploaded_files:
        try:
            # Read the CSV file using pandas
            df = pd.read_csv(uploaded_file)
            file_name = uploaded_file.name
            file_name_no_ext = file_name.replace('.csv', '')

            # Rename columns with prefix
            df = rename_columns_with_prefix(df, file_name_no_ext)
            dataframes.append(df)
            file_names.append(file_name)
        except Exception as e:
            st.error(f"Error processing file {uploaded_file.name}: {e}")
    
    # Display the list of uploaded files in the sidebar
    with st.sidebar:
        st.write("Uploaded Files:")
        for name in file_names:
            st.write(f"- {name}")
else:
    st.sidebar.write("No files uploaded yet.")

# Button to trigger the prediction
if st.button('Predict'):
    if dataframes:
        try:
            # Concatenate all DataFrames column-wise
            concatenated_df = pd.concat(dataframes, axis=1)
            
            # Sort columns alphabetically for consistency
            final_df = concatenated_df[sorted(concatenated_df.columns)]
            
            # Display the organized dataset
            st.write(f"Dataset Size: {final_df.shape[0]}")            
            # Load and apply the model
            model_path = 'parkinson_disease_Model.pkl'
            try:
                with open(model_path, 'rb') as file:
                    model = pickle.load(file)
                
                # Ensure the final_df has the required columns
                expected_columns = model.feature_names_in_  # Assuming the model has this attribute
                if not all(col in final_df.columns for col in expected_columns):
                    raise ValueError(f"The uploaded files do not have the required columns: {expected_columns}")
                
                # Prediction step
                pred = model.predict_proba(final_df)
                
                # OMS_PD - Parkinson’s Disease
                # OMS_AP - Atypical Parkinson’s Disease
                # OMS_CRT - Healthy Controls
                
                pat_group = ['Atypical Parkison Disease', 'Healthy Controls', 'Parkinson Disease']
                pred_df = pd.DataFrame(data=pred, columns=pat_group).add_suffix(suffix=' %')
                pred_df = pred_df.applymap(lambda x: f'{x * 100:.2f}%')
                
                patient_id = []
                
                for pat in range(len(pred_df)):
                    patient_id.append(f'Patient_{pat+1}')
                    
                pred_df['Patients'] = patient_id
                
                st.subheader("Organized Dataset for Prediction")
                pred_org_df = pd.concat((final_df,pred_df),axis=1)
                st.write(pred_org_df)
                st.subheader("Parkison's Patient Predictions")
                st.write("This table shows the percentage chance of a patient developing Parkinson's disease, atypical Parkinson's, or being a healthy control.")
                st.write(pred_df)
                
                # Extract values as percentages
                atypical_values = pred[:, 0] * 100
                healthy_values = pred[:, 1] * 100
                parkinson_values = pred[:, 2] * 100
                index = list(range(1, len(atypical_values) + 1))


                # Plotting with Plotly as bar graph
                fig = go.Figure()

                # Add bar traces for each patient group
                fig.add_trace(go.Bar(x=index, y=atypical_values, name='Atypical Parkinson Disease %'))
                fig.add_trace(go.Bar(x=index, y=healthy_values, name='Healthy Controls %'))
                fig.add_trace(go.Bar(x=index, y=parkinson_values, name='Parkinson Disease %'))

                # Update layout
                fig.update_layout(
                    title="Prediction Distribution for Patients",
                    xaxis_title="Patient Index",
                    yaxis_title="Prediction Probability (%)",
                    legend_title="Patient Groups",
                    barmode='group',  # Groups the bars side by side
                    hovermode="x"
                )

                # Show the bar chart in Streamlit
                st.plotly_chart(fig)

            
            except FileNotFoundError:
                st.error("Model file not found! Please ensure 'parkinson_disease_Model.pkl' is in the correct path.")
            except Exception as e:
                st.error(f"Error with the model prediction: The Uploaded CSV do not have required columns for model.")
        
        except ValueError as ve:
            st.error(f"Incompatible file format: {ve}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
        
    else:
        st.error("Please upload CSV files to continue.")

else:
    st.write("Upload files and click the 'Predict' button to start the prediction process.")
