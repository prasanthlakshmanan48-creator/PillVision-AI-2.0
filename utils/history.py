from datetime import datetime
from database import conn, cursor

def add_history(history_type, title, content):

    cursor.execute("""
    INSERT INTO history(type,title,content,time)
    VALUES(?,?,?,?)
    """,(
        history_type,
        title,
        content,
        datetime.now().strftime("%d-%m-%Y %H:%M")
    ))

    conn.commit()


def get_history():

    cursor.execute("""
    SELECT type,title,content,time
    FROM history
    ORDER BY id DESC
    """)

    rows=cursor.fetchall()

    history=[]

    for row in rows:

        history.append({
            "type":row[0],
            "title":row[1],
            "content":row[2],
            "time":row[3]
        })

    return history


def clear_history():

    cursor.execute("DELETE FROM history")

    conn.commit()
