import os
from sqlalchemy import create_engine, text

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_counselors_from_db():
  with engine.connect() as conn:
    result = conn.execute(
      text(
        "SELECT counselor_name, name, gender, age, occupation, time, about, phone_no, email FROM anuyog_counselor"
      ))
    counselors = []
    for row in result.fetchall():
      counselor = {
        'counselor_name': row[0],
        'name': row[1],
        'gender': row[2],
        'age': row[3],
        'occupation': row[4],
        'time': row[5],
        'about': row[6],
        'phone_no': row[7],
        'email': row[8]
      }
      counselors.append(counselor)
    return counselors


def load_distinct_gender_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT distinct gender FROM anuyog_counselor"))
    gender = []
    for row in result.fetchall():
      genders = {'gender': row[0]}
      gender.append(genders)
    return gender


def load_distinct_age_from_db():
  with engine.connect() as conn:
    result = conn.execute(
      text("SELECT distinct age FROM anuyog_counselor order by age asc"))
    age = []
    for row in result.fetchall():
      ages = {'age': row[0]}
      age.append(ages)
    return age


def load_distinct_time_from_db():
  with engine.connect() as conn:
    result = conn.execute(
      text("SELECT distinct time FROM anuyog_counselor order by time asc;"))
    time = []
    for row in result.fetchall():
      times = {'time': row[0]}
      time.append(times)
    return time


def add_counselor_to_db(data):
  with engine.connect() as conn:
    query = text(
      """INSERT INTO anuyog_counselor (counselor_name, name, gender, age, occupation, time, about, phone_no, email)
                        VALUES (:counselor_name, :name, :gender, :age, :occupation, :time, :about, :phone_no, :email)"""
    )
    params = {
      'counselor_name': data['counselor_name'],
      'name': data['name'],
      'gender': data['gender'],
      'age': data['age'],
      'occupation': data['occupation'],
      'time': data['time'],
      'about': data['about'],
      'phone_no': data['phone_no'],
      'email': data['email']
    }
    conn.execute(query, params)


def selected_counselor_from_db(counselor_name):
  with engine.connect() as conn:
    result = conn.execute(
      text(
        f"SELECT * FROM anuyog_counselor WHERE counselor_name = '{counselor_name}'"
      ))
    rows = result.all()
    if len(rows) == 0:
      return "not available"
    else:
      return rows[0]._mapping


def load_available_counselors_from_db(gender, age, time):
  with engine.connect() as conn:
    result = conn.execute(
      text(
        f"SELECT counselor_name, name, gender, age, occupation, time, about, phone_no, email FROM anuyog_counselor WHERE gender = '{gender}' and age='{age}' and time='{time}'"
      ))
    counselors = []
    for row in result.fetchall():
      counselor = {
        'counselor_name': row[0],
        'name': row[1],
        'gender': row[2],
        'age': row[3],
        'occupation': row[4],
        'time': row[5],
        'about': row[6],
        'phone_no': row[7],
        'email': row[8]
      }
      counselors.append(counselor)
    return counselors


def add_answers_to_db(data):
  with engine.connect() as conn:
    query = text(
      """INSERT INTO anuyog_questions(question_1,question_2,question_3,question_4,question_5,question_6,question_7,question_8,question_9,question_10,question_11,question_12,question_13,question_14,question_15,question_16,question_17,question_18,question_19,question_20,question_21,question_22,question_23,question_24,question_25,question_26,question_27,question_28,question_29,question_30 )
                        VALUES (:question_1,:question_2,:question_3,:question_4,:question_5,:question_6,:question_7,:question_8,:question_9,:question_10,:question_11,:question_12,:question_13,:question_14,:question_15,:question_16,:question_17,:question_18,:question_19,:question_20,:question_21,:question_22,:question_23,:question_24,:question_25,:question_26,:question_27,:question_28,:question_29,:question_30)"""
    )

    params = {
      'question_1': data['question_1'],
      'question_2': data['question_2'],
      'question_3': data['question_3'],
      'question_4': data['question_4'],
      'question_5': data['question_5'],
      'question_6': data['question_6'],
      'question_7': data['question_7'],
      'question_8': data['question_8'],
      'question_9': data['question_9'],
      'question_10': data['question_10'],
      'question_11': data['question_11'],
      'question_12': data['question_12'],
      'question_13': data['question_13'],
      'question_14': data['question_14'],
      'question_15': data['question_15'],
      'question_16': data['question_16'],
      'question_17': data['question_17'],
      'question_18': data['question_18'],
      'question_19': data['question_19'],
      'question_20': data['question_20'],
      'question_21': data['question_21'],
      'question_22': data['question_22'],
      'question_23': data['question_23'],
      'question_24': data['question_24'],
      'question_25': data['question_25'],
      'question_26': data['question_26'],
      'question_27': data['question_27'],
      'question_28': data['question_28'],
      'question_29': data['question_29'],
      'question_30': data['question_30']
    }

    conn.execute(query, params)
