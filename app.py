import streamlit as st
import speedtest

def categorize_speed(download_speed, upload_speed):
    download_speed_mbps = download_speed / (10**6)  # converting from bits to megabits
    upload_speed_mbps = upload_speed / (10**6)

    if download_speed_mbps > 25 and upload_speed_mbps > 3:
        return "Excellent Network Speed. Sync should happen."
    elif download_speed_mbps > 10 and upload_speed_mbps > 1:
        return "Good Network Speed. Sync should happen."
    elif download_speed_mbps > 5 and upload_speed_mbps > 0.5:
        return "Fair Network Speed. Sync might not happen unless better Wi-Fi is used."
    else:
        return "Poor Network Speed. Sync might not happen unless better Wi-Fi is used."

def categorize_malay_speed(download_speed, upload_speed):
    download_speed_mbps = download_speed / (10**6)  # converting from bits to megabits
    upload_speed_mbps = upload_speed / (10**6)

    if download_speed_mbps > 25 and upload_speed_mbps > 3:
        return "Kelajuan rangkaian yang sangat baik. Penyegerakan harus berlaku."
    elif download_speed_mbps > 10 and upload_speed_mbps > 1:
        return "Kelajuan rangkaian yang baik. Penyegerakan harus berlaku."
    elif download_speed_mbps > 5 and upload_speed_mbps > 0.5:
        return "Kelajuan rangkaian yang adil. Penyegerakan mungkin tidak berlaku kecuali Wi-Fi yang lebih baik digunakan."
    else:
        return "Kelajuan rangkaian yang lemah. Penyegerakan mungkin tidak berlaku kecuali Wi-Fi yang lebih baik digunakan."
    
def categorize_gujarati_speed(download_speed, upload_speed):
    download_speed_mbps = download_speed / (10**6)  # converting from bits to megabits
    upload_speed_mbps = upload_speed / (10**6)

    if download_speed_mbps > 25 and upload_speed_mbps > 3:
        return "ઉત્તમ નેટવર્ક સ્પીડ. સમન્વયન થવું જોઈએ."
    elif download_speed_mbps > 10 and upload_speed_mbps > 1:
        return "સારી નેટવર્ક સ્પીડ. સમન્વયન થવું જોઈએ."
    elif download_speed_mbps > 5 and upload_speed_mbps > 0.5:
        return "વાજબી નેટવર્ક ઝડપ. જ્યાં સુધી બહેતર Wi-Fi નો ઉપયોગ કરવામાં ન આવે ત્યાં સુધી સમન્વયન થઈ શકશે નહીં."
    else:
        return "નબળી નેટવર્ક ઝડપ. જ્યાં સુધી બહેતર Wi-Fi નો ઉપયોગ કરવામાં ન આવે ત્યાં સુધી સમન્વયન થઈ શકશે નહીં.."
    
def categorize_swahili_speed(download_speed, upload_speed):
    download_speed_mbps = download_speed / (10**6)  # converting from bits to megabits
    upload_speed_mbps = upload_speed / (10**6)

    if download_speed_mbps > 25 and upload_speed_mbps > 3:
        return "Kasi ya Mtandao Bora. Usawazishaji unapaswa kutokea."
    elif download_speed_mbps > 10 and upload_speed_mbps > 1:
        return "Kasi nzuri ya Mtandao. Usawazishaji unapaswa kutokea."
    elif download_speed_mbps > 5 and upload_speed_mbps > 0.5:
        return "Kasi ya Mtandao ya Haki. Usawazishaji hauwezi kutokea isipokuwa Wi-Fi bora itatumiwa."
    else:
        return "Kasi duni ya Mtandao. Usawazishaji hauwezi kutokea isipokuwa Wi-Fi bora itatumiwa."
    
