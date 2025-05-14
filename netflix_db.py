from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
# Step 1: Create connection to DB
engine = create_engine('sqlite:///netflix.db', echo=True)


Base= declarative_base()


class User(Base):
    __tablename__ = 'users'  # Table name in the DB

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    genre = Column(String)
    year = Column(Integer)

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    rating = Column(Integer)
    comment = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    movie_id = Column(Integer, ForeignKey('movies.id'))

    user = relationship("User", backref="reviews")
    movie = relationship("Movie", backref="reviews")



    # Step 4: Create the table in the DB
Base.metadata.create_all(engine)



Session = sessionmaker(bind=engine)  # Prepares the DB connection
session = Session()  # Starts a DB session

# Add a user
user1 = User(name="Durga", email="durga@example.com")
session.add(user1)

# Create new user and movie
user2 = User(name="Bhavana", email="bhavana@example.com")
movie1 = Movie(title="Inception", genre="Sci-Fi", year=2010)

review1 = Review(rating=5, comment="Mind-blowing!", user=user2, movie=movie1)


# Save it to the DB file

session.add_all([user2, movie1, review1])
session.commit()


# Step 8: Fetch data from the users table
users = session.query(User).all()

# Step 9: Print each user
for user in users:
    print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")



print("\n--- Reviews ---")
reviews = session.query(Review).all()
for r in reviews:
    print(f"{r.user.name} rated '{r.movie.title}' {r.rating} stars – '{r.comment}'")
