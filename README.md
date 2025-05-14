# neflix-_clone
 
Step 1: Create the File
In your netflix_clone folder:

Right-click → New File

Name it exactly: README.md

📝 Step 2: Paste This Content Inside
markdown
Copy code
# 🎬 Netflix Clone DB using SQLAlchemy

A simple project that simulates how streaming platforms like Netflix store data.  
Built with **Python**, **SQLAlchemy ORM**, and **SQLite**.

## ✅ Features
- Create tables for Users, Movies, and Reviews
- Define relationships with `ForeignKey` and `relationship()`
- Insert sample data
- Query and display user reviews

## 🧠 Tables
| Table | Fields |
|-------|--------|
| User | id, name, email |
| Movie | id, title, genre, year |
| Review | id, rating, comment, user_id, movie_id |

## 🚀 How to Run

```bash
pip install sqlalchemy
python netflix_db.py
📦 Example Output
nginx
Copy code
Bhavana rated 'Inception' 5 stars – 'Mind-blowing!'
🔗 Technologies Used
Python

SQLAlchemy ORM

SQLite

✨ Created by Durga
yaml
Copy code

✅ Save the file!

---

### 💥 Step 3: Push to GitHub

In your terminal:

```bash
git add README.md
git commit -m "Added README with project details"
git push
