from flask import Blueprint, render_template, redirect, url_for, request, flash
from .models import User, db, bcrypt
import random

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/about')
def about():
    return render_template('about.html')

@views.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user:
            flash('Username already exists', category='error')
        else:
            new_user = User(username=username)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully!', category='success')
            return redirect(url_for('views.login'))

    return render_template('signup.html')

@views.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            flash('Logged in successfully!', category='success')
            return redirect(url_for('views.home'))
        else:
            flash('Login unsuccessful. Please check your username and password', category='error')

    return render_template('login.html')

@views.route('/rock', methods=["GET"])
def rock():
    quiz_questions = [
        {
            "question": "Bohemian Rhapsody",
            "correct_answer": "Queen",
            "options": ["Queen", "The Beatles", "Led Zeppelin", "Pink Floyd"]
        },
        {
            "question": "Stairway to Heaven",
            "correct_answer": "Led Zeppelin",
            "options": ["Queen", "Led Zeppelin", "Pink Floyd", "AC/DC"]
        },
        {
            "question": "Imagine",
            "correct_answer": "John Lennon",
            "options": ["John Lennon", "The Beatles", "Elton John", "Bob Dylan"]
        },
        {
            "question": "Come Together",
            "correct_answer": "The Beatles",
            "options": ["Paul McCartney", "Bob Dylan", "Elton John", "The Beatles"]
        },
        {
            "question": "Back in Black",
            "correct_answer": "AC/DC",
            "options": ["Guns N' Roses", "The Rolling Stones", "AC/DC", "Nirvana"]
        }
    ]
    quiz_data = random.choice(quiz_questions)
    return render_template('rock.html', quiz=quiz_data)

@views.route('/pop', methods=["GET"])
def pop():
    quiz_questions = [
        {
            "question": "Thriller",
            "correct_answer": "Michael Jackson",
            "options": ["Prince", "Madonna", "Michael Jackson", "Whitney Houston"]
        },
        {
            "question": "Like a Prayer",
            "correct_answer": "Madonna",
            "options": ["Madonna", "Cyndi Lauper", "Whitney Houston", "Janet Jackson"]
        },
        {
            "question": "Rolling in the Deep",
            "correct_answer": "Adele",
            "options": ["Beyoncé", "Adele", "Taylor Swift", "Katy Perry"]
        },
        {
            "question": "Uptown Funk",
            "correct_answer": "Mark Ronson ft. Bruno Mars",
            "options": ["Anderson .Paak", "Mark Ronson ft. Bruno Mars", "Pharrell Williams", "Justin Timberlake"]
        },
        {
            "question": "Shape of You",
            "correct_answer": "Ed Sheeran",
            "options": ["Charlie Puth", "Shawn Mendes", "Ed Sheeran", "Justin Bieber"]
        }
    ]
    quiz_data = random.choice(quiz_questions)
    return render_template('pop.html', quiz=quiz_data)

@views.route('/indie', methods=["GET"])
def indie():
    quiz_questions = [
        {
            "question": "Mr. Brightside",
            "correct_answer": "The Killers",
            "options": ["The Killers", "Arctic Monkeys", "Vampire Weekend", "The Strokes"]
        },
        {
            "question": "Take Me Out",
            "correct_answer": "Franz Ferdinand",
            "options": ["Franz Ferdinand", "The Strokes", "The White Stripes", "Arctic Monkeys"]
        },
        {
            "question": "Electric Feel",
            "correct_answer": "MGMT",
            "options": ["MGMT", "Tame Impala", "Foster the People", "Phoenix"]
        },
        {
            "question": "Do I Wanna Know?",
            "correct_answer": "Arctic Monkeys",
            "options": ["The Black Keys", "The Killers", "The Strokes", "Arctic Monkeys"]
        },
        {
            "question": "Pumped Up Kicks",
            "correct_answer": "Foster the People",
            "options": ["Tame Impala", "Foster the People", "MGMT", "Phoenix"]
        }
    ]
    quiz_data = random.choice(quiz_questions)
    return render_template('indie.html', quiz=quiz_data)

@views.route('/rap', methods=["GET"])
def rap():
    quiz_questions = [
        {
            "question": "Lose Yourself",
            "correct_answer": "Eminem",
            "options": ["Eminem", "Jay-Z", "Kanye West", "Dr. Dre"]
        },
        {
            "question": "Juicy",
            "correct_answer": "The Notorious B.I.G.",
            "options": ["Tupac Shakur", "The Notorious B.I.G.", "Nas", "Jay-Z"]
        },
        {
            "question": "Sicko Mode",
            "correct_answer": "Travis Scott",
            "options": ["Kendrick Lamar", "J. Cole", "Drake", "Travis Scott"]
        },
        {
            "question": "HUMBLE.",
            "correct_answer": "Kendrick Lamar",
            "options": ["Kendrick Lamar", "J. Cole", "Drake", "Future"]
        },
        {
            "question": "God's Plan",
            "correct_answer": "Drake",
            "options": ["Kanye West", "Lil Wayne", "Drake", "Post Malone"]
        }
    ]
    quiz_data = random.choice(quiz_questions)
    return render_template('rap.html', quiz=quiz_data)

@views.route('/folk', methods=["GET"])
def folk():
    quiz_questions = [
        {
            "question": "Blowin' in the Wind",
            "correct_answer": "Bob Dylan",
            "options": ["Bob Dylan", "Joan Baez", "Pete Seeger", "Woody Guthrie"]
        },
        {
            "question": "The Sound of Silence",
            "correct_answer": "Simon & Garfunkel",
            "options": ["Simon & Garfunkel", "Bob Dylan", "Peter, Paul and Mary", "The Byrds"]
        },
        {
            "question": "Big Yellow Taxi",
            "correct_answer": "Joni Mitchell",
            "options": ["Joni Mitchell", "Carly Simon", "Carole King", "Joan Baez"]
        },
        {
            "question": "The Times They Are a-Changin'",
            "correct_answer": "Bob Dylan",
            "options": ["Bob Dylan", "Pete Seeger", "Woody Guthrie", "Joan Baez"]
        },
        {
            "question": "If I Had a Hammer",
            "correct_answer": "Pete Seeger",
            "options": ["Pete Seeger", "Woody Guthrie", "Peter, Paul and Mary", "Joan Baez"]
        }
    ]
    quiz_data = random.choice(quiz_questions)
    return render_template('folk.html', quiz=quiz_data)

@views.route('/country', methods=["GET"])
def country():
    quiz_questions = [
        {
            "question": "Jolene",
            "correct_answer": "Dolly Parton",
            "options": ["Dolly Parton", "Patsy Cline", "Loretta Lynn", "Reba McEntire"]
        },
        {
            "question": "Friends in Low Places",
            "correct_answer": "Garth Brooks",
            "options": ["Garth Brooks", "George Strait", "Alan Jackson", "Tim McGraw"]
        },
        {
            "question": "Ring of Fire",
            "correct_answer": "Johnny Cash",
            "options": ["Johnny Cash", "Willie Nelson", "Merle Haggard", "Hank Williams"]
        },
        {
            "question": "The Gambler",
            "correct_answer": "Kenny Rogers",
            "options": ["Kenny Rogers", "George Jones", "Waylon Jennings", "Willie Nelson"]
        },
                {
            "question": "Take Me Home, Country Roads",
            "correct_answer": "John Denver",
            "options": ["John Denver", "Glen Campbell", "Kris Kristofferson", "Charlie Rich"]
        }
    ]
    quiz_data = random.choice(quiz_questions)
    return render_template('country.html', quiz=quiz_data)


