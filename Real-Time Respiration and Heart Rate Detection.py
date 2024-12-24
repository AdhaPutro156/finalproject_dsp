import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter
import time  # Import time untuk menghitung FPS

# Fungsi untuk membuat filter bandpass
def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

# Fungsi untuk menerapkan filter bandpass
def bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order)
    y = lfilter(b, a, data)
    return y

# Konfigurasi filter
fs = 30.0  # Frame rate kamera
lowcut_resp = 0.1
highcut_resp = 0.5
lowcut_rppg = 0.7
highcut_rppg = 4.0

# Pengaturan matplotlib untuk visualisasi real-time
plt.ion()
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
resp_line, = ax1.plot([], [], 'b-', label="Sinyal Respirasi")
rppg_line, = ax2.plot([], [], 'g-', label="Sinyal rPPG")
ax1.set_xlim(0, 300)
ax1.set_ylim(-1, 1)
ax2.set_xlim(0, 300)
ax2.set_ylim(-1, 1)
ax1.set_title("Sinyal Respirasi")
ax2.set_title("Sinyal rPPG")
ax1.set_xlabel("Waktu (detik)")
ax2.set_xlabel("Waktu (detik)")
ax1.set_ylabel("Amplitudo")
ax2.set_ylabel("Amplitudo")
ax1.legend()
ax2.legend()

# Inisialisasi webcam
cap = cv2.VideoCapture(0)
buffer_size = 300
resp_signal = []
rppg_signal = []

# Load Haar Cascade classifier untuk deteksi wajah
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    start_time = time.time()  # Mulai waktu untuk menghitung FPS
    ret, frame = cap.read()
    if not ret:
        break

    # Deteksi wajah menggunakan Haar Cascade
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    if len(faces) > 0:
        # Ambil wajah pertama yang terdeteksi
        (x, y, w, h) = faces[0]

        # Tambahkan ROI untuk sinyal respirasi
        roi_resp = gray[y:y+h, x:x+w]
        mean_resp = np.mean(roi_resp)
        resp_signal.append(mean_resp)

        # Ekstraksi warna hijau untuk rPPG
        roi_face = frame[y:y+h, x:x+w]
        mean_rppg = np.mean(roi_face[:, :, 1])  # Kanal hijau
        rppg_signal.append(mean_rppg)

        # Gambar kotak deteksi wajah pada frame
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Pastikan sinyal tidak lebih panjang dari buffer
    if len(resp_signal) > buffer_size:
        resp_signal.pop(0)
    if len(rppg_signal) > buffer_size:
        rppg_signal.pop(0)

    # Filter sinyal
    if len(resp_signal) > 1:  # Pastikan ada cukup data untuk difilter
        filtered_resp = bandpass_filter(resp_signal, lowcut_resp, highcut_resp, fs)
    else:
        filtered_resp = np.zeros(len(resp_signal))  # Jika tidak ada data, gunakan array nol

    if len(rppg_signal) > 1:  # Pastikan ada cukup data untuk difilter
        filtered_rppg = bandpass_filter(rppg_signal, lowcut_rppg, highcut_rppg, fs)
    else:
        filtered_rppg = np.zeros(len(rppg_signal))  # Jika tidak ada data, gunakan array nol

    # Update plot
    resp_line.set_ydata(filtered_resp)
    resp_line.set_xdata(range(len(filtered_resp)))
    rppg_line.set_ydata(filtered_rppg)
    rppg_line.set_xdata(range(len(filtered_rppg)))
    ax1.relim()
    ax1.autoscale_view()
    ax2.relim()
    ax2.autoscale_view()
    plt.pause(0.01)

    # Hitung FPS
    elapsed_time = time.time() - start_time
    fps = 1 / elapsed_time if elapsed_time > 0 else 0

    # Tampilkan FPS di frame
    cv2.putText(frame, f'FPS: {fps:.2f}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Tampilkan frame dengan ROI
    cv2.imshow('Webcam', frame)

    # Keluar dari loop jika 'q' ditekan
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Lepaskan webcam dan tutup semua jendela
cap.release()
cv2.destroyAllWindows()
