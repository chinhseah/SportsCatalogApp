#!/usr/bin/env python2.7

"""
Udacity Full-Stack Web Developer Nanodegree
Homework 2 : Catalog Items App
Student: Chin H. Seah
"""

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base, Category, CategoryItem

app = Flask(__name__)

engine = create_engine('sqlite:///catalog.db',
                       connect_args={'check_same_thread': False})
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

class CatItem():
    def __init__(self, id, category, item):
        self.id = id
        self.category = category
        self.item = item

    def __str__(self):
        return "Id: %s Category: %s Name: %s" % (self.id, self.category, self.item)

@app.route('/')
@app.route('/catalog')
def show_catalog():
    """
    Display list of categories and latest category items.
    """
    categories = get_categories()
    numberOfCategories = len(categories)
    latestItems = get_latest_items(numberOfCategories)
    return render_template('catalog.html', categories=categories, latestItems=latestItems)

@app.route('/catalog/<category>/items')
def show_category_items(category):
    """
    Display list of categories and items for selected category.
    """
    categories = get_categories()
    catId = get_category_id(category)
    itemsCount = 0
    items = []
    if catId is None:
        flash("Category %s not found!" % (category))
    else:
        categoryitems = get_category_items(catId)
        if categoryitems is not None:
            itemsCount = len(categoryitems)
            for item in categoryitems:
                newItem = CatItem(catId, category, item.name)
                items.append(newItem)

    if itemsCount == 1:
        categoryTotal = "1 item"
    else:
        categoryTotal = "%d items" % (itemsCount)
    return render_template('catalog.html', categoryName=category, categories=categories, categoryTotal=categoryTotal, latestItems=items)

@app.route('/catalog/<category>/items/<item>')
def show_category_item(category, item):
    """
    Display item description
    """
    itemId = get_item_id(item)
    if itemId is None:
        flash("Item %s not found!" % (item))
        itemDescription = "Not found."
    else:
        itemObj = get_category_item(itemId)
        itemDescription = itemObj.description
    return render_template('itemdetails.html', categoryName=category, itemName=item, itemDescription=itemDescription)

def get_categories():
    """
    Get list of categories.
    """
    return session.query(Category).all()

def get_category_id(name):
    """
    Get category identifier by its name.
    """
    cat = session.query(Category).filter_by(name = name).first()
    return cat.id

def get_category_items(categoryId):
    """
    Get category items by its identifier.
    """
    return session.query(CategoryItem).filter_by(category_id = categoryId).all()

def get_category_item(itemId):
    """
    Get category item by its identifier.
    """
    return session.query(CategoryItem).filter_by(id = itemId).first()

def get_item_id(name):
    """
    Get item identifier by its name.
    """
    item = session.query(CategoryItem).filter_by(name = name).first()
    if item is None:
        return None
    return item.id

def get_latest_items(itemLimit):
    """
    Get list of latest category items with limit for number
    of items. Name of item has category in parenthesis.
    """
    items = []

    for c, ci in session.query(Category, CategoryItem).\
        filter(Category.id == CategoryItem.category_id).\
        order_by(CategoryItem.create_date)[0:itemLimit]:
        newItem = CatItem(ci.id, c.name, ci.name)
        items.append(newItem)

    # for debugging
    #for i in items:
    #    print(i)
    return items

if __name__ == '__main__':
    app.secret_key = "super_secret_key"
    app.debug = True
    app.run(host='0.0.0.0', port=5000, threaded=False)
