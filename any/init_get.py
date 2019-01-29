params = '''date_of_birth: Date!
email: String!
first_name: String!
last_name: String!
middle_name: String
nationality: String!
place_of_birth: String!
residential_addr: AddressInfoInput!'''


def init_gen(params):
    params_list = params.split()
    init_params = "\n".join(params_list)
    print(params_list)
    # print(init_params)

    self_params_list = ['self.' + param + ' = ' + param  for param in params.split()]
    print(self_params_list)
    self_params = "\n".join(self_params_list)
    print(self_params)

def init_gen_1(params):
    # print(params)
    params_list = [param.split(': ')[0] for param in params]
    init_params = "=None,\n".join(params_list)
    print(params_list)
    print(init_params)

    self_params_list = ["'" + param + "': self." + param + ',' for param in params_list]
    print(self_params_list)
    self_params = "\n".join(self_params_list)
    print(self_params)



if __name__ == "__main__":
    init_gen_1(params.split('\n'))
