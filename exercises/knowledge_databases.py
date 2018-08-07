from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(topic, article_title, rating):
	article_object = Knowledge(
		topic = topic,
		article_title = article_title,
		rating = rating)
	session.add(article_object)
	session.commit()


def query_all_articles():
	article = session.query(
		Knowledge).all()
	return article


def query_article_by_topic(topic):
	article = session.query(
		Knowledge).filter_by(
			topic = topic).first()
	return article
	


def delete_article_by_topic(topic):
	session.query(Knowledge).filter_by(
		topic = topic).delete()
	session.commit()
	

def delete_all_articles():
	session.query(Knowledge).all().delete()
	session.commit()
	

def edit_article_rating(topic, new_rating):
	article_object = session.query(
		Knowledge).filer_by(
		topic = topic).first()
	article_object.rating = new_rating
	session.commit()
	

add_article("mhmd", "mhmd123", 10)
print(query_all_articles())
