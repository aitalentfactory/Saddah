from sqlalchemy import text
from sqlalchemy.orm import Session

from src.model.User import User


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_user_by_uuid(self, uuid):
        query = text(
            "SELECT id,username,password,fullname,email,uuid,phone,status FROM ai_user WHERE uuid = :uuid")
        result = self.db.execute(query, {"uuid": uuid}).fetchone()
        user = User()
        if result is not None:
            user.seqId = result.id
            user.username = result.username
            user.password = result.password
            user.fullname = result.fullname
            user.email = result.email
            user.uuid = result.uuid
            user.phone = result.phone
            user.status = result.status
        return user

    def get_user_by_username(self, username):
        query = text(
            "SELECT id,username,password,fullname,email,uuid,phone,status FROM ai_user WHERE username = :username")
        result = self.db.execute(query,  {"username": username}).fetchone()
        user = User()
        if result is not None:
            user.seqId = result.id
            user.username = result.username
            user.password = result.password
            user.fullname = result.fullname
            user.email = result.email
            user.uuid = result.uuid
            user.phone = result.phone
            user.status = result.status
        return user

    def get_user_by_name(self, name):
        query = text(
            "SELECT id,username,password,fullname,email,uuid,phone,status FROM ai_user WHERE UPPER(fullname) like :name")
        result = self.db.execute(query,  {"name": f"%{name}%"}).fetchone()
        user = User()
        if result is not None:
            user.seqId = result.id
            user.username = result.username
            user.password = result.password
            user.fullname = result.fullname
            user.email = result.email
            user.uuid = result.uuid
            user.phone = result.phone
            user.status = result.status
        return user


    def get_users(self):
        query = text(
            "SELECT id,username,password,fullname,email,uuid,phone,status FROM ai_user")
        results = self.db.execute(query).fetchall()

        users = []
        for result in results:
            user = User()
            user.seqId = result.id
            user.username = result.username
            user.password = result.password
            user.fullname = result.fullname
            user.email = result.email
            user.uuid = result.uuid
            user.phone = result.phone
            user.status = result.status
            users.append(user)
        return users

    def insert_user(self, user: User):
        query = text("""
            INSERT INTO ai_user (username, password, fullname, email, uuid, phone, status)
            VALUES (:username, :password, :fullname, :email, :uuid, :phone, :status)
        """)
        result = self.db.execute(query, {
            "username": user.username,
            "password": user.password,
            "fullname": user.fullname,
            "email": user.email,
            "uuid": user.uuid,
            "phone": user.phone,
            "status": user.status
        })
        self.db.commit()
        return result.lastrowid
