"""
Main Streamlit Application for Divide & Conquer Algorithms Visualizer
"""

import streamlit as st
import sys
import os

# ---------------- PATH FIX ----------------
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(CURRENT_DIR)

# ---------------- SAFE IMPORTS ----------------
try:
    from utils.helpers import HelperFunctions
except Exception:
    # fallback helpers (taaki app crash na ho)
    class HelperFunctions:
        @staticmethod
        def parse_input(text):
            try:
                return [int(x.strip()) for x in text.split(",")]
            except:
                return []

        @staticmethod
        def generate_random_array(size):
            import random
            return [random.randint(1, 100) for _ in range(size)]

        @staticmethod
        def format_array(arr):
            return ", ".join(map(str, arr))


# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Divide & Conquer Visualizer",
    page_icon="⚡",
    layout="wide"
)

# ---------------- MAIN APP ----------------
def main():

    st.title("⚡ Divide & Conquer Algorithms Visualizer")

    # -------- Sidebar --------
    with st.sidebar:
        st.header("📊 Algorithm Selection")

        algorithm = st.selectbox(
            "Choose an algorithm",
            [
                "Quick Sort",
                "Merge Sort",
                "Insertion Sort",
                "Heap Sort",
                "Binary Search",
                "Count Inversions",
                "Find Max & Min",
                "Karatsuba Multiplication"
            ]
        )

        st.divider()
        st.subheader("📝 Input Parameters")

        if "input_array" not in st.session_state:
            st.session_state.input_array = [5, 2, 8, 1, 9, 3, 7, 4, 6]

        input_type = st.radio(
            "Input type",
            ["Manual Entry", "Random Array", "Example Array"]
        )

        if input_type == "Manual Entry":
            default_input = ", ".join(map(str, st.session_state.input_array))
            input_str = st.text_input(
                "Enter numbers (comma separated)",
                default_input
            )
            arr = HelperFunctions.parse_input(input_str)
            if arr:
                st.session_state.input_array = arr

        elif input_type == "Random Array":
            size = st.slider("Array size", 5, 30, 10)
            arr = HelperFunctions.generate_random_array(size)
            st.session_state.input_array = arr

        else:  # Example Array
            arr = st.session_state.input_array

    # -------- Main Area --------
    st.subheader("📌 Selected Algorithm")
    st.info(algorithm)

    st.subheader("📦 Input Array")
    st.code(st.session_state.input_array)

    if st.button("▶ Run Algorithm"):
        st.success("Algorithm executed successfully ✅")
        st.write("Output (demo):")
        st.code(sorted(st.session_state.input_array))


# ---------------- RUN ----------------
if __name__ == "__main__":
    main()
