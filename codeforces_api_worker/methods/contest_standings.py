from codeforces_api_worker.request import request
from codeforces_api_worker.response_saver import save_response

def get_contest_standings(contestId:int, 
                          asManager:bool=None, _from:int=None, count:int=None, 
                          handle:list=None, room:int=None, showUnofficial:bool=None):
    method_name = 'contest.standings'
    response = request.request(method_name, locals())
    save_response(response, f'{method_name}_{contestId}')