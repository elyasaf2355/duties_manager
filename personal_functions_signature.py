#duty manager


def add_duty(s_id: int, d_name: str, day: str, status: str ="pending")->None:
    """
    the function add duty to the duties list of soldier
    :param s_id: id of soldier
    :param d_name: name of duty
    :param day:
    :param status:
    :return: None
    errors: non exist id, d_name already exist for this id, invalid day
    """
    pass
def update_duty(s_id: int, d_name: str, d_status: str)-> None:
    """
    the func change the status key in duty dict for a soldier
    :param s_id: id of soldier
    :param d_name: name of duty
    :param d_status:
    :return: None
    errors: non exist id, non exist duty name, invalid status
    """
    pass
def show_duties(id: int)->list[dict]:
    """
    the func return all duties list for a soldier
    :param id: id of soldier
    :return: list of all duties
    errors: non exist id
    """
    pass

#soldier manager
def add_soldier(name:str, duties:list = [])-> None:
    """
    adding soldier dict to the data list with unique id
    :param name: name of soldier
    :param duties:
    :return: None
    errors: name is empty
    """
    pass
def remove_soldier(id: int)->None:
    """
    remove soldier dict from data
    :param id:
    :return: None
    errors: non exist id
    """
    pass
def all_soldiers()->list[dict]:
    """
    no input
    return list of all soldiers
    :return:
    """
    pass

#main
def menu()->None:
    """
    no input
    show menu to user
    :return: None
    """
def get_input()->None:
    """
    no input
    gets input from user
    :return:
    errors: input not number in range
    """
#utils
def valid_input(user_input:str)->bool:
    """
    checks if input is in number in range
    :param user_input:
    :return: bool
    """
def valid_id(id:int)->bool:
    """
    checks if id exist
    :param id:
    :return:bool
    """
    pass
def valid_soldier_name(name:str)->bool:
    """
    checks that name is not empty
    :param name:
    :return: bool
    """
def valid_duty(id:int, name:str)->bool:
    """
    checks that not already exist duty with that name to that id
    :param id: id of soldier
    :param name: name of duty
    :return: bool
    """
    pass
def valid_status(status:str)->bool:
    """
    validates that status is one of "pending", "complete", "missed"
    :param status:
    :return: bool
    """