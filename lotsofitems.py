from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Genre, Base, Instrument, User

engine = create_engine('sqlite:///musicalinstrumentswithusers.db')
""" Bind engine to metadata of Base class so that declaratives
can be accessed by DBSession
"""
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
""" DBSession() is instantiated to establish communication with
itemcatalogwithusers database. This is setup to create several
items to test out the Musical Instrument Application"""
session = DBSession()


# Create dummy User
User1 = User(name="Taylor Burton", email="taylor@example.com",
             picture="https://www.google.com")
session.add(User1)
session.commit()

# Create dummy Genre
genre1 = Genre(user_id=1, name="Gamelan")
session.add(genre1)
session.commit()

# Create dummy Instruments
instrument1 = Instrument(user_id=1, name="Selonding", description="Set of iron mallet instruments \
            from Bali, Indonesia", price="3000.00", category="percussion", genre=genre1)
session.add(instrument1)
session.commit()

instrument2 = Instrument(user_id=1, name="Gender Wayang", description="Set of 4 bronze mallet instruments \
            from Bali, Indonesia", price="1500.00", category="percussion", genre=genre1)
session.add(instrument2)
session.commit()

instrument3 = Instrument(user_id=1, name="Suling", description="Balinese/Javanese flute",
            price="100.00", category="wind", genre=genre1)
session.add(instrument3)
session.commit()

instrument4 = Instrument(user_id=1, name="Rebab", description="2 stringed Balinese/Javanese \
            spike fiddle", price="300.00", category="string", genre=genre1)
session.add(instrument4)
session.commit()

# New dummy Genre
genre2 = Genre(user_id=1, name="Mohori")
session.add(genre2)
session.commit()

# New dummy Instruments
instrument5 = Instrument(user_id=1, name="Tro Khmer", description="Three stringed Khmer spike fiddle \
            played in Mohori and other Cambodian ensembles", category="string", price="200.00",
            genre=genre2)
session.add(instrument5)
session.commit()

instrument6 = Instrument(user_id=1, name="Kim", description="Hammered zither used in Khmer Mohori \
             ensemble", price="250.00", category="percussion", genre=genre2)
session.add(instrument6)
session.commit()

instrument7 = Instrument(user_id=1, name="Sralai", description="Quadruple reed Khmer oboe",
            price="100.00", category="wind", genre=genre2)
session.add(instrument7)
session.commit()

# New dummy Genre
genre3 = Genre(user_id=1, name="Karnatak")
session.add(genre3)
session.commit()

# New dummy Instruments
instrument8 = Instrument(user_id=1, name="Mridangam", description="Two headed drum used in a \
            traditional Karnatak music ensemble", price="400.00", category="percussion", genre=genre3)
session.add(instrument8)
session.commit()

instrument9 = Instrument(user_id=1, name="Veena", description="7 string South Indian bowl lute",
            price="1000.00", category="string", genre=genre3)
session.add(instrument9)
session.commit()

instrument10 = Instrument(user_id=1, name="Venu", description="Karnatak transverse flute",
            price="100.00", category="wind", genre=genre3)
session.add(instrument10)
session.commit()

# New dummy Genre
genre4 = Genre(user_id=1, name="Gagaku")
session.add(genre4)
session.commit()

# New dummy Instruments
instrument11 = Instrument(user_id=1, name="Hichiriki", description="Blown double-reed Japanese oboe \
            similar to shawm", price="150.00", category="wind", genre=genre4)
session.add(instrument11)
session.commit()

instrument12 = Instrument(user_id=1, name="Koto", description="13 string Japanese zither",
            price="300.00", category="string", genre=genre4)
session.add(instrument12)
session.commit()

instrument13 = Instrument(user_id=1, name="Kakko", description="Small hourglass drum, played \
            with 2 wooden sticks", price="100.00", category="percussion", genre=genre4)
session.add(instrument13)
session.commit()
