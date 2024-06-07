from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

# Завантаження даних з файлу CSV
df = pd.read_csv('jewelry.csv', delimiter=';')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/category', methods=['GET', 'POST'])
def category():
    categories = df['category'].unique()
    return render_template('category.html', categories=categories)

@app.route('/type', methods=['POST'])
def type():
    selected_category = request.form['category']
    types = df[df['category'] == selected_category]['type'].unique()
    return render_template('type.html', category=selected_category, types=types)

@app.route('/color', methods=['POST'])
def color():
    selected_category = request.form['category']
    selected_type = request.form['type']
    colors = df[(df['category'] == selected_category) & (df['type'] == selected_type)]['color'].unique()
    return render_template('color.html', category=selected_category, type=selected_type, colors=colors)

@app.route('/results', methods=['POST'])
def results():
    selected_category = request.form['category']
    selected_type = request.form['type']
    selected_color = request.form['color']
    jewelry = df[(df['category'] == selected_category) & (df['type'] == selected_type) & (df['color'] == selected_color)]
    return render_template('results.html', jewelry=jewelry.to_dict('records'))


if __name__ == '__main__':
    app.run(debug=True)