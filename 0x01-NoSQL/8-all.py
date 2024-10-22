#!/usr/bin/env python3
'''List Documents in collection'''


def list_all(mongo_collection):
    '''Lists all documents in collection.'''
    return [doc for doc in mongo_collection.find()]
