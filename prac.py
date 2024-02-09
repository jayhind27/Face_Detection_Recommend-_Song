import streamlit as st
import Spotify as s
import Youtube as y
import handracking as h
import Home as hm
import time
def main():
    #st.title("Streamlit Multi-Page App")

    # Add navigation options
    page = st.sidebar.selectbox("Select a page", ["Home", "Spotify", "Youtube","Handracking"])
    # Display content based on the selected page
    if page == "Home":
       hm.Home()
    elif page == "Spotify":
        s.spotify()
    elif page == "Youtube":
        y.youtube()
    elif page == "Handracking":
        st.title("Welcome to Handracking")
        if st.button("Start"):
            st.empty()
            with st.spinner("Wait for it..."):
                time.sleep(5)
            st.success("Done!")
            #st.write("Camera Started!")
            st.warning("Camera Started")
            h.hand()
        if st.button("Stop"):
            st.warning("Camera Stop")
            st.stop()
            

if __name__ == "__main__":
    main()
