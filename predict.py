st.title("🎯 Student Score Predictor")

st.write("Enter the number of hours you studied to predict your score.")

study_hours = st.number_input(
    "Hours Studied",
    min_value=0.0,
    max_value=24.0,
    value=5.0,
    step=0.5
)

if st.button("🚀 Predict Score"):
    input_data = np.array([[study_hours]])
    input_scaled = scaler.transform(input_data)

    predicted_score = best_model.predict(input_scaled)[0]

    predicted_score = max(0, min(100, predicted_score))

    st.success(f"Predicted Score: {predicted_score:.2f} / 100")