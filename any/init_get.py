params = '''
    identity_document_id
    file_path
    file_type
    status
    created_at
    updated_status_at
    document_expire_date
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
