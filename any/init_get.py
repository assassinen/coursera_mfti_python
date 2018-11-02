params = '''
  user_login 
  hashed_password 
  email
  phone
  user_type
  nationality 
  first_name 
  middle_name
  last_name 
  date_of_birth
  place_of_birth 
  registration_addr_id
  residential_addr_id
  active 
  created_at
  '''


def init_gen(params):
    params_list = params.split()
    init_params = ",\n".join(params_list)
    print(params_list)
    # print(init_params)

    self_params_list = ['self.' + param + ' = ' + param  for param in params.split()]
    print(self_params_list)
    self_params = "\n".join(self_params_list)
    print(self_params)

if __name__ == "__main__":
    init_gen(params)
