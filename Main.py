import streamlit as st

st.title("Parkinson's Disease Prediction")

# Selection for eye movement analysis
options = [
    'Antisaccade Analysis Results (Horizontal)', 
    'Antisaccade Analysis Results (Vertical)',
    'Fixation Analysis Output',
    'Fixation Analysis Saccades',
    'Memory Analysis Results (Horizontal)',
    'Memory Analysis Results (Vertical)',
    'Nystagmus Analysis',
    'Nystagmus Saccade Analysis',
    'Oblique Analysis Results',
    'Pursuit Analysis Trial Report',
    'Reflexive Analysis Results (Horizontal)',
    'Reflexive Analysis Results (Vertical)',
    'Volitional Analysis Results (Horizontal)',
    'Volitional Analysis Results (Vertical)'
]

# Now you can use this list in a selectbox
selected_option = st.selectbox(
    label="Select Eye Movement",
    options=options
)


if selected_option == options[0]:
    # Number inputs for each column
    avg_velocity = st.number_input("Average Velocity", placeholder="Enter Average Velocity")
    avg_amplitude = st.number_input("Average Amplitude", placeholder="Enter Average Amplitude")
    total_complete_saccades = st.number_input("Total Complete Saccades", placeholder="Enter Total Complete Saccades")
    avg_peak_velocity = st.number_input("Average Peak Velocity", placeholder="Enter Average Peak Velocity")
    avg_start_time = st.number_input("Average Start Time", placeholder="Enter Average Start Time")
    avg_accuracy = st.number_input("Average Accuracy", placeholder="Enter Average Accuracy")
    correct_count = st.number_input("Correct Count", placeholder="Enter Correct Count")
    hypo_count = st.number_input("Hypo Count", placeholder="Enter Hypo Count")
    hyper_count = st.number_input("Hyper Count", placeholder="Enter Hyper Count")

elif selected_option == options[1]:
    # Number inputs for the second set of columns
    avg_fix_pupil = st.number_input("Average Fixation Pupil", placeholder="Enter Average Fixation Pupil")
    avg_fix_precision_rms_s2s = st.number_input("Average Fixation Precision RMS S2S", placeholder="Enter Average Fixation Precision RMS S2S")
    avg_fix_precision_sd_window = st.number_input("Average Fixation Precision SD Window", placeholder="Enter Average Fixation Precision SD Window")

elif selected_option == options[2]:
    avg_velocity = st.number_input("Average Velocity", placeholder="Enter Average Velocity")
    avg_peak_velocity = st.number_input("Average Peak Velocity", placeholder="Enter Average Peak Velocity")
    avg_start_time = st.number_input("Average Start Time", placeholder="Enter Average Start Time")
    num_errors = st.number_input("Number of Errors", placeholder="Enter Number of Errors")
    self_correcting_errors = st.number_input("Self-Correcting Errors", placeholder="Enter Self-Correcting Errors")

elif selected_option == options[3]:
    avg_velocity = st.number_input("Average Velocity", placeholder="Enter Average Velocity")
    avg_peak_velocity = st.number_input("Average Peak Velocity", placeholder="Enter Average Peak Velocity")
    avg_start_time = st.number_input("Average Start Time", placeholder="Enter Average Start Time")
    num_errors = st.number_input("Number of Errors", placeholder="Enter Number of Errors")
    self_correcting_errors = st.number_input("Self-Correcting Errors", placeholder="Enter Self-Correcting Errors")

elif selected_option==options[4]:
    small_swj = st.number_input("Small SWJ", placeholder="Enter Small SWJ")
    large_swj = st.number_input("Large SWJ", placeholder="Enter Large SWJ")
    large_is = st.number_input("Large IS", placeholder="Enter Large IS")
    
elif selected_option == options[5]:
    trial_1_small_swj = st.number_input("Trial 1 Small SWJ", placeholder="Enter Trial 1 Small SWJ")
    trial_1_large_swj = st.number_input("Trial 1 Large SWJ", placeholder="Enter Trial 1 Large SWJ")
    trial_1_large_is = st.number_input("Trial 1 Large IS", placeholder="Enter Trial 1 Large IS")
    trial_2_small_swj = st.number_input("Trial 2 Small SWJ", placeholder="Enter Trial 2 Small SWJ")
    trial_2_large_swj = st.number_input("Trial 2 Large SWJ", placeholder="Enter Trial 2 Large SWJ")
    trial_2_large_is = st.number_input("Trial 2 Large IS", placeholder="Enter Trial 2 Large IS")
    trial_3_small_swj = st.number_input("Trial 3 Small SWJ", placeholder="Enter Trial 3 Small SWJ")
    trial_3_large_swj = st.number_input("Trial 3 Large SWJ", placeholder="Enter Trial 3 Large SWJ")
    trial_3_large_is = st.number_input("Trial 3 Large IS", placeholder="Enter Trial 3 Large IS")
    trial_4_small_swj = st.number_input("Trial 4 Small SWJ", placeholder="Enter Trial 4 Small SWJ")
    trial_4_large_swj = st.number_input("Trial 4 Large SWJ", placeholder="Enter Trial 4 Large SWJ")
    trial_4_large_is = st.number_input("Trial 4 Large IS", placeholder="Enter Trial 4 Large IS")

