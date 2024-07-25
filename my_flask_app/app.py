from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Пример данных пользователя для редактирования
user_data = {
    'name': 'Иван Иванов',
    'email': 'ivan@example.com',
    'password': 'password123'
}


@app.route('/templates/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        # Получаем данные из формы
        user_data['name'] = request.form.get('name')
        user_data['email'] = request.form.get('email')
        user_data['password'] = request.form.get('password')
        return redirect(url_for('profile'))
    return render_template('profile.html', user=user_data)


if __name__ == '__main__':
    app.run(debug=True)