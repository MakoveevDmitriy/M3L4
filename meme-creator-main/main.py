#Импорт
from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__)

#Результаты формы
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # получаем выбранное изображение
        selected_image = request.form.get('image-selector')

        # Задание №2.Получаем текст
        text_top = request.form.get('text_top')
        textBottom = request.form.get('textBottom')
        # Задание №3. Получаем расположение текста
        text_top_y = request.form.get('textTop_y')
        text_bottom_y = request.form.get('textBottom_y')
        

        # Задание №3. Получаем цвет текста
        selected_color = request.form.get('selected_color')




        return render_template('index.html', 
                            # отображаем выбранное изображение
                            selected_image=selected_image, 

                            # Задание №2. Отображаем текст
                            text_top=text_top,
                            textBottom=textBottom,

                            # Задание №3. Отображаем цвет 
                            text_top_y = text_top_y,
                            text_bottom_y = text_bottom_y,

                               
                            #Задание №3. Отоброжаем расположение текста
                            selected_color=selected_color
                            )
    else:
        # отображаем первое изображение по умолчанию
        return render_template('index.html', selected_image='logo.svg')


@app.route('/static/img/<path:path>')
def serve_images(path):
    return send_from_directory('static/img', path)

app.run(debug=True)
