from flask import Flask, render_template, flash, request, redirect
from forms import ContactForm
import logging

# Setup logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.secret_key = "a-very-secret-key"  # Required for forms

@app.route('/')
def index():
    form = ContactForm()
    return render_template('index.html', form=form)

@app.route('/contact', methods=['POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        flash('Thank you for your message! We will get back to you soon.', 'success')
        return redirect('/')
    flash('Please check your form entries.', 'error')
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
