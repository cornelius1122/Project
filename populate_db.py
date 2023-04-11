import datetime as datetime

from app import db, Player
from datetime import datetime

# define player data
player_data = [
    {'name': 'Josh Aybar', 'birthday': '2000-12-15', 'position': 'Prop', 'hometown': 'Baltimore, MD', 'grade': 'Jr'},
    {'name': 'Jaiden Brunson', 'birthday': '2002-06-23', 'position': 'Lock', 'hometown': 'Philadelphia, PA',
     'grade': 'Jr'},
    {'name': 'Joe Sharrock', 'birthday': '2003-08-31', 'position': 'Hooker', 'hometown': 'Virginia Beach, VA',
     'grade': 'So'},
    {'name': 'Jeremiah Aybar', 'birthday': '2001-05-12', 'position': 'Scrum-Half', 'hometown': 'Annapolis, MD',
     'grade': 'Fr'},
    {'name': 'Axel Arias', 'birthday': '2000-11-01', 'position': 'Center', 'hometown': 'Wilmington, DE', 'grade': 'Sr'},
    {'name': 'Chris Cleland', 'birthday': '2002-09-17', 'position': 'Flanker', 'hometown': 'Richmond, VA',
     'grade': 'Jr'},
    {'name': 'William McManus', 'birthday': '2003-02-19', 'position': 'Fullback', 'hometown': 'Fredericksburg, VA',
     'grade': 'Jr'},
    {'name': 'James Stelluti', 'birthday': '2001-10-28', 'position': 'Lock', 'hometown': 'Baltimore, MD',
     'grade': 'Jr'},
    {'name': 'Christopher Wylde', 'birthday': '2000-07-09', 'position': '8 Man', 'hometown': 'Virginia Beach, VA',
     'grade': 'Sr'},
    {'name': 'Dominic Sanelli', 'birthday': '2001-04-13', 'position': 'Hooker', 'hometown': 'Pittsburgh, PA',
     'grade': 'Fr'},
    {'name': 'Evan Corbett', 'birthday': '2000-03-04', 'position': 'Wing', 'hometown': 'Richmond, VA', 'grade': 'Fr'},
    {'name': 'Gavin Schisler', 'birthday': '2001-09-27', 'position': 'Scrum-Half', 'hometown': 'Norfolk, VA',
     'grade': 'Jr'},
    {'name': 'Justin Toth', 'birthday': '2002-12-02', 'position': 'Center', 'hometown': 'Harrisburg, PA',
     'grade': 'Fr'},
    {'name': 'Bastain Brunello', 'birthday': '2003-01-25', 'position': 'Prop', 'hometown': 'Baltimore, MD',
     'grade': 'So'},
    {'name': 'Teni Adesida', 'birthday': '2002-07-31', 'position': 'Hooker', 'hometown': 'Newark, DE', 'grade': 'Sr'},
    {'name': 'Khalili Agboola', 'birthday': '2000-04-17', 'position': 'Wing', 'hometown': 'Baltimore, MD',
     'grade': 'So'},
    {'name': 'Shaun Alvarado', 'birthday': '2001-05-08', 'position': 'Fullback', 'hometown': 'Richmond, VA',
     'grade': 'Jr'},
    {'name': 'George Apostol', 'birthday': '2003-08-21', 'position': 'Lock', 'hometown': 'Philadelphia, PA',
         'grade': 'Fr'},
    {'name': 'Bo Baruani', 'birthday': '2002-09-07', 'position': 'Center', 'hometown': 'Chesapeake, VA',
         'grade': 'So'},
    {'name': 'Will Borden', 'birthday': '2001-06-11', 'position': 'Center', 'hometown': 'Silver Spring, MD',
         'grade': 'Fr'},
    {'name': 'Trevon Brodie', 'birthday': '2001-12-22', 'position': 'Flanker', 'hometown': 'Washington, DC',
         'grade': 'So'},
    {'name': 'Conner Cutolo', 'birthday': '2003-05-02', 'position': 'Lock', 'hometown': 'Bethlehem, PA',
         'grade': 'Jr'},
    {'name': 'Cade Cyrus', 'birthday': '2001-06-13', 'position': 'Wing', 'hometown': 'Richmond, VA', 'grade': 'So'},
    {'name': 'Nathan Cysne', 'birthday': '2000-03-17', 'position': 'Hooker', 'hometown': 'Charlotte, NC',
         'grade': 'Fr'},
    {'name': 'Melkwon Dailey', 'birthday': '2002-01-19', 'position': 'Fullback', 'hometown': 'Baltimore, MD',
         'grade': 'Sr'},
    {'name': 'Gianni Danze', 'birthday': '2001-08-08', 'position': 'Scrum-Half', 'hometown': 'Pittsburgh, PA',
         'grade': 'Jr'},
    {'name': 'Michael Deniel', 'birthday': '2003-09-16', 'position': 'Center', 'hometown': 'Westchester, NY',
         'grade': 'So'},
    {'name': 'Enrique Desouza', 'birthday': '2000-07-11', 'position': 'Lock', 'hometown': 'Virginia Beach, VA',
         'grade': 'Fr'},
    {'name': 'Patric Doherty', 'birthday': '2002-11-05', 'position': 'Prop', 'hometown': 'Baltimore, MD',
         'grade': 'Fr'},
    {'name': 'Jude Fangmeyer', 'birthday': '2001-05-21', 'position': 'Flanker', 'hometown': 'Philadelphia, PA',
         'grade': 'Jr'},
    {'name': 'Shane Focht', 'birthday': '2003-04-06', 'position': 'Wing', 'hometown': 'Bethlehem, PA',
         'grade': 'So'},
    {'name': 'Roberto Fuentes', 'birthday': '2001-06-29', 'position': 'Prop', 'hometown': 'Bronx, NY',
         'grade': 'Fr'},
    {'name': 'Marcos Gonzalez', 'birthday': '2002-09-01', 'position': 'Hooker', 'hometown': 'Huntington, NY',
         'grade': 'Jr'},
    {'name': 'Lawson Halsey', 'birthday': '2000-02-28', 'position': 'Fullback', 'hometown': 'Annapolis, MD',
         'grade': 'So'},
    {'name': 'Alex Hatok', 'birthday': '2001-11-27', 'position': 'Lock', 'hometown': 'Pittsburgh, PA', 'grade': 'Sr'},
    {'name': 'Miguel Hernandez', 'birthday': '2003-03-19', 'position': 'Center', 'hometown': 'Wilmington, DE',
     'grade': 'Jr'},
    {'name': 'Hunter Hertzog', 'birthday': '2002-10-12', 'position': 'Scrum-Half', 'hometown': 'Easton, PA',
     'grade': 'Fr'},
    {'name': 'Liam Horton', 'birthday': '2000-07-05', 'position': 'Prop', 'hometown': 'Charlotte, NC', 'grade': 'So'},
    {'name': 'Fintan Hughes', 'birthday': '2003-02-18', 'position': 'Wing', 'hometown': 'Alexandria, VA',
     'grade': 'Jr'},
    {'name': 'Johny Huynh', 'birthday': '2002-09-04', 'position': 'Hooker', 'hometown': 'Frederick, MD', 'grade': 'Fr'},
    {'name': 'Liam Jackson', 'birthday': '2001-08-12', 'position': 'Center', 'hometown': 'Baltimore, MD',
     'grade': 'Fr'},
    {'name': 'Damon James', 'birthday': '1999-03-07', 'position': 'Prop', 'hometown': 'Bethesda, MD', 'grade': 'Jr'},
    {'name': 'Daryl Johnson', 'birthday': '2003-11-22', 'position': 'Flanker', 'hometown': 'Harrisburg, PA',
     'grade': 'Jr'},
    {'name': 'Elijah Jumper', 'birthday': '2000-06-08', 'position': 'Fullback', 'hometown': 'Lancaster, PA',
     'grade': 'So'},
    {'name': 'Rowland Kamara', 'birthday': '2004-05-16', 'position': 'Scrum-Half', 'hometown': 'Richmond, VA',
     'grade': 'Fr'},
    {'name': 'Quintin Kruger', 'birthday': '1999-01-03', 'position': 'Hooker', 'hometown': 'Silver Spring, MD',
     'grade': 'Jr'},
    {'name': 'Shemar Lewis', 'birthday': '2001-10-21', 'position': 'Wing', 'hometown': 'Arlington, VA', 'grade': 'Fr'},
    {'name': 'Raymond McGettigan', 'birthday': '2000-07-11', 'position': 'Fly-Half', 'hometown': 'Dover, DE',
     'grade': 'Fr'},
    {'name': 'Seamus McGroarty', 'birthday': '2003-04-09', 'position': 'Lock', 'hometown': 'Wilmington, DE',
     'grade': 'Jr'},
    {'name': 'Bernard McIntyre', 'birthday': '2004-12-28', 'position': 'Prop', 'hometown': 'Newark, NJ', 'grade': 'So'},
    {'name': 'Hayden McKay',
     'birthday': '1998-09-25',
     'position': 'Scrum-Half',
     'hometown': 'Fairfax, VA',
     'grade': 'Fr'},
    {'name': 'Danny McVearry',
     'birthday': '2002-02-14',
     'position': 'Flanker',
     'hometown': 'Alexandria, VA',
     'grade': 'Fr'},
    {'name': 'Bau Molinari',
     'birthday': '2001-11-02',
     'position': 'Fullback',
     'hometown': 'Bethesda, MD',
     'grade': 'Fr'},
    {'name': 'Gavin Moore',
     'birthday': '2003-06-26',
     'position': 'Hooker',
     'hometown': 'Silver Spring, MD',
     'grade': 'Jr'},
    {'name': 'Michael Murphy',
     'birthday': '2005-01-09',
     'position': 'Lock',
     'hometown': 'Baltimore, MD',
     'grade': 'Sr'},
    {'name': 'Cornelius Nagbe',
     'birthday': '2001-05-11',
     'position': 'Wing',
     'hometown': 'Dover, DE',
     'grade': 'Sr'},
    {'name': 'Richie Nathan',
     'birthday': '2004-05-03',
     'position': 'Fullback',
     'hometown': 'Baltimore, MD',
     'grade': 'Fr'},
    {'name': 'Austin Nganga',
     'birthday': '2001-06-27',
     'position': 'Hooker',
     'hometown': 'Alexandria, VA',
     'grade': 'Jr'},
    {'name': 'Finn O Leary',
     'birthday': '1998-03-17',
     'position': 'Wing',
     'hometown': 'Wilmington, DE',
     'grade': 'Jr'},
    {'name': 'Declan O Loughlin',
     'birthday': '2003-11-29',
     'position': '8 Man',
     'hometown': 'Frederick, MD',
     'grade': 'Fr'},
    {'name': 'Manny Oladapo',
     'birthday': '2000-09-10',
     'position': 'Scrum-Half',
     'hometown': 'Philadelphia, PA',
     'grade': 'Fr'},
    {'name': 'Cole Patterson',
     'birthday': '2005-12-01',
     'position': 'Lock',
     'hometown': 'Salisbury, MD',
     'grade': 'So'},
    {'name': 'Marcus Petersen',
     'birthday': '2001-08-08',
     'position': 'Prop',
     'hometown': 'Annapolis, MD',
     'grade': 'Fr'},
    {'name': 'Elisha Ross',
     'birthday': '2002-07-16',
     'position': 'Fly-Half',
     'hometown': 'Washington, DC',
     'grade': 'Jr'},
    {'name': 'Ford Rubel',
     'birthday': '1999-04-02',
     'position': 'Center',
     'hometown': 'Wilmington, DE',
     'grade': 'So'},
    {'name': 'Noel Ruiz',
     'birthday': '2004-01-22',
     'position': 'Hooker',
     'hometown': 'Newark, NJ', 'grade': 'Jr'},
    {'name': 'Chris Shepherd', 'birthday': '2003-09-08', 'position': 'Wing', 'hometown': 'Baltimore, MD',
         'grade': 'Fr'},
    {'name': 'John Stermel', 'birthday': '2001-06-19', 'position': 'Lock', 'hometown': 'Richmond, VA',
         'grade': 'Fr'},
    {'name': 'Landon Strappazon', 'birthday': '1999-12-28', 'position': 'Prop', 'hometown': 'Arlington, VA',
         'grade': 'So'},
    {'name': 'Jimmy Sullivan', 'birthday': '2002-10-12', 'position': 'Scrum-Half', 'hometown': 'Harrisburg, PA',
         'grade': 'Fr'},
    {'name': 'Branden Taylor', 'birthday': '2005-02-01', 'position': 'Fullback', 'hometown': 'Bethesda, MD',
         'grade': 'So'},
    {'name': 'James Thompson', 'birthday': '2003-07-24', 'position': 'Flanker', 'hometown': 'Alexandria, VA',
         'grade': 'Jr'},
    {'name': 'Dylan Van Stry', 'birthday': '1998-11-08', 'position': 'Fly-Half', 'hometown': 'Wilmington, DE',
         'grade': 'So'},
    {'name': 'Thurman Zollicoffer', 'birthday': '2002-03-14', 'position': 'Fly-Half', 'hometown': 'Emmitsburg, MD', 'grade': 'Sr'}

]

# create Player instances for each player
for data in player_data:
    # convert the birthday string to a datetime object
    birthday = datetime.strptime(data['birthday'], '%Y-%m-%d').date()
    player = Player(name=data['name'], grade=data['grade'], birthday=birthday, position=data['position'],
                    hometown=data['hometown'])
    db.session.add(player)

# commit changes to database
db.session.commit()