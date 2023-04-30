from .models import *

class controller:

    def editUser(id, email='', password='', name=''):
        user = Users.query.filter_by(id=id).first()
        if email != '':
            user.email = email
        if password != '':
            user.password = password
        if name != '':
            user.username = name
        db.session.commit()

    def deleteUser(id):
        user = Users.query.filter_by(id=id).first()
        db.session.delete(user)
        db.session.commit()
    
    def addUserWatchList(item, user_id):
        newUserWatchList = UserWatchList(item=item, user_id=user_id)
        db.session.add(newUserWatchList)
        db.session.commit()
