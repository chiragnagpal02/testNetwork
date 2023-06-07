import streamlit as st
import speedtest

def categorize_speed(download_speed, upload_speed):
    download_speed_mbps = download_speed / (10**6)  # converting from bits to megabits
    upload_speed_mbps = upload_speed / (10**6)

    if download_speed_mbps > 25 and upload_speed_mbps > 3:
        return "Excellent"
    elif download_speed_mbps > 10 and upload_speed_mbps > 1:
        return "Good"
    elif download_speed_mbps > 5 and upload_speed_mbps > 0.5:
        return "Fair"
    else:
        return "Poor"

def perform_speedtest():
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()

    return res["download"], res["upload"]

st.title('Internet Speed Test')

if st.button('Perform Speed Test'):
    with st.spinner('Performing speed test...'):
        download_speed, upload_speed = perform_speedtest()
        speed_category = categorize_speed(download_speed, upload_speed)

    st.write(f'Download speed: {download_speed / (10**6):.2f} Mbps')
    st.write(f'Upload speed: {upload_speed / (10**6):.2f} Mbps')
    st.markdown(f'## **Speed category: {speed_category}**')
