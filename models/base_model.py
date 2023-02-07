#!/usr/bin/python3
"""
The base_model module
defines all common attributes/methods for other classes:
"""


import unittest
import uuid
import cmd
import datetime


class BaseModel:
    """a class BaseModel that defines all common attributes/methods for other classes:""" 
    def __init__(self, *args, **kwargs):
        """Inistantiation of instance attributes"""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'created_at':
                    value, _, m_seconds = value.partition(".")
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")
                    m_seconds = int(m_seconds.rstrip("Z"), 10)
                    value += timedelta(microseconds=m_seconds)
                    self.created_at = value
                if key == 'updated_at':
                    value, _, m_seconds = value.partition(".")
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")
                    m_seconds = int(m_seconds.rstrip("Z"), 10)
                    value += timedelta(microseconds=m_seconds)                    
                    self.updated_at = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
    def __str__(self):
        """Prinnt string representation of an object"""
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of
         __dict__ of the instance:"""
        my_dic = {}
        for key, value in self.__dict__.items():
            if key == "updated_at" or key == "created_at":
                value = value.isoformat()
            my_dic[key] = value
        my_dic["__class__"] = self.__class__.__name__
        return my_dic