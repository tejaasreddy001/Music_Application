# import firebase_admin
# from firebase_admin import credentials, auth 
# from flask import *

# cred = credentials.Certificate('C:/Users/tejas/OneDrive/Desktop/Latest/MobileDev/Final Pro/Plan/mymusic-7c561-firebase-adminsdk-8na2w-46439357fb.json')
# firebase_admin.initialize_app(cred)

# app = Flask(__name__)

# @app.route('/login',methods=['POST'])
# def login():
#     email = request.json['email']
#     password = request.json['password']
#     print("here")
#     try:
#         user = auth.generate_sign_in_with_email_and_password(email,password)
#         return jsonify({'success':True,'user_id':user['localId']})
#     except:
#         return jsonify({'success':False})


# @app.route('/register',methods=['POST'])
# def register():
#     email = request.json['email']
#     password = request.json['password']

#     try:
#         user = auth.create_user(email=email,password=password)
#         return jsonify({'success':True,'user_id':user.uid})
#     except:
#         return jsonify({'success':False})
    
    
# if __name__ == '__main__':
#     app.run(port=7777)


# import firebase_admin
# from firebase_admin import credentials, auth 
# from flask import *

# cred = credentials.Certificate('C:/Users/tejas/OneDrive/Desktop/Latest/MobileDev/Final Pro/Plan/mymusic-7c561-firebase-adminsdk-8na2w-46439357fb.json')
# firebase_admin.initialize_app(cred)

# app = Flask(__name__)

# @app.route('/login',methods=['POST'])
# def login():
#     email = request.json['email']
#     password = request.json['password']
#     print("here")
#     try:
#         user = auth.generate_sign_in_with_email_and_password(email,password)
#         return jsonify({'success':True,'user_id':user['localId']})
#     except Exception as e:
#         return jsonify({'success':False, 'error': str(e)})


# @app.route('/register',methods=['POST'])
# def register():
#     email = request.json['email']
#     password = request.json['password']

#     try:
#         user = auth.create_user(email=email,password=password)
#         return jsonify({'success':True,'user_id':user.uid})
#     except Exception as e:
#         return jsonify({'success':False, 'error': str(e)})
    
    
# if __name__ == '__main__':
#     app.run(port=7777)

import firebase_admin
from firebase_admin import credentials, auth 
from flask import *

cred = credentials.Certificate('C:/Users/tejas/OneDrive/Desktop/Latest/MobileDev/Final Pro/Plan/mymusic-7c561-firebase-adminsdk-8na2w-46439357fb.json')
firebase_admin.initialize_app(cred)

app = Flask(__name__)

@app.route('/login',methods=['POST'])
def login():
    email = request.json['email']
    password = request.json['password']
    print("here")
    try:
        user = auth.get_user_by_email(email)
        return jsonify({'success':True})
    except Exception as e:
        return jsonify({'success':False,'error': str(e)})

@app.route('/register',methods=['POST'])
def register():
    email = request.json['email']
    password = request.json['password']
    try:
        user = auth.create_user(email=email,password=password)
        return jsonify({'success':True,'user_id':user.uid})
    except:
        return jsonify({'success':False})
    
    
if __name__ == '__main__':
    app.run(port=7777)
