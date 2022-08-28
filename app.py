import streamlit as st
import glob

st.header('Humedales de Chile por región')
files=list(glob.glob('DATA/*.json'))
st.write(files)

st.write('versión=?')

#if __name__ == "__main__":    run()