def categorize_indonesian_speed(download_speed, upload_speed):
    download_speed_mbps = download_speed / (10**6)  # converting from bits to megabits
    upload_speed_mbps = upload_speed / (10**6)

    if download_speed_mbps > 25 and upload_speed_mbps > 3:
        return "Kecepatan Jaringan Luar Biasa. Sinkronisasi harus terjadi."
    elif download_speed_mbps > 10 and upload_speed_mbps > 1:
        return "Kecepatan Jaringan Bagus. Sinkronisasi harus terjadi."
    elif download_speed_mbps > 5 and upload_speed_mbps > 0.5:
        return "Kecepatan Jaringan Lumayan. Sinkronisasi mungkin tidak terjadi kecuali Wi-Fi yang lebih baik digunakan."
    else:
        return "Kecepatan Jaringan Buruk. Sinkronisasi mungkin tidak terjadi kecuali Wi-Fi yang lebih baik digunakan."
    
def categorize_kannada_speed(download_speed, upload_speed):
    download_speed_mbps = download_speed / (10**6)  # converting from bits to megabits
    upload_speed_mbps = upload_speed / (10**6)

    if download_speed_mbps > 25 and upload_speed_mbps > 3:
        return "ಅತ್ಯುತ್ತಮ ನೆಟ್‌ವರ್ಕ್ ವೇಗ. ಸಿಂಕ್ ಆಗಬೇಕು."
    elif download_speed_mbps > 10 and upload_speed_mbps > 1:
        return "ಉತ್ತಮ ನೆಟ್‌ವರ್ಕ್ ವೇಗ. ಸಿಂಕ್ ಆಗಬೇಕು."
    elif download_speed_mbps > 5 and upload_speed_mbps > 0.5:
        return "ಫೇರ್ ನೆಟ್ವರ್ಕ್ ಸ್ಪೀಡ್. ಉತ್ತಮ ವೈ-ಫೈ ಬಳಸದ ಹೊರತು ಸಿಂಕ್ ಆಗದೇ ಇರಬಹುದು."
    else:
        return "ಕಳಪೆ ನೆಟ್‌ವರ್ಕ್ ವೇಗ. ಉತ್ತಮ ವೈ-ಫೈ ಬಳಸದ ಹೊರತು ಸಿಂಕ್ ಆಗದೇ ಇರಬಹುದು."
    
def categorize_khmer_speed(download_speed, upload_speed):
    download_speed_mbps = download_speed / (10**6)  # converting from bits to megabits
    upload_speed_mbps = upload_speed / (10**6)

    if download_speed_mbps > 25 and upload_speed_mbps > 3:
        return "ល្បឿនបណ្តាញដ៏អស្ចារ្យ។ សមកាលកម្មគួរតែកើតឡើង។"
    elif download_speed_mbps > 10 and upload_speed_mbps > 1:
        return "ល្បឿនបណ្តាញល្អ។ សមកាលកម្មគួរតែកើតឡើង។"
    elif download_speed_mbps > 5 and upload_speed_mbps > 0.5:
        return "ល្បឿនបណ្តាញយុត្តិធម៌។ សមកាលកម្មអាចនឹងមិនកើតឡើងទេ លុះត្រាតែ Wi-Fi ប្រសើរជាងមុនត្រូវបានប្រើប្រាស់។"
    else:
        return "ល្បឿនបណ្តាញខ្សោយ។ សមកាលកម្មអាចនឹងមិនកើតឡើងទេ លុះត្រាតែ Wi-Fi ប្រសើរជាងមុនត្រូវបានប្រើប្រាស់។"
    
def categorize_sesotho_speed(download_speed, upload_speed):
    download_speed_mbps = download_speed / (10**6)  # converting from bits to megabits
    upload_speed_mbps = upload_speed / (10**6)

    if download_speed_mbps > 25 and upload_speed_mbps > 3:
        return "Lebelo le Khabane la Marang-rang. Sync e tlameha ho etsahala."
    elif download_speed_mbps > 10 and upload_speed_mbps > 1:
        return "Lebelo le Ntle la Marang-rang. Sync e tlameha ho etsahala."
    elif download_speed_mbps > 5 and upload_speed_mbps > 0.5:
        return "Lebelo la Marang-rang le Ntle. Khokahano e kanna ea se etsahale ntle le haeba Wi-Fi e betere e sebelisoa."
    else:
        return "Lebelo le Fosahetseng la Marang-rang. Khokahano e kanna ea se etsahale ntle le haeba Wi-Fi e betere e sebelisoa."

