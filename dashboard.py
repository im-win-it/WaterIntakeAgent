import streamlit as st 
import pandas as pd
from datetime import datetime
from src.agent import WaterIntakeAgent
from src.database import log_intake, get_intake_history

# ✅ Initialize session state
if "tracker_started" not in st.session_state:
    st.session_state.tracker_started = False

# 🚀 Main App
if not st.session_state.tracker_started:
    st.title("💧 AI Water Intake Tracker")
    st.markdown("Track your water intake with the help of AI")

    if st.button("Start Tracking"):
        st.session_state.tracker_started = True
        st.rerun()


else:
    st.title("📊 AI Water Tracking Dashboard")
    st.sidebar.header("Input your water intake")

    user_id = st.sidebar.text_input("User ID", value="user_123")
    intake_ml = st.sidebar.number_input("Water intake (ml)", min_value=0, step=100)

    if st.sidebar.button("Submit"):
        if user_id and intake_ml:
            # Log to DB
            log_intake(user_id, intake_ml)
            st.success(f"✅ Successfully logged {intake_ml} ml for {user_id}")

        history = get_intake_history(user_id)

               # Compute today's total
        today = datetime.now().date()
        todays_intake = sum(
            row[0] for row in history if datetime.strptime(row[1], "%Y-%m-%d").date() == today
        )

        # Run agent on TOTAL intake, not just the new log
        agent = WaterIntakeAgent()
        feedback = agent.analyze_intake(todays_intake)
        st.info(f"🤖 AI Feedback (today's total {todays_intake} ml): {feedback}")

        # Divider
        st.markdown("---")

        # History section
        st.markdown("📈 Water Intake History")

        history = get_intake_history(user_id)
        if history:
            dates = [datetime.strptime(row[1], "%Y-%m-%d") for row in history]
            values = [row[0] for row in history]

            df = pd.DataFrame({
                "Date": dates,
                "Water Intake (ml)": values
            }).sort_values("Date")

            st.dataframe(df)
            st.line_chart(df, x="Date", y="Water Intake (ml)")
        else:
            st.warning("⚠️ No water intake data found. Please log your intake first.")
