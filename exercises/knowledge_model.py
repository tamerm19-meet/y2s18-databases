from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	__tablename__ = 'Knowledge'
	student_id = Column(Integer, primary_key = True)
	topic = Column(String)
	article_title = Column(String)
	rating = Column(Integer)

	def __repr__(self):
		return("if you want to learn about the topic: {}\n"
			"you can look up the article: {}\n"
			"which i give a rating of: {}\n").format(
			self.topic,
			self.article_title,
			self.rating)
	# Create a table with 4 columns
	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
	# an integer, representing your rating of the article.

