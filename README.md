# finalproject_dsp
# Anggota Kelompok
Adha Putro Wicaksono - 121140156 - AdhaPutro156  
Hafiza Eka Ramadhini - 121140048 - hafizaekard  
Ernita - 121140038- TheAqueena1106  

# Deskripsi Project
Proyek ini bertujuan untuk mendeteksi sinyal respirasi dan sinyal Photoplethysmogram (rPPG) untuk pengukuran detak jantung secara real-time menggunakan webcam sebagai sensor utama. Deteksi dilakukan tanpa perangkat keras tambahan, sehingga proyek ini mendukung teknologi non-invasive monitoring. Berikut adalah penjelasan detail tentang proyek ini:  
tujuan proyek:  
1. pemantauan pernafasan, hal ini berdasarkan pola perubahan intensitas citra pada wajah
2. pemantauan detak jantung , mendeteksi sinyal rPPG dengan cara mengekstrak variasi kanal wajah yang berwarna hujau jdari wajah untuk estimasi detak jantung
3. real-time monitoring, ini bertujuan untuk mengolah dan menampilkan si nyal secara langsung sehingga memungkinkan analisis visuak melalui grafik dinamis.

Metode implementasi pada proyek ini melibatkan beberapa langkah utama yang saling terintegrasi. Proses dimulai dengan pengambilan data menggunakan webcam sebagai perangkat utama untuk menangkap citra video secara real-time. Webcam digunakan untuk mendeteksi wajah pengguna melalui teknik Haar Cascade Classifier, yang merupakan metode berbasis machine learning untuk mengidentifikasi objek dalam sebuah gambar. Setelah wajah terdeteksi, area tertentu dari wajah yang disebut Region of Interest (ROI) dipilih untuk dianalisis lebih lanjut. Pada tahap ekstraksi sinyal, intensitas rata-rata dari area abu-abu pada ROI wajah dihitung untuk mendapatkan sinyal respirasi. Sinyal ini merepresentasikan perubahan dalam pola pernapasan berdasarkan variasi intensitas gambar. Selain itu, variasi intensitas warna hijau pada ROI wajah juga diekstraksi, yang berkaitan dengan aliran darah di bawah permukaan kulit. Sinyal ini digunakan untuk mengestimasi rPPG (Photoplethysmogram), yang merupakan representasi digital dari detak jantung.

Sinyal mentah yang diperoleh dari tahap sebelumnya sering kali terkontaminasi oleh noise dari lingkungan, sehingga diterapkan filter bandpass menggunakan algoritma Butterworth. Filter ini dirancang untuk memisahkan frekuensi yang relevan, yaitu 0.1-0.5 Hz untuk sinyal respirasi dan 0.7-4.0 Hz untuk sinyal rPPG. Dengan demikian, hanya komponen sinyal yang sesuai dengan rentang frekuensi tersebut yang dipertahankan, sementara noise yang tidak diinginkan dieliminasi.

Setelah sinyal difilter, hasilnya divisualisasikan secara real-time menggunakan grafik dinamis yang dibuat dengan pustaka matplotlib. Grafik ini menampilkan perubahan amplitudo sinyal terhadap waktu, sehingga pola respirasi dan detak jantung dapat diamati secara langsung oleh pengguna. Selama proses ini, sistem juga menghitung dan menampilkan FPS (Frame Per Second) pada tampilan video, yang berguna untuk memastikan bahwa pemrosesan berjalan dengan lancar tanpa hambatan signifikan. Metode implementasi ini memberikan pendekatan yang efisien untuk mengolah data video menjadi informasi fisiologis yang berguna, sekaligus memungkinkan pengguna untuk memantau kondisi secara intuitif.

# LoogBook Mingguan
30 november - diskusi projek tugas besar   
6 desember - pembuatan github project  
10 desember - pembuatan code   
17 desember - pembuatan code   
20 desember - revisi error   
24 desember - final code   

# Instruksi Instalasi dan Penggunaan Program
## Persyaratan Sistem
Pastikan Anda memiliki hal-hal berikut sebelum menjalankan program:
- Python 3.6 atau versi lebih baru
Paket-paket Python yang diperlukan:
- opencv-python
- numpy
- matplotlib
- scipy
## Instalasi
1. Clone Repository
   Clone repository ini ke komputer Anda menggunakan perintah berikut:
   git clone https://github.com/username/repository-name.git
cd repository-name
2. Install Dependensi
   Install semua dependensi yang dibutuhkan:
   - pip install -r requirements.txt
3. Pastikan Webcam Berfungsi
   Program ini menggunakan webcam, jadi pastikan webcam Anda terhubung dan berfungsi.
## Cara Menggunakan
1. Jalankan program dengan perintah berikut:
   - python main.py
     Ganti main.py dengan nama file Python Anda jika berbeda.
2. Setelah program dijalankan, jendela webcam akan muncul dan:
   - Wajah akan dideteksi menggunakan Haar Cascade.
   - Data sinyal respirasi dan rPPG (Remote Photoplethysmography) akan dianalisis secara real-time.
   - Plot sinyal akan ditampilkan menggunakan matplotlib.
3. Tekan tombol q pada keyboard untuk keluar dari program.
