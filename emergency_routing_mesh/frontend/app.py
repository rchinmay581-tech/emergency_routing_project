import streamlit as st
import sys
import os

# Connect Python pathways so the UI file can call the backend module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.routing import calculate_emergency_mesh_blueprint

# Visual configurations for the dashboard window layout
st.set_page_config(page_title="Emergency Routing Mesh", layout="centered")
st.title("🚨 Live Emergency Routing Console")
st.write("System platform processing via Google Gemma 2 9B API Engine")

# Input text capture box
accident_input = st.text_area(
    "Enter mock traffic accident statement:", 
    placeholder="Example: Multi-car collision reported at 5th Avenue intersection. Main lanes blocked.",
    height=150
)

# Live execution trigger button 
if st.button("🚨 Broadcast & Clear Route Mesh"):
    if accident_input.strip():
        with st.spinner("Gemma 2 9B computing emergency routing vectors..."):
            try:
                # Pipe frontend text input directly into the backend calculation routine
                result_blueprint = calculate_emergency_mesh_blueprint(accident_input)
                
                st.success("Routing Vector Computed Successfully!")
                st.markdown("### 📋 System Routing Blueprint")
                st.info(result_blueprint)
                
            except Exception as e:
                st.error(f"Execution Error: Graphic framework dropped connection. Details: {e}")
    else:
        st.warning("Please type an incident description before triggering broadcast updates.")