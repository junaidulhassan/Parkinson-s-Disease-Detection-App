import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report
from parkinsons_model import ParkinsonsDiseaseModel  # Assuming you saved the previous code in a file called parkinsons_model.py

class ParkinsonsDiseaseApp:
    def __init__(self):
        if 'model' not in st.session_state:
            st.session_state.model = None  # This will store the ParkinsonsDiseaseModel object

    def upload_file(self):
        # Streamlit file uploader for CSV
        uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
        return uploaded_file

    def train_button(self, csv_path):
        if st.button('Train Model'):
            if csv_path:
                st.session_state.model = ParkinsonsDiseaseModel(csv_path)
                st.session_state.model.preprocess_data()
                st.session_state.model.split_data()
                st.session_state.model.train_model()
                st.success('Model training complete!')

    def show_results_button(self):
        if st.button('Show Results'):
            if st.session_state.model:
                st.subheader("Classification Report")
                st.text(classification_report(st.session_state.model.y_test, st.session_state.model))

                # Capture the confusion matrix to display
                st.subheader("Confusion Matrix")
                cm = confusion_matrix(st.session_state.model.y_test, st.session_state.model.y_pred)
                
                # Plot confusion matrix using Seaborn
                plt.figure(figsize=(8, 6))
                sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                            xticklabels=['AP', 'PD', 'CR'], yticklabels=['AP', 'PD', 'CR'])
                plt.title('Confusion Matrix')
                plt.ylabel('True label')
                plt.xlabel('Predicted label')
                st.pyplot(plt)

def main():
    st.title('Parkinson\'s Disease Classification')

    app = ParkinsonsDiseaseApp()

    # Upload CSV file
    uploaded_file = app.upload_file()

    # Train model button
    if uploaded_file:
        # Save the uploaded file to a temporary location
        with open("uploaded_file.csv", "wb") as f:
            f.write(uploaded_file.getbuffer())

        app.train_button("uploaded_file.csv")

    # Show results button
    if st.session_state.model:
        app.show_results_button()

if __name__ == "__main__":
    main()
