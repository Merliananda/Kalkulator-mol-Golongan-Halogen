import streamlit as st

st.title('Kalkulator Menghitung Mol Golongan Halogen')

tab1, tab2, tab3=st.tabs(['Informasi Tentang Golongan Halogen','Informasi Nilai Ar Golongan Halogen','Kalkulator Menghitung Mol'])

with tab1:
    st.header('Informasi Tentang Golongan Halogen')
    st.write('Halogen adalah kelompok unsur kimia yang berada pada golongan 17 (VII atau VIIA) di tabel periodik. Halogen menandakan unsur-unsur yang menghasilkan garam jika bereaksi dengan logam. Halogen juga merupakan golongan dengan keelektronegatifan tertinggi, jadi ia juga merupakan golongan paling non-logam')

with tab2:
    st.header('Nilai Ar Golongan Halogen')
    st.write('F  =19')
    st.write('Cl =35,5')
    st.write('Br =80')
    st.write('I  =127')
    st.write('At =210')

with tab3:
    st.header('Kalkulator Menghitung Mol')
    options=st.multiselect(
        'Nama Logam Mulia',
        ['F','Cl','Br','I','At'])
    x = st.number_input('Masukkan Massa Padatan dari Unsur Golongan Halogen yang Telah dipilih dalam Satuan g:')
    y = st.number_input('Masukkan Massa Atom Relatif (Ar) Golongan Halogen yang telah dipilih dalam satuan g/mol')


    tombol = st.button('Hitung Jumlah Mol dari Suatu Golongan Halogen')

    if tombol:
        jumlah_mol = x/y
        st.success(f'Jumlah Mol Adalah {options} {jumlah_mol}')

    

        
