from django.core.management import utils

ENV_file = ".env.example"

file_obj = open(ENV_file, "w+")
file_obj.write("SECRET_KEY=" + utils.get_random_secret_key())
file_obj.close()