def categorize_isizulu_speed(download_speed, upload_speed):
    download_speed_mbps = download_speed / (10**6)  # converting from bits to megabits
    upload_speed_mbps = upload_speed / (10**6)

    if download_speed_mbps > 25 and upload_speed_mbps > 3:
        return "Isivinini senethiwekhi esihle kakhulu. Ukuvumelanisa kufanele kwenzeke."
    elif download_speed_mbps > 10 and upload_speed_mbps > 1:
        return "Isivinini Senethiwekhi Esihle. Ukuvumelanisa kufanele kwenzeke."
    elif download_speed_mbps > 5 and upload_speed_mbps > 0.5:
        return "Isivinini senethiwekhi esilungile. Ukuvumelanisa kungase kungenzeki ngaphandle uma kusetshenziswe i-Wi-Fi engcono."
    else:
        return "Isivinini Senethiwekhi Esibi. Ukuvumelanisa kungase kungenzeki ngaphandle uma kusetshenziswe i-Wi-Fi engcono."


def perform_speedtest():
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()

    return res["download"], res["upload"]

value = st.selectbox('Language', ('English', 'Melayu', "Kiswahili", "ગુજરાતી", 'bahasa Indonesia', 'ಕನ್ನಡ', 'ខ្មែរ','Sesotho', 'Isizulu'))

if value == "English":

    st.title('reach52 Internet Speed Test')

    if st.button('Perform Speed Test'):
        with st.spinner('Performing speed test...'):
            download_speed, upload_speed = perform_speedtest()
            speed_category = categorize_speed(download_speed, upload_speed)

        st.write(f'Download speed: {download_speed / (10**6):.2f} Mbps')
        st.write(f'Upload speed: {upload_speed / (10**6):.2f} Mbps')
        st.markdown(f'## **Speed category: {speed_category}**')

elif value == "Melayu":
    st.title('Ujian kelajuan internet')

    if st.button('Lakukan ujian kelajuan'):
        with st.spinner('Melakukan ujian kelajuan ...'):
            download_speed, upload_speed = perform_speedtest()
            speed_category = categorize_malay_speed(download_speed, upload_speed)

        st.write(f'Kelajuan muat turun: {download_speed / (10**6):.2f} Mbps')
        st.write(f'Kelajuan muat naik: {upload_speed / (10**6):.2f} Mbps')
        st.markdown(f'## **Kategori kelajuan: {speed_category}**')

elif value == "ગુજરાતી":
    st.title('ઈન્ટરનેટ સ્પીડ ટેસ્ટ')

    if st.button('સ્પીડ ટેસ્ટ કરો'):
        with st.spinner('ઝડપ પરીક્ષણ કરી રહ્યું છે...'):
            download_speed, upload_speed = perform_speedtest()
            speed_category = categorize_gujarati_speed(download_speed, upload_speed)

        st.write(f'ડાઉનલોડ ઝડપ: {download_speed / (10**6):.2f} Mbps')
        st.write(f'અપલોડ ઝડપ: {upload_speed / (10**6):.2f} Mbps')
        st.markdown(f'## **ઝડપ શ્રેણી: {speed_category}**')

elif value == "Kiswahili":
    st.title('Mtihani wa Kasi ya Mtandao')

    if st.button('Fanya Mtihani wa Kasi'):
        with st.spinner('Inafanya jaribio la kasi...'):
            download_speed, upload_speed = perform_speedtest()
            speed_category = categorize_swahili_speed(download_speed, upload_speed)

        st.write(f'Kasi ya upakuaji: {download_speed / (10**6):.2f} Mbps')
        st.write(f'Kasi ya Upakiaji: {upload_speed / (10**6):.2f} Mbps')
        st.markdown(f'## **Aina ya Kasi: {speed_category}**')

