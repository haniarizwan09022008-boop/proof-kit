import streamlit as st
import hashlib
import datetime

st.title("Proof Kit - Tamper-Evident Evidence Tool")
st.write("Upload a screenshot or image of online abuse to generate a SHA-256 cryptographic fingerprint.")

# Restrict the file uploader to accept common image formats
uploaded_file = st.file_uploader("Choose an image / screenshot", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Read the image bytes
    file_bytes = uploaded_file.read()
    file_name = uploaded_file.name

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Generate SHA-256 hash of the image content
    file_hash = hashlib.sha256(file_bytes).hexdigest()

    # Display a preview of the uploaded screenshot
    st.image(uploaded_file, caption=f"Uploaded Evidence: {file_name}", use_container_width=True)

    if st.button("Generate & Log Proof"):
        # Write entry to proof_log.txt
        with open("proof_log.txt", "a") as log_file:
            log_file.write(f"[{timestamp}] Screenshot: {file_name} | Hash: {file_hash}\n")

        st.success("Proof Generated and Logged Successfully!")
        st.write(f"**Timestamp:** {timestamp}")
        st.write(f"**File Name:** {file_name}")
        st.code(file_hash, language="text")