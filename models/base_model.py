#!/usr/bin/python3
"""
==============================================
Base class mother of all classes and chikens
==============================================
"""

from uuid import uuid4
from datetime import datetime
from datetime import timedelta
import models


class BaseModel:
    """Mother of classes and chickens"""

    def __init__(self, *args, **kwargs):
        """The constructor"""
        if kwargs:
            for key, value in kwargs.items():

                if key == "updated_at" or key == "created_at":
                    # reversing iso format to datetime
                    value, _, m_seconds = value.partition(".")
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")
                    m_seconds = int(m_seconds.rstrip("Z"), 10)
                    value += timedelta(microseconds=m_seconds)
                    # Assingning all the values
                    setattr(self, key, value)
                elif key == "__class__":
                    pass
                else:
                    setattr(self, key, value)

        else:
            self.id = str(uuid4())
            self.updated_at = datetime.now()
            self.created_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """print information"""

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     str(self.__dict__))

    def save(self):
        """update the attribute updated_at"""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """save in a dictionary"""

        my_dic = {}
        for key, value in self.__dict__.items():
            my_dic["__class__"] = self.__class__.__name__
            if key == "created_at" or key == "updated_at":
                my_dic[key] = value.isoformat()  # convert to string
            else:
                my_dic[key] = value
        return my_dic
