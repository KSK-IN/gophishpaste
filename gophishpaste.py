import sqlite3
from tabulate import tabulate

# Connect to the database
conn = sqlite3.connect("gophish.db")

def check(name, duser, query):
    cur = conn.cursor()
    cur.execute(query, (duser, name))
    return cur.fetchone() is not None

def email(suser, duser):
    while True:
        cur = conn.cursor()
        res = cur.execute("SELECT id, name FROM templates WHERE user_id = ?", (suser,))
        rows = res.fetchall()
        header = ["ID", "Name"]
        print(tabulate(rows, headers=header, tablefmt="fancy_grid"))

        totalmax = cur.execute("SELECT MAX(id) FROM templates").fetchone()[0] or 0
        did = totalmax + 1

        tid = input("Enter your email template ID (Enter 'b' to back): ")
        
        if tid.isdigit():
            tid = int(tid)
            for template_id, name in rows:
                if template_id == tid:
                    if check(name, duser, "SELECT name FROM templates WHERE user_id = ? AND name = ?"):
                        print("Template already exists for the destination user. Please choose another template.")
                        break
                    else:
                        print("Template does not exist for the destination user. You can proceed.")
                        data = list(cur.execute("SELECT * FROM templates WHERE id = ?", (tid,)).fetchone())
                        data[0] = did  # Update ID
                        data[1] = duser  # Update user_id

                        insert_query = """
                            INSERT INTO templates(id, user_id, name, subject, text, html, modified_date, envelope_sender) 
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                        """
                        cur.execute(insert_query, tuple(data))
                        conn.commit()
                        print("The email template was updated successfully.")
                        break
        elif tid.lower() == 'b':
            break
        else:
            print("Invalid input. Please enter a valid ID.")
            continue

def land(suser, duser):
    while True:
        cur = conn.cursor()
        res = cur.execute("SELECT id, name FROM pages WHERE user_id = ?", (suser,))
        rows = res.fetchall()
        header = ["ID", "Name"]
        print(tabulate(rows, headers=header, tablefmt="fancy_grid"))

        totalmax = cur.execute("SELECT MAX(id) FROM pages").fetchone()[0] or 0
        did = totalmax + 1

        tid = input("Enter your landing page ID (Enter 'b' to back): ")

        if tid.isdigit():
            tid = int(tid)
            for page_id, name in rows:
                if page_id == tid:
                    if check(name, duser, "SELECT name FROM pages WHERE user_id = ? AND name = ?"):
                        print("Landing page already exists for the destination user. Please choose another template.")
                        break
                    else:
                        print("Landing page does not exist for the destination user. You can proceed.")
                        data = list(cur.execute("SELECT * FROM pages WHERE id = ?", (tid,)).fetchone())
                        data[0] = did  # Update ID
                        data[1] = duser  # Update user_id

                        insert_query = """
                            INSERT INTO pages(id, user_id, name, html, modified_date, capture_credentials, capture_passwords, redirect_url) 
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                        """
                        cur.execute(insert_query, tuple(data))
                        conn.commit()
                        print("The landing page was updated successfully.")
                        break
        elif tid.lower() == 'b':
            break
        else:
            print("Invalid input. Please enter a valid ID.")
            continue

def send(suser, duser):
    while True:
        cur = conn.cursor()
        res = cur.execute("SELECT id, name FROM smtp WHERE user_id = ?", (suser,))
        rows = res.fetchall()
        header = ["ID", "Name"]
        print(tabulate(rows, headers=header, tablefmt="fancy_grid"))

        totalmax = cur.execute("SELECT MAX(id) FROM smtp").fetchone()[0] or 0
        did = totalmax + 1

        tid = input("Enter your SMTP ID (Enter 'b' to back): ")

        if tid.isdigit():
            tid = int(tid)
            for smtp_id, name in rows:
                if smtp_id == tid:
                    if check(name, duser, "SELECT name FROM smtp WHERE user_id = ? AND name = ?"):
                        print("SMTP profile already exists for the destination user. Please choose another.")
                        break
                    else:
                        print("SMTP profile does not exist for the destination user. You can proceed.")
                        data = list(cur.execute("SELECT * FROM smtp WHERE id = ?", (tid,)).fetchone())
                        data[0] = did  # Update ID
                        data[1] = duser  # Update user_id

                        insert_query = """
                            INSERT INTO smtp(id, user_id, interface_type, name, host, username, password, from_address, modified_date, ignore_cert_errors) 
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """
                        cur.execute(insert_query, tuple(data))
                        conn.commit()
                        print("The SMTP profile was updated successfully.")
                        break
        elif tid.lower() == 'b':
            break
        else:
            print("Invalid input. Please enter a valid ID.")
            continue

if __name__ == "__main__":
    cur = conn.cursor()
    res = cur.execute("SELECT id, username FROM users")
    rows = res.fetchall()
    header = ["ID", "Username"]
    print(tabulate(rows, headers=header, tablefmt="fancy_grid"))

    suser = input("Enter the source user ID: ")
    duser = input("Enter the destination user ID: ")

    while True:
        print("\nSelect an option:")
        print("1. Email template")
        print("2. Landing pages")
        print("3. Sending profiles")
        print("4. Exit")
        option = input(">> ")

        if option == "1":
            email(suser, duser)
        elif option == "2":
            land(suser, duser)
        elif option == "3":
            send(suser, duser)
        elif option == "4":
            break
        else:
            print("Invalid option. Please try again.")
