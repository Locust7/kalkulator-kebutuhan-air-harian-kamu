import streamlit as st

st.set_page_config(page_title="Kebutuhan Air Harian", layout="centered")

st.title("💧 Kalkulator Kebutuhan Air Harian")
st.write("Hitung kebutuhan air harianmu berdasarkan berat badan, aktivitas, kondisi cuaca, jenis kelamin, dan usia.")

# Input Pengguna
berat = st.number_input("Masukkan berat badan kamu (kg):", min_value=1.0, step=0.5)
aktivitas = st.selectbox("Pilih tingkat aktivitas:", ["Ringan", "Sedang", "Berat"])
cuaca = st.selectbox("Bagaimana kondisi cuaca di tempatmu sekarang?", ["Dingin", "Normal", "Panas"])
jenis_kelamin = st.selectbox("Jenis kelamin:", ["Pria", "Wanita"])
usia = st.number_input("Masukkan usia kamu:", min_value=1, max_value=120, step=1)

# Fungsi perhitungan
def hitung_air(berat, aktivitas, cuaca, jenis_kelamin, usia):
    dasar = berat * 30  # 30 ml per kg

    # Penyesuaian berdasarkan aktivitas
    if aktivitas == "Sedang":
        dasar += 300
    elif aktivitas == "Berat":
        dasar += 600

    # Penyesuaian berdasarkan cuaca
    if cuaca == "Panas":
        dasar += 400
    elif cuaca == "Dingin":
        dasar -= 200

    # Penyesuaian berdasarkan jenis kelamin
    if jenis_kelamin == "Pria":
        dasar += 200  # Pria cenderung butuh lebih banyak air
    elif jenis_kelamin == "Wanita":
dasar -= 100  # Wanita cenderung butuh sedikit lebih sedikit air

    # Penyesuaian berdasarkan usia
    if usia < 18:
        dasar -= 300  # Anak-anak membutuhkan sedikit air
    else:
        dasar += 0  # Dewasa membutuhkan air sesuai hitungan dasar

    return dasar / 1000  # Mengubah dari ml ke liter

# Tombol dan hasil
if st.button("Hitung Kebutuhan Air"):
    if berat > 0:
        total = hitung_air(berat, aktivitas, cuaca, jenis_kelamin, usia)
        st.success(f"Kebutuhan air harian kamu sekitar *{total:.2f} liter*.")
    else:
        st.warning("Masukkan berat badan yang valid.")

st.markdown("---")
st.caption("Proyek Streamlit oleh [IFTA, NADILA, SULTHAN, VANIA, DAVIONA]")
