from flask import Flask, render_template

# Menginisialisasi aplikasi Flask
app = Flask(__name__)

# Mengatur rute utama (Halaman Beranda)
@app.route('/')
def home():
    # Mengirimkan file index.html ke browser pengguna
    return render_template('index.html')

if __name__ == '__main__':
    # Menjalankan server lokal pada mode debug
    app.run(debug=True)
