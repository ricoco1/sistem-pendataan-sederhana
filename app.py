from flask import Flask, request, render_template, redirect,jsonify

app = Flask(__name__)

@app.route('/')
def registrasi():
    return render_template('registrasi.html')

@app.route('/registration_detail', methods=['POST'])
def registration_detail():
    if request.method == 'POST':
        # Mendapatkan data dari form
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Mengalihkan ke halaman detail registrasi dan meneruskan data
        return redirect('/detail-registrasi?username={}&email={}&password={}'.format(username, email, password))

@app.route('/detail-registrasi')
def detail_registraasi():
    # Mendapatkan data yang diteruskan dari halaman registrasi
    username = request.args.get('username')
    email = request.args.get('email')
    password = request.args.get('password')

    # Mengirim data ke halaman detail registrasi
    return render_template('detail_registrasi.html', username=username, email=email, password=password)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
