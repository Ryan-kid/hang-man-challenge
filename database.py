import sqlite3


def create_connection():
    """Create a database connection to a SQLite database"""
    conn = None
    try:
        conn = sqlite3.connect('leaderboards.db')
        print(f"Connected to SQLite version: {sqlite3.version}")
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
    return conn

def create_table(conn):
    """Create players table"""
    try:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS players
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      name TEXT NOT NULL,
                      age INTEGER,
                      wins INTEGER,
                      losses INTEGER)''')
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")

def add_player(conn, player):
    """Add a new player to the database"""
    sql = ''' INSERT INTO players(name,age,wins,losses)
              VALUES(?,?,?,?) '''
    try:
        cur = conn.cursor()
        cur.execute(sql, (player.name, player.age, player.wins, player.losses))
        conn.commit()
        print(f"Player {player.name} added successfully with id {cur.lastrowid}")
        return cur.lastrowid
    except sqlite3.Error as e:
        print(f"Error adding player: {e}")


def viewPlayerData(conn):
    c = conn.cursor()
    c.execute('''
    SELECT * FROM players
  ''')

    playersList = c.fetchall()
    for i, s in enumerate(playersList, start=1):
        print(f"Players {i}, {s}:")

def update_player_stats(conn, player_id, wins, losses):

    try:
        c = conn.cursor()
        c.execute('''UPDATE players 
                     SET wins = wins + ?, losses = losses + ?
                     WHERE id = ?''', (wins, losses, player_id))
        conn.commit()
        print(f"Player stats updated successfully.")
    except sqlite3.Error as e:
        print(f"Error updating player stats: {e}")

