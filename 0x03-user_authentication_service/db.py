#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Add a new user to the database
        Args:
            email (str): The email address of the user
            hashed_password (str): The hashed password of the user
        Returns:
            User: The newly created user
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """returns the first row found in the users table
        as filtered by the method’s input arguments
        """
        keys = ['id', 'email', 'hashes_password', 'session_id', 'reset_token']
        # print(kwargs)
        for key in kwargs.keys():
            if key not in keys:
                raise InvalidRequestError
        user = self._session.query(User).filter_by(**kwargs).first()
        if user is None:
            raise NoResultFound
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """takes as argument a required user_id integer and
        arbitrary keyword arguments, and returns None.
        use find_user_by to locate the user to update
        """
        user = self.find_user_by(id=user_id)
        keys = ['id', 'email', 'hashed_password', 'session_id', 'reset_token']
        for key, value in kwargs.items():
            if key in keys:
                setattr(user, key, value)
            else:
                raise ValueError
        self._session.commit()
