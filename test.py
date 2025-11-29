import streamlit as st
import time

def stream_text():
    msg = "This is a streamed response from the bot."
    for char in msg:
        yield char
        time.sleep(0.01)

stream_area = st.empty()
label = st.markdown("🤖 **Bot:**")
stream_area.write_stream(stream_text)
