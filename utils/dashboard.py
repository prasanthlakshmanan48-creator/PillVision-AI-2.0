from database import cursor

def total_records():
    cursor.execute("SELECT COUNT(*) FROM history")
    return cursor.fetchone()[0]

def total_scans():
    cursor.execute("SELECT COUNT(*) FROM history WHERE type='Medicine Scan'")
    return cursor.fetchone()[0]

def total_searches():
    cursor.execute("SELECT COUNT(*) FROM history WHERE type='Medicine Search'")
    return cursor.fetchone()[0]

def total_interactions():
    cursor.execute("SELECT COUNT(*) FROM history WHERE type='Drug Interaction'")
    return cursor.fetchone()[0]

def total_chats():
    cursor.execute("SELECT COUNT(*) FROM history WHERE type='AI Chat'")
    return cursor.fetchone()[0]
