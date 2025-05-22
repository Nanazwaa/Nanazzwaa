import streamlit as st

st.title("😆💞❤ halo wllcome nanazwarnas")
st.write(
    "20-04-ganti)."
)
st.image("IMG_6012.jpeg",width=150)
st.write("\n")
st.subheader("Nanazwa Aura D")
st.write("Mari Belajar Bersama  Yesz!") 
#with col 1:
st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis Sebuah Angka:",value=0,step=1)
if(angka % 2) == 0 : 
    st.write(f"{angka}adalah bilangan genap") else:
    st.write(f"{angka}adalah bilangan ganjil")
