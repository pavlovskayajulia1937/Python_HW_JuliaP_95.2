from sqlalchemy import create_engine, inspect, text

db_connection = "postgresql://postgres:1234@localhost:5432/QA"

db = create_engine(db_connection)

def test_add_subject():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("INSERT into subject(subject_title, subject_id) VALUES (:subject_title, :subject_id)")
    connection.execute(sql, {'subject_title': "Skypro", 'subject_id': "16"})
    
    res = connection.execute(text("select subject_title from subject where subject_id = :id"), {"id": 16}).fetchone()
    
    assert res[0] == "Skypro"
    sql = text("DELETE FROM subject WHERE subject_id = :subject_id")
    connection.execute(sql, {"subject_id": 16})
    
    transaction.commit()
    connection.close()

def test_edit_subject():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("INSERT into subject(subject_title, subject_id) VALUES (:subject_title, :subject_id)")
    connection.execute(sql, {'subject_title': "Skypro", 'subject_id': "16"})

    sql = text("UPDATE subject SET subject_title = :subject_title WHERE subject_id = :subject_id")
    connection.execute(sql, {'subject_title': "New_subject_title", 'subject_id': 16})
    
    res = connection.execute(text("select subject_title from subject where subject_id = :id"), {"id": 16}).fetchone()
    assert res[0] == "New_subject_title"
    
    sql = text("DELETE FROM subject WHERE subject_id = :subject_id")
    connection.execute(sql, {"subject_id": 16})
    
    transaction.commit()
    connection.close()

def test_delete_subject():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("INSERT into subject(subject_title, subject_id) VALUES (:subject_title, :subject_id)")
    connection.execute(sql, {'subject_title': "Skypro", 'subject_id': "16"})

    sql = text("DELETE FROM subject WHERE subject_id = :subject_id")
    connection.execute(sql, {"subject_id": 16})

    res = connection.execute(text("select subject_title from subject where subject_id = :id"), {"id": 16}).fetchone()
    assert res is None

    transaction.commit()
    connection.close()