elif value == "bahasa Indonesia":
    st.title('Tes Kecepatan Internet')

    if st.button('Lakukan Tes Kecepatan'):
        with st.spinner('Melakukan uji kecepatan...'):
            download_speed, upload_speed = perform_speedtest()
            speed_category = categorize_swahili_speed(download_speed, upload_speed)

        st.write(f'Kecepatan unduh: {download_speed / (10**6):.2f} Mbps')
        st.write(f'Kecepatan mengunggah: {upload_speed / (10**6):.2f} Mbps')
        st.markdown(f'## **Kategori Kecepatan: {speed_category}**')

elif value == "ಕನ್ನಡ": #kannada
    st.title('ಇಂಟರ್ನೆಟ್ ವೇಗ ಪರೀಕ್ಷೆ')

    if st.button('ಸ್ಪೀಡ್ ಟೆಸ್ಟ್ ಮಾಡಿ'):
        with st.spinner('ವೇಗ ಪರೀಕ್ಷೆಯನ್ನು ನಡೆಸಲಾಗುತ್ತಿದೆ...'):
            download_speed, upload_speed = perform_speedtest()
            speed_category = categorize_kannada_speed(download_speed, upload_speed)

        st.write(f'ಡೌನ್‌ಲೋಡ್ ವೇಗ: {download_speed / (10**6):.2f} Mbps')
        st.write(f'ವೇಗವಾಗಿ ಜಾಲಕ್ಕೆ ರವಾನಿಸು: {upload_speed / (10**6):.2f} Mbps')
        st.markdown(f'## **ವೇಗ ವರ್ಗ: {speed_category}**')

elif value == "ខ្មែរ": #khmer
    st.title('តេស្តល្បឿនអ៊ីនធឺណិត')

    if st.button('ធ្វើតេស្តល្បឿន'):
        with st.spinner('ធ្វើតេស្តល្បឿន...'):
            download_speed, upload_speed = perform_speedtest()
            speed_category = categorize_khmer_speed(download_speed, upload_speed)

        st.write(f'ល្បឿនទាញយក៖ {download_speed / (10**6):.2f} Mbps')
        st.write(f'ល្បឿនផ្ទុកឡើង៖ {upload_speed / (10**6):.2f} Mbps')
        st.markdown(f'## **ប្រភេទល្បឿន៖ {speed_category}**')

elif value == "Sesotho": 
    st.title('Teko ea Lebelo la Marang-rang')

    if st.button('Etsa Tlhahlobo ea Lebelo'):
        with st.spinner('E etsa teko ea lebelo...'):
            download_speed, upload_speed = perform_speedtest()
            speed_category = categorize_sesotho_speed(download_speed, upload_speed)

        st.write(f'Lebelo la ho khoasolla: {download_speed / (10**6):.2f} Mbps')
        st.write(f'Lebelo la ho Kenya: {upload_speed / (10**6):.2f} Mbps')
        st.markdown(f'## **Sehlopha sa lebelo: {speed_category}**')

elif value == "Isizulu": 
    st.title('Ukuhlolwa Kwesivinini Se-inthanethi')

    if st.button('Yenza Test Speed'):
        with st.spinner('Yenza ukuhlolwa kwesivinini...'):
            download_speed, upload_speed = perform_speedtest()
            speed_category = categorize_isizulu_speed(download_speed, upload_speed)

        st.write(f'Isivinini sokulanda: {download_speed / (10**6):.2f} Mbps')
        st.write(f'Isivinini sokulayisha: {upload_speed / (10**6):.2f} Mbps')
        st.markdown(f'## **Isigaba sesivinini: {speed_category}**')