elif selected_option==options[6]:
    recording_session_label_2 = st.number_input("Recording Session Label", placeholder="Enter Recording Session Label")
    total_complete_saccades = st.number_input("Total Complete Saccades", placeholder="Enter Total Complete Saccades")
    avg_amplitude = st.number_input("Average Amplitude", placeholder="Enter Average Amplitude")
    avg_velocity = st.number_input("Average Velocity", placeholder="Enter Average Velocity")
    avg_peak_velocity = st.number_input("Average Peak Velocity", placeholder="Enter Average Peak Velocity")
    avg_start_time = st.number_input("Average Start Time", placeholder="Enter Average Start Time")
    avg_accuracy = st.number_input("Average Accuracy", placeholder="Enter Average Accuracy")
    correct_count = st.number_input("Correct Count", placeholder="Enter Correct Count")
    hypo_count = st.number_input("Hypo Count", placeholder="Enter Hypo Count")
    hyper_count = st.number_input("Hyper Count", placeholder="Enter Hyper Count")

elif selected_option == options[7]:
    
    total_complete_saccades = st.number_input("Total Complete Saccades", placeholder="Enter Total Complete Saccades")
    avg_amplitude = st.number_input("Average Amplitude", placeholder="Enter Average Amplitude")
    avg_velocity = st.number_input("Average Velocity", placeholder="Enter Average Velocity")
    avg_peak_velocity = st.number_input("Average Peak Velocity", placeholder="Enter Average Peak Velocity")
    avg_start_time = st.number_input("Average Start Time", placeholder="Enter Average Start Time")
    avg_accuracy = st.number_input("Average Accuracy", placeholder="Enter Average Accuracy")
    correct = st.number_input("Correct Count", placeholder="Enter Correct Count")
    hypo = st.number_input("Hypo Count", placeholder="Enter Hypo Count")
    Hyper = st.number_input("Hyper Count", placeholder="Enter Hyper Count")
    
elif selected_option == options[7]:  # Update the index based on where you want to insert this block
    
    avg_vel_gain_trial_1 = st.number_input("Average Velocity Gain Trial 1", placeholder="Enter Average Velocity Gain Trial 1")
    avg_vel_gain_trial_2 = st.number_input("Average Velocity Gain Trial 2", placeholder="Enter Average Velocity Gain Trial 2")
    avg_vel_gain_trial_3 = st.number_input("Average Velocity Gain Trial 3", placeholder="Enter Average Velocity Gain Trial 3")
    avg_vel_gain_trial_4 = st.number_input("Average Velocity Gain Trial 4", placeholder="Enter Average Velocity Gain Trial 4")
    avg_vel_gain_trial_5 = st.number_input("Average Velocity Gain Trial 5", placeholder="Enter Average Velocity Gain Trial 5")
    avg_vel_gain_trial_6 = st.number_input("Average Velocity Gain Trial 6", placeholder="Enter Average Velocity Gain Trial 6")
    avg_vel_gain_trial_7 = st.number_input("Average Velocity Gain Trial 7", placeholder="Enter Average Velocity Gain Trial 7")
    avg_vel_gain_trial_8 = st.number_input("Average Velocity Gain Trial 8", placeholder="Enter Average Velocity Gain Trial 8")
    avg_rmse_gaze_trial_1 = st.number_input("Average RMSE Gaze Trial 1", placeholder="Enter Average RMSE Gaze Trial 1")
    avg_rmse_gaze_trial_2 = st.number_input("Average RMSE Gaze Trial 2", placeholder="Enter Average RMSE Gaze Trial 2")
    avg_rmse_gaze_trial_3 = st.number_input("Average RMSE Gaze Trial 3", placeholder="Enter Average RMSE Gaze Trial 3")
    avg_rmse_gaze_trial_4 = st.number_input("Average RMSE Gaze Trial 4", placeholder="Enter Average RMSE Gaze Trial 4")
    avg_rmse_gaze_trial_5 = st.number_input("Average RMSE Gaze Trial 5", placeholder="Enter Average RMSE Gaze Trial 5")
    avg_rmse_gaze_trial_6 = st.number_input("Average RMSE Gaze Trial 6", placeholder="Enter Average RMSE Gaze Trial 6")
    avg_rmse_gaze_trial_7 = st.number_input("Average RMSE Gaze Trial 7", placeholder="Enter Average RMSE Gaze Trial 7")
    avg_rmse_gaze_trial_8 = st.number_input("Average RMSE Gaze Trial 8", placeholder="Enter Average RMSE Gaze Trial 8")

