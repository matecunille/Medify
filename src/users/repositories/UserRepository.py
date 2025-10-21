from users.models import User
from django.contrib.auth.hashers import make_password, check_password

class UserRepository:
    @staticmethod
    def get_by_id(pk):
        return User.objects.filter(pk=pk).first()

    @staticmethod
    def get_all():
        return User.objects.all()

    @staticmethod
    def update(pk, **kwargs):
        User.objects.filter(pk=pk).update(**kwargs)

    @staticmethod
    def delete(pk):
        User.objects.filter(pk=pk).delete()

    @staticmethod
    def get_by_username(username):
        return User.objects.filter(username=username).first()

    @staticmethod
    def verify_password(user, raw_password):
        return check_password(raw_password, user.password)

    @staticmethod
    def create_user(data):
        try:
            # First create user without specialty
            hashed_password = make_password(data['password'])
            user = User.objects.create(
                username=data['username'],
                password=hashed_password,
                email=data['email'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                role=data['role'],
                dni=data['dni'],
                photo=data.get('photo')
            )
            
            # If doctor and has specialty, assign it
            if data['role'] == 'doctor' and 'specialty' in data:
                user.specialty = data['specialty']
                user.save()
                
            return user
        except Exception as e:
            print(f"Error creating user: {e}")
            return None